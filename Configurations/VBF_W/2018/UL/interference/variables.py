

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
}

variables['high0p5events'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (1,0.5,1.),    #   variable range
                            'xaxis' : 'events',  #   x axis name
                            'fold' :2 ,
                        }

# variables['DNNJoinedDphijet1jet2PU'] = {   'name': 'Dphijet1jet2',            #   variable name    
#                             'range' : (5,0.,3.14),    #   variable range
#                             'xaxis' : 'Dphijet1jet2',  #   x axis name
#                             'fold' :3 ,
#                         }
# variables['DNNJoinedDphijet1jet2PU2'] = {   'name': 'Dphijet1jet2',            #   variable name    
#                             'range' : (10,0.,3.14),    #   variable range
#                             'xaxis' : 'Dphijet1jet2',  #   x axis name
#                             'fold' :3 ,
#                         }
# variables['DNNJoinedDphijet1jet2PU3'] = {   'name': 'Dphijet1jet2',            #   variable name    
#                             'range' : (20,0.,3.14),    #   variable range
#                             'xaxis' : 'Dphijet1jet2',  #   x axis name
#                             'fold' :3 ,
#                         }

###### 1D
variables['DNNJoined2'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (20,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput',  #   x axis name
                            'fold' :3 ,
                            # 'blind': {
                            #   'ele_SR' : 'significance=5', 
                            #   'mu_SR' : 'significance=5', 
                            # }
                        }
variables['DNNJoined'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput',  #   x axis name
                            'fold' :3 ,
                            # 'blind': {
                            #   'ele_SR' : 'significance=5', 
                            #   'mu_SR' : 'significance=5', 
                            # }
                        }


variables['ptW']  = {   'name': 'ptW',     
                        'range' : (30,0,300),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=5', 
                           'mu_SR' : 'significance=5', 
                         }
                        }


# variables['jetpt1PU']  = {
#                         'name': 'CleanJet_pt[0]',
#                         'range' : (10,40,350),
#                         'xaxis' : 'p_{T} 1st jet',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=5', 
#                            'mu_SR' : 'significance=5', 
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }

# variables['Dphijet1jet2']  = {
#                         'name': 'Dphijet1jet2',
#                         'range' : (100,0,3.14),
#                         'xaxis' : 'Dphijet1jet2',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=5', 
#                            'mu_SR' : 'significance=5', 
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }

# variables['Dphilep1met']  = {
#                         'name': 'Dphilep1met',
#                         'range' : (100,0,3.14),
#                         'xaxis' : 'Dphilep1met',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=5', 
#                            'mu_SR' : 'significance=5', 
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }

###### 2D

# variables['DNNJoinedDphijet1jet2PU2'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
#                             'range' : ([0, 0.2, 0.4, 0.6, 0.8, 1.],[0, 2., 2.3, 2.6, 2.9, 3.14]),     #   variable range
#                             'xaxis' : 'DNNoutput : Dphijet1jet2 [GeV]',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=5', 
#                               'mu_SR' : 'significance=5', 
#                             }
#                         }
# # variables['DNNJoinedDphijet1jet2PU2_cut3'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
# #                             'range' : ([0.4, 0.6, 0.8, 1.],[0, 2., 2.3, 2.6, 2.9, 3.14]),     #   variable range
# #                             'xaxis' : 'DNNoutput : Dphijet1jet2 [GeV]',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

# variables['DNNJoinedDphijet1jet2PU3'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
#                             'range' : ([0, 0.33, 0.66, 1.],[0, 2., 2.3, 2.6, 2.9, 3.14]),    #   variable range
#                             'xaxis' : 'DNNoutput : Dphijet1jet2 [GeV]',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=5', 
#                               'mu_SR' : 'significance=5', 
#                             }
#                         }

# variables['DNNJoinedDphilep1metPU'] = {   'name': 'Dphilep1met:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,5,0.,3.14),    #   variable range
#                             'xaxis' : 'DNNoutput : Dphilep1met [GeV]',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=5', 
#                               'mu_SR' : 'significance=5', 
#                             }
#                         }


