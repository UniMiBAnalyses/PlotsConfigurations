from pprint import pprint
# # # name of samples here must match keys in samples.py 

mc =["WLNuJJ", "Wjets_HT", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
# regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","mu_topcr","ele_topcr","ele_FakeCR","mu_FakeCR"]
regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr","ele_FakeCR","mu_FakeCR"]
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]
phase_spaces_tot_sr = [ c for c in regions if 'SR' in c]
phase_spaces_tot_sr_top = [ c for c in regions if 'SR' in c or "topcr" in c]
wj_region = [ c for c in regions if 'HWJ' in c]

# # # # # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# # #### Luminosity

# nuisances['lumi_Uncorrelated'] = {
#     'name': 'lumi_13TeV_2018',
#     'type': 'lnN',
#     'samples': dict((skey, '1.015') for skey in mc)
# }

# nuisances['lumi_XYFact'] = {
#     'name': 'lumi_13TeV_XYFact',
#     'type': 'lnN',
#     'samples': dict((skey, '1.02') for skey in mc)
# }

# nuisances['lumi_LScale'] = {
#     'name': 'lumi_13TeV_LSCale',
#     'type': 'lnN',
#     'samples': dict((skey, '1.002') for skey in mc)
# }

# nuisances['lumi_CurrCalib'] = {
#     'name': 'lumi_13TeV_CurrCalib',
#     'type': 'lnN',
#     'samples': dict((skey, '1.002') for skey in mc)
# }


# ##########Fakes
# # fakeW_jetUp       = '( fakeWeight_45 / fakeWeight_35  )'
# # fakeW_jetDown     =  '( fakeWeight_25 / fakeWeight_35  )'
# ## not a systematic because i preselect my phase-space!

# fakeW_statUp        =  '( fakeWeight_statUp / fakeWeight_30  )'
# fakeW_statDown      =  '( fakeWeight_statDo / fakeWeight_30  )'
# fakeW_EWKsub     =  '( fakeWeight_EWKsubtractionSF / fakeWeight_30  )'

# nuisances['fake_syst_ele']  = {
#                'name'  : 'CMS_fake_syst_ele',
#                'type'  : 'lnN',
#                'samples'  : {
#                              'Fake' : '1.30',
#                              },
#                'cuts': phase_spaces_tot_ele
#                }

# nuisances['fake_syst_mu']  = {
#                'name'  : 'CMS_fake_syst_mu',
#                'type'  : 'lnN',
#                'samples'  : {
#                              'Fake' : '1.30',
#                              },
#                 'cuts': phase_spaces_tot_mu
#                }


# nuisances['fake_ele_stat']  = {
#                 'name'  : 'CMS_fake_ele_stat_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_statUp , fakeW_statDown ],
#                              },
#                 'cuts':  phase_spaces_tot_ele
# }


# nuisances['fake_mu_stat']  = {
#                 'name'  : 'CMS_fake_mu_stat_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'     :[ fakeW_statUp , fakeW_statDown ],
#                              },
#                 'cuts':  phase_spaces_tot_mu
# }

# nuisances['fake_ele_EWKsub']  = {
#                 'name'  : 'CMS_fake_ele_EWKsub_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_EWKsub , "1." ],
#                              },
#                 'symmetrize': True,
#                 'cuts':  phase_spaces_tot_ele
# }

# nuisances['fake_mu_EWKsub']  = {
#                 'name'  : 'CMS_fake_mu_EWKsub_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_EWKsub , "1." ],
#                              },
#                 'symmetrize': True,
#                 'cuts':  phase_spaces_tot_mu
# }



# # ##### Btag nuisances

# for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
#     btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

#     name = 'CMS_btag_%s' % shift
#     if 'stats' in shift:
#         name += '_2018'

#     nuisances['btag_shape_%s' % shift] = {
#         'name': name,
#         'kind': 'weight',
#         'type': 'shape',
#         'samples': dict((skey, btag_syst) for skey in mc)
#     }

# # # # # ##### Trigger Efficiency

# # trig_syst = ['((TriggerSFWeight_1l_u)/(TriggerSFWeight_1l))*(TriggerSFWeight_1l>0.02) + (TriggerSFWeight_1l<=0.02)', '(TriggerSFWeight_1l_d)/(TriggerSFWeight_1l)']
# trig_syst = ['((TriggerSFWeight_1l_u)/(TriggerSFWeight_1l))', '(TriggerSFWeight_1l_d)/(TriggerSFWeight_1l)']

# nuisances['trigg']  = {
#                 'name'  : 'CMS_eff_trigger_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples' :  dict((skey, trig_syst) for skey in mc)
# }


# # # # # ##### Electron Efficiency and energy scale

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
#                 'name'  : 'CMS_eff_e_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  :   dict((skey, id_syst_ele) for skey in mc ),
#                 'cuts': phase_spaces_tot_ele
# }

