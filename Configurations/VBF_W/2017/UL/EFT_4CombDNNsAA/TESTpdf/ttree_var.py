
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'pt1',
    'puppimet_phi',
    'mtw1',
    'puppimet',
    'Dphilep1met',
    'njet_30',
    'njet_40',
    'njet_80',
    'mjj',
    'detajj',
    'Dphijet1met', 
    'Dphijet2met', 
    'Dphijet1jet2', 
    'Dphilep1jet1',
    'Dphilep1jet2',
    'R',
    'Zl1',
    'QGL1',
    'QGL2',
    'ptW',
    'ptjj',
    'FatJet_Id',
    'FatJet_eta',
    'FatJet_pt',
    'FatJet_phi',
    'FatJet_tau1',
    'FatJet_tau2',
    'FatJet_msoftdrop',
    'FatJet_tau12',
    'jet_phi1',
    'jet_phi2',
    'jet_pt1',
    'jet_pt2',
    'jet_eta1',
    'jet_eta2',
    'lep_eta1',
    'lep_phi1',
    'DNN',
]


all_var = { v:v for v in var }

## need expressions for this!
all_var['pt1'] = 'Lepton_pt[0]'
all_var['lep_eta1'] = 'Lepton_eta[0]'
all_var['lep_phi1'] = 'Lepton_phi[0]'
all_var['puppimet_phi'] =  'PuppiMET_phi'
all_var['puppimet'] = 'PuppiMET_pt'
all_var['njet_30'] = 'Sum$(CleanJet_pt>30)'
all_var['njet_40'] = 'Sum$(CleanJet_pt>40)'
all_var['njet_80'] = 'Sum$(CleanJet_pt>80)'
all_var['jet_pt1'] = 'CleanJet_pt[0]'
all_var['jet_pt2'] = 'CleanJet_pt[1]'
all_var['jet_eta1'] = 'CleanJet_eta[0]'
all_var['jet_phi1'] = 'CleanJet_phi[0]'
all_var['jet_eta2'] = 'CleanJet_eta[1]'
all_var['jet_phi2'] = 'CleanJet_phi[1]'
all_var['R'] = 'R_AN'
all_var['QGL1'] = 'Jet_qgl[0]'
all_var['QGL2'] = 'Jet_qgl[1]'
all_var['FatJet_Id'] = 'FatJet_jetId[0]'
all_var['FatJet_eta'] = 'FatJet_eta[0]'
all_var['FatJet_pt'] = 'FatJet_pt[0]'
all_var['FatJet_phi'] = 'FatJet_phi[0]'
all_var['FatJet_tau1'] = 'FatJet_tau1[0]'
all_var['FatJet_tau2'] = 'FatJet_tau2[0]'
all_var['FatJet_msoftdrop'] = 'FatJet_msoftdrop[0]'
all_var['FatJet_tau12'] = 'FatJet_tau1[0]/FatJet_tau2[0]'
all_var['DNN'] = 'DNNJoined'




variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['ele_SR', 'mu_SR']
}
# variables['dnn_inputs_all'] = {
#     'tree': all_var,
#     'cuts' : ['SR2', 'SR4', 'SRAll', 'HWJ2', 'HWJ4', 'HWJAll']
# }