# ######### 3D
# variables['DNNJoined_Dphijj_DphilepMET2'] = {
#     'name': 'Dphilep1met:Dphijet1jet2:DNNJoined',  # Z : Y : X
#     'range': (3, 0., 1.0,        # X axis: DNN output
#               3, 0., 3.14,       # Y axis: dphijj
#               3, 0., 3.14),      # Z axis: dphil1met
#     'xaxis': 'DNN : Dphi(j1,j2) : Dphi(lep,MET)',  # 
#     'fold': 3,
#     'blind': {
#         'ele_SR': 'significance=5',
#         'mu_SR' : 'significance=5',
#     }
# }

# variables['DNNJoined_Dphijj_DphilepMET3'] = {
#     'name': 'Dphilep1met:Dphijet1jet2:DNNJoined',  # Z : Y : X
#     'range' : ([0, 0.3, 0.6, 1.],[0, 2., 2.5, 3.14],[0, 1., 2., 3.14]),    #   variable range
#     'xaxis': 'DNN : Dphi(j1,j2) : Dphi(lep,MET)',  # 
#     'fold': 3,
#     'blind': {
#         'ele_SR': 'significance=5',
#         'mu_SR' : 'significance=5',
#     }
# }



# variables['DNNJoined_Dphijj_jet1pt1'] = {
#     'name': 'CleanJet_pt[0]:Dphijet1jet2:DNNJoined',  # Z : Y : X
#     'range' : ([0, 0.3, 0.6, 1.],[0, 2., 2.5, 3.14],[0, 120., 170., 1000.]),    #   variable range
#     'xaxis': 'DNN : Dphi(j1,j2) : jet1pt',  # 
#     'fold': 3,
#     'blind': {
#         'ele_SR': 'significance=5',
#         'mu_SR' : 'significance=5',
#     }
# }

# variables['DNNJoined_Dphijj_jet1pt2'] = {
#     'name': 'CleanJet_pt[0]:Dphijet1jet2:DNNJoined',  # Z : Y : X
#     'range' : ([0, 0.33, 0.66, 1.],[0, 1., 2., 3.14],[0, 120., 170., 1000.]),    #   variable range
#     'xaxis': 'DNN : Dphi(j1,j2) : jet1pt',  # 
#     'fold': 3,
#     'blind': {
#         'ele_SR': 'significance=5',
#         'mu_SR' : 'significance=5',
#     }
# }

# variables['DNNJoined_Dphilep1met_jet1pt1'] = {
#     'name': 'CleanJet_pt[0]:Dphilep1met:DNNJoined',  # Z : Y : X
#     'range' : ([0, 0.33, 0.66, 1.],[0, 1., 2., 3.14],[0, 120., 170., 1000.]),    #   variable range
#     'xaxis': 'DNN : Dphi(l1,MET) : jet1pt',  # 
#     'fold': 3,
#     'blind': {
#         'ele_SR': 'significance=5',
#         'mu_SR' : 'significance=5',
#     }
# }
# variables['DNNJoined_Dphilep1met_jet1pt2'] = {
#     'name': 'CleanJet_pt[0]:Dphilep1met:DNNJoined',  # Z : Y : X
#     'range' : ([0, 0.5, 0.8, 1.],[0, 1., 2., 3.14],[0, 120., 170., 1000.]),    #   variable range
#     'xaxis': 'DNN : Dphi(l1,MET) : jet1pt',  # 
#     'fold': 3,
#     'blind': {
#         'ele_SR': 'significance=5',
#         'mu_SR' : 'significance=5',
#     }
# }

variables['jetpt1PU2']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (30,40,250),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        }

variables['jetpt2']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (60,30,300),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 3,
                        }

variables['jetpt2PU']  = {
                        'name': 'CleanJet_pt[1]',
                        'range' : (30,0,200),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 3,
                        }


variables['detajj'] = {   'name': 'detajj',            #   variable name    
                            'range' : (20,2,8.),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                        }
                        
# # variables['detajjtop'] = {   'name': 'detajj',            #   variable name    
# #                             'range' : (40,2,6.),    #   variable range
# #                             'xaxis' : '#Delta#eta_{jj}',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

# # variables['detajjH'] = {   'name': 'detajj',            #   variable name    
# #                             'range' : (20,2.,4.),    #   variable range
# #                             'xaxis' : '#Delta#eta_{jj}',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

