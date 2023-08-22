res_vars = ['mjj', 'mll']

res_branches =  { v:v for v in res_vars }


##################################

variables['vars4giulia'] = {
    'tree': res_branches,
    # 'cuts' : ['res_sig_ele', 'res_sig_mu']
}
