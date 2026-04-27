
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'jet1pt',
    'jet2pt',
    'jet1eta',
    'jet2eta',
    'jet1phi',
    'jet2phi',
    'MET_pt',
    'MET_phi',
]


all_var = { v:v for v in var }

## need expressions for this!
all_var['jet1pt'] = 'CleanJet_pt[0]'
all_var['jet2pt'] = 'CleanJet_pt[1]'
all_var['jet1eta'] = 'CleanJet_eta[0]'
all_var['jet2eta'] = 'CleanJet_eta[1]'
all_var['jet1phi'] = 'CleanJet_phi[0]'
all_var['jet2phi'] = 'CleanJet_phi[1]'
all_var['MET_pt'] = 'PuppiMET_pt'
all_var['MET_phi'] = 'PuppiMET_phi'




variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['SR', 'HWJ', 'PUWJ', 'topcr']
}


