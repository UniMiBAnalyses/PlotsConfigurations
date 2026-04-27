from pprint import pprint
import json
from collections import defaultdict, OrderedDict
# # # name of samples here must match keys in samples.py 

mc_sm = ["sm", "Wjets_HT_hardJets","Wjets_HT_PUJets", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]

mc_bkg = [c for c in mc_sm if "sm" not in c]
mc_eft = [c for c in samples if any(substring in c for substring in ["lin", "quad", "mixed"])]
signals = [c for c in samples if "sm" in c and c not in mc_eft]
mc = mc_sm + mc_eft
# regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","mu_topcr","ele_topcr","ele_FakeCR","mu_FakeCR"]
regions = ["ele_SR", "mu_SR", "ele_HWJ", "mu_HWJ", "ele_PUWJ", "mu_PUWJ", "ele_topcr", "mu_topcr"]
# regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr","ele_FakeCR","mu_FakeCR"]
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]
phase_spaces_tot_sr = [ c for c in regions if 'SR' in c]

wj_region = [ c for c in regions if 'HWJ' in c]

# # Function to split a nuisance on different folders for different group of samples
bkg_to_norm = ['top', 'Wjets_HT_hardJets', 'Wjets_HT_PUJets']
# # ################################ EXPERIMENTAL UNCERTAINTIES  #################################


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
# ## TO BE  FIXED FOR COMBINATION

# # ### Luminosity

# # # https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#LumiComb
# # # Uncorrelated 2016               1.0
# # # Uncorrelated       2017              2.0
# # # Uncorrelated             2018             1.5
# # # Correlated   2016, 2017, 2018   0.6, 0.9, 2.0
# # # Correlated         2017, 2018        0.6, 0.2

# nuisances['lumi_Uncorrelated'] = {
#     'name'    : 'lumi_13TeV_2016',
#     'type'    : 'lnN',
#     'samples' : dict((skey, '1.010') for skey in mc if skey not in ["top", "Wjets_HT_hardJets", "Wjets_HT_PUJets"])
# }

# nuisances['lumi_Correlated_Run2'] = {
#     'name'    : 'lumi_13TeV_correlated',
#     'type'    : 'lnN',
#     'samples' : dict((skey, '1.006') for skey in mc if skey not in ["top", "Wjets_HT_hardJets", "Wjets_HT_PUJets"])
# }


# fakeW_statUp = '\
# (\
#     (fakeWeight_0p9 <= 20) *\
#     (\
#         (abs(fakeWeight_statUp / fakeWeight_0p9 - 1) <= 0.3) * (fakeWeight_statUp / fakeWeight_0p9) +\
#         (abs(fakeWeight_statUp / fakeWeight_0p9 - 1) > 0.3) * 1.\
#     )\
# )\
# '

# fakeW_statDown = '\
# (\
#     (fakeWeight_0p9 <= 20) *\
#     (\
#         (abs(fakeWeight_statDo / fakeWeight_0p9 - 1) <= 0.3) * (fakeWeight_statDo / fakeWeight_0p9) +\
#         (abs(fakeWeight_statDo / fakeWeight_0p9 - 1) > 0.3) * 1.\
#     )\
# )\
# '

# fakeW_EWKsubUp = '\
# (\
#     (fakeWeight_0p9 <= 20) *\
#     (\
#         (abs(fakeWeight_0p9Up / fakeWeight_0p9 - 1) <= 0.3) * (fakeWeight_0p9Up / fakeWeight_0p9) +\
#         (abs(fakeWeight_0p9Up / fakeWeight_0p9 - 1) > 0.3) * 1.\
#     )\
# )\
# '

# fakeW_EWKsubDown = '\
# (\
#     (fakeWeight_0p9 <= 20) *\
#     (\
#         (abs(fakeWeight_0p9Down / fakeWeight_0p9 - 1) <= 0.3) * (fakeWeight_0p9Down / fakeWeight_0p9) +\
#         (abs(fakeWeight_0p9Down / fakeWeight_0p9 - 1) > 0.3) * 1.\
#     )\
# )\
# '


