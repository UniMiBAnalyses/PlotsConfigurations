from pprint import pprint
# # # name of samples here must match keys in samples.py 

mc =["WLNuJJ", "Wjets_HT", "top", "VV", "VBS", "ggWW", "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VVV"]
mc_selected =["WLNuJJ", "Wjets_HT", "DY_M-50", "DY_else"]
regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr","ele_FakeCR","mu_FakeCR"]
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

phase_spaces_tot_ele = [c for c in regions if "ele" in c]
phase_spaces_tot_mu = [c for c in regions if "mu" in c]

# Function to split a nuisance on different folders for different group of samples
# keeping the same nuisance name
# groups = [ (list of samples, folder), ...  ]
# def split_nuisance_samples_dir(nuisance_name, nuisance_options, variation, groups):
#     for ig, (samples_list, folder) in enumerate(groups):
#         n = {}
#         n.update(nuisance_options)
#         n["samples"] = dict((skey, ['1.','1.']) for skey in samples_list)
#         n["folderUp"] = folder +'_'+variation + 'up'
#         n["folderDown"] = folder +'_'+variation + 'do'
#         nuisances['{}_{}'.format(nuisance_name, ig)] = n

# ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# #### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.01') for skey in mc )
}


nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc )
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc)
}


nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
}


nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc )
}


# #### FAKES

##########Fakes

fakeW_jetUp       = '( fakeWeight_45 / fakeWeight_35  )'
fakeW_jetDown     =  '( fakeWeight_25 / fakeWeight_35  )'
fakeW_statUp        =  '( fakeWeight_35_statUp / fakeWeight_35  )'
fakeW_statDown      =  '( fakeWeight_35_statDo / fakeWeight_35  )'

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

nuisances['fake_ele']  = {
                'name'  : 'CMS_fake_ele_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_jetUp , fakeW_jetDown ],
                             },
                'cuts':  phase_spaces_tot_ele
}

nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_ele_stat_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statUp , fakeW_statDown ],
                             },
                'cuts':  phase_spaces_tot_ele
}

nuisances['fake_mu']  = {
                'name'  : 'CMS_fake_mu_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_jetUp , fakeW_jetDown ],
                             },
                'cuts':  phase_spaces_tot_mu
}


nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_mu_stat_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     :[ fakeW_statUp , fakeW_statDown ],
                             },
                'cuts':  phase_spaces_tot_mu
}

# # ##### Btag nuisances

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc)
    }

# # ##### Trigger Efficiency
trig_syst = ['( SingleLepton_trigEff_corrected_up / SingleLepton_trigEff_corrected )*(SingleLepton_trigEff_corrected>0.02) + (SingleLepton_trigEff_corrected<=0.02)', 
            '(SingleLepton_trigEff_corrected_down/SingleLepton_trigEff_corrected)']

nuisances['trigg']  = {
                'name'  : 'CMS_eff_trigger_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :   dict((skey, trig_syst) for skey in mc)
}

# # Prefire correction
prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire']  = {
                'name'  : 'CMS_eff_prefiring_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, trig_syst) for skey in mc)
}

# # ##### Electron Efficiency and energy scale

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
                'name'  : 'CMS_eff_e_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :   dict((skey, id_syst_ele) for skey in mc),
                'cuts': phase_spaces_tot_ele
}

# nuisances['electronpt']  = {
#                 'name'  : 'CMS_scale_e_2016',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp': 'ElepTup',
#                 'mapDown': 'ElepTdo',
#                 'cuts': phase_spaces_tot_ele,  
#                 'samples': dict((skey, ['1.','1.']) for skey in mc_selected ),
#                 'folderUp' : mcDirectory+'_ElepTup',
#                 'folderDown' : mcDirectory+'_ElepTdo',
# }

# # ##### Muon Efficiency and energy scale


nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_mu) for skey in mc),
                 'cuts': phase_spaces_tot_mu
}

# nuisances['muonpt']  = {
#                 'name'  : 'CMS_scale_m_2016',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp': 'MupTdo',
#                 'mapDown': 'MupTdo',
#                 'cuts': phase_spaces_tot_mu, 
#                 'samples': dict((skey, ['1.','1.']) for skey in mc_selected),
#                 'folderUp' : mcDirectory+'_MupTup',
#                 'folderDown' : mcDirectory+'_MupTdo',
# }


##################
# PU jet id

nuisances['JetPUID_sf']  = {
                'name'  : 'CMS_jetpuid_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc ),
}

