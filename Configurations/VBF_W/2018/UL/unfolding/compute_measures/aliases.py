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