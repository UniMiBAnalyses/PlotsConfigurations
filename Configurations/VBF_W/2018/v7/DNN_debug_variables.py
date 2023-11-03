

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
                        }


######## lepton 1 ##########

variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (5,50,200),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }


variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (12,-2.4,2.4),   
                        'xaxis' : '#eta 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }                         
                        }



variables['ptW']  = {   'name': 'ptW',     
                        'range' : (10,0,200),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
                        }

############# getti ###################

variables['jetpt1']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (10,50,250),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
                        
variables['jetpt1_bin1']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (50,50,1000),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['mjj']      = {   'name': 'mjj',            #   variable name    
                            'range' : (5,400,800),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['detajj_H'] = {   'name': 'detajj',            #   variable name    
                            'range' : (15,2,5),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}H',  #   x axis name
                            'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
                        }


variables['R'] = {   'name': 'R_AN',     
                        'range' : (12,0,0.3),   
                        'xaxis' : 'R_AN',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}


variables['Zl1bin4'] = {   'name': 'Zl1',     
                        'range' : (10,-3,3),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['QGL1'] = {   'name': 'Jet_qgl[0]',     
                        'range' : (10,0,1),   
                        'xaxis' : 'QGL1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['QGL2'] = {   'name': 'Jet_qgl[1]',     
                        'range' : (10,0,1),   
                        'xaxis' : 'QGL2',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['DNNoutput_ALLbin1'] = {   'name': 'DNNoutputSR_ALL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['DNNoutput_ALLbin2'] = {   'name': 'DNNoutputSR_ALL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['DNNoutput_ALLbin3'] = {   'name': 'DNNoutputSR_ALL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 0.9, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}
variables['DNNoutput_ALLbin4'] = {   'name': 'DNNoutputSR_ALL',     
                        'range' : (10,0,1), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