# nuisances['fake_syst']  = {
#                'name'  : 'CMS_fake_syst',
#                'type'  : 'lnN',
#                'samples'  : {
#                              'Fake' : '1.30',
#                              }
#                }

# nuisances['fake_ele_stat']  = {
#                 'name'  : 'CMS_fake_stat_e_2016_1lep',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_statUp , fakeW_statDown ],
#                              },
#                 'cuts':  phase_spaces_tot_ele,
#                 'AsLnN' : '1',
# }

# nuisances['fake_mu_stat']  = {
#                 'name'  : 'CMS_fake_stat_m_2016_1lep',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'     :[ fakeW_statUp , fakeW_statDown ],
#                              },
#                 'cuts':  phase_spaces_tot_mu,
#                 'AsLnN' : '1',
# }

# nuisances['fake_ele_EWKsub']  = {
#                 'name'  : 'VBFW_fake_e_EWKsub_2016_HIPM',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_EWKsubUp , fakeW_EWKsubDown ],
#                              },
#                 'cuts':  phase_spaces_tot_ele,
#                 'AsLnN' : '1',
# }

# nuisances['fake_mu_EWKsub']  = {
#                 'name'  : 'VBFW_fake_m_EWKsub_2016_HIPM',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_EWKsubUp , fakeW_EWKsubDown ],
#                              },
#                 'cuts':  phase_spaces_tot_mu,
#                 'AsLnN' : '1',
# }

# # nuisances['fake_mu_PRMC']  = {
# #                 'name'  : 'VBFW_fake_m_PR_fromMC_2016_HIPM',
# #                 'kind'  : 'weight',
# #                 'type'  : 'shape',
# #                 'samples'  : {
# #                               'Fake'      : [ fakeW_PRMC , "1." ],
# #                              },
# #                 'cuts':  phase_spaces_tot_mu
# # }

# # nuisances['fake_ele_PRMC']  = {
# #                 'name'  : 'VBFW_fake_e_PR_fromMC_2016_HIPM',
# #                 'kind'  : 'weight',
# #                 'type'  : 'shape',
# #                 'samples'  : {
# #                               'Fake'      : [ fakeW_PRMC , "1." ],
# #                              },
# #                 'cuts':  phase_spaces_tot_ele
# # }

# prefire_syst = ['L1PreFiringWeight_Up/L1PreFiringWeight_Nom', '1.']
# nuisances['prefire']  = {
#                 'name'  : 'CMS_eff_prefiring_2016',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, prefire_syst) for skey in mc),
#                 'symmetrize': True,
# }


# json_file ='/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/utils/2016/HIPM/VetoAndtopCRSplit/nuisance_incl_norm_factors_2016HIPM_ele_exp.json'
# with open(json_file) as jsonfile:
#     data_exp_ele = json.load(jsonfile)

# json_file ='/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/utils/2016/HIPM/VetoAndtopCRSplit/nuisance_incl_norm_factors_2016HIPM_mu_exp.json'
# with open(json_file) as jsonfile:
#     data_exp_mu = json.load(jsonfile)

# # # ##### Btag nuisances
# ### TO BE  FIXED FOR COMBINATION


# for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
#     btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

#     name = 'CMS_btag_%s' % shift
#     if 'stats' in shift:
#         name += '_2016'

#     nuisances['btag_shape_%s' % shift] = {
#         'name': name,
#         'kind': 'weight',
#         'type': 'shape',
#         'samples': dict((skey, btag_syst) for skey in mc)
#     }

# # ##### Trigger Efficiency
# ## TO BE  FIXED FOR COMBINATION
# # trig_syst = ['( SingleLepton_trigEff_corrected_up / SingleLepton_trigEff_corrected )*(SingleLepton_trigEff_corrected>0.02) + (SingleLepton_trigEff_corrected<=0.02)', '(SingleLepton_trigEff_corrected_down/SingleLepton_trigEff_corrected)']
# trig_syst = ['((TriggerSFWeight_1l_u)/(TriggerSFWeight_1l))', '(TriggerSFWeight_1l_d)/(TriggerSFWeight_1l)']

# nuisances['trigg']  = {
#                 'name'  : 'CMS_eff_trigger_2016',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples' :  dict((skey, trig_syst) for skey in mc)
# }

