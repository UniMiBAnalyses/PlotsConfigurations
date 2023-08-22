res_vars = [
            'met', 'metphi',
            'mjj',
            'etaj1', 'etaj2', 

            'El1','pxl1','pyl1','pzl1', 'idl_W1',
            'El2','pxl2','pyl2','pzl2', 'idl_W2',
            'ptl1','etal1','phil1',
            'ptl2','etal2','phil2',

            'Ev1','pxv1','pyv1','pzv1', 'idv_W1',
            'Ev2','pxv2','pyv2','pzv2', 'idv_W2',

            'Ej1','pxj1','pyj1','pzj1',
            'Ej2','pxj2','pyj2','pzj2',
            'massj1','ptj1','etaj1','phij1',
            'massj2','ptj2','etaj2','phij2',

            'myFLAG',
#            'XSWeight'
]

res_branches =  { v:v for v in res_vars }


##################################

variables['vars4giulia'] = {
    'tree': res_branches,
    # 'cuts' : ['res_sig_ele', 'res_sig_mu']
}
