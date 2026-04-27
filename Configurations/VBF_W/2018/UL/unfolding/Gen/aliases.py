import os
import copy
import inspect
import json

configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
conf_folder = configurations +"/VBF_W/2018/"
utils_folder = configurations +"/VBF_W/utils/"

signals = [c for c in samples if "WLNuJJ" in c]
#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

####################


aliases['nCleanGenJet20'] = {
    'expr': 'Sum$(CleanGenJet_pt > 20.)',
    'samples': signals
}


#####################################
######## user defined ###############
#####################################


############# L1 GEN ###########
aliases ['x_ptl1_gen'] = {
    'expr': 'Alt$(DressedLepton_pt[0],-9999.) * TMath::Cos(Alt$(DressedLepton_phi[0],-9999.))',
    'samples': signals
}

aliases ['y_ptl1_gen'] = {
    'expr': 'Alt$(DressedLepton_pt[0],-9999.) * TMath::Sin(Alt$(DressedLepton_phi[0],-9999.))',
    'samples': signals
}


########## NEUTRINO GEN ############
aliases ['x_ptMET_gen'] = {
    'expr': 'NeutrinoGen_pt * TMath::Cos(NeutrinoGen_phi)',
    'samples': signals
}

aliases ['y_ptMET_gen'] = {
    'expr': 'NeutrinoGen_pt * TMath::Sin(NeutrinoGen_phi)',
    'samples': signals
}


########### W (L1+MET) GEN ###########
aliases['x_ptW_gen'] = {
    'expr': 'x_ptl1_gen + x_ptMET_gen',
    'samples': signals
}

aliases['y_ptW_gen'] = {
    'expr': 'y_ptl1_gen + y_ptMET_gen',
    'samples': signals
}

aliases['ptW_gen'] = {
    'expr': 'TMath::Sqrt(x_ptW_gen*x_ptW_gen + y_ptW_gen*y_ptW_gen)',
    'samples': signals
}


aliases['jeteta1_gen_abs'] = {
    'expr': 'TMath::Abs(Alt$(CleanGenJet_eta[0],-9999.))',
    'samples': signals
}

aliases['jeteta2_gen_abs'] = {
    'expr': 'TMath::Abs(Alt$(CleanGenJet_eta[1],-9999.))',
    'samples': signals
}

aliases['lepeta_gen_abs'] = {
    'expr': 'TMath::Abs(Alt$(DressedLepton_eta[0],-9999.))',
    'samples': signals
}


aliases['CleanGenJet1_px'] = {
    'expr': 'Alt$(CleanGenJet_pt[0],-9999.) * TMath::Cos(Alt$(CleanGenJet_phi[0],-9999.))',
    'samples': signals
}

aliases['CleanGenJet1_py'] = {
    'expr': 'Alt$(CleanGenJet_pt[0],-9999.) * TMath::Sin(Alt$(CleanGenJet_phi[0],-9999.))',
    'samples': signals
}

aliases['CleanGenJet2_px'] = {
    'expr': 'Alt$(CleanGenJet_pt[1],-9999.) * TMath::Cos(Alt$(CleanGenJet_phi[1],-9999.))',
    'samples': signals
}

aliases['CleanGenJet2_py'] = {
    'expr': 'Alt$(CleanGenJet_pt[1],-9999.) * TMath::Sin(Alt$(CleanGenJet_phi[1],-9999.))',
    'samples': signals
}

aliases['ptjj_gen'] = {
    'expr': 'TMath::Sqrt(( (CleanGenJet1_px + CleanGenJet2_px)**2 + (CleanGenJet1_py + CleanGenJet2_py)**2 ))',
    'samples': signals
}

############ DELTAPHI #####################
aliases['Dphijet1jet2_gen'] = {    
    'expr': 'abs((CleanGenJet_phi[0] - CleanGenJet_phi[1]) - 2*3.1415*((CleanGenJet_phi[0] - CleanGenJet_phi[1]) > 3.1415) + 2*3.1415*((CleanGenJet_phi[0] - CleanGenJet_phi[1]) < -3.1415))',
    'samples': signals
}



#####################################
########### GEN ALIASES #############
#####################################

########## Ratio / topology variables ##########

# R_AN is typically the ratio of ptW / mjj, keeping same style as reco
aliases['R_AN_gen'] = {
    'expr': '(ptW_gen / (Alt$(CleanGenJet_pt[0],-9999.) + Alt$(CleanGenJet_pt[1],-9999.) + ptW_gen))',
    'samples': signals
}

########## Zeppenfeld variables ##########

# average eta of the two leading jets
aliases['avgEta_jj_gen'] = {
    'expr': '(Alt$(CleanGenJet_eta[0],-9999.) + Alt$(CleanGenJet_eta[1],-9999.)) / 2.',
    'samples': signals
}

# Zl1: distance of lepton from average jet eta
aliases['Zl1_gen'] = {
    'expr': 'Alt$(DressedLepton_eta[0],-9999.) - avgEta_jj_gen',
    'samples': signals
}





#####################################
########### 3rd JET GEN #############
#####################################

aliases['ptj3_gen'] = {
    'expr': 'Alt$(CleanGenJet_pt[2]*(CleanGenJet_pt[2]>20.), 0.)',
    'samples': signals
}

aliases['etaj3_gen'] = {
    'expr': 'Alt$(CleanGenJet_eta[2]*(CleanGenJet_pt[2]>20.), -9999.)',
    'samples': signals
}