# # ##### Electron Efficiency and energy scale
# ## TO BE  FIXED FOR COMBINATION

# ele_id_syst_up = '(abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'_Up[0])/\
#                     (Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 13)'
# ele_id_syst_do = '(abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'_Down[0])/\
#                     (Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 13)'
# mu_id_syst_up = '(abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'_Up[0])/\
#                     (Lepton_tightMuon_'+muWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 11)'
# mu_id_syst_do = '(abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'_Down[0])/\
#                     (Lepton_tightMuon_'+muWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 11)'

# id_syst_ele = [ ele_id_syst_up, ele_id_syst_do ]
# id_syst_mu = [ mu_id_syst_up, mu_id_syst_do ]

# nuisances['eff_e']  = {
#                 'name'  : 'CMS_eff_e_2016',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  :   dict((skey, id_syst_ele) for skey in mc ),
#                 'cuts': phase_spaces_tot_ele
# }

# nuisances['electronpt']  = {
#                 'name'  : 'CMS_scale_e_2016',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp': 'ElepTup',
#                 'mapDown': 'ElepTdo',
#                 'cuts': phase_spaces_tot_ele,
#                 'samples': dict((skey, ['1.','1.']) for skey in mc),
#                 'folderUp' : mcDirectoryLat+'__ElepTup_suffix',
#                 'folderDown' : mcDirectoryLat+'__ElepTdo_suffix'
# }

# # # # ##### Muon Efficiency and energy scale
# ### TO BE  FIXED FOR COMBINATION

# nuisances['eff_m']  = {
#                 'name'  : 'CMS_eff_m_2016',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, id_syst_mu) for skey in mc),
#                 'cuts': phase_spaces_tot_mu
# }

# nuisances['muonpt']  = {
#                 'name'  : 'CMS_scale_m_2016',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp': 'MupTup',
#                 'mapDown': 'MupTdo',
#                 'cuts': phase_spaces_tot_mu,
#                 'samples': dict((skey, ['1.','1.']) for skey in mc),
#                 'folderUp' : mcDirectoryLat+'__MupTup_suffix',
#                 'folderDown' : mcDirectoryLat+'__MupTdo_suffix'
# }


# # ##################
# # # PU jet id
# ### TO BE  FIXED FOR COMBINATION

# nuisances['JetPUID_sf']  = {
#                 'name'  : 'CMS_jetpuid_2016',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc )
# }

# # ##### Jet energy scale
# jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2','JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal','JESRelativeSample_2016']

# for js in jes_systs:
#     nuisances[js] = {
#         'name': 'CMS_scale_'+js,
#         'kind': 'suffix',
#         'type': 'shape',
#         'mapUp': js+'up',
#         'mapDown': js+'do',
#         # 'samples': dict((skey, ['1.', '1.']) for skey in mc if skey not in bkg_to_norm),
#         'samples': dict((skey, ['1.', '1.']) for skey in mc),
#         'folderUp': mcDirectoryLat+'__JESup_suffix',
#         'folderDown': mcDirectoryLat+'__JESdo_suffix'
#     }

#     # for flavor in ["ele", "mu"]:
#     #     data_exp = data_exp_ele if flavor == "ele" else data_exp_mu
#     #     cut = phase_spaces_tot_ele if flavor == "ele" else phase_spaces_tot_mu
#     #     for bkg in bkg_to_norm:
#     #         if js in data_exp[bkg]:
#     #             name = 'CMS_scale_'+js+"_"+bkg+"_norm_"+flavor+"HIPM"
#     #             upFact = str(float(1./data_exp[bkg][js][-1]))
#     #             doFact = str(float(1./data_exp[bkg][js][0]))
#     #         else:
#     #             name = 'CMS_scale_'+js
#     #             upFact = "1."
#     #             doFact = "1."

#     #         nuisances[js+"_"+bkg+"_norm_{}".format(flavor)]  = {
#     #             'name': name,
#     #             'kind': 'suffix',
#     #             'type': 'shape',
#     #             'mapUp': js+'up',
#     #             'mapDown': js+'do',
#     #             'samples': {
#     #                 bkg: [upFact,doFact] 
#     #             },
#     #             'folderUp': mcDirectoryLat+'__JESup_suffix',
#     #             'folderDown': mcDirectoryLat+'__JESdo_suffix',
#     #             'cuts': cut
#     #         }

