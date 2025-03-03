
##############################################
# now variables to plot
# Include also variables to be plotted

var = [
    'leppt',
    'lepeta',
    'ptW',
    'jetpt1',
    'jetpt2',
    'jeteta1',
    'jeteta2',
    'jetphi1',
    'jetphi2',
    'nJets',
    'mjj',
    'detajj',
    'DNNoutputSR_noQGL',
    'DNNJoined',
    'Dphijet1met',
    'Dphijet2met',
    'Dphijet1jet2',
    'Dphilep1jet1',
    'Dphilep1jet2',
    'Dphilep1met',

]

all_var = { v:v for v in var }
## need expressions for this!
all_var['leppt'] = 'Lepton_pt[0]'
all_var['lepeta'] = 'Lepton_eta[0]'
all_var['jetpt1'] = 'CleanJet_pt[0]'
all_var['jetpt2'] = 'CleanJet_pt[1]'
all_var['jeteta1'] = 'CleanJet_eta[0]'
all_var['jeteta2'] = 'CleanJet_eta[1]'
all_var['jetphi1'] = 'CleanJet_phi[0]'
all_var['jetphi2'] = 'CleanJet_phi[1]'
all_var['nJets'] = 'nCleanJet'
# all_var['leppt_gen'] = 'DressedLepton_pt[0]'
# all_var['lepeta_gen'] = 'DressedLepton_eta[0]'
# all_var['jetpt1_gen'] = 'CleanGenJet_pt[0]'
# all_var['jetpt2_gen'] = 'CleanGenJet_pt[1]'
# all_var['jeteta1_gen'] = 'CleanGenJet_eta[0]'
# all_var['jeteta2_gen'] = 'CleanGenJet_eta[1]'
# all_var['jetphi1_gen'] = 'CleanGenJet_phi[0]'
# all_var['jetphi2_gen'] = 'CleanGenJet_phi[1]'
# all_var['nJets_gen'] = 'nCleanGenJet'


variables['dnn_inputs_all'] = {
    'tree': all_var,
}