##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2',
            'JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal',
            'JESRelativeSample_2016']

for js in jes_systs:
    nuisances[js]  = {
                    'name': 'CMS_j_scale_'+js,
                    'kind': 'suffix',
                    'type': 'shape',
                    'mapUp':   js+'up',
                    'mapDown': js+'do',
                    'samples': dict((skey, ['1.','1.']) for skey in mc_selected),
                    'folderUp' : mcDirectory+'_JESup',
                    'folderDown' : mcDirectory+'_JESdo',
                    'AsLnN'      : '1',               
    }


# # ##### Jet energy resolution
# nuisances['JER'] = {
#                 'name': 'CMS_res_j_2016',
#                 'kind': 'suffix',
#                 'type': 'shape',
#                 'mapUp': 'JERup',
#                 'mapDown': 'JERdo',
#                 'samples': dict((skey, ['1.','1.']) for skey in mc_selected),
#                 'folderUp' : mcDirectory+'__JERup_suffix',
#                 'folderDown' : mcDirectory+'__JERdo_suffix',
#                 'AsLnN'      : '1',
# }

# # ##### MET energy scale
# nuisances['MET']  = {
#                 'name'  : 'CMS_scale_met_2016',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp':   'METup',
#                 'mapDown': 'METdo', 
#                 'samples': dict((skey, ['1.','1.']) for skey in mc_selected),
#                 'folderUp' : mcDirectory+'_METup',
#                 'folderDown' : mcDirectory+'_METdo',
#                 'AsLnN'      : '1',
# }


# # Top pT reweighting uncertainty

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
## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
   'name': 'CMS_topPtRew',   # Theory uncertainty
   'kind': 'weight',
   'type': 'shape',
   'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
   'symmetrize': True
}

##################

### why questa nuisance? e poi che valori prende???

# for jtype in ["quark", "gluon"]:
#       for  jeta in ["higheta", "loweta"]:
#         nuisances['QGLmorphing_{}_{}'.format(jtype, jeta)]  = {
#             'name': 'QGLmorph_{}_{}_16'.format(jtype, jeta),
#             'kind': 'suffix',
#             'type': 'shape',
#             'samples': dict((skey, ['1.','1.']) for skey in mc),
#         }

# ######################
# # Theory nuisance

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
# qcdscale_variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
import json, os

# for sample in mc :
#     if sample in ["WLNuJJ"] : continue
#     nuisances['QCD_scale_'+sample] = {
#         'name'  : 'QCDscale_'+sample,
#         'kind'  : 'weight',
#         'type'  : 'shape',
#         'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
#     }
for sample in mc :
    if sample in ["WLNuJJ"] : continue
    nuisances['QCD_scale_bkg'] = {
        'name'  : 'QCDscale_bkg',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
    }

#Correlate all signal samples
nuisances['QCD_scale_WLNuJJ_accept'] = {
            'name'  : 'QCD_scale_WLNuJJ_accept',
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples'  :  { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in ["WLNuJJ"] }
        }

# # Adding also the non-normalized 
# nuisances['QCD_scale_VBS_WV_full'] = {
#             'name'  : 'QCDscale_VBS_WV',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VBS_WV_samples }
#         }

# nuisances['QCD_scale_VBS_ZV_full'] = {
#             'name'  : 'QCDscale_VBS_ZV',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VBS_ZV_samples }
#         }

        
# nuisances['QCD_scale_VV_accept'] = {
#             'name'  : 'QCDscale_VV_accept',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in VV_samples }
#         }


## PS nuisance taken from 2018 effect, split by sample

# ### Propagated from 2018 effect, split by sample
# samples_PS = ['top','DY','VV','VVV','Vg','VgS','VBF-V_dipole','ggWW'] + wjets_bins #VBS_dipoleRecoil


