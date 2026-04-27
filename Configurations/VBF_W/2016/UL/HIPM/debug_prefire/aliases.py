import os
import copy
import inspect

configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
conf_folder = configurations +"/VBF_W/2016/"
utils_folder = configurations +"/VBF_W/utils/"

signals = [c for c in samples if "WLNuJJ" in c]
#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

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
    # 'expr' : '(CleanJet_phi[0] - PuppiMET_phi) * (abs(CleanJet_phi[0] - PuppiMET_phi) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[0] - PuppiMET_phi)) * (abs(CleanJet_phi[0] - PuppiMET_phi) >= 3.1415)'
} 

aliases['Dphijet2met'] = {
    'expr' : 'abs(CleanJet_phi[1] - PuppiMET_phi) * (abs(CleanJet_phi[1] - PuppiMET_phi) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[1] - PuppiMET_phi)) * (abs(CleanJet_phi[1] - PuppiMET_phi) >= 3.1415)'
    # 'expr' : '(CleanJet_phi[1] - PuppiMET_phi) * (abs(CleanJet_phi[1] - PuppiMET_phi) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[1] - PuppiMET_phi)) * (abs(CleanJet_phi[1] - PuppiMET_phi) >= 3.1415)'
} 

aliases['Dphijet1jet2'] = {    
    'expr': 'abs((CleanJet_phi[0] - CleanJet_phi[1]) - 2*3.1415*((CleanJet_phi[0] - CleanJet_phi[1]) > 3.1415) + 2*3.1415*((CleanJet_phi[0] - CleanJet_phi[1]) < -3.1415))'
    # 'expr': '(CleanJet_phi[0] - CleanJet_phi[1]) - 2*3.1415*((CleanJet_phi[0] - CleanJet_phi[1]) > 3.1415) + 2*3.1415*((CleanJet_phi[0] - CleanJet_phi[1]) < -3.1415)'
}


aliases['Dphilep1jet1'] = {
    'expr' : 'abs(CleanJet_phi[0] - Lepton_phi[0]) * (abs(CleanJet_phi[0] - Lepton_phi[0]) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[0] - Lepton_phi[0])) * (abs(CleanJet_phi[0] - Lepton_phi[0]) >= 3.1415)'
    # 'expr' : '(CleanJet_phi[0] - Lepton_phi[0]) * (abs(CleanJet_phi[0] - Lepton_phi[0]) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[0] - Lepton_phi[0])) * (abs(CleanJet_phi[0] - Lepton_phi[0]) >= 3.1415)'
} 

aliases['Dphilep1jet2'] = {
    'expr' : 'abs(CleanJet_phi[1] - Lepton_phi[0]) * (abs(CleanJet_phi[1] - Lepton_phi[0]) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[1] - Lepton_phi[0])) * (abs(CleanJet_phi[1] - Lepton_phi[0]) >= 3.1415)'
    # 'expr' : '(CleanJet_phi[1] - Lepton_phi[0]) * (abs(CleanJet_phi[1] - Lepton_phi[0]) < 3.1415) + (2*3.1415 - abs(CleanJet_phi[1] - Lepton_phi[0])) * (abs(CleanJet_phi[1] - Lepton_phi[0]) >= 3.1415)'
} 

aliases['Dphilep1met'] = {
    'expr' : 'abs(Lepton_phi[0] - PuppiMET_phi) * (abs(Lepton_phi[0] - PuppiMET_phi) < 3.1415) + (2*3.1415 - abs(Lepton_phi[0] - PuppiMET_phi)) * (abs(Lepton_phi[0] - PuppiMET_phi) >= 3.1415)'
    # 'expr' : '(Lepton_phi[0] - PuppiMET_phi) * (abs(Lepton_phi[0] - PuppiMET_phi) < 3.1415) + (2*3.1415 - abs(Lepton_phi[0] - PuppiMET_phi)) * (abs(Lepton_phi[0] - PuppiMET_phi) >= 3.1415)'
} 

############ DELTAETA #####################

aliases['detalep1jet1'] = {
    'expr': 'abs(Lepton_eta[0] - CleanJet_eta[0])'
}

aliases['detalep1jet2'] = {
    'expr': 'abs(Lepton_eta[0] - CleanJet_eta[1])'
}


