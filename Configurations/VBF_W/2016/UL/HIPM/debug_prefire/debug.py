import uproot
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt

# =====================
# CONFIG
# =====================
# Modifica qui:
filename   = "/eos/cms/store/group/phys_smp/ec/Latinos/HWWNano/Summer20UL16_106x_nAODv9_HIPM_Full2016v9/MCl1loose2016v9__MCCorr2016v9NoJERInHorn/nanoLatino_Wp_LNuJJ_EWK__part2.root"      # <-- metti il tuo
treename   = "Events"            # oppure "latino" se è un latino
flavour    = "mu"               # "ele" o "mu" se vuoi cambiare canale

# =====================
# FUNZIONCINE UTILI
# =====================

def first(a, default=0):
    """Equivalente ad Alt$(x[0], default)"""
    return ak.fill_none(ak.firsts(a), default)

def second(a, default=0):
    """Equivalente ad Alt$(x[1], default)"""
    # pad a lunghezza 2 e prendo il secondo
    a2 = ak.pad_none(a, 2)
    return ak.fill_none(a2[:,1], default)

def abs_first(a, default=0):
    return np.abs(first(a, default))

# =====================
# LEGGI IL TTREE
# =====================

branches = [
    "nLepton",
    "Lepton_pt", "Lepton_eta", "Lepton_pdgId", "Lepton_isLoose",
    "CleanJet_pt", "CleanJet_eta", "CleanJet_jetIdx", "Jet_btagDeepB", "Jet_btagSF_deepcsv_shape",
    "Jet_jetId", "Jet_PUIDSF_loose",
    "mjj", "detajj", "mtw1",
    # pesi
    "XSWeight",
    "puWeight",
    "Lepton_RecoSF",
    "Lepton_tightElectron_mvaFall17V2Iso_WP90_tthmva_70_IdIsoSF",
    "Lepton_tightMuon_cut_Tight80x_tthmva_80_IdIsoSF",
    "TriggerSFWeight_1l",
    "EMTFbug_veto",
    "L1PreFiringWeight_Nom",
    "L1PreFiringWeight_Up",
    "Lepton_genmatched",
    "METFilter_MC",
    # trigger bits
    "HLT_IsoTkMu24",
    "HLT_IsoMu24",
    "HLT_Ele27_WPTight_Gsf",
    "HLT_Ele25_eta2p1_WPTight_Gsf",
]

print("➜ Apro file:", filename)
with uproot.open(filename) as f:
    tree = f[treename]
    events = tree.arrays(branches, library="ak")

print("N eventi totali:", len(events))

# =====================
# COSTRUZIONE SUPER-CUT
# =====================

nLepton = events["nLepton"]
Lepton_pt  = events["Lepton_pt"]
Lepton_eta = events["Lepton_eta"]
Lepton_pdgId = events["Lepton_pdgId"]
Lepton_isLoose = events["Lepton_isLoose"]
CleanJet_pt = events["CleanJet_pt"]
CleanJet_eta = events["CleanJet_eta"]
mjj     = events["mjj"]
detajj  = events["detajj"]

# Alt$ equivalenti
lep0_pt   = first(Lepton_pt, 0)
lep1_pt   = second(Lepton_pt, 0)
lep0_eta  = first(Lepton_eta, 0)
lep1_isLoose = second(Lepton_isLoose, 1)

cj0_pt   = first(CleanJet_pt, 0)
cj1_pt   = second(CleanJet_pt, 0)
cj0_etaA = abs_first(CleanJet_eta, 3)         # Alt$(abs(CleanJet_eta[0]),3)
cj1_etaA = np.abs(second(CleanJet_eta, 3))    # Alt$(abs(CleanJet_eta[1]),3)

# condizioni su jet eta come nelle tue stringhe
jet0_eta_sel = ((cj0_etaA < 2.5) | ((np.abs(first(CleanJet_eta,0)) > 3.0)))
jet1_eta_sel = ((cj1_etaA < 2.5) | ((np.abs(second(CleanJet_eta,0)) > 3.0)))

# Extract arrays
CleanJet_jetIdx = events["CleanJet_jetIdx"]
Jet_btagDeepB = events["Jet_btagDeepB"]

# b-veto: troviamo per ogni jet se soddisfa la condizione
is_btagged = (
    (CleanJet_pt > 20.) &
    (np.abs(CleanJet_eta) < 2.5) &
    (Jet_btagDeepB[CleanJet_jetIdx] > 0.6001)
)

# b-veto = nessun jet soddisfa la condizione
bVeto = (ak.sum(is_btagged, axis=1) == 0)

