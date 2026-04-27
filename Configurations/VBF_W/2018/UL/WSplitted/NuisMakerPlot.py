
import argparse
import ROOT
import numpy as np
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt
import sys
import os
import inspect
import collections
import shutil
import json
from collections import defaultdict,OrderedDict
ROOT.gROOT.SetBatch(True)

from matplotlib.colors import to_rgba


SYSTEMATIC_GROUPS = {
    "QCD": {
        "members": [
            "QCDscale",
        ],
        "color": "#56B4E9",  # arancio
        "pattern": "//"  
    },
    "PDF": {
        "members": [
            "pdf_weight",
        ],
        "color": "#D55E00",  # arancio
        "pattern": "++"  
    },
    "PS": {
        "members": [
            "CMS_PS",
        ],
        "color": "#CC79A7",  # arancio
        "pattern": ".."  
    },
}

# SYSTEMATIC_GROUPS = {
#     # === Theory uncertainties ===
#     # "theory": {
#     #     "members": [
#     #         "CMS_top_pT_reweighting",
#     #         "QCDscale",
#     #         "UE_CP5", "pdf_weight",
#     #         "singleTopToTTbar",
#     #         "CMS_PS",
#     #     ],
#     #     "color": "#E69F00",  # arancio
#     #     "pattern": "//"  
#     # },

#     # === Experimental uncertainties ===
#     "experimental": {
#         "members": [
#             # Efficiencies & triggers
#             "CMS_eff",
#             # PU jet ID, pileup, lumi
#             "CMS_jetpuid",
#             "CMS_PU_2016",
#             "lumi_13TeV",
#             # Fakes & data-driven corrections
#             "CMS_fake_stat", "CMS_fake_syst",
#             "VBFW_fake_", "VBFW_WJets_rew_",
#         ],
#         "color": "#56B4E9",
#         "pattern": ".."
#     },

#     # === Calibration: b-tagging ===
#     "btag": {
#         "members": [
#             "CMS_btag",
#         ],
#         "color": "#009E73",
#         "pattern": "oo" 
#     },

#     # === Calibration: JES/JER ===
#     "JEC": {
#         "members": [
#             "CMS_res_j_2016", "CMS_res_j_2017",
#             "CMS_scale_JES", "CMS_scale_JER",
#         ],
#         "color": "#D55E00", # arancio scuro
#         "pattern": "++"
#     },

#     # === Calibration: lepton / MET scales ===
#     "scale": {
#         "members": [
#             "CMS_scale_e_", "CMS_scale_m_", "CMS_scale_met_",
#         ],
#         "color": "#CC79A7",
#         "pattern": "xx"
#     },

# }


# SYSTEMATIC_GROUPS = {
#     # === Theory uncertainties ===
#     "theory": {
#         "members": [
#             "CMS_top_pT_reweighting",
#             "QCDscale",
#             "UE_CP5", "pdf_weight",
#             "singleTopToTTbar",
#             "CMS_PS",
#         ],
#         "color": "#E69F00",  # arancio
#         "pattern": "//"  
#     },

#     # === Experimental uncertainties ===
#     "experimental": {
#         "members": [
#             # Efficiencies & triggers
#             "CMS_eff",
#             # PU jet ID, pileup, lumi
#             "CMS_jetpuid",
#             "CMS_PU_2016",
#             "lumi_13TeV",
#             "lumi_13TeV",
#             # Fakes & data-driven corrections
#             "CMS_fake_stat", "CMS_fake_syst",
#             "VBFW_fake_", "VBFW_WJets_rew_",

#             ##btag
#             "CMS_btag",

#             ## JEC/JER
#             "CMS_res_j_2016", "CMS_res_j_2017",
#             "CMS_scale_JES", "CMS_scale_JER",
#             ## lepton/MET scales
#             "CMS_scale_e_", "CMS_scale_m_", "CMS_scale_met_",


#         ],
#         "color": "#56B4E9",
#         "pattern": ".."
#     }

# }