# # variables['detajjPU'] = {   'name': 'detajj',            #   variable name    
# #                             'range' : (20,4.,10.),    #   variable range
# #                             'xaxis' : '#Delta#eta_{jj}',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

# # variables['detajjPU2'] = {   'name': 'detajj',            #   variable name    
# #                             'range' : (10,4.,10.),    #   variable range
# #                             'xaxis' : '#Delta#eta_{jj}',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

# # variables['mjj'] = {   'name': 'mjj',            #   variable name    
# #                             'range' : (40,300.,700.),    #   variable range
# #                             'xaxis' : 'm_{jj} [GeV]',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

variables['mjj1'] = {   'name': 'mjj',            #   variable name    
                            'range' : (36,400.,4000.),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                        }

variables['mjj2'] = {   'name': 'mjj',            #   variable name    
                            'range' : (36,400.,3000.),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                        }

# # variables['mjj2'] = {   'name': 'mjj',            #   variable name    
# #                             'range' : (17,300.,2000.),    #   variable range
# #                             'xaxis' : 'm_{jj} [GeV]',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

# variables['R'] = {   'name': 'R_AN',     
#                         'range' : (50,0,1),   
#                         'xaxis' : 'R',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=5', 
#                            'mu_SR' : 'significance=5', 
#                          }
# }

# # variables['RPU'] = {   'name': 'R_AN',     
# #                         'range' : (20,0,1),   
# #                         'xaxis' : 'R',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'mu_SR' : 'significance=5', 
# #                          }
# # }

variables['Rcut'] = {   'name': 'R_AN',     
                        'range' : (50,0,0.5),   
                        'xaxis' : 'R',
                        'fold' : 3,
}

# # variables['RPUcut'] = {   'name': 'R_AN',     
# #                         'range' : (20,0,0.5),   
# #                         'xaxis' : 'R',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'mu_SR' : 'significance=5', 
# #                          }
# # }


variables['leppt'] = {   'name': 'Lepton_pt[0]',            #   variable name    
                            'range' : (35,0,200),    #   variable range
                            'xaxis' : 'p_{T} lepton [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'significance=5', 
                              'mu_SR' : 'significance=5', 
                            }
                        }   

# # variables['leppt2'] = {   'name': 'Lepton_pt[0]',            #   variable name    
# #                             'range' : (35,0,100),    #   variable range
# #                             'xaxis' : 'p_{T} lepton [GeV]',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }   


variables['Zl1'] = {   'name': 'Zl1',     
                        'range' : (50,-5,5),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
}

variables['Zl3'] = {   'name': 'Zl1',     
                        'range' : (20,-5,5),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
}


# # variables['lepeta']  = {  'name': 'Lepton_eta[0]',     
# #                         'range' : (24,-2.4,2.4),   
# #                         'xaxis' : '#eta 1st lep',
# #                         'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

variables['jeteta1']  = {
                        'name': 'CleanJet_eta[0]',
                        'range' : (40,-5.0,5.0),
                        'xaxis' : '#eta 1st jet',
                        'fold' :3 ,
                        }

# # variables['jeteta2']  = {
# #                         'name': 'CleanJet_eta[1]',
# #                         'range' : (40,-5.0,5.0),
# #                         'xaxis' : '#eta 2nd jet',
# #                         'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'mu_SR' : 'significance=5', 
# #                             }
# #                         }

# #this
# # variables['Dphilep1met']  = {   'name': 'Dphilep1met',     
# #                         'range' : (15, 0.,3.14),   
# #                         'xaxis' : '#Delta#phi{l1, met}',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# #                         }

# # variables['Dphilep1jet1']  = {   'name': 'Dphilep1jet1',     
# #                         'range' : (60,-3.14,3.14),   
# #                         'xaxis' : '#Delta#phi{L1, J1}',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# #                         }

# # variables['Dphilep1jet1PU']  = {   'name': 'Dphilep1jet1',     
# #                         'range' : (30,-3.14,3.14),   
# #                         'xaxis' : '#Delta#phi{L1, J1}PU',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# #                         }

# # variables['Dphilep1jet2']  = {   'name': 'Dphilep1jet2',     
# #                         'range' : (60,-3.14,3.14),   
# #                         'xaxis' : '#Delta#phi{L1, J2}',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# #                         }

