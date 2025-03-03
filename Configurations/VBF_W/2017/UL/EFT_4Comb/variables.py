

# ##############################################
# # now variables to plot
# # Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }
}



variables['Dphijet1jet2PU']  = {   'name': 'Dphijet1jet2',     
                        'range' : (15, 0.,3.14),   
                        'xaxis' : '#Delta#phi{J1, J2}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }
                        }

variables['Dphilep1metPU']  = {   'name': 'Dphilep1met',     
                        'range' : (15, 0.,3.14),   
                        'xaxis' : '#Delta#phi{l1, MET}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }
                        }


variables['DNNJoinedDphijet1jet2PU'] = {   'name': 'DNNJoined:Dphijet1jet2',            #   variable name    
                            'range' : (5,0.,3.14,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#phi j_{1}j_{2} [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'significance=0.1', 
                              'mu_SR' : 'significance=0.1', 
                            }
                        }

variables['DNNJoinedDphijet1jet2PU2'] = {   'name': 'DNNJoined:Dphijet1jet2',            #   variable name    
                            'range' : ([0, 2.3, 2.65, 2.85, 3.0, 3.14],[0., 0.2, 0.4, 0.6, 0.8, 1.],),    #   variable range
                            'xaxis' : 'DNNoutput : Dphijet1jet2 [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'significance=0.1', 
                              'mu_SR' : 'significance=0.1', 
                            }
                        }

variables['DNNJoinedDphijet1jet2PU3'] = {   'name': 'DNNJoined:Dphijet1jet2',            #   variable name    
                            'range' : ([0, 1.9, 2.29, 2.5, 2.65, 2.75, 2.85, 2.95, 3.0, 3.07, 3.14],[0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.],),    #   variable range
                            'xaxis' : 'DNNoutput : Dphijet1jet2 [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'significance=0.1', 
                              'mu_SR' : 'significance=0.1', 
                            }
                        }


# # ######## lepton 1 ##########


variables['puppimet_phi']  = {  'name': 'PuppiMET_phi',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi MET',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'significance=0.1', 
                              'mu_SR' : 'significance=0.1',
                            }
                        }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (40,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'significance=0.1', 
                              'mu_SR' : 'significance=0.1', 
                            }
                        }


variables['ptW']  = {   'name': 'ptW',     
                        'range' : (30,0,300),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }
                        }


variables['jetpt1']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (70,40,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt1PU']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (20,40,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['detajj'] = {   'name': 'detajj',            #   variable name    
                            'range' : (40,2,10.),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'significance=0.1', 
                              'mu_SR' : 'significance=0.1', 
                            }
                        }

variables['mjj'] = {   'name': 'mjj',            #   variable name    
                            'range' : (27,300.,3000.),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'significance=0.1', 
                              'mu_SR' : 'significance=0.1', 
                            }
                        }

variables['R'] = {   'name': 'R_AN',     
                        'range' : (50,0,1),   
                        'xaxis' : 'R_AN',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }
}

variables['RPU'] = {   'name': 'R_AN',     
                        'range' : (20,0,1),   
                        'xaxis' : 'R_ANPU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }
}


variables['leppt'] = {   'name': 'Lepton_pt[0]',            #   variable name    
                            'range' : (35,0,200),    #   variable range
                            'xaxis' : 'p_{T} lepton [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'significance=0.1', 
                              'mu_SR' : 'significance=0.1', 
                            }
                        }   


variables['Zl1bin3'] = {   'name': 'Zl1',     
                        'range' : (60,-3,3),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'significance=0.1', 
                           'mu_SR' : 'significance=0.1', 
                         }
}

# variables['Zl1bin4'] = {   'name': 'Zl1',     
#                         'range' : (20,-3,3),   
#                         'xaxis' : 'Zl1',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'mu_SR' : 'significance=0.1', 
#                          }
# }


# variables['leppt_eta'] = {   'name': 'Lepton_eta[0]',            #   variable name    
#                             'range' : ([-2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.],),    #   variable range
#                             'xaxis' : 'Lepton_eta [GeV]',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                               'mu_SR' : 'significance=0.1', 
#                             }
#                         }

#this
# variables['Dphilep1met']  = {   'name': 'Dphilep1met',     
#                         'range' : (15, 0.,3.14),   
#                         'xaxis' : '#Delta#phi{l1, met}',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
#                         }