# # nuisances['electronpt']  = {
# #                 'name'  : 'CMS_scale_e_2018',
# #                 'kind'  : 'suffix',
# #                 'type'  : 'shape',
# #                 'mapUp': 'ElepTup',
# #                 'mapDown': 'ElepTdo',
# #                 'cuts': phase_spaces_tot_ele,
# #                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
# #                 'folderUp' : mcPrivateDirectory+'__ElepTup_suffix',
# #                 'folderDown' : mcPrivateDirectory+'__ElepTdo_suffix'
# # }

# # # # # ##### Muon Efficiency and energy scale

# nuisances['eff_m']  = {
#                 'name'  : 'CMS_eff_m_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, id_syst_mu) for skey in mc ),
#                 'cuts': phase_spaces_tot_mu
# }

# # nuisances['muonpt']  = {
# #                 'name'  : 'CMS_scale_m_2018',
# #                 'kind'  : 'suffix',
# #                 'type'  : 'shape',
# #                 'mapUp': 'MupTup',
# #                 'mapDown': 'MupTdo',
# #                 'cuts': phase_spaces_tot_mu,
# #                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
# #                 'folderUp' : mcPrivateDirectory+'__MupTup_suffix',
# #                 'folderDown' : mcPrivateDirectory+'__MupTdo_suffix'
# # }

# # # ##################
# # # # PU jet id

# nuisances['JetPUID_sf']  = {
#                 'name'  : 'CMS_jetpuid_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc )
# }

# # # ##### Jet energy scale
# # jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']

# # for js in jes_systs:

# #   nuisances[js] = {
# #       'name': 'CMS_scale_'+js,
# #       'kind': 'suffix',
# #       'type': 'shape',
# #       'mapUp': js+'up',
# #       'mapDown': js+'do',
# #       'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VZ', 'Vg', 'VgS']),
# #       'folderUp': mcPrivateDirectory+'__JESup_suffix',
# #       'folderDown': mcPrivateDirectory+'__JESdo_suffix',
# #       'AsLnN': '1'
# #   }

# # # ##### Jet energy resolution
# # nuisances['JER'] = {
# #                 'name': 'CMS_res_j_2018',
# #                 'kind': 'suffix',
# #                 'type': 'shape',
# #                 'mapUp': 'JERup',
# #                 'mapDown': 'JERdo',
# #                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
# #                 'folderUp' : mcPrivateDirectory+'__JERup_suffix',
# #                 'folderDown' : mcPrivateDirectory+'__JERdo_suffix',
# #                 'AsLnN'      : '1',
# # }

# # # # # ##### MET energy scale
# # nuisances['MET']  = {
# #                 'name'  : 'CMS_scale_met_2018',
# #                 'kind'  : 'suffix',
# #                 'type'  : 'shape',
# #                 'mapUp':   'METup',
# #                 'mapDown': 'METdo', 
# #                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
# #                 'folderUp' : mcPrivateDirectory+'__METup_suffix',
# #                 'folderDown' : mcPrivateDirectory+'__METdo_suffix',
# #                 'AsLnN'      : '1',
# # }


# # # ## Top pT reweighting uncertainty

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

# # # # ## Top pT reweighting uncertainty

# nuisances['TopPtRew'] = {
#    'name': 'CMS_topPtRew',   # Theory uncertainty
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
#    'symmetrize': True
# }


# # # # ######################
# # # # # Theory nuisance


# import json, os
# # VBS_pdf_factors = json.load(open("/afs/cern.ch/work/d/dvalsecc/private/CMSSW_11_1_4" + "/src/PlotsConfigurations/Configurations/VBSjjlnu/Full2018v7/conf_fit_v4.3/pdf_normcorr_VBS.json"))
# configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
# conf_folder = configurations +"/VBF_W/"
# FileJson = "/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/utils/2018/nuisance_incl_norm_factors_2018.json"
# with open(FileJson) as jsonFile:
#     nuis_factors = json.load(jsonFile)
#     jsonFile.close()

# for sample in mc :
#     if sample in ["WLNuJJ"] : continue
#     nuisances['QCD_scale_'+sample] = {
#         'name'  : 'QCDscale_'+sample,
#         'kind'  : 'weight',
#         'type'  : 'shape',
#         'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
#     }

# # # # #Correlate all signal samples

# nuisances['QCD_scale_WLNuJJ_accept'] = {
#             'name'  : 'QCD_scale_WLNuJJ_accept',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples'  :  { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in ["WLNuJJ"] }
#         }


# # # # #
# # # # # PS and UE
# # # # # #
# # # # #### USE this for producing shapes
# nuisances['PS_ISR']  = {
#                 'name'  : 'CMS_PS_ISR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {   
#                     s : ['PSWeight[2] * {}'.format(nuis_factors[s]["PS_ISR"][0]),
#                          'PSWeight[0] * {}'.format(nuis_factors[s]["PS_ISR"][1]) ] for s in mc if s not in ["Higgs"] }
#             }

# nuisances['PS_FSR']  = {
#                 'name'  : 'CMS_PS_FSR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {   
#                     s : ['PSWeight[3] * {}'.format(nuis_factors[s]["PS_FSR"][0]),
#                          'PSWeight[1] * {}'.format(nuis_factors[s]["PS_FSR"][1]) ] for s in mc if s not in ["Higgs"]}
#             }

