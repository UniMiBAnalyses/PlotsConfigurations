from pprint import pprint
import re
from collections import defaultdict, OrderedDict
# # # name of samples here must match keys in samples.py 

# mc_bkg =["Wjets_HT_hardJets","Wjets_HT_PUJets", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
mc_bkg =["Wjets_HT_hardJets","Wjets_HT_PUJets", "top", "DY_M-50", "Others"]
signals = [c for c in samples if "WLNuJJ" in c and "Out" not in c] 
out = [ c for c in samples if "Out" in c]

mc_bkg = mc_bkg + out

mc = signals + mc_bkg

regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","ele_topcr","mu_topcr","ele_FakeCR","mu_FakeCR"]

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]

bkg_to_norm = ['top', 'Wjets_HT_hardJets', 'Wjets_HT_PUJets']
# # # # # # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

def merge_nuisances(nuisances):
    # Step 1: Raggruppa le keys per "name"
    name_to_keys = defaultdict(list)

    for key, nuis in nuisances.items():
        name = nuis.get('name')
        if name:
            name_to_keys[name].append(key)

    # Step 2: Per ogni gruppo di keys con lo stesso "name", fai il merge
    merged_nuisances = OrderedDict()

    # Mantieni l'ordine di apparizione di 'name' in nuisances
    seen_names = []
    for key, nuis in nuisances.items():
        name = nuis.get('name')
        if name and name not in seen_names:
            seen_names.append(name)

    for name in seen_names:
        keys = name_to_keys[name]

        # Usa la prima entry come base
        base_key = keys[0]
        base_nuis = dict(nuisances[base_key])  # copia

        # Mergia 'samples' e 'cuts' da tutte le altre entries
        merged_samples = dict(base_nuis.get('samples', {}))
        merged_cuts = list(base_nuis.get('cuts', []))  # se non esiste 'cuts', prende lista vuota

        for other_key in keys[1:]:
            other_nuis = nuisances[other_key]

            # Unisci samples
            for sample, val in other_nuis.get('samples', {}).items():
                merged_samples[sample] = val

            # Unisci cuts solo se esiste in questa nuisance
            if 'cuts' in other_nuis:
                merged_cuts.extend(other_nuis.get('cuts', []))

        # Rimuovi duplicati in cuts
        if merged_cuts:
            merged_cuts = sorted(set(merged_cuts))
            base_nuis['cuts'] = merged_cuts
        elif 'cuts' in base_nuis:
            del base_nuis['cuts']  # se alla fine non ci sono cuts, rimuovi

        # Aggiorna la nuisance unificata
        base_nuis['samples'] = merged_samples

        # Mantieni la chiave master (es: 'JESAbsolute') se esiste
        master_key = None
        for k in keys:
            if not ('_ele' in k or '_mu' in k):
                master_key = k
                break
        if not master_key:
            master_key = base_key  # fallback

        merged_nuisances[master_key] = base_nuis

    return merged_nuisances

# # #### Luminosity

# https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#LumiComb
# Uncorrelated 2016               1.0
# Uncorrelated       2017              2.0
# Uncorrelated             2018             1.5
# Correlated   2016, 2017, 2018   0.6, 0.9, 2.0
# Correlated         2017, 2018        0.6, 0.2

nuisances['lumi_Uncorrelated'] = {
    'name'    : 'lumi_13TeV_2017',
    'type'    : 'lnN',
    'samples' : dict((skey, '1.020') for skey in mc if skey not in ["top", "Wjets_HT_hardJets", "Wjets_HT_PUJets"])
}

nuisances['lumi_Correlated_Run2'] = {
    'name'    : 'lumi_13TeV_correlated',
    'type'    : 'lnN',
    'samples' : dict((skey, '1.009') for skey in mc if skey not in ["top", "Wjets_HT_hardJets", "Wjets_HT_PUJets"])
}

nuisances['lumi_Correlated_2017_2018'] = {
    'name'    : 'lumi_13TeV_1718',
    'type'    : 'lnN',
    'samples' : dict((skey, '1.006') for skey in mc if skey not in ["top", "Wjets_HT_hardJets", "Wjets_HT_PUJets"])
}

##########Fakes
# fakeW_jetUp       = '( fakeWeight_45 / fakeWeight_35  )'
# fakeW_jetDown     =  '( fakeWeight_25 / fakeWeight_35  )'
## not a systematic because i preselect my phase-space!
fakeW_statUp = '\
(\
    (fakeWeight_0p9 <= 20) *\
    (\
        (abs(fakeWeight_statUp / fakeWeight_0p9 - 1) <= 0.3) * (fakeWeight_statUp / fakeWeight_0p9) +\
        (abs(fakeWeight_statUp / fakeWeight_0p9 - 1) > 0.3) * 1.\
    )\
)\
'