# variables['Dphilep1jet1']  = {   'name': 'Dphilep1jet1',     
#                         'range' : (60,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{L1, J1}',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
#                         }

# variables['Dphilep1jet1PU']  = {   'name': 'Dphilep1jet1',     
#                         'range' : (30,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{L1, J1}PU',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
#                         }

# variables['Dphilep1jet2']  = {   'name': 'Dphilep1jet2',     
#                         'range' : (60,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{L1, J2}',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
#                         }

# variables['Dphilep1jet2PU']  = {   'name': 'Dphilep1jet2',     
#                         'range' : (30,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{L1, J2}PU',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
#                         }

## this 


# variables['DNNoutput_ALLbin1'] = {   'name': 'DNNoutputSR_noQGL',     
#                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 1.],), 
#                         'xaxis' : 'DNNoutput',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
# }

# variables['DNNoutput_ALLbin2'] = {   'name': 'DNNoutputSR_noQGL',     
#                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 1.],), 
#                         'xaxis' : 'DNNoutput',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
# }

# variables['DNNoutput_ALLbin3'] = {   'name': 'DNNoutputSR_noQGL',     
#                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 1.],), 
#                         'xaxis' : 'DNNoutput',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
# }

# variables['DNNoutput_ALLbin4'] = {   'name': 'DNNoutputSR_noQGL',     
#                         'range' : (10,0,1), 
#                         'xaxis' : 'DNNoutput',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                            'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                          }
# }


# variables['mjj_bin1']      = {   'name': 'mjj',            #   variable name    
#                             'range' : ([400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2500.],),    #   variable range
#                             'xaxis' : 'm_{jj} [GeV]',  #   x axis name
#                             'fold' : 3,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }

# variables['leppt_eta'] = {   'name': 'Lepton_pt[0]:Lepton_eta[0]',            #   variable name    
#                             'range' : ([-2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.],[25., 30., 35., 40., 45., 60., 75.,],),    #   variable range
#                             'xaxis' : 'Lepton_pt : Lepton_eta [GeV]',  #   x axis name
#                             'fold' :0 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }

# #### leptons (l, nu, l+nu)

# variables['DNN1ptW'] = {   'name': 'DNNoutputSR_noQGL:ptW',            #   variable name    
#                             'range' : (30,0.,500.,10,0.,1.),    #   variable range
#                             'xaxis' : 'DNNoutput : ptW [GeV]',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                               'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                               'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }

# variables['DNN1leppt'] = {   'name': 'DNNoutputSR_noQGL:Lepton_pt[0]',            #   variable name    
#                             'range' : (35,0,200,10,0.,1.),    #   variable range
#                             'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }   

# variables['DNN1lepeta'] = {   'name': 'DNNoutputSR_noQGL:Lepton_eta[0]',            #   variable name    
#                             'range' : (20,-2.,2.,10,0.,1.),    #   variable range
#                             'xaxis' : 'DNNoutput : #eta lepton',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }    


# # ######## jets

# variables['DNN1jet1pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[0]',            #   variable name    
#                             'range' : (35,40.,350.,10,0.,1.),    #   variable range
#                             'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }

# variables['DNN1jet1eta'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_eta[0]',            #   variable name    
#                             'range' : (40,-5.0,5.0,10,0.,1.),    #   variable range
#                             'xaxis' : 'DNNoutput : #eta 1st jet',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }

# variables['DNN1jet2pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[1]',            #   variable name    
#                             'range' : (25,30.,250.,10,0.,1.),    #   variable range
#                             'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }

# variables['DNN1jet2eta'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_eta[1]',            #   variable name    
#                             'range' : (40,-5.0,5.0,10,0.,1.),    #   variable range
#                             'xaxis' : 'DNNoutput : #eta 2nd jet',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }

# thiss2


# variables['DNN1nJet'] = {   'name': 'DNNoutputSR_noQGL:nCleanJet',            #   variable name    
#                             'range' : ([1.5, 2.5, 3.5, 4.5, 5.5, 10.5],[0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 0.7, 0.8, 0.9, 1.],),    #   variable range
#                             'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
#                             'fold' :3 ,
#                             'blind': {
#                               'ele_SR' : 'significance=0.1', 
#                            'ele_SR_highDNN' : 'significance=0.1',
#                               'mu_SR' : 'significance=0.1', 
#                            'mu_SR_highDNN' : 'significance=0.1'
#                             }
#                         }