supercut_mask = (
    (nLepton >= 1)
    & (lep0_pt > 25.)
    & jet0_eta_sel
    & jet1_eta_sel
    & (cj1_pt > 30.)
    & (cj0_pt > 40.)
    & (mjj >= 400.)
    & (detajj > 2.)
    & (lep0_eta > -2.)
    & (lep0_eta <  2.)
    & (lep1_pt <= 15.)
    & (lep1_isLoose > 0.5)
)

print("Eventi che passano SUPERcut:", ak.sum(supercut_mask))

# =====================
# CUT DI CANALE (ele_SR)
# =====================

lep0_pdg = first(Lepton_pdgId, 0)
mtw1     = events["mtw1"]

if flavour == "ele":
    chan_mask = (
        (np.abs(lep0_pdg) == 11)
        & (lep0_pt > 30.)
    )
elif flavour == "mu":
    chan_mask = (
        (np.abs(lep0_pdg) == 13)
    )
else:
    raise RuntimeError("flavour deve essere 'ele' o 'mu'")

# tagli comuni SR (detajj, ptj2, mtw1, bVeto)
sr_extra_mask = (
    ak.values_astype(bVeto, bool)
    & (detajj > 4.)
    & (cj1_pt > 70.)
    & (mtw1 > 50.)
)

total_mask = supercut_mask & chan_mask & sr_extra_mask

print("Eventi che passano SUPERcut + SR({}): {}".format(flavour, ak.sum(total_mask)))

# =====================
# COSTRUZIONE PESO NOMINALE E UP
# =====================


# Working points
bWP_medium = 0.6001   # deepCSV medium WP
bSF_name   = "Jet_btagSF_deepcsv_shape"   # per coerenza con Latino

# Jet quantities
cj_pt     = events["CleanJet_pt"]
cj_eta    = events["CleanJet_eta"]
cj_jetIdx = events["CleanJet_jetIdx"]

jet_btag  = events["Jet_btagDeepB"]
jet_btagSF = events[bSF_name]

# =============================================
# 1) Costruzione dei bool per bVeto e bReq
# =============================================

# boolean mask for jets relevant to the veto (pt>20, |eta|<2.5)
mask_veto_jets = (cj_pt > 20) & (abs(cj_eta) < 2.5)

# boolean mask for jets relevant to b-tag (veto region)
mask_btag_veto = mask_veto_jets & (jet_btag[cj_jetIdx] > bWP_medium)

# bVeto = no jets passing b-tag medium
bVeto = (ak.sum(mask_btag_veto, axis=1) == 0)


# boolean mask for jets relevant to bReq (pt>30, |eta|<2.5)
mask_req_jets = (cj_pt > 30) & (abs(cj_eta) < 2.5)

mask_btag_req = mask_req_jets & (jet_btag[cj_jetIdx] > bWP_medium)

# bReq = at least 2 b-tagged jets
bReq = (ak.sum(mask_btag_req, axis=1) >= 2)


# =============================================
# 2) Costruzione bVetoSF (Latino logic)
#    bVetoSF = exp(sum(log( SF_j )))
# =============================================

# SF per i jet da considerare nel veto
sf_veto = ak.where(mask_veto_jets,
                   jet_btagSF[cj_jetIdx],
                   1.0)

bVetoSF = np.exp(ak.sum(np.log(sf_veto), axis=1))


# =============================================
# 3) Costruzione bReqSF (Latino logic)
# =============================================

sf_req = ak.where(mask_req_jets,
                  jet_btagSF[cj_jetIdx],
                  1.0)

bReqSF = np.exp(ak.sum(np.log(sf_req), axis=1))


# =============================================
# 4) btagSF finale
# =============================================

btagSF = ak.where(
    bVeto,
    bVetoSF,
    ak.where(
        bReq,
        bReqSF,
        0.0      # Zona “intermedia”: esattamente come in Latino
    )
)

###### jetpuidSF

jetId   = events["Jet_jetId"]
jet_puid_sf = events["Jet_PUIDSF_loose"]

# mask: solo jet con jetId >= 2
mask_puid = (jetId >= 2)

# Per sicurezza: evita log(0) se mai ci fossero SF = 0
safe_sf = ak.where(mask_puid, jet_puid_sf, 1.0)
safe_sf = ak.where(safe_sf > 0, safe_sf, 1.0)

PUJetIdSF = np.exp(ak.sum(np.log(safe_sf), axis=1))

# pezzi del peso
XSWeight   = events["XSWeight"]
puWeight   = events["puWeight"]
RecoSF0    = events["Lepton_RecoSF"][:,0]
EleTightSF = events["Lepton_tightElectron_mvaFall17V2Iso_WP90_tthmva_70_IdIsoSF"][:,0]
MuTightSF  = events["Lepton_tightMuon_cut_Tight80x_tthmva_80_IdIsoSF"][:,0]
# btagSF     = events["btagSF"]
# PUJetIdSF  = events["PUJetIdSF"]
TrigSF1l   = events["TriggerSFWeight_1l"]
EMTFbug    = events["EMTFbug_veto"]
L1Nom      = events["L1PreFiringWeight_Nom"]
L1Up       = events["L1PreFiringWeight_Up"]
GenLepMatch = events["Lepton_genmatched"][:,0]
METFilter_MC = events["METFilter_MC"]