def list_dirs(obj):
    return [k.GetName() for k in obj.GetListOfKeys() if k.IsFolder()]

def find_histograms(rootfile, region, variable, sample, valid_nuisances=None):
    base_path = f"{region}/{variable}"
    nominal_name = f"{base_path}/histo_{sample}"
    nominal = rootfile.Get(nominal_name)
    if not nominal:
        return None, {}

    all_keys = [k.GetName() for k in rootfile.Get(base_path).GetListOfKeys()]
    systs = {}
    for k in all_keys:
        # Caso standard: Up/Down
        if k.startswith(f"histo_{sample}_") and k.endswith("Up"):
            syst = k[len(f"histo_{sample}_"):-2]
            if valid_nuisances and syst not in valid_nuisances:
                print(f"[DEBUG] ❌ '{syst}' ignorata: non è in nuisances.py (name)")
                continue

            up = rootfile.Get(f"{base_path}/histo_{sample}_{syst}Up")
            down = rootfile.Get(f"{base_path}/histo_{sample}_{syst}Down")
            if up and down:
                systs[syst] = (up, down)

        # 🔸 Caso speciale: QCDscale_WLNuJJ_acceptVar*
        elif (
            k.startswith(f"histo_{sample}_QCDscale_WLNuJJ_accept")
            and k.endswith("Var")
        ):
            # Prepara le 6 variazioni (V0..V5)
            var_hists = []
            for i in range(6):
                hname = f"{base_path}/histo_{sample}_QCDscale_WLNuJJ_acceptV{i}Var"
                h = rootfile.Get(hname)
                if not h:
                    print(f"[DEBUG] ⚠️ Manca {hname}")
                    continue
                var_hists.append(h)

            if len(var_hists) < 6:
                print(f"[DEBUG] ⚠️ Sistematiche Var incomplete, skip.")
                continue

            # --- Raggruppamento fisico ---
            # V0 (corr down)  | V5 (corr up)
            # V1 (μR down)    | V4 (μR up)
            # V2 (μF down)    | V3 (μF up)

            systs["QCDscale_muR"] = (var_hists[1], var_hists[4])
            systs["QCDscale_muF"] = (var_hists[2], var_hists[3])
            systs["QCDscale_corr"] = (var_hists[0], var_hists[5])

            print(f"[DEBUG] ✅ Sistematiche speciali 'QCDscale_WLNuJJ_accept' scomposte in muR, muF, corr")

    return nominal, systs

def load_nuisances(nuisance_file, sample_names):
    full_context = {
        "__builtins__": __builtins__,
        "samples": {name: None for name in sample_names},
        "eleWP": "mvaFall17V2Iso_WP90_tthmva_70", 
        "muWP": "cut_Tight_HWWW_tthmva_80",  
        "mcDirectoryLat": "/path/to/mc/directory",
        "nuisances": {}, 
        # Mock delle funzioni che causano problemi
        "getSampleFiles": lambda *args, **kwargs: [],
        "getBaseW": lambda *args, **kwargs: "",
        "addSampleWeight": lambda *args, **kwargs: None,
        "os": os,
        "collections": collections,
        "json": json,
        "defaultdict": defaultdict,
        "OrderedDict": OrderedDict,
        "re": __import__("re"),
        "pprint": __import__("pprint").pprint,
    }


    try:
        with open(nuisance_file, "r") as f:
            lines = f.readlines()

        # Rimuovi gli import
        clean_lines = []
        for line in lines:
            if line.strip().startswith("import") or line.strip().startswith("from "):
                continue
            clean_lines.append(line)

        code = compile("".join(clean_lines), nuisance_file, 'exec')
        exec(code, full_context)  # tutto in un unico contesto

    except Exception as e:
        print(f"⚠️ Errore durante l'import di {nuisance_file}.\nImporta solo i dati necessari nel file, oppure commenta gli import esterni.\nErrore: {e}")
        sys.exit(1)

    if "nuisances" not in full_context:
        raise ValueError(f"File {nuisance_file} non definisce un dizionario 'nuisances'.")

    nuisance_dict = full_context["nuisances"]
    nuisance_names = {entry["name"] for entry in nuisance_dict.values() if "name" in entry}
    return nuisance_names