# # # # ##### Jet energy resolution
# nuisances['JER'] = {
#                 'name': 'CMS_res_j_2016_UL',
#                 'kind': 'suffix',
#                 'type': 'shape',
#                 'mapUp': 'JERup',
#                 'mapDown': 'JERdo',
#                 'samples': dict((skey, ['1.','1.']) for skey in mc),
#                 'folderUp' : mcDirectoryLat+'__JERup_suffix',
#                 'folderDown' : mcDirectoryLat+'__JERdo_suffix',
# }

# # ##### MET energy scale

# nuisances['MET']  = {
#                 'name'  : 'CMS_scale_met_2016_UL',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp':   'METup',
#                 'mapDown': 'METdo', 
#                 # 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in bkg_to_norm),
#                 'samples': dict((skey, ['1.','1.']) for skey in mc),
#                 'folderUp' : mcDirectoryLat+'__METup_suffix',
#                 'folderDown' : mcDirectoryLat+'__METdo_suffix'
# }

# # for flavor in ["ele", "mu"]:
# #     data_exp = data_exp_ele if flavor == "ele" else data_exp_mu
# #     cut = phase_spaces_tot_ele if flavor == "ele" else phase_spaces_tot_mu
# #     for bkg in bkg_to_norm:
# #         upFact = str(float(1./data_exp[bkg]["scale_met_2016_UL"][-1]))
# #         doFact = str(float(1./data_exp[bkg]["scale_met_2016_UL"][0]))

# #         nuisances["MET_"+bkg+"_norm_{}".format(flavor)]  = {
# #             'name': 'CMS_scale_met_2016HIPM_{}_norm_UL_{}'.format(bkg, flavor),
# #             'kind'  : 'suffix',
# #             'type'  : 'shape',
# #             'mapUp':   'METup',
# #             'mapDown': 'METdo', 
# #             'samples'  : {
# #                 bkg      : [upFact,doFact]                                                                                                                                                                                                                 
# #             },
# #             'folderUp' : mcDirectoryLat+'__METup_suffix',
# #             'folderDown' : mcDirectoryLat+'__METdo_suffix',
# #             'cuts': cut
# #         }


# # # # # Top pT reweighting uncertainty

# nuisances['singleTopToTTbar'] = {
#     'name': 'singleTopToTTbar',
#     'skipCMS': 1,
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': { 
#        'top': [
#         'isSingleTop * 1.0816 + isTTbar',
#         'isSingleTop * 0.9184 + isTTbar']
#       }
# }

# # # ## Top pT reweighting uncertainty

# nuisances['TopPtRew'] = {
#    'name': 'CMS_top_pT_reweighting',   # Theory uncertainty
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
#    'symmetrize': True
# }


# # # # # # ######################
# # # # # # # Theory nuisance
# # # # # # #
# # # # # # # PS and UE
# # # # # # # #
# # # # # # #### USE this for producing shapes

# ## normalized theorical ones for main bkgs!!
# json_file ='/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/utils/2016/HIPM/VetoAndtopCRSplit/nuisance_incl_norm_factors_2016HIPM_ele_theo.json'
# with open(json_file) as jsonfile:
#     data_bkg_th_ele = json.load(jsonfile)

# json_file ='/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/utils/2016/HIPM/VetoAndtopCRSplit/nuisance_incl_norm_factors_2016HIPM_mu_theo.json'
# with open(json_file) as jsonfile:
#     data_bkg_th_mu = json.load(jsonfile)

# nuisances['PS_ISR']  = {
#                 'name'  : 'CMS_PS_ISR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 # 'samples'  : {   sample : ['PSWeight[2]','PSWeight[0]'] for sample in mc if sample not in ['VBS', 'VBF-Z']+signals+mc_eft+bkg_to_norm}
#                 'samples'  : {   sample : ['PSWeight[2]','PSWeight[0]'] for sample in mc if sample not in ['VBS', 'VBF-Z']+signals+mc_eft}
#             }

