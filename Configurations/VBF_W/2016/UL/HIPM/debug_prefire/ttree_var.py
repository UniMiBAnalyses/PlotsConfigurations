
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'event',
    'pt1',
    'eta1',
    'phi1',
    'puppimet_phi',
    'mtw1',
    'puppimet',
    'Dphilep1met',
    'ptW',
    'jetpt1',
    'jetpt2',
    'jeteta1',
    'jeteta1',
    'mjj',
    'detajj',
    'Dphijet1met', 
    'Dphijet2met', 
    'Dphijet1jet2', 
    'Dphilep1jet1',
    'Dphilep1jet2',
    'R',
    'Zl1',
    'DNNJoined',
    'TriggerSFWeight_1l_u',
    'TriggerSFWeight_1l_d',
    'TriggerSFWeight_1l',
    'L1PreFiringWeight_Nom',
    'L1PreFiringWeight_Up',
    'L1PreFiringWeight_Dn',
    'puWeight',
    'btagSF',
    'PUJetIdSF',
    'lepton_recoSF',
    'lepton_genmatched',
    'ele_istight',
    'mu_istight',
    'ele_istightSF',
    'mu_istightSF',
    'HLT_IsoTkMu24',
    'HLT_IsoMu24',
    'HLT_Ele27_WPTight_Gsf',
    'HLT_Ele25_eta2p1_WPTight_Gsf',
    'EMTFbug_veto',
    'XSWeight',
    'METFilter_MC',
]

all_var = { v:v for v in var }

## need expressions for this!
all_var['pt1'] = 'Lepton_pt[0]'
all_var['eta1'] = 'Lepton_eta[0]'
all_var['phi1'] = 'Lepton_phi[0]'
all_var['puppimet_phi'] =  'PuppiMET_phi'
all_var['puppimet'] = 'PuppiMET_pt'
all_var['jetpt1'] = 'CleanJet_pt[0]'
all_var['jetpt2'] = 'CleanJet_pt[1]'
all_var['jeteta1'] = 'CleanJet_eta[0]'
all_var['jeteta2'] = 'CleanJet_eta[1]'
all_var['R'] = 'R_AN'
all_var['ele_istight'] = 'Lepton_isTightElectron_mvaFall17V2Iso_WP90_tthmva_70[0]'
all_var['mu_istight'] = 'Lepton_isTightMuon_cut_Tight80x_tthmva_80[0]'
all_var['ele_istightSF'] = 'Lepton_tightElectron_mvaFall17V2Iso_WP90_tthmva_70_IdIsoSF[0]'
all_var['mu_istightSF'] = 'Lepton_tightMuon_cut_Tight80x_tthmva_80_IdIsoSF[0]'
all_var['lepton_genmatched'] = 'Lepton_genmatched[0]'
all_var['lepton_recoSF'] = 'Lepton_RecoSF[0]'


variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['ele_SR', 'mu_SR', 'all', 'presel']
}
# variables['dnn_inputs_all'] = {
#     'tree': all_var,
#     'cuts' : ['SR2', 'SR4', 'SRAll', 'HWJ2', 'HWJ4', 'HWJAll']
# }

