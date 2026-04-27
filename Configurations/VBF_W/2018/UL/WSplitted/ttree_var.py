
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'event',
    'pt1',
    # 'eta1',
    # 'phi1',
    # 'puppimet_phi',
    # 'mtw1',
    # 'puppimet',
    # 'Dphilep1met',
    # 'ptW',
    # 'njet_30',
    # 'njet_40',
    # 'njet_80',
    # 'jetpt1',
    # 'jetpt2',
    # 'jeteta1',
    # 'jeteta1',
    # 'mjj',
    # 'detajj',
    # 'Dphijet1met', 
    # 'Dphijet2met', 
    # 'Dphijet1jet2', 
    # 'Dphilep1jet1',
    # 'Dphilep1jet2',
    # 'R',
    # 'Zl1',
    # 'QGL1',
    # 'QGL2'
]


all_var = { v:v for v in var }

## need expressions for this!
all_var['pt1'] = 'Lepton_pt[0]'
# all_var['eta1'] = 'Lepton_eta[0]'
# all_var['phi1'] = 'Lepton_phi[0]'
# all_var['puppimet_phi'] =  'PuppiMET_phi'
# all_var['puppimet'] = 'PuppiMET_pt'
# all_var['njet_30'] = 'Sum$(CleanJet_pt>30)'
# all_var['njet_40'] = 'Sum$(CleanJet_pt>40)'
# all_var['njet_80'] = 'Sum$(CleanJet_pt>80)'
# all_var['jetpt1'] = 'CleanJet_pt[0]'
# all_var['jetpt2'] = 'CleanJet_pt[1]'
# all_var['jeteta1'] = 'CleanJet_eta[0]'
# all_var['jeteta2'] = 'CleanJet_eta[1]'
# all_var['R'] = 'R_AN'
# all_var['QGL1'] = 'Jet_qgl[0]'
# all_var['QGL2'] = 'Jet_qgl[1]'



variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['ele_SR_plus', 'mu_SR_plus', 'ele_SR_minus', 'mu_SR_minus', 'ele_HWJ_plus', 'ele_PUWJ_plus', 'mu_HWJ_plus', 'mu_PUWJ_plus', 'ele_HWJ_minus', 'ele_PUWJ_minus',  'mu_HWJ_minus', 'mu_PUWJ_minus', 'ele_topcr_plus', 'mu_topcr_plus']
}
# variables['dnn_inputs_all'] = {
#     'tree': all_var,
#     'cuts' : ['SR2', 'SR4', 'SRAll', 'HWJ2', 'HWJ4', 'HWJAll']
# }

