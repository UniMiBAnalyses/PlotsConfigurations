
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'event',
    'pt1',
    'eta1',
    'phi1',
    'jetpt1',
    'jeteta1',
    'jetphi1',
    'jetpt2',
    'jeteta2',
    'jetphi2',
    'puppimet_pt',
    'puppimet_phi',
    'ptW',
    'mtw1',
    'mjj',
    'detajj',
    'ptjj',
    'Dphijet1met', 
    'Dphijet2met', 
    'Dphijet1jet2', 
    'Dphilep1jet1',
    'Dphilep1jet2',
    'Dphilep1met',
    'detalep1jet1', 
    'detalep1jet2',
    'mlep1jet1', 
    'mlep1jet2',
    'R',
    'Zl1',
    'QGL1',
    'QGL2',
    'nCleanJet30',
    'detajj_gen',
    'Dphijet1jet2_gen',
    'jeteta1_gen_abs',
    'CleanGenJet_pt1',
    'jeteta2_gen_abs',
    'CleanGenJet_pt2',
    'lepeta_gen_abs',
    'DressedLepton_pt1',
    'mjj_gen',
    'nCleanGenJet20',
    'ptW_gen',
    'ptjj_gen',
]


all_var = { v:v for v in var }

## need expressions for this!
all_var['pt1'] = 'Lepton_pt[0]'
all_var['eta1'] = 'Lepton_eta[0]'
all_var['phi1'] = 'Lepton_phi[0]'
all_var['jetpt1'] = 'CleanJet_pt[0]'
all_var['jeteta1'] = 'CleanJet_eta[0]'
all_var['jetphi1'] = 'CleanJet_phi[0]'
all_var['jetpt2'] = 'CleanJet_pt[1]'
all_var['jeteta2'] = 'CleanJet_eta[1]'
all_var['jetphi2'] = 'CleanJet_phi[1]'
all_var['puppimet_pt'] = 'PuppiMET_pt'
all_var['puppimet_phi'] =  'PuppiMET_phi'
all_var['R'] = 'R_AN'
all_var['QGL1'] = 'Jet_qgl[0]'
all_var['QGL2'] = 'Jet_qgl[1]'
all_var['CleanGenJet_pt1'] = 'CleanGenJet_pt[0]'
all_var['CleanGenJet_pt2'] = 'CleanGenJet_pt[1]'
all_var['DressedLepton_pt1'] = 'DressedLepton_pt[0]'



variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['ele_SR', 'mu_SR']
}
