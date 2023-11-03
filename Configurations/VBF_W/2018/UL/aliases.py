import os
import copy
import inspect

configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
conf_folder = configurations +"/VBF_W/2018/"
utils_folder = configurations +"/VBF_W/utils/"

#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
# mc = [skey for skey in samples]

####################

aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}



#####################################
######## user defined ###############
#####################################

############# Zeppendfeld variable for l1 ###########
aliases ['Zl1'] = {
    'expr': 'Alt$(Lepton_eta[0],-9999.) - 0.5*(Alt$(CleanJet_eta[0],-9999.) + Alt$(CleanJet_eta[1],-9999.))'
}

############# L1 ###########
aliases ['x_ptl1'] = {
    'expr': 'Alt$(Lepton_pt[0],-9999.) * TMath::Cos(Alt$(Lepton_phi[0],-9999.))'
}

aliases ['y_ptl1'] = {
    'expr': 'Alt$(Lepton_pt[0],-9999.) * TMath::Sin(Alt$(Lepton_phi[0],-9999.))'
}

############# J1, J2 ###########
aliases ['x_ptj1'] = {
    'expr': 'Alt$(CleanJet_pt[0],-9999.) * TMath::Cos(Alt$(CleanJet_phi[0],-9999.))'
}

aliases ['x_ptj2'] = {
    'expr': 'Alt$(CleanJet_pt[1],-9999.) * TMath::Cos(Alt$(CleanJet_phi[1],-9999.))'
}

aliases ['y_ptj1'] = {
    'expr': 'Alt$(CleanJet_pt[0],-9999.) * TMath::Sin(Alt$(CleanJet_phi[0],-9999.))'
}

aliases ['y_ptj2'] = {
    'expr': 'Alt$(CleanJet_pt[1],-9999.) * TMath::Sin(Alt$(CleanJet_phi[1],-9999.))'
}


########## MET ############
aliases ['x_ptMET'] = {
    'expr': 'PuppiMET_pt * TMath::Cos(PuppiMET_phi)'
}

aliases ['y_ptMET'] = {
    'expr': 'PuppiMET_pt * TMath::Sin(PuppiMET_phi)'
}


########### W (L1+MET) ###########
aliases['x_ptW'] = {
    'expr': 'x_ptl1 + x_ptMET'
}

aliases['y_ptW'] = {
    'expr': 'y_ptl1 + y_ptMET'
}

aliases['ptW'] = {
    'expr': 'TMath::Sqrt(x_ptW*x_ptW + y_ptW*y_ptW)'
}


#############  R from AN ##############
aliases['x_Wjj'] = {
    'expr': 'x_ptj1 + x_ptj2 + x_ptW'
}

aliases['y_Wjj'] = {
    'expr': 'y_ptj1 + y_ptj2 + y_ptW'
}

aliases['ptWjj'] = {
    'expr': 'TMath::Sqrt(x_Wjj*x_Wjj + y_Wjj*y_Wjj)'
}

aliases['R_AN'] = {
    'expr': '(ptWjj / (Alt$(CleanJet_pt[0],-9999.) + Alt$(CleanJet_pt[1],-9999.) + ptW))'
}

aliases['Rpt_req_0p2'] = {
    'expr': '(R_AN < 0.2)'
    #'expr': '(ptWjj / (ptW)) < 0.2)'
}


############ DELTAPHI #####################
aliases['Dphijet1met'] = {
    'expr' : 'abs(CleanJet_phi[0] - PuppiMET_phi) * (abs(CleanJet_phi[0] - PuppiMET_phi) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[0] - PuppiMET_phi)) * (abs(CleanJet_phi[0] - PuppiMET_phi) >= 3.1415)'
} 

aliases['Dphijet2met'] = {
    'expr' : 'abs(CleanJet_phi[1] - PuppiMET_phi) * (abs(CleanJet_phi[1] - PuppiMET_phi) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[1] - PuppiMET_phi)) * (abs(CleanJet_phi[1] - PuppiMET_phi) >= 3.1415)'
} 

aliases['Dphijet1jet2'] = {
    'expr' : 'abs(CleanJet_phi[0] - CleanJet_phi[1]) * (abs(CleanJet_phi[0] - CleanJet_phi[1]) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[0] - CleanJet_phi[1])) * (abs(CleanJet_phi[0] - CleanJet_phi[1]) >= 3.1415)'
} 

aliases['Dphilep1jet1'] = {
    'expr' : 'abs(CleanJet_phi[0] - Lepton_phi[0]) * (abs(CleanJet_phi[0] - Lepton_phi[0]) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[0] - Lepton_phi[0])) * (abs(CleanJet_phi[0] - Lepton_phi[0]) >= 3.1415)'
} 