aliases['etaj3_gen_abs'] = {
    'expr': 'TMath::Abs(Alt$(CleanGenJet_eta[2]*(CleanGenJet_pt[2]>20.), -9999.))',
    'samples': signals
}

aliases['phij3_gen'] = {
    'expr': 'Alt$(CleanGenJet_phi[2]*(CleanGenJet_pt[2]>20.), -9999.)',
    'samples': signals
}


#####################################
########### dphi wrt jets #############
#####################################

# dphi tra j3 e j1
aliases['Dphij3j1_gen'] = {
    'expr': '((abs((Alt$(CleanGenJet_phi[2],0.) - Alt$(CleanGenJet_phi[0],0.)) \
                  - 2*3.1415*((Alt$(CleanGenJet_phi[2],0.) - Alt$(CleanGenJet_phi[0],0.)) > 3.1415) \
                  + 2*3.1415*((Alt$(CleanGenJet_phi[2],0.) - Alt$(CleanGenJet_phi[0],0.)) < -3.1415))) ) \
               * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
               + (-9999.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}

# dphi tra j3 e j2
aliases['Dphij3j2_gen'] = {
    'expr': '((abs((Alt$(CleanGenJet_phi[2],0.) - Alt$(CleanGenJet_phi[1],0.)) \
                  - 2*3.1415*((Alt$(CleanGenJet_phi[2],0.) - Alt$(CleanGenJet_phi[1],0.)) > 3.1415) \
                  + 2*3.1415*((Alt$(CleanGenJet_phi[2],0.) - Alt$(CleanGenJet_phi[1],0.)) < -3.1415))) ) \
               * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
               + (-9999.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}

# phi del sistema j1+j2
aliases['phi_jj_gen'] = {
    'expr': 'TMath::ATan2((CleanGenJet1_py + CleanGenJet2_py), (CleanGenJet1_px + CleanGenJet2_px))',
    'samples': signals
}

# dphi tra j3 e jj-system
aliases['Dphij3jj_gen'] = {
    'expr': '((abs((Alt$(CleanGenJet_phi[2],0.) - phi_jj_gen) \
                  - 2*3.1415*((Alt$(CleanGenJet_phi[2],0.) - phi_jj_gen) > 3.1415) \
                  + 2*3.1415*((Alt$(CleanGenJet_phi[2],0.) - phi_jj_gen) < -3.1415))) ) \
               * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
               + (-9999.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}


#####################################
########### deta wrt jets #############
#####################################

aliases['Detaj3j1_gen'] = {
    'expr': '(abs(Alt$(CleanGenJet_eta[2],-9999.) - Alt$(CleanGenJet_eta[0],-9999.))) \
              * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
              + (-9999.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}

aliases['Detaj3j2_gen'] = {
    'expr': '(abs(Alt$(CleanGenJet_eta[2],-9999.) - Alt$(CleanGenJet_eta[1],-9999.))) \
              * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
              + (-9999.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}

aliases['avgEta_jj_gen'] = {
    'expr': '(Alt$(CleanGenJet_eta[0],-9999.) + Alt$(CleanGenJet_eta[1],-9999.)) / 2.',
    'samples': signals
}

aliases['Detaj3jj_gen'] = {
    'expr': '(abs(Alt$(CleanGenJet_eta[2],-9999.) - avgEta_jj_gen)) \
              * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
              + (-9999.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}


#####################################
########### vs Lepton ###############
#####################################

aliases['Dphij3lep_gen'] = {
    'expr': '((abs((Alt$(CleanGenJet_phi[2],0.) - Alt$(DressedLepton_phi[0],0.)) \
                  - 2*3.1415*((Alt$(CleanGenJet_phi[2],0.) - Alt$(DressedLepton_phi[0],0.)) > 3.1415) \
                  + 2*3.1415*((Alt$(CleanGenJet_phi[2],0.) - Alt$(DressedLepton_phi[0],0.)) < -3.1415))) ) \
               * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
               + (-9999.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}

aliases['Detaj3lep_gen'] = {
    'expr': '(abs(Alt$(CleanGenJet_eta[2],-9999.) - Alt$(DressedLepton_eta[0],-9999.))) \
              * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
              + (-9999.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}


#####################################
########### dR combined #############
#####################################

aliases['DRj3jj_gen'] = {
    'expr': '(TMath::Sqrt(Detaj3jj_gen*Detaj3jj_gen + Dphij3jj_gen*Dphij3jj_gen)) \
              * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
              + (-1.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}

aliases['DRj3lep_gen'] = {
    'expr': '(TMath::Sqrt(Detaj3lep_gen*Detaj3lep_gen + Dphij3lep_gen*Dphij3lep_gen)) \
              * (Alt$(CleanGenJet_pt[2],0.) > 20.) \
              + (-1.) * (Alt$(CleanGenJet_pt[2],0.) <= 20.)',
    'samples': signals
}

aliases['lhe_gensel'] = {
    'class': 'LHE_GEN',
    'args': (),
     'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}macros/lheGEN.cc+'.format(utils_folder)
        ] 
} 

# aliases['tauVetoALL'] = {
#     'expr': '(Sum$(abs(LHEPart_pdgId)==15 && LHEPart_status==1) == 0)',
#     'samples': [c for c in signals if 'SHERPA' not in c]
# }

# aliases['tauVeto'] = {
#     'expr': '( (abs(Alt$(LHEPart_pdgId[2],0)) != 15) && (abs(Alt$(LHEPart_pdgId[3],0)) != 15) )',
#     'samples': [c for c in signals if 'SHERPA' not in c]
# }