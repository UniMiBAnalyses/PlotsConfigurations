from pprint import pprint
# # # name of samples here must match keys in samples.py 

mc =["WLNuJJ", "Wjets_HT", "top", "VV", "VBS", "ggWW", "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
# regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","mu_topcr","ele_topcr","ele_FakeCR","mu_FakeCR"]
regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr","ele_FakeCR","mu_FakeCR", "ele_HWJ-SR", "mu_HWJ-SR"]
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]

# # # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# # # #### Luminosity

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
# fakeW_jetUp       = '( fakeWeight_45 / fakeWeight_35  )'
# fakeW_jetDown     =  '( fakeWeight_25 / fakeWeight_35  )'
# fakeW_statUp        =  '( fakeWeight_35_statUp / fakeWeight_35  )'
# fakeW_statDown      =  '( fakeWeight_35_statDo / fakeWeight_35  )'

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

# nuisances['fake_ele']  = {
#                 'name'  : 'CMS_fake_ele_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'     : [ fakeW_jetUp , fakeW_jetDown ],
#                              },
#                 'cuts':  phase_spaces_tot_ele
# }

# nuisances['fake_ele_stat']  = {
#                 'name'  : 'CMS_fake_ele_stat_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'      : [ fakeW_statUp , fakeW_statDown ],
#                              },
#                 'cuts':  phase_spaces_tot_ele
# }

# nuisances['fake_mu']  = {
#                 'name'  : 'CMS_fake_mu_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                               'Fake'     : [ fakeW_jetUp , fakeW_jetDown ],
#                              },
#                 'cuts':  phase_spaces_tot_mu
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

# # # # ##### Trigger Efficiency

# trig_syst = ['( SingleLepton_trigEff_corrected_up / SingleLepton_trigEff_corrected )*(SingleLepton_trigEff_corrected>0.02) + (SingleLepton_trigEff_corrected<=0.02)', 
#             '(SingleLepton_trigEff_corrected_down/SingleLepton_trigEff_corrected)']

# nuisances['trigg']  = {
#                 'name'  : 'CMS_eff_trigger_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples' :  dict((skey, trig_syst) for skey in mc)
# }


# # # # ##### Electron Efficiency and energy scale

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

# nuisances['electronpt']  = {
#                 'name'  : 'CMS_scale_e_2018',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp': 'ElepTup',
#                 'mapDown': 'ElepTdo',
#                 'cuts': phase_spaces_tot_ele,
#                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
#                 'folderUp' : mcPrivateDirectory+'__ElepTup_suffix',
#                 'folderDown' : mcPrivateDirectory+'__ElepTdo_suffix'
# }

# # # # ##### Muon Efficiency and energy scale

# nuisances['eff_m']  = {
#                 'name'  : 'CMS_eff_m_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, id_syst_mu) for skey in mc ),
#                 'cuts': phase_spaces_tot_mu
# }

# nuisances['muonpt']  = {
#                 'name'  : 'CMS_scale_m_2018',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp': 'MupTup',
#                 'mapDown': 'MupTdo',
#                 'cuts': phase_spaces_tot_mu,
#                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
#                 'folderUp' : mcPrivateDirectory+'__MupTup_suffix',
#                 'folderDown' : mcPrivateDirectory+'__MupTdo_suffix'
# }

# # ##################
# # # PU jet id

# nuisances['JetPUID_sf']  = {
#                 'name'  : 'CMS_jetpuid_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc )
# }

# # ##### Jet energy scale
# jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']

# for js in jes_systs:

#   nuisances[js] = {
#       'name': 'CMS_scale_'+js,
#       'kind': 'suffix',
#       'type': 'shape',
#       'mapUp': js+'up',
#       'mapDown': js+'do',
#       'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VZ', 'Vg', 'VgS']),
#       'folderUp': mcPrivateDirectory+'__JESup_suffix',
#       'folderDown': mcPrivateDirectory+'__JESdo_suffix',
#       'AsLnN': '1'
#   }

# # ##### Jet energy resolution
# nuisances['JER'] = {
#                 'name': 'CMS_res_j_2018',
#                 'kind': 'suffix',
#                 'type': 'shape',
#                 'mapUp': 'JERup',
#                 'mapDown': 'JERdo',
#                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
#                 'folderUp' : mcPrivateDirectory+'__JERup_suffix',
#                 'folderDown' : mcPrivateDirectory+'__JERdo_suffix',
#                 'AsLnN'      : '1',
# }

# # # # ##### MET energy scale
# nuisances['MET']  = {
#                 'name'  : 'CMS_scale_met_2018',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp':   'METup',
#                 'mapDown': 'METdo', 
#                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
#                 'folderUp' : mcPrivateDirectory+'__METup_suffix',
#                 'folderDown' : mcPrivateDirectory+'__METdo_suffix',
#                 'AsLnN'      : '1',
# }


# # ## Top pT reweighting uncertainty

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
#    'name': 'CMS_topPtRew',   # Theory uncertainty
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
#    'symmetrize': True
# }