# trigger MC (semplificato, ma ok per debug)
HLT_IsoTkMu24 = events["HLT_IsoTkMu24"]
HLT_IsoMu24   = events["HLT_IsoMu24"]
HLT_Ele27     = events["HLT_Ele27_WPTight_Gsf"]
HLT_Ele25     = events["HLT_Ele25_eta2p1_WPTight_Gsf"]

trigg_MC = (
    ((np.abs(lep0_pdg) == 13) * ((HLT_IsoTkMu24 > 0.5) | (HLT_IsoMu24 > 0.5))) |
    ((np.abs(lep0_pdg) == 11) * ((HLT_Ele27 > 0.5) | (HLT_Ele25 > 0.5)))
)

# LepWP cut
LepWPCut_1l = (
    (events["Lepton_tightElectron_mvaFall17V2Iso_WP90_tthmva_70_IdIsoSF"][:,0] > 0.0) |
    (events["Lepton_tightMuon_cut_Tight80x_tthmva_80_IdIsoSF"][:,0] > 0.0)
)

# LepWPWeight
LepWPWeight_1l = EleTightSF * MuTightSF


# ============================
#  COSTRUZIONE DEI PESI
# ============================

# SF totale (come nel tuo CommonWeight), includendo già L1Nom
SF = (
    puWeight
    * RecoSF0
    * LepWPWeight_1l
    * LepWPCut_1l
    * btagSF
    * PUJetIdSF
    * TrigSF1l
    * trigg_MC
    * EMTFbug
    * L1Nom
)

# peso nominale completo
w_nom = XSWeight * SF * METFilter_MC * GenLepMatch

# ratio prefiring Up/Nom (protetto da divisione per 0)
ratio_pref = ak.where(L1Nom != 0, L1Up / L1Nom, 1.0)

# peso con variazione Up
w_up = w_nom * ratio_pref

import matplotlib.pyplot as plt
import numpy as np

# ========================================
# COSTRUZIONE DEI DATI PER IL PLOT
# ========================================

mjj_sel = mjj[total_mask]

w_nom_sel = w_nom[total_mask]
w_up_sel  = w_nom[total_mask] * ratio_pref[total_mask]

# Convertiamo in numpy (matplotlib non digerisce bene awkward)
mjj_np      = np.array(mjj_sel)
w_nom_np    = np.array(w_nom_sel)
w_up_np     = np.array(w_up_sel)

# Binning
bins = np.linspace(400, 2000, 20)

# ========================================
# FIGURA CON DUE PANNELLI
# ========================================
fig = plt.figure(figsize=(7, 7))
gs = fig.add_gridspec(2, 1, height_ratios=[3, 1], hspace=0.05)

# --- PLOT PRINCIPALE ---
ax1 = fig.add_subplot(gs[0])

ax1.hist(
    mjj_np, bins=bins, weights=w_nom_np,
    histtype="step", label="Nominal", color="black"
)
ax1.hist(
    mjj_np, bins=bins, weights=w_up_np,
    histtype="step", label="Prefiring Up", color="red"
)

ax1.set_ylabel("Events (weighted)")
ax1.legend()
ax1.grid(True)
ax1.set_xticklabels([])

# --- RATIO PLOT ---
ax2 = fig.add_subplot(gs[1], sharex=ax1)

# Calcoliamo ratio bin-per-bin
nom_hist, _ = np.histogram(mjj_np, bins=bins, weights=w_nom_np)
up_hist,  _ = np.histogram(mjj_np, bins=bins, weights=w_up_np)

# Evita divisione per zero
ratio = np.divide(up_hist, nom_hist, out=np.zeros_like(up_hist), where=nom_hist!=0)

##stampa media di ratio (saltando zeri)
mean_ratio = np.mean(ratio[ratio != 0])
print("Mean Up/Nom ratio (excluding zeros): {:.4f}".format(mean_ratio))

bin_centers = 0.5 * (bins[:-1] + bins[1:])

ax2.plot(bin_centers, ratio, "o-", color="blue")
ax2.axhline(1.0, color="gray", linestyle="--")

ax2.set_xlabel(r"$m_{jj}$ [GeV]")
ax2.set_ylabel("Up/Nom")
ax2.grid(True)
ax2.set_ylim(0.95, 1.05)

# --- SALVATAGGIO ---
plt.tight_layout()
plt.savefig("mjj_prefiring_ratio.png", dpi=150)
plt.show()