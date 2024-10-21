

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }


######## lepton 1 ##########

variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (35,0,175),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['pt1bin2']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (20,20,50),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 0,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['pt1bin3']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (6,25,75),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 0,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (24,-2.4,2.4),   
                        'xaxis' : '#eta 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }                         
                        }
variables['eta1binHEM']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (30,-2.,-1.),   
                        'xaxis' : '#eta 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }                         
                        }
                        
variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['puppimet_phi']  = {  'name': 'PuppiMET_phi',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi MET',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['puppimet_phiPU']  = {  'name': 'PuppiMET_phi',
                        'range' : (20,-3.2,3.2),
                        'xaxis' : '#phi METPU',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['mtw1']  = {   'name': 'mtw1',
                        'range' : (20,0,200),
                         'xaxis' : 'm_{T}^{l1+MET} [GeV]',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                       }

variables['mtw1bin2']  = {   'name': 'mtw1',
                        'range' : (100,0,200),
                         'xaxis' : 'm_{T}^{l1+MET} [GeV]',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                       }

variables['mtw1bin1']  = {   'name': 'mtw1',
                        'range' : (50,0,50),
                         'xaxis' : 'm_{T}^{l1+MET} [GeV]',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                       }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (40,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['puppimetbin1']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (60,0,60),
                        'xaxis' : 'puppimet [GeV]',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['met']  = {
                        'name': 'MET_pt',
                        'range' : (40,0,200),
                        'xaxis' : 'MET_pt [GeV]',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['metbin1']  = {
                        'name': 'MET_pt',
                        'range' : (60,0,60),
                        'xaxis' : 'MET_pt [GeV]',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }


variables['Dphilep1met']  = {   'name': 'Dphilep1met',     
                        'range' : (60,-3.14,3.14),   
                        'xaxis' : '#Delta#phi_{L1, MET}',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphilep1metPU']  = {   'name': 'Dphilep1met',     
                        'range' : (30,-3.14,3.14),   
                        'xaxis' : '#Delta#phi_{L1, MET}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['ptW']  = {   'name': 'ptW',     
                        'range' : (30,0,300),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

############# getti ###################
variables['njet_30']  = {
                         'name': 'Sum$(CleanJet_pt>30)',     
                         'range' : (8,0,8),   
                         'xaxis' : 'Number of jets w/ pt>30 GeV',
                         'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                         }


# variables['basew']  = {
#                          'name': 'baseW',     
#                          'range' : (100,-0.2,0.2),   
#                          'xaxis' : 'baseW',
#                          'fold' : 3,
#                          'blind': {
#                            'ele_SR' : 'full', 
                          #  'ele_SR_highDNN' : 'full',
#                            'mu_SR' : 'full', 
                          #  'mu_SR_highDNN' : 'full'
#                           }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                          }


# variables['njet_40']  = {
#                          'name': 'Sum$(CleanJet_pt>40)',     
#                          'range' : (8,0,8),   
#                          'xaxis' : 'Number of jets w/ pt>40 GeV',
#                          'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full', 
                          #  'ele_SR_highDNN' : 'full',
#                            'mu_SR' : 'full', 
                          #  'mu_SR_highDNN' : 'full'
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                          }

# variables['njet_80']  = {
#                          'name': 'Sum$(CleanJet_pt>80)',     
#                          'range' : (8,0,8),   
#                          'xaxis' : 'Number of jets w/ pt>80 GeV',
#                          'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full', 
                          #  'ele_SR_highDNN' : 'full',
#                            'mu_SR' : 'full', 
                          #  'mu_SR_highDNN' : 'full'
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                          }

variables['jetpt1']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (70,40,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

# variables['CleanJetNS_pt1']  = {
#                         'name': 'CleanJetNS_pt1',
#                         'range' : (70,40,350),
#                         'xaxis' : 'p_{T} 1st jet',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full', 
                          #  'ele_SR_highDNN' : 'full',
#                            'mu_SR' : 'full', 
                          #  'mu_SR_highDNN' : 'full'
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }


variables['jetpt1_PU']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (25,40,150),
                        'xaxis' : 'p_{T}PU 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt2']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (50,30,250),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

# variables['CleanJetNS_pt2']  = {
#                         'name': 'CleanJetNS_pt2',
#                         'range' : (50,30,250),
#                         'xaxis' : 'p_{T} 2nd jet',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full', 
                          #  'ele_SR_highDNN' : 'full',
#                            'mu_SR' : 'full', 
                          #  'mu_SR_highDNN' : 'full'
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }

variables['jetpt2_PU']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (10,30,60),
                        'xaxis' : 'p_{T}PU 2nd jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jeteta1']  = {
                        'name': 'CleanJet_eta[0]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 1st jet',
                         'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['jeteta2']  = {
                        'name': 'CleanJet_eta[1]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 2nd jet',
                         'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['jetphi1']  = {
                        'name': 'CleanJet_phi[0]',
                         'range' : (40,-3.2,3.2),
                         'xaxis' : '#phi 1st jet',
                         'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['jetphi2']  = {
                        'name': 'CleanJet_phi[1]',
                         'range' : (40,-3.2,3.2),
                         'xaxis' : '#phi 2nd jet',
                         'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['mjj']      = {   'name': 'mjj',            #   variable name    
                            'range' : (25,0,2500),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['mjjPU']      = {   'name': 'mjj',            #   variable name    
                            'range' : (15,0,2500),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]PU',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['mjj_H']      = {   'name': 'mjj',            #   variable name    
                            'range' : (20,0,1000),    #   variable range
                            'xaxis' : 'm_{jj}H [GeV]',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['detajj'] = {   'name': 'detajj',            #   variable name    
                            'range' : (80,-1,10),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['detajj_PU'] = {   'name': 'detajj',            #   variable name    
                            'range' : (20,4,10),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}PU',  #   x axis name
                            'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['detajj_H'] = {   'name': 'detajj',            #   variable name    
                            'range' : (30,2,5),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}H',  #   x axis name
                            'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphijet1met']  = {   'name': 'Dphijet1met',     
                        'range' : (60,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{J1, MET}',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphijet1metPU']  = {   'name': 'Dphijet1met',     
                        'range' : (30,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{J1, MET}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphijet2met']  = {   'name': 'Dphijet2met',     
                        'range' : (60,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{J2, MET}',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphijet2metPU']  = {   'name': 'Dphijet2met',     
                        'range' : (30,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{J2, MET}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphijet1jet2']  = {   'name': 'Dphijet1jet2',     
                        'range' : (60,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{J1, J2}',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphijet1jet2PU']  = {   'name': 'Dphijet1jet2',     
                        'range' : (30,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{J1, J2}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphilep1jet1']  = {   'name': 'Dphilep1jet1',     
                        'range' : (60,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{L1, J1}',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphilep1jet1PU']  = {   'name': 'Dphilep1jet1',     
                        'range' : (30,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{L1, J1}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphilep1jet2']  = {   'name': 'Dphilep1jet2',     
                        'range' : (60,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{L1, J2}',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['Dphilep1jet2PU']  = {   'name': 'Dphilep1jet2',     
                        'range' : (30,-3.14,3.14),   
                        'xaxis' : '#Delta#phi{L1, J2}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
                        }

variables['R'] = {   'name': 'R_AN',     
                        'range' : (50,0,1),   
                        'xaxis' : 'R_AN',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
}

variables['RPU'] = {   'name': 'R_AN',     
                        'range' : (20,0,1),   
                        'xaxis' : 'R_ANPU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
}

variables['Zl1bin3'] = {   'name': 'Zl1',     
                        'range' : (60,-3,3),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
}

variables['Zl1bin4'] = {   'name': 'Zl1',     
                        'range' : (20,-3,3),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
}

variables['DNNoutput_ALLbin1'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
}

variables['DNNoutput_ALLbin2'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
}

variables['DNNoutput_ALLbin3'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
}

variables['DNNoutput_ALLbin4'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : (10,0,1), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                           'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                         }
}


variables['mjj_bin1']      = {   'name': 'mjj',            #   variable name    
                            'range' : ([400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2500.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['leppt_eta'] = {   'name': 'Lepton_pt[0]:Lepton_eta[0]',            #   variable name    
                            'range' : ([-2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.],[25., 30., 35., 40., 45., 60., 75.,],),    #   variable range
                            'xaxis' : 'Lepton_pt : Lepton_eta [GeV]',  #   x axis name
                            'fold' :0 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

#### leptons (l, nu, l+nu)

variables['DNN1ptW'] = {   'name': 'DNNoutputSR_noQGL:ptW',            #   variable name    
                            'range' : (30,0.,500.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : ptW [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['DNN1leppt'] = {   'name': 'DNNoutputSR_noQGL:Lepton_pt[0]',            #   variable name    
                            'range' : (35,0,200,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }   

variables['DNN1lepeta'] = {   'name': 'DNNoutputSR_noQGL:Lepton_eta[0]',            #   variable name    
                            'range' : (20,-2.,2.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta lepton',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }    


# ######## jets

variables['DNN1jet1pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[0]',            #   variable name    
                            'range' : (35,40.,350.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['DNN1jet1eta'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_eta[0]',            #   variable name    
                            'range' : (40,-5.0,5.0,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta 1st jet',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['DNN1jet2pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[1]',            #   variable name    
                            'range' : (25,30.,250.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['DNN1jet2eta'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_eta[1]',            #   variable name    
                            'range' : (40,-5.0,5.0,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta 2nd jet',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['DNN1mjj'] = {   'name': 'DNNoutputSR_noQGL:mjj',            #   variable name    
                            'range' : (27,300.,3000.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['DNN1detajj'] = {   'name': 'DNNoutputSR_noQGL:detajj',            #   variable name    
                            'range' : (26,3.5,10.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }

variables['DNN1nJet'] = {   'name': 'DNNoutputSR_noQGL:nCleanJet',            #   variable name    
                            'range' : ([1.5, 2.5, 3.5, 4.5, 5.5, 10.5],[0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 0.7, 0.8, 0.9, 1.],),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                           'ele_SR_highDNN' : 'full',
                              'mu_SR' : 'full', 
                           'mu_SR_highDNN' : 'full'
                            }
                        }