# # # ##############

# nuisances['PU']  = {
#                 'name'  : 'CMS_PU_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     s : ['(puWeightUp/puWeight) * {}'.format(nuis_factors[s]["CMS_PU_2018"][0]),
#                          '(puWeightDown/puWeight) * {}'.format(nuis_factors[s]["CMS_PU_2018"][1])] for s in mc if s not in ["Higgs"]},
#                 'AsLnN'      : '1',
# }

# #### mettere per tutti i sample ma in SR, poi anche in CR per quelli che hanno una CR
# ## valutare se le cose sono strane con drawnuisances e se sono piatti via di logN

# # # ######## PDF uncertainty
# # nuisances['pdf_weight'] = {
# #     'name'  : 'pdf_weight_1718',
# #     'kind'  : 'weight_envelope',
# #     'type'  : 'shape',
# #     'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc },
# #     'AsLnN':  '1',
# #     'cuts':  phase_spaces_tot_sr
# # }

# ###### uncomment from here 4 datacards
# nuisances['pdf_weight_'+"Wjets_HT"] = {
#     'name'  : 'pdf_weight_1718_'+"Wjets_HT",
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["Wjets_HT"]},
#     'AsLnN':  '1',
#     'cuts':  wj_region + phase_spaces_tot_sr
# }

# nuisances['pdf_weight_'+"top"] = {
#     'name'  : 'pdf_weight_1718_'+"top",
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["top"] },
#     'AsLnN':  '1',
#     'cuts':  phase_spaces_tot_sr_top
# }
# nuisances['pdf_weight_'+"VV"] = {
#     'name'  : 'pdf_weight_1718_'+"VV",
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["VV"] },
#     'AsLnN':  '1',
#     'cuts':  phase_spaces_tot_sr_top
# }
# nuisances['pdf_weight_'+"VBS"] = {
#     'name'  : 'pdf_weight_1718_'+"VBS",
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["VBS"] },
#     'AsLnN':  '1',
#     'cuts':  phase_spaces_tot_sr_top
# }

# nuisances['pdf_weight_accept'] = {
#     'name'  : 'pdf_weight_1718_accept',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples': { k : [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ] for k in ["WLNuJJ"] },
#     'cuts':  phase_spaces_tot_sr
# }
# ####### until here

# # # # An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# # # # And we don't observe any dependency of UE variations on njet
# nuisances['UE']  = {
#                 'name'  : 'UE_CP5',
#                 'skipCMS' : 1,
#                 'type': 'lnN',
#                 # 'samples': dict((skey, '1.015') for skey in mc if skey not in ["top","Wjets_HT"]),  why not this? they use CP5...
#                 'samples': dict((skey, '1.015') for skey in mc ), 
# }

# # reweight wjet nuisances
# WJets_up = '( WJets_reweight_up / WJets_reweight )'
# WJets_do = '( WJets_reweight_do / WJets_reweight )'

# nuisances['WJets_reweight_stat'] = {
#     'name': 'WJets_rew_2018',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': { 
#        'Wjets_HT_hardJets': [WJets_up, WJets_do]
#       }
# }

# WJets_functional = '( WJets_reweight_func /  WJets_reweight )'
# nuisances['WJets_reweight_functional_2018'] = {
#     'name': 'WJets_rew_func_2018',
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': {
#        'Wjets_HT_hardJets': [WJets_functional, "1."]
#       },
#     'symmetrize': True
# }


# # ####### Generic "cross section uncertainties"
# # ##############
# # # Normalization factors
# # ##############


# nuisances["Top_norm_2018"]  = {
#     'name'  : 'CMS_Top_norm_2018',
#     'samples'  : {
#         'top' : '1.00',
#         },
#     'type'  : 'rateParam'
# }

# # # for fl in ["ele", "mu"]:
# # #     nuisances["Fake_norm_{}_2018".format(fl)]  = {
# # #         'name'  : 'CMS_Fake_norm_{}_2018'.format(fl),
# # #         'samples'  : {
# # #             'Fake' : '1.00',
# # #             },
# # #         'type'  : 'rateParam',
# # #         'cuts': [region for region in regions if fl in region or "topcr" in region]
# # #     }

# for fl in ["ele", "mu"]:
#     nuisances["WPUJet_norm_{}_2018".format(fl)]  = {
#         'name'  : 'CMS_WPUJet_norm_{}_2018'.format(fl),
#         'samples'  : {'Wjets_HT_PUJets' : '1.00'},
#         'type'  : 'rateParam',
#         'cuts': [region for region in regions if fl in region or "topcr" in region]
#     }


# for fl in ["ele", "mu"]:
#     nuisances["WhardJet_norm_{}_2018".format(fl)]  = {
#                     'name'  : 'CMS_WhardJet_norm_{}_2018'.format(fl),
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

   

# # # nuisances = {k:v for k,v in nuisances.items() if k in ['detavbs_residual', 'zlep_residual']} #if 'PS' in k or 'QCD' in k

# # # print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))