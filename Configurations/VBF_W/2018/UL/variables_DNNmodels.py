

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        }


######## lepton 1 ##########

variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (35,0,175),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3,
                        }


variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (24,-2.4,2.4),   
                        'xaxis' : '#eta 1st lep',
                        'fold' : 3,
                        }
                        
variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold' : 3,
                        }

variables['puppimet_phi']  = {  'name': 'PuppiMET_phi',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi MET',
                        'fold' : 3,
                        }

variables['mtw1']  = {   'name': 'mtw1',
                        'range' : (20,0,200),
                         'xaxis' : 'm_{T}^{l1+MET} [GeV]',
                        'fold' : 3,
                       }

variables['ptW']  = {   'name': 'ptW',     
                        'range' : (30,0,300),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        }

############# getti ###################

variables['jetpt1']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (70,40,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        }


variables['jetpt1_PU']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (25,40,150),
                        'xaxis' : 'p_{T}PU 1st jet',
                        'fold' : 3,
                        }

variables['jetpt2']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (50,30,250),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 3,
                        }

variables['jetpt2_PU']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (10,30,60),
                        'xaxis' : 'p_{T}PU 2nd jet',
                        'fold' : 3,
                        }

variables['jeteta1']  = {
                        'name': 'CleanJet_eta[0]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 1st jet',
                         'fold' : 3,
                        }

variables['jeteta2']  = {
                        'name': 'CleanJet_eta[1]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 2nd jet',
                         'fold' : 3,
                        }

variables['jetphi1']  = {
                        'name': 'CleanJet_phi[0]',
                         'range' : (40,-3.2,3.2),
                         'xaxis' : '#phi 1st jet',
                         'fold' : 3,
                        }

variables['jetphi2']  = {
                        'name': 'CleanJet_phi[1]',
                         'range' : (40,-3.2,3.2),
                         'xaxis' : '#phi 2nd jet',
                         'fold' : 3,
                        }

variables['mjj']      = {   'name': 'mjj',            #   variable name    
                            'range' : (25,0,2500),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,
                        }

variables['mjjPU']      = {   'name': 'mjj',            #   variable name    
                            'range' : (15,0,2500),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]PU',  #   x axis name
                            'fold' : 3,
                        }

variables['mjj_H']      = {   'name': 'mjj',            #   variable name    
                            'range' : (20,0,1000),    #   variable range
                            'xaxis' : 'm_{jj}H [GeV]',  #   x axis name
                            'fold' : 3,
                        }

variables['detajj'] = {   'name': 'detajj',            #   variable name    
                            'range' : (80,-1,10),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}',  #   x axis name
                            'fold' : 3,
                        }

variables['detajj_PU'] = {   'name': 'detajj',            #   variable name    
                            'range' : (20,4,10),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}PU',  #   x axis name
                            'fold' : 3,
                        }

variables['detajj_H'] = {   'name': 'detajj',            #   variable name    
                            'range' : (30,2,5),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}H',  #   x axis name
                            'fold' : 3,
                        }


variables['R'] = {   'name': 'R_AN',     
                        'range' : (50,0,1),   
                        'xaxis' : 'R_AN',
                        'fold' : 3,
}

variables['RPU'] = {   'name': 'R_AN',     
                        'range' : (20,0,1),   
                        'xaxis' : 'R_ANPU',
                        'fold' : 3,
}

# variables['Zl1bin1'] = {   'name': 'Zl1',     
#                         'range' : (50,0,5),   
#                         'xaxis' : 'Zl1',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
# }

# variables['Zl1bin2'] = {   'name': 'Zl1',     
#                         'range' : (10,0,5),   
#                         'xaxis' : 'Zl1',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
# }

variables['Zl1bin3'] = {   'name': 'Zl1',     
                        'range' : (60,-3,3),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
}

variables['Zl1bin4'] = {   'name': 'Zl1',     
                        'range' : (20,-3,3),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
}


variables['DNNoutput_noQGLbin1'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.5, 0.7, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
}

variables['DNNoutput_noQGLbin2'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
}

variables['DNNoutput_noQGLbin3'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
}

variables['DNNoutput_noQGLbin4'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : (10,0,1), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
}

variables['mjj_bin1']      = {   'name': 'mjj',            #   variable name    
                            'range' : ([400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2500.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,

                        }

variables['LHEjet_pt1']  = {
                        'name': 'LHEPart_pt[4]',
                        'range' : (70,40,350),
                        'xaxis' : 'p_{T} 1st jet @ LHE',
                        'fold' : 3,
                        }

variables['LHEjet_pt2']  = {
                        'name': 'LHEPart_pt[5]',
                        'range' : (70,40,350),
                        'xaxis' : 'p_{T} 2nd jet @ LHE',
                        'fold' : 3,
                        }

variables['LHEmjj']  = {
                        'name': 'lhe_mjj',
                        'range' : (25,0,2500),    #   variable range
                        'xaxis' : 'm_{jj} [GeV] @LHE',  #   x axis name
                        'fold' : 3,
                        }

variables['LHEpt1']  = {   'name': 'LHEPart_pt[2]',     
                        'range' : (35,0,175),   
                        'xaxis' : 'p_{T} 1st lep @LHE',
                        'fold' : 3,
                        }

variables['LHEeta1']  = {  'name': 'LHEPart_eta[2]',     
                        'range' : (24,-2.4,2.4),   
                        'xaxis' : '#eta 1st lep @LHE',
                        'fold' : 3,
                        }
                        
variables['LHEphi1']  = {  'name': 'LHEPart_phi[2]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 1st lep @LHE',
                        'fold' : 3,
                        }


variables['LHEjet_eta1']  = {
                        'name': 'LHEPart_eta[4]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 1st jet @LHE',
                         'fold' : 3,
                        }

variables['LHEjet_eta2']  = {
                        'name': 'LHEPart_eta[5]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 2nd jet @LHE',
                         'fold' : 3,
                        }

variables['LHEjet_phi1']  = {  'name': 'LHEPart_phi[4]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 1st jet @LHE',
                        'fold' : 3,
                        }

variables['LHEjet_phi2']  = {  'name': 'LHEPart_phi[5]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 2nd jet @LHE',
                        'fold' : 3,
                        }