# nuisances['PS_FSR']  = {
#                 'name'  : 'CMS_PS_FSR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {     
#                     # sample : ['PSWeight[3]','PSWeight[1]'] for sample in mc if sample not in ['VBS', 'VBF-Z']+signals+mc_eft+bkg_to_norm}
#                     sample : ['PSWeight[3]','PSWeight[1]'] for sample in mc if sample not in ['VBS', 'VBF-Z']+signals+mc_eft}
#             }

# # for flavor in ["ele", "mu"]:
# #     data_bkg_th = data_bkg_th_ele if flavor == "ele" else data_bkg_th_mu
# #     cut = phase_spaces_tot_ele if flavor == "ele" else phase_spaces_tot_mu
    
# #     for bkg in bkg_to_norm:
# #         nuisances['PS_ISR_{}_accept_{}'.format(bkg,flavor)]  = {
# #                         'name'  : 'CMS_PS_ISR_{}_acceptVBFW_{}16HIPM'.format(bkg,flavor),
# #                         'kind'  : 'weight',
# #                         'type'  : 'shape',
# #                         'samples'  : { bkg : ['PSWeight[2]/{}'.format(data_bkg_th[bkg]["PSISR"][-1]),'PSWeight[0]/{}'.format(data_bkg_th[bkg]["PSISR"][0])] },
# #                         'cuts': cut
# #                     }

# #         nuisances['PS_FSR_{}_accept_{}'.format(bkg,flavor)]  = {
# #                         'name'  : 'CMS_PS_FSR_{}_acceptVBFW_{}16HIPM'.format(bkg,flavor),
# #                         'kind'  : 'weight',
# #                         'type'  : 'shape',
# #                         'samples'  : { bkg : ['PSWeight[3]/{}'.format(data_bkg_th[bkg]["PSFSR"][-1]),'PSWeight[1]/{}'.format(data_bkg_th[bkg]["PSFSR"][0])] },
# #                         'cuts': cut
# #                     }

# nuisances['PS_ISR_dipole']  = {
#                 'name'  : 'CMS_PS_ISR_dipole',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {   sample : ['PSWeight[2]','PSWeight[0]'] for sample in ['VBS', 'VBF-Z']+signals+mc_eft}
#             }

# nuisances['PS_FSR_dipole']  = {
#                 'name'  : 'CMS_PS_FSR_dipole',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {     sample : ['PSWeight[3]','PSWeight[1]'] for sample in ['VBS', 'VBF-Z']+signals+mc_eft}
#             }

# # nuisances['PS_ISR_dipolePvt']  = {
# #                 'name'  : 'CMS_PS_ISR_dipole',
# #                 'kind'  : 'weight',
# #                 'type'  : 'shape',
# #                 'samples'  : {   sample : ['ISRSig_ModUp','ISRSig_ModDown'] for sample in signals+mc_eft},
# #                 'cuts': phase_spaces_tot_sr
# #             }

# # nuisances['PS_FSR_dipolePvt']  = {
# #                 'name'  : 'CMS_PS_FSR_dipole',
# #                 'kind'  : 'weight',
# #                 'type'  : 'shape',
# #                 'samples'  : {   sample : ['FSRSig_ModUp','FSRSig_ModDown'] for sample in signals+mc_eft},
# #                 'cuts': phase_spaces_tot_sr
# #             }



# # # # ##############

# nuisances['PU']  = {
#                 'name'  : 'CMS_PU_2016HIPM',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     sample : ['(puWeightUp/puWeight)','(puWeightDown/puWeight)'] for sample in mc},
# }

# ## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
# variations   = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-4],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-2],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-1],1)']

# for sample in mc_bkg :
#     if sample in bkg_to_norm:
#         nuisances['PDFscale_'+sample] = {
#                 'name'  : 'pdf_weight_{}'.format(sample),
#                 'kind'  : 'weight_square',
#                 'type'  : 'shape',
#                 'samples' :  { sample: ['Alt$(LHEPdfWeight[{}], 1.)'.format(i) for i in range(0,101)]},
#         }
#     #     for flavor in ["ele", "mu"]:
#     #         data_bkg_th = data_bkg_th_ele if flavor == "ele" else data_bkg_th_mu
#     #         cut = phase_spaces_tot_ele if flavor == "ele" else phase_spaces_tot_mu