aliases['Dphilep1jet2'] = {
    'expr' : 'abs(CleanJet_phi[1] - Lepton_phi[0]) * (abs(CleanJet_phi[1] - Lepton_phi[0]) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[1] - Lepton_phi[0])) * (abs(CleanJet_phi[1] - Lepton_phi[0]) >= 3.1415)'
} 

aliases['Dphilep1met'] = {
    'expr' : 'abs(Lepton_phi[0] - PuppiMET_phi) * (abs(Lepton_phi[0] - PuppiMET_phi) < 3.1415) + (2*3.1415 - abs(Lepton_phi[0] - PuppiMET_phi)) * (abs(Lepton_phi[0] - PuppiMET_phi) >= 3.1415)'
} 

aliases['singleW'] = {
    'expr' : 'baseW/(1000*Xsec)',
    'samples' : mc
}

# ####### trigger
# aliases['ele_trig_eff'] = {
#     'linesToAdd': [
#         'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#         '.L %s/src/PlotsConfigurations/Configurations/patches/triggerEff_1lep.cc+' % os.getenv('CMSSW_BASE')
#     ],
#     'class': 'TrigEff_1lep',
#     'args': ('/afs/cern.ch/user/a/arun/public/fixedTextfiles/2018/mvaid/Ele32_pt_eta_efficiency_withSys_Run2018.txt'),
#     'samples': mc
# }

# aliases['SingleLepton_trigEff_corrected'] = {
#     'expr': '(abs(Lepton_pdgId[0])==11)*ele_trig_eff[0] +  (abs(Lepton_pdgId[0])==13)*TriggerEffWeight_1l',
#     'samples': mc
# }

############################################
# B tagging
# loose 0.1241
# tight 0.7527

aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 2)'
}

aliases['bReqTight'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.7527) >= 2)'
}


aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

# aliases['btagSF'] = {
#     'expr': 'bVeto*bVetoSF + bReqTight *bReqSF',
#     'samples': mc
# }

aliases['btagSF'] = {
    'expr': 'bVetoSF',
    'samples': mc
}


aliases['nJetsBtag']= {
    'expr' : 'Sum$(CleanJet_pt > 20 && abs(CleanJet_eta)<2.5 )'
}

systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:
  aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReqTight*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReqTight) ))', 'samples':mc  }
  aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReqTight*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReqTight) ))', 'samples':mc }


aliases['hardJets'] = {
    'expr':  'Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 10 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 10',
    'samples': ['Wjets_HT']
}

aliases['PUJets'] = {
    'expr':  '!(Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 10 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 10)',
    'samples': ['Wjets_HT']
}

aliases['WJH_correction'] = {
    'expr': '((abs(Lepton_pdgId[0])==11)*1.2795330335917352 + (abs(Lepton_pdgId[0])==13)*1.1231175589276459)',
    'samples': ['Wjets_HT']
}

aliases['WPU_correction'] = {
    'expr': '((abs(Lepton_pdgId[0])==11)*1.1768637821969707 + (abs(Lepton_pdgId[0])==13)*1.0958905448504972)',
    'samples': ['Wjets_HT']
}

# ################################################################################################


# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

aliases['topGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['antitopGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) + isSingleTop',
    'samples': ['top']
}

#########################################################################################

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/Differential/ngenjet.cc+' % configurations],
    'class': 'CountGenJet',
    'samples': mc
}

##### DY Z pT reweighting
aliases['getGenZpt_OTF'] = {
    'linesToAdd':['.L %s/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'getGenZpt',
    'samples': mc
}
handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew30.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2018']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': mc
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2018']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': mc
}


###########################################################################################
#fakes

basedir_fakes = configurations + "/VBF_W/utils/weights_files/my_latest"

ets = ["30"]

el_pr_file = configurations + "/VBF_W/utils/weights_files/my_latest/ElePR.root"
mu_pr_file = configurations + "/VBF_W/utils/weights_files/my_latest/MuonPR.root"

for et in ets:
    el_fr_file = basedir_fakes + "/EleFR_jet"+et+".root"
    mu_fr_file = basedir_fakes + "/MuonFR_jet"+et+".root"
    aliases['fakeWeight_'+et] = { 
        'class': 'newFakeWeightOTFall',
        'args': (eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file), False, False, False),  #doabsEta=True (weights files have only positive value for eta), no stat variations
        'linesToAdd' : [
            'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
            '.L {}/VBF_W/utils/macros/newfakeweight_OTFall.cc+'.format(configurations)
        ],
        'samples': ["Fake"]
    }

    aliases['fakeWeight_statUp'] = { 
            'class': 'newFakeWeightOTFall',
            'args': (eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file), False, True, False),   
            'samples': ["Fake"]
        }
    aliases['fakeWeight_statDo'] = { 
            'class': 'newFakeWeightOTFall',
            'args': (eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file), False, False, True), 
            'samples': ["Fake"]
        }