# # variables['Dphilep1jet2PU']  = {   'name': 'Dphilep1jet2',     
# #                         'range' : (30,-3.14,3.14),   
# #                         'xaxis' : '#Delta#phi{L1, J2}PU',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# #                         }

# ## this 


# # variables['DNNoutput_ALLbin1'] = {   'name': 'DNNoutputSR_noQGL',     
# #                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 1.],), 
# #                         'xaxis' : 'DNNoutput',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# # }

# # variables['DNNoutput_ALLbin2'] = {   'name': 'DNNoutputSR_noQGL',     
# #                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 1.],), 
# #                         'xaxis' : 'DNNoutput',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# # }

# # variables['DNNoutput_ALLbin3'] = {   'name': 'DNNoutputSR_noQGL',     
# #                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 1.],), 
# #                         'xaxis' : 'DNNoutput',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# # }

# # variables['DNNoutput_ALLbin4'] = {   'name': 'DNNoutputSR_noQGL',     
# #                         'range' : (10,0,1), 
# #                         'xaxis' : 'DNNoutput',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                            'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                          }
# # }


# # variables['mjj_bin1']      = {   'name': 'mjj',            #   variable name    
# #                             'range' : ([400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2500.],),    #   variable range
# #                             'xaxis' : 'm_{jj} [GeV]',  #   x axis name
# #                             'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }

# # variables['leppt_eta'] = {   'name': 'Lepton_pt[0]:Lepton_eta[0]',            #   variable name    
# #                             'range' : ([-2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.],[25., 30., 35., 40., 45., 60., 75.,],),    #   variable range
# #                             'xaxis' : 'Lepton_pt : Lepton_eta [GeV]',  #   x axis name
# #                             'fold' :0 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }

# # #### leptons (l, nu, l+nu)

# # variables['DNN1ptW'] = {   'name': 'DNNoutputSR_noQGL:ptW',            #   variable name    
# #                             'range' : (30,0.,500.,10,0.,1.),    #   variable range
# #                             'xaxis' : 'DNNoutput : ptW [GeV]',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                               'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                               'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }

# # variables['DNN1leppt'] = {   'name': 'DNNoutputSR_noQGL:Lepton_pt[0]',            #   variable name    
# #                             'range' : (35,0,200,10,0.,1.),    #   variable range
# #                             'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }   

# # variables['DNN1lepeta'] = {   'name': 'DNNoutputSR_noQGL:Lepton_eta[0]',            #   variable name    
# #                             'range' : (20,-2.,2.,10,0.,1.),    #   variable range
# #                             'xaxis' : 'DNNoutput : #eta lepton',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }    


# # # ######## jets

# # variables['DNN1jet1pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[0]',            #   variable name    
# #                             'range' : (35,40.,350.,10,0.,1.),    #   variable range
# #                             'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }

# # variables['DNN1jet1eta'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_eta[0]',            #   variable name    
# #                             'range' : (40,-5.0,5.0,10,0.,1.),    #   variable range
# #                             'xaxis' : 'DNNoutput : #eta 1st jet',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }

# # variables['DNN1jet2pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[1]',            #   variable name    
# #                             'range' : (25,30.,250.,10,0.,1.),    #   variable range
# #                             'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }

# # variables['DNN1jet2eta'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_eta[1]',            #   variable name    
# #                             'range' : (40,-5.0,5.0,10,0.,1.),    #   variable range
# #                             'xaxis' : 'DNNoutput : #eta 2nd jet',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }

# # thiss2


# # variables['DNN1nJet'] = {   'name': 'DNNoutputSR_noQGL:nCleanJet',            #   variable name    
# #                             'range' : ([1.5, 2.5, 3.5, 4.5, 5.5, 10.5],[0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 0.7, 0.8, 0.9, 1.],),    #   variable range
# #                             'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
# #                             'fold' :3 ,
# #                             'blind': {
# #                               'ele_SR' : 'significance=5', 
# #                            'ele_SR_highDNN' : 'significance=5',
# #                               'mu_SR' : 'significance=5', 
# #                            'mu_SR_highDNN' : 'significance=5'
# #                             }
# #                         }