# # # ######################
# # # # Theory nuisance


# import json, os
# # VBS_pdf_factors = json.load(open("/afs/cern.ch/work/d/dvalsecc/private/CMSSW_11_1_4" + "/src/PlotsConfigurations/Configurations/VBSjjlnu/Full2018v7/conf_fit_v4.3/pdf_normcorr_VBS.json"))
# configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
# conf_folder = configurations +"/VBF_W/"
# FileJson = "/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/utils/nuisance_incl_norm_factors_2018.json"
# with open(FileJson) as jsonFile:
#     nuis_factors = json.load(jsonFile)
#     jsonFile.close()

# for sample in mc :
#     if sample in ["ggWW","VV", "VBS", "Wjets_HT"]: continue
#     nuisances['QCD_scale_'+sample] = {
#         'name'  : 'QCDscale_'+sample,
#         'kind'  : 'weight',
#         'type'  : 'shape',
#         'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
#     }

# # #Correlate all signal samples
# nuisances['QCD_scale_VBS'] = {
#             'name'  : 'QCDscale_VBS_accept',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             # 'samples'  :  { "VBS": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"],
#             #                 "VBS_dipoleRecoil": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"], }
#             'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in ["VBS"] }
#         }


# nuisances['QCD_scale_VV_accept'] = {
#             'name'  : 'QCDscale_VV_accept',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in ["VV"] }
#         }

# nuisances['QCD_scale_VV'] = {
#             'name'  : 'QCDscale_VV',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in ["VV"]}
#         }

# nuisances['QCD_scale_Wjets'] = {
#             'name'  : 'QCDscale_Wjets',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for sample in ["Wjets_HT"]}
#         }


# # # #
# # # # PS and UE
# # # # #
# # # #### USE this for producing shapes
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

# # ##############

# nuisances['PU']  = {
#                 'name'  : 'CMS_PU_2018',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     s : ['(puWeightUp/puWeight) * {}'.format(nuis_factors[s]["CMS_PU_2018"][0]),
#                          '(puWeightDown/puWeight) * {}'.format(nuis_factors[s]["CMS_PU_2018"][1])] for s in mc if s not in ["Higgs"]},
#                 'AsLnN'      : '1',
# }

# ## should i include wjets here??
# # ######## PDF uncertainty
# nuisances['pdf_weight'] = {
#     'name'  : 'pdf_weight_1718',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc if s not in ["VBS", "top", "Wjets_HT", "VBS"]},
#     'AsLnN':  '1'
# }

# nuisances['pdf_weight_accept'] = {
#     'name'  : 'pdf_weight_1718_accept',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     # 'samples' :  { "VBS": [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ],
#     #                "VBS_dipoleRecoil": [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ]}
#     'samples': { k : [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ] for k in ["VV"]}
# }

# # # An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# # # And we don't observe any dependency of UE variations on njet
# nuisances['UE']  = {
#                 'name'  : 'UE_CP5',
#                 'skipCMS' : 1,
#                 'type': 'lnN',
#                 'samples': dict((skey, '1.015') for skey in mc if skey not in ["top","Wjets_HT"]), 
# }


# # ####### Generic "cross section uncertainties"
# ##############
# # Normalization factors
# ##############


# nuisances["Top_norm_2018"]  = {
#     'name'  : 'CMS_Top_norm_2018',
#     'samples'  : {
#         'top' : '1.00',
#         },
#     'type'  : 'rateParam'
# }

# for fl in ["ele", "mu"]:
#     nuisances["Fake_norm_{}_2018".format(fl)]  = {
#         'name'  : 'CMS_Fake_norm_{}_2018'.format(fl),
#         'samples'  : {
#             'Fake' : '1.00',
#             },
#         'type'  : 'rateParam'
#     }

# for fl in ["ele", "mu"]:
#     nuisances["WPUJet_norm_{}_2018".format(fl)]  = {
#         'name'  : 'CMS_WPUJet_norm_{}_2018'.format(fl),
#         'samples'  : {'Wjets_HT_PUJets' : '1.00'},
#         'type'  : 'rateParam'
#     }

# binRegions = ["HWJbin1", "HWJbin2", "HWJbin3", "HWJbin4", "HWJbin5", "HWJbin6", "HWJbin7", "HWJbin8", "HWJbin9", "HWJbin10", "HWJbin11"]

# for fl in ["ele", "mu"]:
#     for subs in binRegions:
#         nuisances["WhardJet_norm_{}_{}_2018".format(fl,subs)]  = {
#                         'name'  : 'CMS_WhardJet_norm_{}_{}_2018'.format(fl, subs),
#                         'samples'  : {'Wjets_HT_{}'.format(subs) : '1.00'},
#                         'type'  : 'rateParam',
#                 }


# ## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
            #    nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
            #    nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }


for n in nuisances.values():
    n['skipCMS'] = 1

   

# # nuisances = {k:v for k,v in nuisances.items() if k in ['detavbs_residual', 'zlep_residual']} #if 'PS' in k or 'QCD' in k

# # print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))