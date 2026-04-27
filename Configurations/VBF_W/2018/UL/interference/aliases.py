import os
import copy
import inspect

configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
conf_folder = configurations +"/VBF_W/2018/"
utils_folder = configurations +"/VBF_W/utils/"

signals = [c for c in samples if "WLNuJJ" in c]
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



####################################################################################
# b tagging WPs: https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL18
####################################################################################
### to be checked!!!!!

# DeepB = DeepCSV
bWP_loose_deepB  = '0.1208'
bWP_medium_deepB = '0.4168' 
bWP_tight_deepB  = '0.7665'

# DeepFlavB = DeepJet
bWP_loose_deepFlavB  = '0.0490'
bWP_medium_deepFlavB = '0.2783'
bWP_tight_deepFlavB  = '0.7100'

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




###################################


#DNNs
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

aliases['lhesel'] = {
    'class': 'LHE_selection',
    'args': (),
     'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}macros/lhemjj.cc+'.format(utils_folder)
        ] 
} 