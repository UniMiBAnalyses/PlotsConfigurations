##############################################
# now variables to plot
# Include also variables to be plotted
res_cuts = [ c for c in cuts if 'res' in c]
boost_cuts = [ c for c in cuts if 'boost' in c]
sig_cuts =  [ c for c in cuts if 'sig' in c]



res_vars = [
    'Mww',
    'DNNoutput_resolved_v1',
    'fit_bin_res',
    'w_lep_pt',
    'vbs_1_pt',
    'deltaeta_vbs',
    'mjj_vbs',
    'nJets30',
    'Zlep',
    'vbs_0_pt',
    'vjet_1_pt',
    'vjet_0_pt',
    'Zvjets_0',
    'deltaphi_vbs',
    'Lepton_eta',
    'Lepton_pt',
    'Centr_ww',
    'deltaeta_vjet',
]

boost_vars = [
    'Mww',
    'DNNoutput_boosted',
    'w_lep_pt', #also known as fit_bins_boost
    'vbs_1_pt',
    'deltaeta_vbs',
    'mjj_vbs',
    'nJets30',
    'Zlep',
    'vbs_0_pt',
    'w_had_pt',
    'vjet_1_pt',
    'vjet_0_pt',
    'Zvjets_0',
    'deltaphi_vbs',
    'Lepton_eta',
    'Lepton_pt',
    'Centr_ww',
    'deltaeta_vjet'
]

res_branches =  { v:v for v in res_vars }
boost_branches =  { v:v for v in boost_vars }


variables['dnn_inputs_resolved'] = {
    'tree': res_branches,
    'cuts' : ['res_sig_ele_DNN_geq_0p5', 'res_sig_ele_DNN_leq_0p5', 'res_sig_mu_DNN_geq_0p5', 'res_sig_mu_DNN_leq_0p5']
}

variables['dnn_inputs_boosted'] = {
    'tree':  boost_branches,
    'cuts' : ['boost_sig_ele_DNN_geq_0p5', 'boost_sig_ele_DNN_leq_0p5', 'boost_sig_mu_DNN_geq_0p5', 'boost_sig_mu_DNN_leq_0p5']
}