def plot_ratio(region, variable, sample, nominal, syst_name, up, down, outdir):
    """
    Produce un plot con parte principale (valori assoluti) e rapporto rispetto al nominale.
    Gestisce sia il caso standard (un solo up/down) che il caso multiplo (liste di istogrammi, es. V0..V5).
    """
    index_php_src = "/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/plots/index.php"

    # =======================
    # Verifiche preliminari
    # =======================
    if nominal is None:
        print(f"[DEBUG] ❌ Istogramma nominale mancante per {region}/{variable}/{sample}")
        return

    if up is None or down is None:
        print(f"[DEBUG] ❌ Sistematiche mancanti per {syst_name} in {sample}")
        return

    # =====================================
    # CASO SPECIALE: liste multiple di TH1
    # =====================================
    if isinstance(up, list) and all(hasattr(h, "GetNbinsX") for h in up):
        print(f"[DEBUG] ⚙️ Sistematiche multiple (lista di TH1) rilevate per {syst_name}")

        # Numero di bin e asse x
        nbins = up[0].GetNbinsX()
        x = np.array([up[0].GetBinCenter(i+1) for i in range(nbins)])
        nom_vals = np.array([nominal.GetBinContent(i+1) for i in range(nbins)])

        # Calcolo dei ratio per ciascun istogramma up/down
        up_ratios = []
        down_ratios = []
        for h in up:
            vals = np.array([h.GetBinContent(i+1) for i in range(nbins)])
            r = np.divide(vals, nom_vals, out=np.full_like(vals, np.nan), where=nom_vals!=0)
            up_ratios.append(r)
        for h in down:
            vals = np.array([h.GetBinContent(i+1) for i in range(nbins)])
            r = np.divide(vals, nom_vals, out=np.full_like(vals, np.nan), where=nom_vals!=0)
            down_ratios.append(r)

        # ------------------------------
        # Creazione figure e subplots
        # ------------------------------
        fig, (ax_main, ax_ratio) = plt.subplots(
            2, 1, sharex=True,
            gridspec_kw={'height_ratios': [2, 1]},
            figsize=(8, 6)
        )

        # MAIN plot
        ax_main.step(x, nom_vals, where='mid', color='black', label='Nominal')

        from matplotlib.colors import to_rgba

        # Più caldi per le Up (dal salmone all’arancio acceso)
        cmap_up = [to_rgba(c) for c in ["#FFB3A7", "#FF8066", "#FF4C33", "#FF1A00"][:len(up)]]

        # Più freddi per le Down (dal celeste al blu medio)
        cmap_down = [to_rgba(c) for c in ["#A7D8FF", "#66B2FF", "#3385FF", "#0066CC"][:len(down)]]

        for i, h in enumerate(up):
            vals = np.array([h.GetBinContent(j+1) for j in range(nbins)])
            ax_main.step(x, vals, where='mid', color=cmap_up[i],
                         label=f'V{i}', linewidth=1.5)
        for i, h in enumerate(down):
            vals = np.array([h.GetBinContent(j+1) for j in range(nbins)])
            ax_main.step(x, vals, where='mid', color=cmap_down[i],
                         label=f'V{i+3}', linewidth=1.5)

        ax_main.set_ylabel('Content')
        ax_main.set_title(f"{region}/{variable} - {sample} - {syst_name}")
        ax_main.legend(fontsize=8, ncol=2)
        ax_main.grid(True, linestyle='--', alpha=0.3)

        # RATIO plot
        for i, r in enumerate(up_ratios):
            ax_ratio.step(x, r, where='mid', color=cmap_up[i], linewidth=1.5)
        for i, r in enumerate(down_ratios):
            ax_ratio.step(x, r, where='mid', color=cmap_down[i], linewidth=1.5)

        ax_ratio.axhline(1.0, color='gray', linestyle='--')
        ax_ratio.set_ylabel('Ratio')
        ax_ratio.set_xlabel('Bin')
        ax_ratio.grid(True, linestyle='--', linewidth=0.5)

        # Range automatico ma simmetrico attorno a 1
        all_ratios = np.concatenate(up_ratios + down_ratios)
        all_ratios = all_ratios[np.isfinite(all_ratios)]
        if len(all_ratios) > 0:
            max_dev = max(abs(all_ratios - 1))
            pad = 0.1 * max_dev
            ax_ratio.set_ylim(1 - max_dev - pad, 1 + max_dev + pad)

        # ======================
        # Salvataggio del plot
        # ======================
        outpath = os.path.join(outdir, region, variable, sample)
        endsure_directory_with_index_php(outpath, index_php_src)

        outfile_base = os.path.join(outpath, f"{sample}_{syst_name}_multi_ratio")

        plt.savefig(f"{outfile_base}.png", dpi=150)
        plt.savefig(f"{outfile_base}.pdf")

        plt.close(fig)
        print(f"[DEBUG] ✅ Plot multiplo salvato in {outfile_base}.png e {outfile_base}.pdf")
        return

    # =====================================
    # CASO STANDARD: singolo Up/Down (TH1)
    # =====================================
    if not hasattr(up, "GetNbinsX") or not hasattr(down, "GetNbinsX"):
        print(f"[DEBUG] ⚠️ Tipo di input non riconosciuto per {syst_name}, salto.")
        return

    nbins_nom = nominal.GetNbinsX()
    nbins_up = up.GetNbinsX()
    nbins_down = down.GetNbinsX()
    if nbins_nom != nbins_up or nbins_nom != nbins_down:
        print(f"[DEBUG] ⚠️ Numero di bin non corrisponde per {sample} {syst_name}")
        return

    x = np.array([nominal.GetBinCenter(i+1) for i in range(nbins_nom)])
    nom_vals = np.array([nominal.GetBinContent(i+1) for i in range(nbins_nom)])
    up_vals = np.array([up.GetBinContent(i+1) for i in range(nbins_up)])
    down_vals = np.array([down.GetBinContent(i+1) for i in range(nbins_down)])

    with np.errstate(divide='ignore', invalid='ignore'):
        ratio_up = np.divide(up_vals, nom_vals, out=np.full_like(up_vals, np.nan), where=nom_vals!=0)
        ratio_down = np.divide(down_vals, nom_vals, out=np.full_like(down_vals, np.nan), where=nom_vals!=0)

    # ------------------------------
    # Plot standard
    # ------------------------------
    fig, (ax_main, ax_ratio) = plt.subplots(
        2, 1, sharex=True,
        gridspec_kw={'height_ratios': [2, 1]},
        figsize=(8, 6)
    )

    ax_main.step(x, nom_vals, where='mid', label='Nominal', color='black')
    ax_main.step(x, up_vals, where='mid', label='Up', color='red')
    ax_main.step(x, down_vals, where='mid', label='Down', color='blue')
    ax_main.set_ylabel('Content')
    ax_main.set_title(f"{region}/{variable} - {sample} - {syst_name}")
    ax_main.legend()

    ax_ratio.step(x, ratio_up, where='mid', color='red', label='Up/Nom')
    ax_ratio.step(x, ratio_down, where='mid', color='blue', label='Down/Nom')
    ax_ratio.axhline(1.0, color='gray', linestyle='--')
    ax_ratio.set_xlabel('Bin')
    ax_ratio.set_ylabel('Ratio')
    ax_ratio.grid(True, linestyle='--', linewidth=0.5)
    ax_ratio.legend()

    outpath = os.path.join(outdir, region, variable, sample)
    ensure_directory_with_index_php(outpath, index_php_src)

    ## sia png che pdf
    outfile_base = os.path.join(outpath, f"{sample}_{syst_name}_ratio")

    plt.savefig(f"{outfile_base}.png", dpi=150)
    plt.savefig(f"{outfile_base}.pdf")

    plt.close(fig)
    print(f"[DEBUG] ✅ Plot salvato in {outfile_base}.png e {outfile_base}.pdf")


