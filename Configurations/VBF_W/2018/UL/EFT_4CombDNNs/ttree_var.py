
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'pt1',
    'puppimet_phi',
    'mtw1',
    'puppimet',
    'Dphilep1met',
    'detajj',
    'Dphijet1met', 
    'Dphijet2met', 
    'Dphijet1jet2', 
    'Dphilep1jet1',
    'Dphilep1jet2',
    'R',
    'Zl1',
    'ptW',
    'jet_phi1',
    'jet_phi2',
    'jet_pt1',
    'jet_pt2',
    'jet_eta1',
    'jet_eta2',
    'lep_eta1',
    'lep_phi1',
    'DNN',
    'fakeWeight_0p9',
    'fakeWeight_0p9Up',
    'fakeWeight_0p9Down',
    'fakeWeight_statUp',
    'fakeWeight_statDo',
]


all_var = { v:v for v in var }

## need expressions for this!
all_var['pt1'] = 'Lepton_pt[0]'
all_var['lep_eta1'] = 'Lepton_eta[0]'
all_var['lep_phi1'] = 'Lepton_phi[0]'
all_var['puppimet_phi'] =  'PuppiMET_phi'
all_var['puppimet'] = 'PuppiMET_pt'
all_var['jet_pt1'] = 'CleanJet_pt[0]'
all_var['jet_pt2'] = 'CleanJet_pt[1]'
all_var['jet_eta1'] = 'CleanJet_eta[0]'
all_var['jet_phi1'] = 'CleanJet_phi[0]'
all_var['jet_eta2'] = 'CleanJet_eta[1]'
all_var['jet_phi2'] = 'CleanJet_phi[1]'
all_var['R'] = 'R_AN'
all_var['DNN'] = 'DNNJoined'




variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['ele_SR', 'mu_SR', 'ele_HWJ', 'mu_HWJ', 'ele_PUWJ', 'mu_PUWJ', 'ele_topcr', 'mu_topcr']
}
# variables['dnn_inputs_all'] = {
#     'tree': all_var,
#     'cuts' : ['SR2', 'SR4', 'SRAll', 'HWJ2', 'HWJ4', 'HWJAll']
# }