############ masses #####################
aliases['mlep1jet1'] = {
    'expr': 'TMath::Sqrt(2*Lepton_pt[0]*CleanJet_pt[0]*(TMath::CosH(Lepton_eta[0]-CleanJet_eta[0]) - TMath::Cos(Lepton_phi[0]-CleanJet_phi[0])))'
}

aliases['mlep1jet2'] = {
    'expr': 'TMath::Sqrt(2*Lepton_pt[0]*CleanJet_pt[1]*(TMath::CosH(Lepton_eta[0]-CleanJet_eta[1]) - TMath::Cos(Lepton_phi[0]-CleanJet_phi[1])))'
}

##########################################################################################
# b tagging WPs: https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL16preVFP
##########################################################################################

# DeepB = DeepCSV
bWP_loose_deepB  = '0.2027'
bWP_medium_deepB = '0.6001' 
bWP_tight_deepB  = '0.8819'

# DeepFlavB = DeepJet
bWP_loose_deepFlavB  = '0.0508'
bWP_medium_deepFlavB = '0.2598'
bWP_tight_deepFlavB  = '0.6502'

# Actual algo and WP definition. BE CONSISTENT!!
bAlgo = 'DeepB'          # ['DeepB',        'DeepFlavB'         ]
bWP   = bWP_medium_deepB # [bWP_loose_deepB, bWP_loose_deepFlavB]
bSF   = 'deepcsv'        # ['deepcsv',      'deepjet'           ]



# b veto
aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btag{}[CleanJet_jetIdx] > {}) == 0)'.format(bAlgo, bWP),
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_{}_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))'.format(bSF),
    'samples': mc
}

# At least two b-tagged jet
aliases['bReq'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btag{}[CleanJet_jetIdx] > {}) >= 2)'.format(bAlgo, bWP),
}
# aliases['bReqTight'] = {
#     'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btag{}[CleanJet_jetIdx] > {}) >= 2)'.format(bAlgo, bWP_tight_deepB),
# }

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_{}_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))'.format(bSF),
    'samples': mc
}

aliases['btagSF'] = {
    'expr': 'bVeto*bVetoSF + bReq*bReqSF',
    'samples': mc
}

systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:
  aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }
  aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc }

aliases['hardJets'] = {
    'expr':  'Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 10 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 10',
    'samples': ['Wjets_HT_hardJets', 'Wjets_HT_PUJets']
}

aliases['PUJets'] = {
    'expr':  '!(Jet_genJetIdx[CleanJet_jetIdx[0]] >= 0 && Jet_genJetIdx[CleanJet_jetIdx[1]] >= 0 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[0]]] > 10 && GenJet_pt[Jet_genJetIdx[CleanJet_jetIdx[1]]] > 10)',
    'samples': ['Wjets_HT_hardJets', 'Wjets_HT_PUJets']
}

###################################

# PU jet Id SF


# Need to redefine PUID scale factors, so that they are double and not vectors
aliases['PUJetIdSF'] = {
    'expr'    : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))',
    'samples' : mc,
}

aliases['PUJetIdSF_up'] = {
    'expr'    : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_up)))',
    'samples' : mc,
}

aliases['PUJetIdSF_down'] = {
    'expr'    : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_down)))',
    'samples' : mc,
}

##########################################################

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

# Data-NLO  : SF(pT) = e^(0.0615-0.0005*pT)  
# Data-NNLO : SF(pT) = e^(0.0416-0.0003*pT)
# NNLO-NLO  : SF(pT) = 0.103*e^(-0.0118*pT) - 0.000134*pT + 0.973

##### Top pT reweighting
aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPtOTF) * TMath::Exp(0.0615 - 0.0005 * antitopGenPtOTF))) + isSingleTop',
    # 'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0416 - 0.0003 * topGenPtOTF) * TMath::Exp(0.0416 - 0.0003 * antitopGenPtOTF))) + isSingleTop',
    # 'expr': 'isTTbar * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) + isSingleTop',
    'samples': ['top']
}

###########################################################################################
#fakes

basedir_fakes = configurations + "/VBF_W/utils/2016/HIPM/fakes/HLTMC_highPT_newWP"

el_pr_file = basedir_fakes + "/PR_eleDATA.root"
mu_pr_file = basedir_fakes + "/PR_muDATA.root"

