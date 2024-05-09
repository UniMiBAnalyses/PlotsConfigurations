from pprint import pprint
# # # name of samples here must match keys in samples.py 

mc =["WLNuJJ", "Wjets_HT", "top", "VV", "VBS", "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
mc_selected =["WLNuJJ", "Wjets_HT", "top", "DY_M-50", "DY_else"]
regions = ["ele_SR", "mu_SR", "ele_HWJ", "mu_HWJ", "ele_PUWJ", "mu_PUWJ", "topcr", "ele_FakeCR", "mu_FakeCR"]
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]
phase_spaces_tot_sr = [ c for c in regions if 'SR' in c]
phase_spaces_tot_sr_top = [ c for c in regions if 'SR' in c or "topcr" in c]
wj_region = [ c for c in regions if 'HWJ' in c]


# # # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# # #### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc)
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc)
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc)
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc)
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc)
}


nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc)
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc)
}


##########Fakes
# fakeW_jetUp       = '( fakeWeight_45 / fakeWeight_35  )'
# fakeW_jetDown     =  '( fakeWeight_25 / fakeWeight_35  )'
## not a systematic because i preselect my phase-space!

fakeW_statUp        =  '( fakeWeight_statUp / fakeWeight_1p3  )'
fakeW_statDown      =  '( fakeWeight_statDo / fakeWeight_1p3  )'
fakeW_EWKsubUp     =  '( fakeWeight_1p4 / fakeWeight_1p3  )'
fakeW_EWKsubDown     =  '( fakeWeight_1p2 / fakeWeight_1p3  )'
fakeW_PRMC     =  '( fakeWeight_PRfromMC / fakeWeight_1p3  )'

nuisances['fake_syst_ele']  = {
               'name'  : 'CMS_fake_syst_ele',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
               'cuts': phase_spaces_tot_ele
               }

nuisances['fake_syst_mu']  = {
               'name'  : 'CMS_fake_syst_mu',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
                'cuts': phase_spaces_tot_mu
               }

nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_ele_stat_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statUp , fakeW_statDown ],
                             },
                'cuts':  phase_spaces_tot_ele
}

nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_mu_stat_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     :[ fakeW_statUp , fakeW_statDown ],
                             },
                'cuts':  phase_spaces_tot_mu
}

nuisances['fake_ele_EWKsub']  = {
                'name'  : 'CMS_fake_ele_EWKsub_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_EWKsubUp , fakeW_EWKsubDown ],
                             },
                'cuts':  phase_spaces_tot_ele
}

nuisances['fake_mu_EWKsub']  = {
                'name'  : 'CMS_fake_mu_EWKsub_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_EWKsubUp , fakeW_EWKsubDown ],
                             },
                'cuts':  phase_spaces_tot_mu
}

nuisances['fake_mu_PRMC']  = {
                'name'  : 'CMS_fake_mu_PR_fromMC_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_PRMC , "1." ],
                             },
                # 'symmetrize': True,
                'cuts':  phase_spaces_tot_mu
}

nuisances['fake_ele_PRMC']  = {
                'name'  : 'CMS_fake_ele_PR_fromMC_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_PRMC , "1." ],
                             },
                # 'symmetrize': True,
                'cuts':  phase_spaces_tot_ele
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
                'name'  : 'CMS_eff_trigger_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' :  dict((skey, trig_syst) for skey in mc)
}

# # Prefire correction
prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire']  = {
                'name'  : 'CMS_eff_prefiring_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, trig_syst) for skey in mc)
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
                'samples'  :   dict((skey, id_syst_ele) for skey in mc),
                'cuts': phase_spaces_tot_ele
}

nuisances['electronpt']  = {
                'name'  : 'CMS_scale_e_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'ElepTup',
                'mapDown': 'ElepTdo',
                'cuts': phase_spaces_tot_ele,
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']),
                'folderUp' : mcDirectoryHWW+'__ElepTup_suffix',
                'folderDown' : mcDirectoryHWW+'__ElepTdo_suffix'
}

# # # ##### Muon Efficiency and energy scale


nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_mu) for skey in mc),
                'cuts': phase_spaces_tot_mu
}

nuisances['muonpt']  = {
                'name'  : 'CMS_scale_m_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'MupTup',
                'mapDown': 'MupTdo',
                'cuts': phase_spaces_tot_mu,
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']),
                'folderUp' : mcDirectoryHWW+'__MupTup_suffix',
                'folderDown' : mcDirectoryHWW+'__MupTdo_suffix'
}

# ##################
# # PU jet id

nuisances['JetPUID_sf']  = {
                'name'  : 'CMS_jetpuid_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc )
}


# # ##### Jet energy scale

# # ##### Jet energy scale
# # jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2',
# #             'JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal',
# #             'JESRelativeSample_2017']

# # for js in jes_systs:
# #     nuisances[js]  = {
# #                     'name': 'CMS_j_scale_'+js,
# #                     'kind': 'suffix',
# #                     'type': 'shape',
# #                     'mapUp': js+'up',
# #                     'mapDown': js+'do',
# #                     # 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']+wjets_res_bins),
# #                     'samples': dict((skey, ['1.','1.']) for skey in mc_selected),
# #                     'folderUp' : mcDirectory+'_JESup',
# #                     'folderDown' : mcDirectory+'_JESdo',
# #                     'AsLnN'      : '1',             
# #     }


# # ##### Jet energy resolution
# # nuisances['JER']  = {
# #                 'name': 'CMS_res_j_2017',
# #                 'kind': 'suffix',
# #                 'type': 'shape',
# #                 'mapUp': 'JERup',
# #                 'mapDown': 'JERdo',
# #                 'samples': dict((skey, ['1.','1.']) for skey in mc_selected),
# #                 'folderUp' : mcDirectory+'_JERup',
# #                 'folderDown' : mcDirectory+'_JERdo',
# #                 'AsLnN'      : '1',
# # }


