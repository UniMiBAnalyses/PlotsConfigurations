
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'fakeWeight_1p3',
    'fakeWeight_1p4',
    'fakeWeight_1p2',
    'fakeWeight_PRfromMC',
    'fakeWeight_statUp',
    'fakeWeight_statDo',
    'EWK1',
    'EWK2',
    'PR1',
    'statUp',
    'statDo',
]


all_var = { v:v for v in var }

## need expressions for this!
all_var['EWK1'] = 'fakeWeight_1p4 / fakeWeight_1p3'
all_var['EWK2'] = 'fakeWeight_1p2 / fakeWeight_1p3'
all_var['PR1'] = 'fakeWeight_PRfromMC / fakeWeight_1p3'
all_var['statUp'] = 'fakeWeight_statUp / fakeWeight_1p3'
all_var['statDo'] = 'fakeWeight_statDo / fakeWeight_1p3'




variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['Z']
}
# variables['dnn_inputs_all'] = {
#     'tree': all_var,
#     'cuts' : ['SR2', 'SR4', 'SRAll', 'HWJ2', 'HWJ4', 'HWJAll']
# }