el_fr_file = basedir_fakes + "/FR_ele0p9.root"
mu_fr_file = basedir_fakes + "/FR_mu0p9.root"
aliases['fakeWeight_0p9'] = { 
    'class': 'newFakeWeightOTFall',
    'args': (eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file), False, False, False, False),  #doabsEta=True (weights files have only positive value for eta), no stat variations, no PromtRate shifting
    'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}/VBF_W/utils/macros/newfakeweight_OTFall.cc+'.format(configurations)
    ],
    'samples': ["Fake"]
}

aliases['fakeWeight_statUp'] = { 
        'class': 'newFakeWeightOTFall',
        'args': (eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file), False, True, False, False),   
        'samples': ["Fake"]
}
aliases['fakeWeight_statDo'] = { 
        'class': 'newFakeWeightOTFall',
        'args': (eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file), False, False, True, False), 
        'samples': ["Fake"]
}

for ewk_sf in ["0p9Down","0p9Up"]:
    el_fr_file = basedir_fakes + "/FR_ele{}.root".format(ewk_sf)
    mu_fr_file = basedir_fakes + "/FR_mu{}.root".format(ewk_sf)

    aliases['fakeWeight_{}'.format(ewk_sf)] = { 
            'class': 'newFakeWeightOTFall',
            'args': (eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file), False, False, False, False), 
            'samples': ["Fake"]
    }



################################################
# For VgS
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}



#######################################

aliases['QCDscale_normalized'] = {
    'class': 'QCDScaleNormalized',
    'args': (),
    'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}/VBF_W/utils/macros/QCDscale_normalize.cc+'.format(configurations)
    ] ,
    'samples':["WLNuJJ"]
}

aliases['PDFweight_normalized'] = {
    'class': 'PDFWeightNormalized',
    'args': (),
    'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}/VBF_W/utils/macros/PDFweight_normalize.cc+'.format(configurations)
    ] ,
    'samples':["WLNuJJ"]
}


aliases['lhe_mjj'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[4] * LHEPart_pt[5] * (TMath::CosH(LHEPart_eta[4] - LHEPart_eta[5]) - TMath::Cos(LHEPart_phi[4] - LHEPart_phi[5])))',
    'samples': ['VBF-Z','Others']
}

aliases['lhesel'] = {
    'class': 'LHE_selection',
    'samples': ["WLNuJJ"],
    'args': (),
     'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}macros/lhemjj.cc+'.format(utils_folder)
        ] 
} 

## WJET REWEIGHT

##reweight for Wjets samples
morphing_file = utils_folder + '2016/HIPM/reweight/reweight.root'
aliases['WJets_reweight'] = {
    'class': 'ReweightJet1pT',
    'samples': ["Wjets_HT_hardJets"],
    'args': (morphing_file, "ele_ideal_function", "mu_ideal_function"),
     'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}macros/reweight_Jet1pT.cc+'.format(utils_folder)
        ] 
} 

aliases['WJets_reweight_up'] = {
    'class': 'ReweightJet1pT',
    'samples': ["Wjets_HT_hardJets"],
    'args': (morphing_file, copy.deepcopy("ele_sys_up"), copy.deepcopy("mu_sys_up"))
} 

aliases['WJets_reweight_do'] = {
    'class': 'ReweightJet1pT',
    'samples': ["Wjets_HT_hardJets"],
    'args': (morphing_file, copy.deepcopy("ele_sys_down"), copy.deepcopy("mu_sys_down"))
} 

aliases['WJets_reweight_func'] = {
    'class': 'ReweightJet1pT',
    'samples': ["Wjets_HT_hardJets"],
    'args': (morphing_file, copy.deepcopy("ele_pol2_HWJ"), copy.deepcopy("mu_pol2_HWJ"))
} 

# DNN
models_path = utils_folder + '2018/NN'

model_ev = models_path+"/"+'64_64_64/SR_RUN2_newWP_ev/'
transform_ev = model_ev + 'cumulative_signal_2018.root'

model_odd = models_path+"/"+'64_64_64/SR_RUN2_newWP_odd/'
transform_odd = model_odd + 'cumulative_signal_2018.root'

aliases['DNNJoined'] = {
    'class': 'MVAReaderDNNnoQGLEvOdd',
    'args': ( model_ev, transform_ev, model_odd, transform_odd ,False),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L {}macros/noQGLmva_reader_DNN_EVODD.cc+'.format(utils_folder)
    ]
}