# for sample in samples_PS:
#     nuisances['PS_ISR_'+sample]  = {
#                     'name'  : 'CMS_PS_ISR_'+sample,
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {
#                         sample :      ['PSWeight[2]', 'PSWeight[0]'],
#                     },
#                     'cuts_samples':{'Vg': [ f for f in phasespaces if "boost_topcr" not in f  ]} # necessary only for postfit in the cr
#                 }
#     nuisances['PS_FSR_'+sample]  = {
#                     'name'  : 'CMS_PS_FSR_'+sample,
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {
#                         sample :      ['PSWeight[3]', 'PSWeight[1]'],
#                     },
#                     'cuts_samples':{'Vg': [ f for f in phasespaces if "boost_topcr" not in f  ]}  # necessary only for postfit in the cr
#                 }



# nuisances['PS_ISR_VBS_WV']  = {
#                     'name'  : 'CMS_PS_ISR_VBS_WV',
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {
#                         sample : ['PSWeight[2]', 'PSWeight[0]'] for sample in VBS_WV_samples
#                     }
#                 }
# nuisances['PS_FSR_VBS_WV']  = {
#                 'name'  : 'CMS_PS_FSR_VBS_WV',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     sample :  ['PSWeight[3]', 'PSWeight[1]'] for sample in VBS_WV_samples
#                 }
#             }

# nuisances['PS_ISR_VBS_ZV']  = {
#                     'name'  : 'CMS_PS_ISR_VBS_ZV',
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {
#                         sample : ['PSWeight[2]', 'PSWeight[0]'] for sample in VBS_ZV_samples
#                     }
#                 }
# nuisances['PS_FSR_VBS_ZV']  = {
#                 'name'  : 'CMS_PS_FSR_VBS_ZV',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     sample :  ['PSWeight[3]', 'PSWeight[1]'] for sample in VBS_ZV_samples
#                 }
#             }

# # When VV is a background all the PS is correlated

# nuisances['PS_ISR_QCD_VV']  = {
#                     'name'  : 'CMS_PS_ISR_QCD_VV',
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {
#                         sample : ['PSWeight[2]', 'PSWeight[0]'] for sample in VV_samples
#                     }
#                 }
# nuisances['PS_FSR_QCD_VV']  = {
#                 'name'  : 'CMS_PS_FSR_QCD_VV',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     sample :  ['PSWeight[3]', 'PSWeight[1]'] for sample in VV_samples
#                 }
#             }


#########################################


# ###### PDF uncertainty

# nuisances['pdf_weight'] = {
#     'name'  : 'pdf_weight_16',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc if s not in ["VBS", "VV", "top","Wjets_boost"]},
#     'AsLnN':  '1'
# }
# nuisances['pdf_weight_VBS'] = {
#     'name'  : 'pdf_weight_16_accept',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { "VBS": [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ]}
# }


#############################
nuisances['PU']  = {
                'name'  : 'CMS_PU_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    s : ['(puWeightUp/puWeight)',
                         '(puWeightDown/puWeight)'] for s in mc },
                'AsLnN'      : '1',
}

# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CUET',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if skey not in ["top","Wjets_HT"]), 
}


#########################

# reweight wjet nuisances
WJets_up = '( WJets_reweight_up / WJets_reweight )'
WJets_do = '( WJets_reweight_do / WJets_reweight )'

nuisances['WJets_reweight'] = {
    'name': 'WJets_rew_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': { 
       'Wjets_HT': [WJets_up, WJets_do]
      }
}

WJets_functional = '( WJets_reweight_func /  WJets_reweight )'
nuisances['WJets_reweight_functional'] = {
    'name': 'WJets_rew_func_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
       'Wjets_HT': [WJets_functional, "1."]
      },
    'symmetrize': True
}


####### Generic "cross section uncertainties"
##############
# Normalization factors
##############


nuisances["Top_norm_2016"]  = {
    'name'  : 'CMS_Top_norm_2016',
    'samples'  : {
        'top' : '1.00',
        },
    'type'  : 'rateParam'
}

for fl in ["ele", "mu"]:
    nuisances["WPUJet_norm_{}_2016".format(fl)]  = {
        'name'  : 'CMS_WPUJet_norm_{}_2016'.format(fl),
        'samples'  : {'Wjets_HT_PUJets' : '1.00'},
        'type'  : 'rateParam',
        'cuts': [region for region in regions if fl in region or "topcr" in region]
    }


for fl in ["ele", "mu"]:
    nuisances["WhardJet_norm_{}_2016".format(fl)]  = {
                    'name'  : 'CMS_WhardJet_norm_{}_2016'.format(fl),
                    'samples'  : {'Wjets_HT_hardJets' : '1.00'},
                    'type'  : 'rateParam',
                    'cuts': [region for region in regions if fl in region or "topcr" in region]
            }


## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }


for n in nuisances.values():
    n['skipCMS'] = 1


################################
## Customizations

# Customization for mu fit with QCDscale normalization excluded
# exclude = ["QCD_scale_VBS_WV_full","QCD_scale_VBS_ZV_accept", "QCD_scale_QCD_WV_accept", "pdf_weight"]
# nuisances = {k:v for k,v in nuisances.items() if k not in exclude}


# print ' '.join(nname for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))