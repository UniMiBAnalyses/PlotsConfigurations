from pprint import pprint
# # # name of samples here must match keys in samples.py 

mc_sm = ["sm", "Wjets_HT", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]

mc_bkg = [c for c in mc_sm if "sm" not in c]
mc_eft = [c for c in samples if any(substring in c for substring in ["lin", "quad", "mixed"])]
signals = [c for c in samples if "sm" in c and c not in mc_eft]
mc = mc_sm + mc_eft
# regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","mu_topcr","ele_topcr","ele_FakeCR","mu_FakeCR"]
regions = ["ele_SR","mu_SR","ele_SR_highDNN","mu_SR_highDNN", "ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr","ele_FakeCR","mu_FakeCR"]
# regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr","ele_FakeCR","mu_FakeCR"]
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]
phase_spaces_tot_sr = [ c for c in regions if 'SR' in c]
phase_spaces_tot_sr_top = [ c for c in regions if 'SR' in c or "topcr" in c]
wj_region = [ c for c in regions if 'HWJ' in c]

# # Function to split a nuisance on different folders for different group of samples
# # keeping the same nuisance name
# # groups = [ (list of samples, folder), ...  ]
# # def split_nuisance_samples_dir(nuisance_name, nuisance_options, variation, groups):
# #     for ig, (samples_list, folder) in enumerate(groups):
# #         n = {}
# #         n.update(nuisance_options)
# #         n["samples"] = dict((skey, ['1.','1.']) for skey in samples_list)
# #         n["folderUp"] = folder +'_'+variation + 'up'
# #         n["folderDown"] = folder +'_'+variation + 'do'
# #         nuisances['{}_{}'.format(nuisance_name, ig)] = n

# # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# # # #### Luminosity
# ### TO BE  FIXED FOR COMBINATION

# #### Luminosity

# # https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#LumiComb
# # Uncorrelated 2016               1.0
# # Uncorrelated       2017              2.0
# # Uncorrelated             2018             1.5
# # Correlated   2016, 2017, 2018   0.6, 0.9, 2.0
# # Correlated         2017, 2018        0.6, 0.2

# nuisances['lumi_Uncorrelated'] = {
#     'name'    : 'lumi_13TeV_2016',
#     'type'    : 'lnN',
#     'samples' : dict((skey, '1.010') for skey in mc)
# }

# nuisances['lumi_Correlated_Run2'] = {
#     'name'    : 'lumi_13TeV_correlated',
#     'type'    : 'lnN',
#     'samples' : dict((skey, '1.006') for skey in mc)
# }

# ##########Fakes
# # fakeW_jetUp       = '( fakeWeight_45 / fakeWeight_35  )'
# # fakeW_jetDown     =  '( fakeWeight_25 / fakeWeight_35  )'
# ## not a systematic because i preselect my phase-space!

# fakeW_statUp        =  '( fakeWeight_statUp / fakeWeight_1p3  )'
# fakeW_statDown      =  '( fakeWeight_statDo / fakeWeight_1p3  )'
# fakeW_EWKsubUp     =  '( fakeWeight_1p4 / fakeWeight_1p3  )'
# fakeW_EWKsubDown     =  '( fakeWeight_1p2 / fakeWeight_1p3  )'
# fakeW_PRMC     =  '( fakeWeight_PRfromMC / fakeWeight_1p3  )'

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
#                 'cuts':  phase_spaces_tot_ele
# }

# nuisances['fake_mu_stat']  = {
#                 'name'  : 'CMS_fake_stat_m_2016_1lep',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'     :[ fakeW_statUp , fakeW_statDown ],
#                              },
#                 'cuts':  phase_spaces_tot_mu
# }

# nuisances['fake_ele_EWKsub']  = {
#                 'name'  : 'VBFW_fake_e_EWKsub_2016_HIPM',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_EWKsubUp , fakeW_EWKsubDown ],
#                              },
#                 'cuts':  phase_spaces_tot_ele
# }

# nuisances['fake_mu_EWKsub']  = {
#                 'name'  : 'VBFW_fake_m_EWKsub_2016_HIPM',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_EWKsubUp , fakeW_EWKsubDown ],
#                              },
#                 'cuts':  phase_spaces_tot_mu
# }

# nuisances['fake_mu_PRMC']  = {
#                 'name'  : 'VBFW_fake_m_PR_fromMC_2016_HIPM',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_PRMC , "1." ],
#                              },
#                 'cuts':  phase_spaces_tot_mu
# }

# nuisances['fake_ele_PRMC']  = {
#                 'name'  : 'VBFW_fake_e_PR_fromMC_2016_HIPM',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_PRMC , "1." ],
#                              },
#                 'cuts':  phase_spaces_tot_ele
# }


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

# # # ##### Trigger Efficiency
# ### TO BE  FIXED FOR COMBINATION
# # trig_syst = ['( SingleLepton_trigEff_corrected_up / SingleLepton_trigEff_corrected )*(SingleLepton_trigEff_corrected>0.02) + (SingleLepton_trigEff_corrected<=0.02)', '(SingleLepton_trigEff_corrected_down/SingleLepton_trigEff_corrected)']
# trig_syst = ['((TriggerSFWeight_1l_u)/(TriggerSFWeight_1l))', '(TriggerSFWeight_1l_d)/(TriggerSFWeight_1l)']