###################################

# PU jet Id SF

puidSFSource = '{}/patches/PUID_81XTraining_EffSFandUncties.root'.format(configurations)

aliases['PUJetIdSF'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2 && ( (Jet_electronIdx1 != Lepton_electronIdx[0]) || Jet_electronIdx1 < 0 )  \
                                          && ( (Jet_muonIdx1 != Lepton_muonIdx[0] ) || Jet_muonIdx1 < 0 ) \
                            )*TMath::Log(Jet_PUIDSF_loose)))',
  'samples': mc
}


aliases['PUJetIdSF_up'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2 && ( (Jet_electronIdx1 != Lepton_electronIdx[0]) || Jet_electronIdx1 < 0 )  \
                                          && ( (Jet_muonIdx1 != Lepton_muonIdx[0] ) || Jet_muonIdx1 < 0 ) \
                            )*TMath::Log(Jet_PUIDSF_loose_up)))',
  'samples': mc
}


aliases['PUJetIdSF_down'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2 && ( (Jet_electronIdx1 != Lepton_electronIdx[0]) || Jet_electronIdx1 < 0 )  \
                                          && ( (Jet_muonIdx1 != Lepton_muonIdx[0] ) || Jet_muonIdx1 < 0 ) \
                            )*TMath::Log(Jet_PUIDSF_loose_down)))',
  'samples': mc
}


######################################


# For VgS
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

###################################

############################################

aliases['QCDscale_normalized'] = {
            'class': 'QCDScaleNormalized',
            'args': (),
            'linesToAdd' : [
                'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                '.L {}/VBSjjlnu/macros/QCDscale_normalize.cc+'.format(configurations)
            ] ,
            'samples':["WLNuJJ"]
}

aliases['PDFweight_normalized'] = {
            'class': 'PDFWeightNormalized',
            'args': (),
            'linesToAdd' : [
                'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                '.L {}/VBSjjlnu/macros/PDFweight_normalize.cc+'.format(configurations)
            ] ,
            'samples':["WLNuJJ"]
}


aliases['lhe_mjj'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[4] * LHEPart_pt[5] * (TMath::CosH(LHEPart_eta[4] - LHEPart_eta[5]) - TMath::Cos(LHEPart_phi[4] - LHEPart_phi[5])))',
    'samples': ['VBF-Z']
}

aliases['mu_isT'] = {
    'expr': '(Lepton_isTightMuon_cut_Tight_HWWW[0]<0.5)+(Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5)',
    'samples': ['Fake'] 
}

aliases['ele_isT'] = {
    'expr': '(Lepton_isTightElectron_mvaFall17V2Iso_WP90[0]<0.5)+(Lepton_isTightElectron_mvaFall17V2Iso_WP90[0]>0.5)',
    'samples': ['Fake'] 
}


## WJET REWEIGHT

##reweight for Wjets samples
morphing_file = utils_folder + '2018/UL/reweight/UL_approx_4fakes.root'
aliases['WJets_reweight'] = {
    'class': 'ReweightJet1pT',
    'samples': ['Wjets_HT'],
    'args': (morphing_file, "ele_ideal_function", "mu_ideal_function"),
     'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}macros/reweight_Jet1pT.cc+'.format(utils_folder)
        ] 
} 

aliases['WJets_reweight_up'] = {
    'class': 'ReweightJet1pT',
    'samples': ['Wjets_HT'],
    'args': (morphing_file, copy.deepcopy("ele_sys_up"), copy.deepcopy("mu_sys_up"))
} 

aliases['WJets_reweight_do'] = {
    'class': 'ReweightJet1pT',
    'samples': ['Wjets_HT'],
    'args': (morphing_file, copy.deepcopy("ele_sys_down"), copy.deepcopy("mu_sys_down"))
} 

# aliases['WJets_reweight_func'] = {
#     'class': 'ReweightJet1pT',
#     'samples': ['Wjets_HT'],
#     'args': (morphing_file, copy.deepcopy("ele_pol2_HWJ"), copy.deepcopy("mu_pol2_HWJ"))
# } 

# DNN
models_path = utils_folder + '2018/NN'
model_best = '64_64_64/SR_part/ALL/'

aliases['DNNoutputSR_ALL'] = {
  'class': 'MVAReaderDNN',
  'args': ( models_path + '/' + model_best, models_path + '/' + model_best + 'cumulative_signal_2018.root', False, 1),
  'linesToAdd':[
      'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
      'gSystem->Load("libDNNEvaluator.so")',
      '.L {}macros/ALLmva_reader_DNN.cc+'.format(utils_folder)
  ]
}