def plot_systematic_breakdown(region, variable, sample, nominal, syst_dict, outdir, systematic_groups):
    """
    Aggrega sistematiche in gruppi, somma in quadratura e produce un breakdown plot con up/down.
    """
    index_php_src = "/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/plots/index.php"
    ordered_groups = ["experimental", "btag", "scale", "JEC", "theory"]
    ordered_groups = ["experimental", "btag", "scale", "JEC"]
    ordered_groups = ["PS", "PDF", "QCD"]
    # ordered_groups = ["experimental", "theory"]
    ## reverse the order for better visibility in the plot
    ordered_groups = ordered_groups[::-1]

    if nominal is None or not syst_dict:
        print(f"[DEBUG] ❌ Dati mancanti per {region}/{variable}/{sample}")
        return

    nbins = nominal.GetNbinsX()
    # Bin edges reali dal ROOT histogram
    edges = np.array([nominal.GetBinLowEdge(i+1) for i in range(nbins+1)])
    centers = edges[:-1] + 0.5 * np.diff(edges)

    # Usati per disegnare le bande
    nom_vals = np.array([nominal.GetBinContent(i+1) for i in range(nbins)])

    # Per step/ratio/bande usiamo GLI SPIGOLI!
    x_edges = edges

    # Inizializza dizionario gruppi
    group_up = {}
    group_down = {}

    for group, info in systematic_groups.items():
        color = info.get("color", "gray")
        hatch = info.get("pattern", "")
        members = info["members"]

        # somma in quadratura per bin
        up2 = np.zeros(nbins)
        down2 = np.zeros(nbins)

        for syst_name, (h_up, h_down) in syst_dict.items():
            if any(m in syst_name for m in members):
                vals_up = np.array([h_up.GetBinContent(i+1) for i in range(nbins)])
                vals_down = np.array([h_down.GetBinContent(i+1) for i in range(nbins)])
                diff_up = np.abs(vals_up - nom_vals)
                diff_down = np.abs(vals_down - nom_vals)
                up2 += diff_up**2
                down2 += diff_down**2

        group_up[group] = np.sqrt(up2)
        group_down[group] = np.sqrt(down2)

    # Calcolo totale
    total_up = np.sqrt(np.sum([v**2 for v in group_up.values()], axis=0))
    total_down = np.sqrt(np.sum([v**2 for v in group_down.values()], axis=0))
    group_up["TOTAL"] = total_up
    group_down["TOTAL"] = total_down
    systematic_groups["TOTAL"] = {"color": "black", "members": []}

    # === Plot ===
    fig, (ax_main, ax_ratio) = plt.subplots(2, 1, sharex=True,
                                            gridspec_kw={'height_ratios':[2,1]},
                                            figsize=(8,6))

    # MAIN plot
    ax_main.step(x_edges, np.r_[nom_vals, nom_vals[-1]],
             where='post', color='k', linewidth=1.5)

    for group in ordered_groups:
        if group not in group_up: 
            continue
        if group == "TOTAL":
            continue

        info = systematic_groups.get(group, {})
        color = info.get("color", "gray")
        hatch = info.get("pattern", "")

        up = nom_vals + group_up[group]
        down = nom_vals - group_down[group]

        ax_main.fill_between(
            x_edges, 
            np.r_[down, down[-1]],
            np.r_[up, up[-1]],
            step='post',
            facecolor=color,        # pastello
            edgecolor=color,      # outline per leggibilità
            hatch=hatch,            # pattern distintivo
            alpha=0.50,
            linewidth=0.5,
            label=group
        )

    ax_main.set_ylabel("Events")
    ax_main.set_title(f"{region}/{variable} - {sample} (Grouped systematics)")
    ax_main.legend(ncol=2, fontsize=8)
    ax_main.grid(True, linestyle="--", alpha=0.3)

    # --- Breakdown per gruppo ---
    for group in ordered_groups:
        info = systematic_groups.get(group, {})
        color = info.get("color", "gray")
        hatch = info.get("pattern", "")

        ratio_up = 1 + group_up[group] / np.maximum(nom_vals, 1e-8)
        ratio_down = 1 - group_down[group] / np.maximum(nom_vals, 1e-8)

        ratio_up_ext = np.r_[ratio_up, ratio_up[-1]]
        ratio_down_ext = np.r_[ratio_down, ratio_down[-1]]

        ax_ratio.fill_between(
            x_edges,
            ratio_down_ext,
            ratio_up_ext,
            step='post',
            facecolor=color,
            alpha=0.5,
            edgecolor=color,
            hatch=hatch,
            linewidth=0.0,
            label=group
        )

    # --- Linea del totale ---
    total_up = group_up["TOTAL"] / np.maximum(nom_vals, 1e-8)
    total_down = group_down["TOTAL"] / np.maximum(nom_vals, 1e-8)

    # Prepara array esteso con nbins+1 valori
    total_up_ext = np.r_[total_up, total_up[-1]]
    total_down_ext = np.r_[total_down, total_down[-1]]

    # Disegno tratteggiato su edges
    ax_ratio.step(
        x_edges, 1 + total_up_ext,
        where='post', color='black', linestyle='--', linewidth=1.3, label="TOTAL"
    )
    ax_ratio.step(
        x_edges, 1 - total_down_ext,
        where='post', color='black', linestyle='--', linewidth=1.3
    )
    # Styling
    ax_ratio.axhline(1.0, color='gray', linestyle='--')
    ax_ratio.set_ylim(0.5, 1.5)  # regolabile se serve
    ax_ratio.set_ylabel("Uncertainty ratio")
    ax_ratio.set_xlabel(variable)
    ax_ratio.grid(True, linestyle="--", linewidth=0.5)

    # Applica alle due assi (main e ratio)
    # ax_main.set_xlim(x_left, x_right)
    # ax_ratio.set_xlim(x_left, x_right)

    # Save
    outpath = os.path.join(outdir, region, variable, sample)
    os.makedirs(outpath, exist_ok=True)

    # Copia index.php in ogni livello gerarchico dell'output
    levels = outpath.split(os.sep)
    for i in range(1, len(levels) + 1):
        folder = os.sep.join(levels[:i])
        if folder:
            os.makedirs(folder, exist_ok=True)
            os.system(f"cp {index_php_src} '{folder}/index.php'")

    outfile = os.path.join(outpath, f"{sample}_systBreakdown_detail_th")
    plt.savefig(f"{outfile}.png", dpi=150)
    plt.savefig(f"{outfile}.pdf")
    plt.close(fig)

    print(f"[DEBUG] ✅ Breakdown plot salvato in {outfile}.png/.pdf")

