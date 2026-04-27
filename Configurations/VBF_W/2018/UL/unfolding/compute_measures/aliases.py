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

aliases['nCleanGenJet20'] = {
    'expr': 'Sum$(CleanGenJet_pt > 20.)',
}

#####################################
######## user defined ###############
#####################################

############# L1 GEN ###########
aliases ['x_ptl1_gen'] = {
    'expr': 'Alt$(DressedLepton_pt[0],-9999.) * TMath::Cos(Alt$(DressedLepton_phi[0],-9999.))',
    'samples' : signals
}

aliases ['y_ptl1_gen'] = {
    'expr': 'Alt$(DressedLepton_pt[0],-9999.) * TMath::Sin(Alt$(DressedLepton_phi[0],-9999.))',
    'samples' : signals
}

########## NEUTRINO GEN ############
aliases ['x_ptMET_gen'] = {
    'expr': 'NeutrinoGen_pt * TMath::Cos(NeutrinoGen_phi)',
    'samples' : signals
}

aliases ['y_ptMET_gen'] = {
    'expr': 'NeutrinoGen_pt * TMath::Sin(NeutrinoGen_phi)',
    'samples' : signals
}

########### W (L1+MET) GEN ###########
aliases['x_ptW_gen'] = {
    'expr': 'x_ptl1_gen + x_ptMET_gen',
    'samples' : signals
}

aliases['y_ptW_gen'] = {
    'expr': 'y_ptl1_gen + y_ptMET_gen',
    'samples' : signals
}

aliases['ptW_gen'] = {
    'expr': 'TMath::Sqrt(x_ptW_gen*x_ptW_gen + y_ptW_gen*y_ptW_gen)',
    'samples' : signals
}

aliases['jeteta1_gen_abs'] = {
    'expr': 'TMath::Abs(Alt$(CleanGenJet_eta[0],-9999.))'
}

aliases['jeteta2_gen_abs'] = {
    'expr': 'TMath::Abs(Alt$(CleanGenJet_eta[1],-9999.))'
}

aliases['lepeta_gen_abs'] = {
    'expr': 'TMath::Abs(Alt$(DressedLepton_eta[0],-9999.))'
}

aliases['CleanGenJet1_px'] = {
    'expr': 'Alt$(CleanGenJet_pt[0],-9999.) * TMath::Cos(Alt$(CleanGenJet_phi[0],-9999.))'
}

aliases['CleanGenJet1_py'] = {
    'expr': 'Alt$(CleanGenJet_pt[0],-9999.) * TMath::Sin(Alt$(CleanGenJet_phi[0],-9999.))'
}

aliases['CleanGenJet2_px'] = {
    'expr': 'Alt$(CleanGenJet_pt[1],-9999.) * TMath::Cos(Alt$(CleanGenJet_phi[1],-9999.))'
}

aliases['CleanGenJet2_py'] = {
    'expr': 'Alt$(CleanGenJet_pt[1],-9999.) * TMath::Sin(Alt$(CleanGenJet_phi[1],-9999.))'
}

aliases['ptjj_gen'] = {
    'expr': 'TMath::Sqrt(( (CleanGenJet1_px + CleanGenJet2_px)**2 + (CleanGenJet1_py + CleanGenJet2_py)**2 ))'
}
aliases['Dphijet1jet2_gen'] = {    
    'expr': 'abs((CleanGenJet_phi[0] - CleanGenJet_phi[1]) - 2*3.1415*((CleanGenJet_phi[0] - CleanGenJet_phi[1]) > 3.1415) + 2*3.1415*((CleanGenJet_phi[0] - CleanGenJet_phi[1]) < -3.1415))'
}

aliases['lhesel'] = {
    'class': 'LHE_selection',
    'args': (),
     'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}macros/lhemjj.cc+'.format(utils_folder)
        ] 
} 