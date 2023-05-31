##############################################
# now variables to plot
# Include also variables to be plotted
res_cuts = [ c for c in cuts if 'res' in c]
boost_cuts = [ c for c in cuts if 'boost' in c]
sig_cuts =  [ c for c in cuts if 'sig' in c]

########################
variables['Lepton_Pt_Mww_5per5'] = {   'name': 'Lepton_pt:Mww',      
                        'range' : ([250., 360., 470., 580., 690., 800.],[ 100.,  380.,  660.,  940., 1220., 1500.],), 
                        'xaxis' : 'p_{T}^{l} : m_{WW}', 
                        'fold' : 3,
                         #'blind': [1000,2000]
                        }


variables['Lepton_Pt_Mww_3per3'] = {   'name': 'Lepton_pt:Mww',      
                        'range' : ([200., 400., 600., 800.],[ 300.,  700., 1100., 1500.],), 
                        'xaxis' : 'p_{T}^{l} : m_{WW}', 
                        'fold' : 3,
                         #'blind': [1000,2000]
                        }

