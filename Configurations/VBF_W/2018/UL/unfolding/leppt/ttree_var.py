
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'pt1',
    'genpt1'
]


all_var = { v:v for v in var }

## need expressions for this!
all_var['pt1'] = 'Lepton_pt[0]'
all_var['genpt1'] = 'DressedLepton_pt[0]'


variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['ele_SR', 'mu_SR']
}
# variables['dnn_inputs_all'] = {
#     'tree': all_var,
#     'cuts' : ['SR2', 'SR4', 'SRAll', 'HWJ2', 'HWJ4', 'HWJAll']
# }