# # ##### MET energy scale
nuisances['MET']  = {
                'name'  : 'CMS_scale_met_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp':   'METup',
                'mapDown': 'METdo', 
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]),
                'folderUp' : mcDirectoryHWW+'__METup_suffix',
                'folderDown' : mcDirectoryHWW+'__METdo_suffix',
                'AsLnN'      : '1',
}


# ## Top pT reweighting uncertainty

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

# ## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
   'name': 'CMS_topPtRew',   # Theory uncertainty
   'kind': 'weight',
   'type': 'shape',
   'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
   'symmetrize': True
}

# ##################

# # for jtype in ["quark", "gluon"]:
# #       for  jeta in ["higheta", "loweta"]:
# #         nuisances['QGLmorphing_{}_{}'.format(jtype, jeta)]  = {
# #             'name': 'QGLmorph_{}_{}_1718'.format(jtype, jeta),
# #             'kind': 'suffix',
# #             'type': 'shape',
# #             'samples': dict((skey, ['1.','1.']) for skey in mc),
# #         }


# # ######################
# # # Theory nuisance


# # # # #
# # # # # PS and UE
# # # # # #
# # # # #### USE this for producing shapes
for sample in mc :
    nuisances['PS_ISR']  = {
                    'name'  : 'CMS_PS_ISR_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {   
                        sample : ['PSWeight[2]','PSWeight[0]'] }
                }

    nuisances['PS_FSR']  = {
                    'name'  : 'CMS_PS_FSR_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {     
                        sample : ['PSWeight[3]','PSWeight[1]'] }
                }

    # # # ##############

    nuisances['PU']  = {
                    'name'  : 'CMS_PU_2017_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                        sample : ['(puWeightUp/puWeight)','(puWeightDown/puWeight)'] },
                    'AsLnN'      : '1',
    }

for sample in mc :
    if sample in ["WLNuJJ"] : continue
    nuisances['QCD_scale_'+sample] = {
        'name'  : 'QCDscale_'+sample,
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
    }

# # # # #Correlate all signal samples

nuisances['QCD_scale_WLNuJJ_accept'] = {
            'name'  : 'QCD_scale_WLNuJJ_accept',
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples'  :  { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in ["WLNuJJ"] }
        }

# ###### uncomment from here 4 datacards
nuisances['pdf_weight_'+"Wjets_HT"] = {
    'name'  : 'pdf_weight_1718_'+"Wjets_HT",
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["Wjets_HT"]},
    'AsLnN':  '1',
    'cuts':  wj_region + phase_spaces_tot_sr
}

nuisances['pdf_weight_'+"top"] = {
    'name'  : 'pdf_weight_1718_'+"top",
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["top"] },
    'AsLnN':  '1',
    'cuts':  phase_spaces_tot_sr_top
}

nuisances['pdf_weight_accept'] = {
    'name'  : 'pdf_weight_1718_accept',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples': { k : [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ] for k in ["WLNuJJ"] },
    'cuts':  phase_spaces_tot_sr
}

# # # # An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# # # # And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                # 'samples': dict((skey, '1.015') for skey in mc if skey not in ["top","Wjets_HT"]),  why not this? they use CP5...
                'samples': dict((skey, '1.015') for skey in mc ), 
}

# reweight wjet nuisances
WJets_up = '( WJets_reweight_up / WJets_reweight )'
WJets_do = '( WJets_reweight_do / WJets_reweight )'

nuisances['WJets_reweight'] = {
    'name': 'WJets_rew_stat_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': { 
       'Wjets_HT_hardJets': [WJets_up, WJets_do]
      }
}

WJets_functional = '( WJets_reweight_func /  WJets_reweight )'
nuisances['WJets_reweight_functional_2018'] = {
    'name': 'WJets_rew_func_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
       'Wjets_HT_hardJets': [WJets_functional, "1."]
      },
    # 'symmetrize': True
}


# # ####### Generic "cross section uncertainties"
# # ##############
# # # Normalization factors
# # ##############


nuisances["Top_norm_2017"]  = {
    'name'  : 'CMS_Top_norm_2017',
    'samples'  : {
        'top' : '1.00',
        },
    'type'  : 'rateParam'
}

# # for fl in ["ele", "mu"]:
# #     nuisances["Fake_norm_{}_2018".format(fl)]  = {
# #         'name'  : 'CMS_Fake_norm_{}_2018'.format(fl),
# #         'samples'  : {
# #             'Fake' : '1.00',
# #             },
# #         'type'  : 'rateParam',
# #         'cuts': [region for region in regions if fl in region or "topcr" in region]
# #     }

for fl in ["ele", "mu"]:
    nuisances["WPUJet_norm_{}_2017".format(fl)]  = {
        'name'  : 'CMS_WPUJet_norm_{}_2017'.format(fl),
        'samples'  : {'Wjets_HT_PUJets' : '1.00'},
        'type'  : 'rateParam',
        'cuts': [region for region in regions if fl in region or "topcr" in region]
    }


for fl in ["ele", "mu"]:
    nuisances["WhardJet_norm_{}_2017".format(fl)]  = {
                    'name'  : 'CMS_WhardJet_norm_{}_2017'.format(fl),
                    'samples'  : {'Wjets_HT_hardJets' : '1.00'},
                    'type'  : 'rateParam',
                    'cuts': [region for region in regions if fl in region or "topcr" in region]
            }


# ## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
            #    nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
            #    nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }


# for n in nuisances.values():
#     n['skipCMS'] = 1

   
   

# # nuisances = {k:v for k,v in nuisances.items() if "JES" in k } #if 'PS' in k or 'QCD' in k


# # print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))