#     #         nuisances['QCDscale_'+sample+'_accept_VBFW_{}'.format(flavor)] = {
#     #             'name'  : 'QCDscale_'+sample+'_accept_VBFW_{}16HIPM'.format(flavor),
#     #             'kind'  : 'weight_envelope',
#     #             'type'  : 'shape',
#     #             'samples': {sample: [
#     #                     'Alt$(LHEScaleWeight[{}]/{},1)'.format(
#     #                         idx if idx >= 0 else "nLHEScaleWeight{}".format(idx), data_bkg_th[sample]["QCDSF"][i]
#     #                     )
#     #                     for i, idx in enumerate([0, 1, 3, -4, -2, -1])
#     #                     ]},
#     #             'cuts': cut
#     #         }

#     #         nuisances['pdf_weight_{}_accept_VBFW_{}'.format(sample,flavor)] = {
#     #             'name'  : 'pdf_weight_{}_accept_VBFW_{}16HIPM'.format(sample,flavor),
#     #             'kind'  : 'weight_square',
#     #             'type'  : 'shape',
#     #             'samples' :  { sample: ['Alt$(LHEPdfWeight[{}]/{}, 1.)'.format(i, data_bkg_th[sample]["PDFSF"][i]) for i in range(0,101)]},
#     #             'cuts': cut
#     #         }

#     #         # nuisances['pdf_weight_{}_Alpha_acceptVBFW_{}'.format(sample,flavor)] = {
#     #         #     'name'  : 'pdf_weight_{}_Alpha_acceptVBFW_{}16HIPM'.format(sample,flavor),
#     #         #     'kind'  : 'weight',
#     #         #     'type'  : 'shape',
#     #         #     'samples' :  { sample: ['Alt$(LHEPdfWeight[{}]/{}, 1.)'.format(102, data_bkg_th[sample]["PDFSF"][102]), 'Alt$(LHEPdfWeight[{}]/{}, 1.)'.format(101, data_bkg_th[sample]["PDFSF"][101])]},
#     #         #     'cuts': cut
#     #         # }
#     # else:
#     nuisances['QCDscale_'+sample] = {
#         'name'  : 'QCDscale_'+sample,
#         'kind'  : 'weight_envelope',
#         'type'  : 'shape',
#         'samples'  :  { sample: variations }
#     }


# # # # # # # #Correlate all signal samples
# nuisances['QCD_scale_VBFW'] = {
#             'name'  : 'QCDscale_VBFW',
#             'kind'  : 'weight_envelope',
#             'type'  : 'shape',
#             'samples'  :  { s: variations for s in signals+mc_eft}
#         }

# # nuisances['QCD_scale_VBFW'] = {
# #             'name'  : 'QCDscale_VBFW',
# #             'kind'  : 'weight',
# #             'type'  : 'shape',
# #             'samples'  :  { s : ['QCDscaleSig_ModUp','QCDscaleSig_ModDown'] for s in signals+mc_eft},
# #             'cuts': phase_spaces_tot_sr
# #         }


# # # #### mettere per tutti i sample ma in SR, poi anche in CR per quelli che hanno una CR
# # # ## valutare se le cose sono strane con drawnuisances e se sono piatti via di logN

# # nuisances['pdf_weight103'] = {
# #     'name'  : 'pdf103',
# #     'kind'  : 'weight',
# #     'type'  : 'shape',
# #     'samples' :  { s: ['PDFweight_ModUp', 'PDFweight_ModDown'] for s in signals+mc_eft },
# #     'cuts': phase_spaces_tot_sr
# # }

# # nuisances['pdf_weight100'] = {
# #     'name'  : 'pdf100',
# #     'kind'  : 'weight',
# #     'type'  : 'shape',
# #     'samples' :  { s: ['PDFweight_100ModUp', 'PDFweight_100ModDown'] for s in signals+mc_eft },
# #     'cuts': phase_spaces_tot_sr
# # }