fakeW_statDown = '\
(\
    (fakeWeight_0p9 <= 20) *\
    (\
        (abs(fakeWeight_statDo / fakeWeight_0p9 - 1) <= 0.3) * (fakeWeight_statDo / fakeWeight_0p9) +\
        (abs(fakeWeight_statDo / fakeWeight_0p9 - 1) > 0.3) * 1.\
    )\
)\
'

fakeW_EWKsubUp = '\
(\
    (fakeWeight_0p9 <= 20) *\
    (\
        (abs(fakeWeight_0p9Up / fakeWeight_0p9 - 1) <= 0.3) * (fakeWeight_0p9Up / fakeWeight_0p9) +\
        (abs(fakeWeight_0p9Up / fakeWeight_0p9 - 1) > 0.3) * 1.\
    )\
)\
'

fakeW_EWKsubDown = '\
(\
    (fakeWeight_0p9 <= 20) *\
    (\
        (abs(fakeWeight_0p9Down / fakeWeight_0p9 - 1) <= 0.3) * (fakeWeight_0p9Down / fakeWeight_0p9) +\
        (abs(fakeWeight_0p9Down / fakeWeight_0p9 - 1) > 0.3) * 1.\
    )\
)\
'

nuisances['fake_syst_ele']  = {
               'name'  : 'CMS_fake_syst_ele',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
               'cuts': phase_spaces_tot_ele,
               }

nuisances['fake_syst_mu']  = {
               'name'  : 'CMS_fake_syst_mu',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
                'cuts': phase_spaces_tot_mu,
               }


nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_stat_e_2017_1lep',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statUp , fakeW_statDown ],
                             },
                'cuts':  phase_spaces_tot_ele,
                'AsLnN' : '1',
}

nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_stat_m_2017_1lep',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     :[ fakeW_statUp , fakeW_statDown ],
                             },
                'cuts':  phase_spaces_tot_mu,
                'AsLnN' : '1',
}

nuisances['fake_ele_EWKsub']  = {
                'name'  : 'VBFW_fake_e_EWKsub_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_EWKsubUp , fakeW_EWKsubDown ],
                             },
                'cuts':  phase_spaces_tot_ele,
                'AsLnN' : '1',
}

nuisances['fake_mu_EWKsub']  = {
                'name'  : 'VBFW_fake_m_EWKsub_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_EWKsubUp , fakeW_EWKsubDown ],
                             },
                'cuts':  phase_spaces_tot_mu,
                'AsLnN' : '1',
}


prefire_syst = ['L1PreFiringWeight_Up/L1PreFiringWeight_Nom', 'L1PreFiringWeight_Dn/L1PreFiringWeight_Nom']
nuisances['prefire']  = {
                'name'  : 'CMS_eff_prefiring_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, prefire_syst) for skey in mc)
}


# # ##### Btag nuisances

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc)
    }

# # # ##### Trigger Efficiency

# trig_syst = ['((TriggerSFWeight_1l_u)/(TriggerSFWeight_1l))*(TriggerSFWeight_1l>0.02) + (TriggerSFWeight_1l<=0.02)', '(TriggerSFWeight_1l_d)/(TriggerSFWeight_1l)']
trig_syst = ['((TriggerSFWeight_1l_u)/(TriggerSFWeight_1l))', '(TriggerSFWeight_1l_d)/(TriggerSFWeight_1l)']

nuisances['trigg']  = {
                'name'  : 'CMS_eff_trigger_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' :  dict((skey, trig_syst) for skey in mc),
                'symmetrize': True
}


# # # ##### Electron Efficiency and energy scale

ele_id_syst_up = '(abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'_Up[0])/\
                    (Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 13)'
ele_id_syst_do = '(abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'_Down[0])/\
                    (Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 13)'
mu_id_syst_up = '(abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'_Up[0])/\
                    (Lepton_tightMuon_'+muWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 11)'
mu_id_syst_do = '(abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'_Down[0])/\
                    (Lepton_tightMuon_'+muWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 11)'

id_syst_ele = [ ele_id_syst_up, ele_id_syst_do ]
id_syst_mu = [ mu_id_syst_up, mu_id_syst_do ]

nuisances['eff_e']  = {
                'name'  : 'CMS_eff_e_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :   dict((skey, id_syst_ele) for skey in mc ),
                'cuts': phase_spaces_tot_ele
}

nuisances['electronpt']  = {
                'name'  : 'CMS_scale_e_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'ElepTup',
                'mapDown': 'ElepTdo',
                'cuts': phase_spaces_tot_ele,
                'samples': dict((skey, ['1.','1.']) for skey in mc),
                'folderUp' : mcDirectoryLat+'__ElepTup_suffix',
                'folderDown' : mcDirectoryLat+'__ElepTdo_suffix'
}

# # # ##### Muon Efficiency and energy scale

nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_mu) for skey in mc),
                'cuts': phase_spaces_tot_mu,
}