def ensure_directory_with_index_php(path, index_php_src):
    os.makedirs(path, exist_ok=True)
    index_php_dst = os.path.join(path, 'index.php')
    if os.path.exists(index_php_src):
        shutil.copy(index_php_src, index_php_dst)


def worker(args):
    inputfile, region, variable, sample, outdir, valid_nuisances = args
    rootfile = ROOT.TFile.Open(inputfile, "READ")
    nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
    if nominal and systs:
        for syst, (up, down) in systs.items():
            plot_ratio(region, variable, sample, nominal, syst, up, down, outdir)
        # plot_systematic_breakdown(region, variable, sample, nominal, systs, outdir, SYSTEMATIC_GROUPS)
    rootfile.Close()


def load_samples_keys(samples_path):
    samples = {}

    fake_globals = {
        "__builtins__": __builtins__,
        "samples": samples,
        "nanoGetSampleFiles": lambda *args, **kwargs: [],
        "mcDirectoryLat": "",
        "XSWeight": "",
        "SFweight": "",
        "METFilter_MC": "",
        "GenLepMatch": "",
        "CommonWeight": "",
        "os": os,  # Aggiungiamo os
        "inspect": inspect,  # Aggiungiamo inspect
        "collections": collections,  # Aggiungiamo collections
        "getSampleFiles": lambda *args, **kwargs: [],
        "addSampleWeight": lambda *args, **kwargs: [],
        "CMSSW_BASE": os.environ.get("CMSSW_BASE", ""),
    }

    try:
        with open(samples_path, "r") as f:
            lines = f.readlines()

        clean_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("import") or stripped.startswith("from "):
                continue
            clean_lines.append(line)

        code = "".join(clean_lines)
        exec(code, fake_globals)

    except Exception as e:
        print(f"⚠️ Errore durante l'import di {samples_path}.\nImporta solo i dati necessari nel file, oppure commenta gli import esterni.\nErrore: {e}")
        sys.exit(1)

    return list(fake_globals["samples"].keys())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input ROOT file")
    parser.add_argument("--samples", required=True, help="Path to a Python file that defines the 'samples' dict")
    parser.add_argument("--nuisances", help="Path to nuisances.py file (must define a 'nuisances' dict)")
    parser.add_argument("--outdir", default="ratio_plots", help="Output directory")
    parser.add_argument("--onlyCut", nargs='+', help="Restrict to specific regions", default=[])
    parser.add_argument("--onlyVar", nargs='+', help="Restrict to specific variables", default=[])
    parser.add_argument("--onlySample", nargs='+', help="Restrict to specific samples", default=[])
    parser.add_argument("--onlySyst", nargs='+', help="Restrict to specific systematics", default=[])
    parser.add_argument("--workers", type=int, default=cpu_count(), help="Number of parallel workers")
    args = parser.parse_args()

    rootfile = ROOT.TFile.Open(args.input, "READ")

    regions = list_dirs(rootfile)
    if args.onlyCut:
        regions = [r for r in regions if any(cut in r for cut in args.onlyCut)]

    sample_names = load_samples_keys(args.samples)
    # ops=["cW","cHDD","cHWB"]
    ops=[]
    for op1 in ops:
        sample_names.append(f"sm_lin_quad_{op1}")
        sample_names.append(f"quad_{op1}")
        for op2 in ops:
            if op1 != op2:
                sample_names.append(f"sm_lin_quad_mixed_{op1}_{op2}")
    if args.onlySample:
        sample_names = [s for s in sample_names if any(sample in s for sample in args.onlySample)]

    valid_nuisances = None
    if args.nuisances:
        valid_nuisances = load_nuisances(args.nuisances, sample_names)
        if args.onlySyst:
            valid_nuisances = [n for n in valid_nuisances if any(syst in n for syst in args.onlySyst)]

    if isinstance(valid_nuisances, list):
        valid_nuisances = set(valid_nuisances)

    # valid_nuisances = valid_nuisances | {"QCDscale_WLNuJJ_acceptV1Var", "QCDscale_WLNuJJ_acceptV2Var", "QCDscale_WLNuJJ_acceptV3Var", "QCDscale_WLNuJJ_acceptV4Var", "QCDscale_WLNuJJ_acceptV5Var", "QCDscale_WLNuJJ_acceptV6Var"}
    tasks = []
    for region in regions:
        region_dir = rootfile.Get(region)
        variables = list_dirs(region_dir)
        if args.onlyVar:
            variables = [v for v in variables if any(v == var for var in args.onlyVar)]
        for variable in variables:
            for sample in sample_names:
                if args.onlySample and sample not in args.onlySample:
                    continue
                tasks.append((args.input, region, variable, sample, args.outdir, valid_nuisances))

    print(f"Launching {len(tasks)} tasks with {args.workers} workers...")
    with Pool(args.workers) as pool:
        pool.map(worker, tasks)

    print(f"All done. Plots saved to: {args.outdir}")