# # nuisances['pdf_weightAlpha'] = {
# #     'name'  : 'pdfAlpha',
# #     'kind'  : 'weight',
# #     'type'  : 'shape',
# #     'samples' :  { s: ['PDFweight_AlphaModUp', 'PDFweight_AlphaModDown'] for s in signals+mc_eft },
# #     'cuts': phase_spaces_tot_sr
# # }

# nuisances['pdf_weight'] = {
#     'name'  : 'pdf',
#     'kind'  : 'weight_square',
#     'type'  : 'shape',
#     'samples' :  { sample: ['Alt$(LHEPdfWeight[{}], 1.)'.format(i) for i in range(0,101)] for sample in signals+mc_eft},
# }

# # nuisances['pdf_weightAlpha'.format(sample)] = {
# #     'name'  : 'pdfAlpha'.format(sample),
# #     'kind'  : 'weight',
# #     'type'  : 'shape',
# #     'samples' :  { sample: ['Alt$(LHEPdfWeight[{}], 1.)'.format(102), 'Alt$(LHEPdfWeight[{}], 1.)'.format(101)] for sample in signals+mc_eft},
# # }


# # # # # An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# # # # # And we don't observe any dependency of UE variations on njet
# nuisances['UE']  = {
#                 'name'  : 'UE_CP5',
#                 'type': 'lnN',
#                 'samples': dict((skey, '1.015') for skey in mc if skey not in ["top", "Wjets_HT_hardJets", "Wjets_HT_PUJets"])
# }

# # # # reweight wjet nuisances
# #### this should apply only for Wjets_HT_hardjets BUUTT non riesco
# ### poi lo tolgo a mano...

# WJets_up = '( WJets_reweight_up / WJets_reweight )'
# WJets_do = '( WJets_reweight_do / WJets_reweight )'

# nuisances['WJets_reweight_stat'] = {
#     'name': 'VBFW_WJets_rew_stat_2016_HIPM',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': { 
#        'Wjets_HT_hardJets': [WJets_up, WJets_do]
#       }
# }

# WJets_functional = '( WJets_reweight_func /  WJets_reweight )'
# nuisances['WJets_reweight_functional_2016_HIPM'] = {
#     'name': 'VBFW_WJets_rew_func_2016_HIPM',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': {
#        'Wjets_HT_hardJets': [WJets_functional, "1."]
#       },
# }


# # # ####### Generic "cross section uncertainties"
# # # ##############
# # # # Normalization factors
# # # ##############

# for fl in ["ele", "mu"]:
#     nuisances["Top_norm_{}".format(fl)]  = {
#         'name'  : 'CMS_Top_norm_{}16HIPM'.format(fl),
#         'samples'  : {
#             'top' : '1.00',
#             },
#         'range': (0.5,1.5),
#         'type'  : 'rateParam',
#         'cuts': [region for region in regions if fl in region]
#     }

# for fl in ["ele", "mu"]:
#     nuisances["WPUJet_norm_{}".format(fl)]  = {
#         'name'  : 'CMS_WPUJet_norm_{}16HIPM'.format(fl),
#         'samples'  : {'Wjets_HT_PUJets' : '1.00'},
#         'type'  : 'rateParam',
#         'range': (0.5,1.5),
#         'cuts': [region for region in regions if fl in region]
#     }


# for fl in ["ele", "mu"]:
#     nuisances["WhardJet_norm_{}".format(fl)]  = {
#                     'name'  : 'CMS_WhardJet_norm_{}16HIPM'.format(fl),
#                     'samples'  : {'Wjets_HT_hardJets' : '1.00'},
#                     'type'  : 'rateParam',
#                     'range': (0.5,1.5),
#                     'cuts': [region for region in regions if fl in region]
#             }


# for n in nuisances.values():
#     n['skipCMS'] = 1

# nuisances = merge_nuisances(nuisances)

# # ## Use the following if you want to apply the automatic combine MC stat nuisances.
# nuisances['stat']  = {
#               'type'  : 'auto',
#               'maxPoiss'  : '10',
#               'includeSignal'  : '0',
#             #    nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
#             #    nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
#               'samples' : {}
#              }

