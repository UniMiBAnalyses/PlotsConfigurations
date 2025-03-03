
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'fakeWeight_0p8',
    'fakeWeight_0p7',
    'fakeWeight_0p9',
    'fakeWeight_statUp',
    'fakeWeight_statDo',
    'fakeWeight_PRfromMC',
    'EWK1',
    'EWK2',
    'statDo',
    'statUp',
    'PR1'    
]


all_var = { v:v for v in var }

# ## need expressions for this!
all_var['EWK1'] = 'fakeWeight_0p9/fakeWeight_0p8'
all_var['EWK2'] = 'fakeWeight_0p7/fakeWeight_0p8'
all_var['statUp'] = 'fakeWeight_statUp/fakeWeight_0p8'
all_var['statDo'] = 'fakeWeight_statDo/fakeWeight_0p8'
all_var['PR1'] = 'fakeWeight_PRfromMC/fakeWeight_0p8'

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
    'cuts' : ['Z']
}
# variables['dnn_inputs_all'] = {
#     'tree': all_var,
#     'cuts' : ['SR2', 'SR4', 'SRAll', 'HWJ2', 'HWJ4', 'HWJAll']
# }