# nuisances['trigg']  = {
#                 'name'  : 'CMS_eff_trigger_2016',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples' :  dict((skey, trig_syst) for skey in mc)
# }

# # # Prefire correction
# prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

# nuisances['prefire']  = {
#                 'name'  : 'CMS_eff_prefiring_2016',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, trig_syst) for skey in mc)
# }

# # # ##### Electron Efficiency and energy scale
# ### TO BE  FIXED FOR COMBINATION

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
#     nuisances[js]  = {
#         'name': 'CMS_scale_'+js,
#         'kind': 'suffix',
#         'type': 'shape',
#         'mapUp': js+'up',
#         'mapDown': js+'do',
#         'samples': dict((skey, ['1.', '1.']) for skey in mc ),
#         'folderUp': mcDirectoryLat+'__JESup_suffix',
#         'folderDown': mcDirectoryLat+'__JESdo_suffix'
#     }


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
#                 'samples': dict((skey, ['1.','1.']) for skey in mc ),
#                 'folderUp' : mcDirectoryLat+'__METup_suffix',
#                 'folderDown' : mcDirectoryLat+'__METdo_suffix'
# }


# # # # Top pT reweighting uncertainty

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

# # ## Top pT reweighting uncertainty

# nuisances['TopPtRew'] = {
#    'name': 'CMS_top_pT_reweighting',   # Theory uncertainty
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
#    'symmetrize': True
# }


# # # # # ######################
# # # # # # Theory nuisance
# # # # # #
# # # # # # PS and UE
# # # # # # #
# # # # # #### USE this for producing shapes

# nuisances['PS_ISR']  = {
#                 'name'  : 'CMS_PS_ISR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {   sample : ['PSWeight[2]','PSWeight[0]'] for sample in mc if sample not in ['VBS', 'VBF-Z']+signals+mc_eft}
#             }

# nuisances['PS_FSR']  = {
#                 'name'  : 'CMS_PS_FSR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {     
#                     sample : ['PSWeight[3]','PSWeight[1]'] for sample in mc if sample not in ['VBS', 'VBF-Z']+signals+mc_eft}
#             }

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

# # # # ##############

# nuisances['PU']  = {
#                 'name'  : 'CMS_PU_2016',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     sample : ['(puWeightUp/puWeight)','(puWeightDown/puWeight)'] for sample in mc},
# }

# ## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
# variations   = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-4],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-2],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-1],1)']

# for sample in mc_bkg :
#     nuisances['QCDscale_'+sample] = {
#         'name'  : 'QCDscale_'+sample,
#         'kind'  : 'weight_envelope',
#         'type'  : 'shape',
#         'samples'  :  { sample: variations }
#     }

# # # # # # #Correlate all signal samples
# nuisances['QCD_scale_VBFW'] = {
#             'name'  : 'QCDscale_VBFW',
#             'kind'  : 'weight_envelope',
#             'type'  : 'shape',
#             'samples'  :  { s: variations for s in signals+mc_eft}
#         }

# nuisances['pdf_weight'] = {
#     'name'  : 'pdf',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["Wjets_HT", "top", "sm"] },
# }



# # # # # An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# # # # # And we don't observe any dependency of UE variations on njet
# nuisances['UE']  = {
#                 'name'  : 'UE_CP5',
#                 'type': 'lnN',
#                 'samples': dict((skey, '1.015') for skey in mc ), 
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
#        'Wjets_HT': [WJets_up, WJets_do]
#       }
# }

# WJets_functional = '( WJets_reweight_func /  WJets_reweight )'
# nuisances['WJets_reweight_functional_2016_HIPM'] = {
#     'name': 'VBFW_WJets_rew_func_2016_HIPM',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': {
#        'Wjets_HT': [WJets_functional, "1."]
#       },
# }


# # # ####### Generic "cross section uncertainties"
# # # ##############
# # # # Normalization factors
# # # ##############


# nuisances["Top_norm"]  = {
#     'name'  : 'CMS_Top_norm',
#     'samples'  : {
#         'top' : '1.00',
#         },
#     'type'  : 'rateParam'
# }

# for fl in ["ele", "mu"]:
#     nuisances["WPUJet_norm_{}".format(fl)]  = {
#         'name'  : 'CMS_WPUJet_norm_{}'.format(fl),
#         'samples'  : {'Wjets_HT_PUJets' : '1.00'},
#         'type'  : 'rateParam',
#         'cuts': [region for region in regions if fl in region or "topcr" in region]
#     }


# for fl in ["ele", "mu"]:
#     nuisances["WhardJet_norm_{}".format(fl)]  = {
#                     'name'  : 'CMS_WhardJet_norm_{}'.format(fl),
#                     'samples'  : {'Wjets_HT_hardJets' : '1.00'},
#                     'type'  : 'rateParam',
#                     'cuts': [region for region in regions if fl in region or "topcr" in region]
#             }


# # ## Use the following if you want to apply the automatic combine MC stat nuisances.
# nuisances['stat']  = {
#               'type'  : 'auto',
#               'maxPoiss'  : '10',
#               'includeSignal'  : '1',
#             #    nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
#             #    nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
#               'samples' : {}
#              }


# for n in nuisances.values():
#     n['skipCMS'] = 1
