##############################################
# now variables to plot
# Include also variables to be plotted
res_cuts = [ c for c in cuts if 'res' in c]
boost_cuts = [ c for c in cuts if 'boost' in c]
sig_cuts =  [ c for c in cuts if 'sig' in c]

res_vars = [
    'lin_weight_cHbox',
    #'quad_weight_cHbox'
]

res_branches =  { v:v for v in res_vars }


boost_vars = res_vars
boost_branches =  { v:v for v in boost_vars }

##################################

variables['lin_weights_resolved'] = {
    'tree': res_branches,
    'cuts' : res_cuts
}

variables['lin_weights_boosted'] = {
    'tree':  boost_branches,
    'cuts' : boost_cuts
}

variables['dnn_inputs_all'] = {
    'tree':  res_branches,
    'cuts' : ['all']
}



# variables['lin_weight_cHbox'] = {   'name': 'lin_weight_cHbox',      
#                         'range' : (20,-0.00001,0.00001),  
#                         'xaxis' : 'lin_weight_cHbox', 
#                         'fold' : 3,
#                         'cuts': [c for c in res_cuts + boost_cuts]
#                         }  


# variables['quad_weight_cHbox'] = {   'name': 'quad_weight_cHbox',      
#                         'range' : (20,-0.00001,0.00001),  
#                         'xaxis' : 'quad_weight_cHbox', 
#                         'fold' : 3,
#                         'cuts': [c for c in res_cuts + boost_cuts]
#                         }   


# variables['run_info_boost'] = {
#     'tree':  {"run":"run","lumi":"luminosityBlock","event":"event", "DNN":"DNNoutput_boosted"},
#     'cuts' : ['boost_sig_ele', 'boost_sig_mu']
# }

# variables['run_info_res'] = {
#     'tree':  {"run":"run","lumi":"luminosityBlock","event":"event", "DNN":"DNNoutput_resolved_v1"},
#     'cuts' : ['res_sig_ele', 'res_sig_mu']
# }


#variables = {k:v for k,v in variables.items() if k in ["DNNoutput_res_v1", "DNNoutput_boost"]}

# variables = {k:v for k,v in variables.items() if k in ["DNNoutput_res_v1", "lin_weight_cHbox"]}