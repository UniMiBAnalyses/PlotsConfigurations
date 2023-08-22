res_vars = [  'detajj', 
            'dphijj', 
            'dphillmet',
            'mth',
            'etaj1', 
            'etaj2', 
            'etal1', 
            'etal2',
            'phij1',
            'phij2',
            'phil1',
            'phil2',
            'MET_pt',
            'MET_phi',
            'mjj',
            'mll',  
            'ptj1', 
            'ptj2', 
            'ptl1',
            'ptl2', 
            'ptll',
#            'massj1',
#            'massj2',
            'pdgIDl1',
            'pdgIDl2',
            # 'NeutrinoGen1_phi',
            # 'NeutrinoGen2_phi',
            # 'NeutrinoGen1_pt',
            # 'NeutrinoGen2_pt',
            # 'NeutrinoGen1_eta',
            # 'NeutrinoGen2_eta',
            # 'NeutrinoGen1_mass',
            # 'NeutrinoGen2_mass',
            # 'NeutrinoGen1_pdgID',
            # 'NeutrinoGen2_pdgID',

            # 'Lepton1_E',
            # 'Lepton1_px',
            # 'Lepton1_py',
            # 'Lepton1_pz',
            # 'Lepton2_E',
            # 'Lepton2_px',
            # 'Lepton2_py',
            # 'Lepton2_pz',
            # 'NeutrinoGen1_E',
            # 'NeutrinoGen1_px',
            # 'NeutrinoGen1_py',
            # 'NeutrinoGen1_pz',
            # 'NeutrinoGen2_E',
            # 'NeutrinoGen2_px',
            # 'NeutrinoGen2_py',
            # 'NeutrinoGen2_pz',

            # 'myFLAG',
#            'XSWeight'
]

res_branches =  { v:v for v in res_vars }


##################################

variables['vars4giulia'] = {
    'tree': res_branches,
    # 'cuts' : ['res_sig_ele', 'res_sig_mu']
}