nuisances['muonpt']  = {
                'name'  : 'CMS_scale_m_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'MupTup',
                'mapDown': 'MupTdo',
                'cuts': phase_spaces_tot_mu,
                'samples': dict((skey, ['1.','1.']) for skey in mc),
                'folderUp' : mcDirectoryLat+'__MupTup_suffix',
                'folderDown' : mcDirectoryLat+'__MupTdo_suffix'
}

# # # ##################
# # # # PU jet id

nuisances['JetPUID_sf']  = {
                'name'  : 'CMS_jetpuid_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc )
}

# # ##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2','JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal','JESRelativeSample_2017']

for js in jes_systs:
    nuisances[js] = {
        'name': 'CMS_scale_'+js,
        'kind': 'suffix',
        'type': 'shape',
        'mapUp': js+'up',
        'mapDown': js+'do',
        # 'samples': dict((skey, ['1.', '1.']) for skey in mc if skey not in bkg_to_norm),
        'samples': dict((skey, ['1.', '1.']) for skey in mc),
        'folderUp': mcDirectoryLat+'__JESup_suffix',
        'folderDown': mcDirectoryLat+'__JESdo_suffix'
    }

# ##### Jet energy resolution
nuisances['JER'] = {
                'name': 'CMS_res_j_2017',
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': 'JERup',
                'mapDown': 'JERdo',
                'samples': dict((skey, ['1.','1.']) for skey in mc),
                'folderUp' : mcDirectoryLat+'__JERup_suffix',
                'folderDown' : mcDirectoryLat+'__JERdo_suffix',
}

# # # # # # ##### MET energy scale

nuisances['MET']  = {
                'name'  : 'CMS_scale_met_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp':   'METup',
                'mapDown': 'METdo', 
                # 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in bkg_to_norm),
                'samples': dict((skey, ['1.','1.']) for skey in mc),
                'folderUp' : mcDirectoryLat+'__METup_suffix',
                'folderDown' : mcDirectoryLat+'__METdo_suffix'
}


# # ## Top pT reweighting uncertainty

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': { 
       'top': [
        'isSingleTop * 1.0816 + isTTbar',
        'isSingleTop * 0.9184 + isTTbar']
      }
}

# # ## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
   'name': 'CMS_top_pT_reweighting',   # Theory uncertainty
   'kind': 'weight',
   'type': 'shape',
   'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
   'symmetrize': True
}


# # # # ######################
# # # # # Theory nuisance
# # # # #
# # # # # PS and UE
# # # # # #
# # # # #### USE this for producing shapes

nuisances['PS_ISR']  = {
                'name'  : 'CMS_PS_ISR',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {   sample : ['PSWeight[2]','PSWeight[0]'] for sample in mc if sample not in signals}
            }

nuisances['PS_FSR']  = {
                'name'  : 'CMS_PS_FSR',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {     
                    sample : ['PSWeight[3]','PSWeight[1]'] for sample in mc if sample not in signals}
            }

nuisances['PU']  = {
                'name'  : 'CMS_PU_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    sample : ['(puWeightUp/puWeight)','(puWeightDown/puWeight)'] for sample in mc},
}

# ## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations   = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-4],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-2],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-1],1)']

for sample in mc_bkg :
    nuisances['QCDscale_'+sample] = {
        'name'  : 'QCDscale_'+sample,
        'kind'  : 'weight_envelope',
        'type'  : 'shape',
        'samples'  :  { sample: variations }
    }
    if sample in bkg_to_norm + out:
        nuisances['pdf_weight_'+sample] = {
            'name'  : 'pdf_weight_'+sample,
            'kind'  : 'weight_square',
            'type'  : 'shape',
            'samples'  :  { sample: ['Alt$(LHEPdfWeight[{}], 1.)'.format(i) for i in range(0,103)]},
        }


### now the signal
json_file = '/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/utils/2018/nuisance_incl_norm_factors_2018_sigcharged.json'
with open(json_file) as jsonfile:
    data_sig_th = json.load(jsonfile)


