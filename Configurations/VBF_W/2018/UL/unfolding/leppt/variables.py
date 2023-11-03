

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
                        }


######## lepton 1 ##########

variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (35,0,175),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }



variables['pt1Zb2']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (20,20,50),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 0,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }


variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (24,-2.4,2.4),   
                        'xaxis' : '#eta 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }                         
                        }
                        
variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['puppimet_phi']  = {  'name': 'PuppiMET_phi',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi MET',
                        'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['puppimet_phiPU']  = {  'name': 'PuppiMET_phi',
                        'range' : (20,-3.2,3.2),
                        'xaxis' : '#phi METPU',
                        'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['mtw1']  = {   'name': 'mtw1',
                        'range' : (20,0,200),
                         'xaxis' : 'm_{T}^{l1+MET} [GeV]',
                        'fold' : 3,
                        'blind': {
                          'ele_SR1' : 'full',
                          'ele_SR2' : 'full',
                          'ele_SR3' : 'full',
                          'ele_SR4' : 'full',
                          'ele_SR5' : 'full',
                          'mu_SR1' : 'full',
                          'mu_SR2' : 'full',
                          'mu_SR3' : 'full',
                          'mu_SR4' : 'full',
                          'mu_SR5' : 'full',
                         }
                       }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (40,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }



variables['ptW']  = {   'name': 'ptW',     
                        'range' : (30,0,300),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
                        }

############# getti ###################
variables['njet_30']  = {
                         'name': 'Sum$(CleanJet_pt>30)',     
                         'range' : (8,0,8),   
                         'xaxis' : 'Number of jets w/ pt>30 GeV',
                         'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                         }


variables['jetpt1']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (70,40,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['jetpt1_PU']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (25,40,150),
                        'xaxis' : 'p_{T}PU 1st jet',
                        'fold' : 3,
                        'blind': {
                          'ele_SR1' : 'full',
                          'ele_SR2' : 'full',
                          'ele_SR3' : 'full',
                          'ele_SR4' : 'full',
                          'ele_SR5' : 'full',
                          'mu_SR1' : 'full',
                          'mu_SR2' : 'full',
                          'mu_SR3' : 'full',
                          'mu_SR4' : 'full',
                          'mu_SR5' : 'full',
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt2']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (50,30,250),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 3,
                        'blind': {
                          'ele_SR1' : 'full',
                          'ele_SR2' : 'full',
                          'ele_SR3' : 'full',
                          'ele_SR4' : 'full',
                          'ele_SR5' : 'full',
                          'mu_SR1' : 'full',
                          'mu_SR2' : 'full',
                          'mu_SR3' : 'full',
                          'mu_SR4' : 'full',
                          'mu_SR5' : 'full',
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt2_PU']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (10,30,60),
                        'xaxis' : 'p_{T}PU 2nd jet',
                        'fold' : 3,
                        'blind': {
                          'ele_SR1' : 'full',
                          'ele_SR2' : 'full',
                          'ele_SR3' : 'full',
                          'ele_SR4' : 'full',
                          'ele_SR5' : 'full',
                          'mu_SR1' : 'full',
                          'mu_SR2' : 'full',
                          'mu_SR3' : 'full',
                          'mu_SR4' : 'full',
                          'mu_SR5' : 'full',
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jeteta1']  = {
                        'name': 'CleanJet_eta[0]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 1st jet',
                         'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['jeteta2']  = {
                        'name': 'CleanJet_eta[1]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 2nd jet',
                         'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['mjj']      = {   'name': 'mjj',            #   variable name    
                            'range' : (25,500,2500),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['mjjPU']      = {   'name': 'mjj',            #   variable name    
                            'range' : (15,400,2500),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]PU',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['mjj_H']      = {   'name': 'mjj',            #   variable name    
                            'range' : (20,400,1000),    #   variable range
                            'xaxis' : 'm_{jj}H [GeV]',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['detajj'] = {   'name': 'detajj',            #   variable name    
                            'range' : (80,-1,10),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }

variables['detajj_PU'] = {   'name': 'detajj',            #   variable name    
                            'range' : (20,4,10),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}PU',  #   x axis name
                            'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
                        }

variables['detajj_H'] = {   'name': 'detajj',            #   variable name    
                            'range' : (30,2,5),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}H',  #   x axis name
                            'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
                        }


variables['R'] = {   'name': 'R_AN',     
                        'range' : (50,0,1),   
                        'xaxis' : 'R_AN',
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
}

variables['RPU'] = {   'name': 'R_AN',     
                        'range' : (20,0,1),   
                        'xaxis' : 'R_ANPU',
                        'fold' : 3,
                        'blind': {
                          'ele_SR1' : 'full',
                          'ele_SR2' : 'full',
                          'ele_SR3' : 'full',
                          'ele_SR4' : 'full',
                          'ele_SR5' : 'full',
                          'mu_SR1' : 'full',
                          'mu_SR2' : 'full',
                          'mu_SR3' : 'full',
                          'mu_SR4' : 'full',
                          'mu_SR5' : 'full',
                         }
}


variables['Zl1bin3'] = {   'name': 'Zl1',     
                        'range' : (60,-3,3),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
}

variables['Zl1bin4'] = {   'name': 'Zl1',     
                        'range' : (20,-3,3),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
}

variables['DNNoutput_ALLbin1'] = {   'name': 'DNNoutputSR_ALL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                          'ele_SR1' : 'full',
                          'ele_SR2' : 'full',
                          'ele_SR3' : 'full',
                          'ele_SR4' : 'full',
                          'ele_SR5' : 'full',
                          'mu_SR1' : 'full',
                          'mu_SR2' : 'full',
                          'mu_SR3' : 'full',
                          'mu_SR4' : 'full',
                          'mu_SR5' : 'full',
                         }
}

variables['DNNoutput_ALLbin2'] = {   'name': 'DNNoutputSR_ALL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
}

variables['DNNoutput_ALLbin3'] = {   'name': 'DNNoutputSR_ALL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
}

variables['DNNoutput_ALLbin4'] = {   'name': 'DNNoutputSR_ALL',     
                        'range' : (10,0,1), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                            'ele_SR1' : 'full',
                            'ele_SR2' : 'full',
                            'ele_SR3' : 'full',
                            'ele_SR4' : 'full',
                            'ele_SR5' : 'full',
                            'mu_SR1' : 'full',
                            'mu_SR2' : 'full',
                            'mu_SR3' : 'full',
                            'mu_SR4' : 'full',
                            'mu_SR5' : 'full',
                         }
}


variables['mjj_bin1']      = {   'name': 'mjj',            #   variable name    
                            'range' : ([400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2500.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR1' : 'full',
                              'ele_SR2' : 'full',
                              'ele_SR3' : 'full',
                              'ele_SR4' : 'full',
                              'ele_SR5' : 'full',
                              'mu_SR1' : 'full',
                              'mu_SR2' : 'full',
                              'mu_SR3' : 'full',
                              'mu_SR4' : 'full',
                              'mu_SR5' : 'full',
                            }
                        }


variables['DNN1leppt'] = {   'name': 'mjj:detajj',            #   variable name    
                            'range' : ([0., 0.10, 0.20, 0.30, 0.40, 1.],[35., 50., 75., 100., 200.,1000.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV] : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            # do weighted plot too
                            'doWeight' : 1,
                            'binX'     : 6,
                            'binY'     : 4
                        }
