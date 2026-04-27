

##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'XSWeight',
    'mjj_gen',
    'jetpt2_gen',
    'jetpt1_gen',
    'LHEScaleWeight3',
    'LHEScaleWeight4',
    'LHEScaleWeight5',
    'mjj'
]

all_var = { v:v for v in var }

## need expressions for this!
all_var['LHEScaleWeight3'] = 'LHEScaleWeight[3]'
all_var['LHEScaleWeight4'] = 'LHEScaleWeight[4]'
all_var['LHEScaleWeight5'] = 'LHEScaleWeight[5]'
all_var['jetpt1_gen'] = 'Alt$(CleanGenJet_pt[0],0)'
all_var['jetpt2_gen'] = 'Alt$(CleanGenJet_pt[1],0)'


variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['ALL', 'SR']
}