for s in signals:
    # ----------------------------------------
    #   QCD SCALE ACCEPTANCE
    # ----------------------------------------
    nuis_name = "QCDscale_%s_accept" % s

    nuisances[nuis_name] = {
        'name': nuis_name,
        'kind': 'weight_envelope',
        'type': 'shape',
        'samples': {}
    }

    QCDSF = data_sig_th[s]["all"]["QCDSF"]
    weights = []

    for i in range(9):  # da 0 a 8 inclusi
        norm = QCDSF[i]
        expr = "(LHEScaleWeight[{}]/{})".format(i, norm)
        weights.append(expr)

    nuisances[nuis_name]['samples'][s] = weights


    # ----------------------------------------
    #   PDF ACCEPTANCE
    # ----------------------------------------

    nuis_name = "pdf_weight_%s_accept" % s

    nuisances[nuis_name] = {
        'name': nuis_name,
        'kind': 'weight_square',
        'type': 'shape',
        'samples': {}
    }

    PDFSF = data_sig_th[s]["all"]["PDFSF"]

    nuisances[nuis_name]['samples'][s] = [
        "Alt$(LHEPdfWeight[%d]/%s, 1.)" % (i, PDFSF[i])
        for i in range(0,103)
    ]


    # ----------------------------------------
    #   PARTON SHOWER (ISR/FSR) per singolo sample
    # ----------------------------------------
    # ---------- ISR ----------
    nuis_name_isr  = 'PS_ISR_dipole_accept_%s' % s
    nuis_label_isr = 'CMS_PS_ISR_dipole_accept_%s' % s

    PS_ISR = data_sig_th[s]['all']['PS_ISR']

    nuisances[nuis_name_isr] = {
        'name': nuis_label_isr,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
            s: [
                'PSWeight[2]/%s' % PS_ISR[0],
                'PSWeight[0]/%s' % PS_ISR[1],
            ]
        }
    }

    # ---------- FSR ----------
    nuis_name_fsr  = 'PS_FSR_dipole_accept_%s' % s
    nuis_label_fsr = 'CMS_PS_FSR_dipole_accept_%s' % s

    PS_FSR = data_sig_th[s]['all']['PS_FSR']

    nuisances[nuis_name_fsr] = {
        'name': nuis_label_fsr,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
            s: [
                'PSWeight[3]/%s' % PS_FSR[0],
                'PSWeight[1]/%s' % PS_FSR[1],
            ]
        }
    }

# # # # An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# # # # And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if skey not in ["top", "Wjets_HT_hardJets", "Wjets_HT_PUJets"])
}

# reweight wjet nuisances
WJets_up = '( WJets_reweight_up / WJets_reweight )'
WJets_do = '( WJets_reweight_do / WJets_reweight )'

nuisances['WJets_reweight_stat'] = {
    'name': 'VBFW_WJets_rew_stat_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': { 
       'Wjets_HT_hardJets': [WJets_up, WJets_do]
      }
}

WJets_functional = '( WJets_reweight_func /  WJets_reweight )'
nuisances['WJets_reweight_functional_2017'] = {
    'name': 'VBFW_WJets_rew_func_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
       'Wjets_HT_hardJets': [WJets_functional, "1."]
      },
}


# # # ####### Generic "cross section uncertainties"
# # # ##############
# # # # Normalization factors
# # # ##############

for fl in ["ele", "mu"]:
    nuisances["Top_norm_{}".format(fl)]  = {
        'name'  : 'CMS_Top_norm_{}17'.format(fl),
        'samples'  : {
            'top' : '1.00',
            },
        'range': (0.5,1.5),
        'type'  : 'rateParam',
        'cuts': [region for region in regions if fl in region]
    }

for fl in ["ele", "mu"]:
    nuisances["WPUJet_norm_{}".format(fl)]  = {
        'name'  : 'CMS_WPUJet_norm_{}17'.format(fl),
        'samples'  : {'Wjets_HT_PUJets' : '1.00'},
        'type'  : 'rateParam',
        'range': (0.5,1.5),
        'cuts': [region for region in regions if fl in region]
    }


for fl in ["ele", "mu"]:
    nuisances["WhardJet_norm_{}".format(fl)]  = {
                    'name'  : 'CMS_WhardJet_norm_{}17'.format(fl),
                    'samples'  : {'Wjets_HT_hardJets' : '1.00'},
                    'type'  : 'rateParam',
                    'range': (0.5,1.5),
                    'cuts': [region for region in regions if fl in region]
            }



for n in nuisances.values():
    n['skipCMS'] = 1

nuisances = merge_nuisances(nuisances)

# ## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '0',
            #    nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
            #    nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }