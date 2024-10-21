

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


# # ######## lepton 1 ##########

# # variables['pt1']  = {   'name': 'Lepton_pt[0]',     
# #                         'range' : (20,20,50),   
# #                         'xaxis' : 'p_{T} 1st lep',
# #                         'fold' : 0,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }
                     
# # variables['eta1']  = {  'name': 'Lepton_eta[0]',     
# #                         'range' : (24,-2.4,2.4),   
# #                         'xaxis' : '#eta 1st lep',
# #                         'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }                         
# #                         }

# # variables['phi1']  = {  'name': 'Lepton_phi[0]',
# #                         'range' : (40,-3.2,3.2),
# #                         'xaxis' : '#phi 1st lep',
# #                         'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }

# variables['mtw1']  = {   'name': 'mtw1',
#                         'range' : (20,0,200),
#                          'xaxis' : 'm_{T}^{l1+MET} [GeV]',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
#                        }

# variables['mtw1bin2']  = {   'name': 'mtw1',
#                         'range' : (100,0,200),
#                          'xaxis' : 'm_{T}^{l1+MET} [GeV]',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
#                        }


# # variables['puppimet']  = {
# #                         'name': 'PuppiMET_pt',
# #                         'range' : (40,0,200),
# #                         'xaxis' : 'puppimet [GeV]',
# #                         'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }

# # variables['puppimetbin1']  = {
# #                         'name': 'PuppiMET_pt',
# #                         'range' : (60,0,60),
# #                         'xaxis' : 'puppimet [GeV]',
# #                         'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }


# variables['ptW']  = {   'name': 'ptW',     
#                         'range' : (30,0,300),   
#                         'xaxis' : 'pT(W) [GeV]',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
#                         }

# # ############# getti ###################
# variables['njet_30']  = {
#                          'name': 'Sum$(CleanJet_pt>30)',     
#                          'range' : (8,0,8),   
#                          'xaxis' : 'Number of jets w/ pt>30 GeV',
#                          'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                          }


# variables['jetpt1']  = {
#                         'name': 'CleanJet_pt[0]',
#                         'range' : (70,40,350),
#                         'xaxis' : 'p_{T} 1st jet',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }



# variables['jetpt2']  = {
#                         'name': 'CleanJet_pt[1]',
#                         'range' : (50,30,250),
#                         'xaxis' : 'p_{T} 2nd jet',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }



# variables['mjj']      = {   'name': 'mjj',            #   variable name    
#                             'range' : (25,0,2500),    #   variable range
#                             'xaxis' : 'm_{jj} [GeV]',  #   x axis name
#                             'fold' : 3,
#                             'blind': {
#                               'ele_SR' : 'full',
#                               'mu_SR' : 'full'
#                             }
#                         }

# variables['mjjPU']      = {   'name': 'mjj',            #   variable name    
#                             'range' : (15,0,2500),    #   variable range
#                             'xaxis' : 'm_{jj} [GeV]PU',  #   x axis name
#                             'fold' : 3,
#                             'blind': {
#                               'ele_SR' : 'full',
#                               'mu_SR' : 'full'
#                             }
#                         }

# variables['mjj_H']      = {   'name': 'mjj',            #   variable name    
#                             'range' : (20,0,1000),    #   variable range
#                             'xaxis' : 'm_{jj}H [GeV]',  #   x axis name
#                             'fold' : 3,
#                             'blind': {
#                               'ele_SR' : 'full',
#                               'mu_SR' : 'full'
#                             }
#                         }

# variables['detajj'] = {   'name': 'detajj',            #   variable name    
#                             'range' : (80,-1,10),    #   variable range
#                             'xaxis' : '#Delta#eta_{jj}',  #   x axis name
#                             'fold' : 3,
#                             'blind': {
#                               'ele_SR' : 'full',
#                               'mu_SR' : 'full'
#                             }
#                         }

# variables['detajj_PU'] = {   'name': 'detajj',            #   variable name    
#                             'range' : (20,4,10),    #   variable range
#                             'xaxis' : '#Delta#eta_{jj}PU',  #   x axis name
#                             'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
#                         }

# variables['detajj_H'] = {   'name': 'detajj',            #   variable name    
#                             'range' : (30,2,5),    #   variable range
#                             'xaxis' : '#Delta#eta_{jj}H',  #   x axis name
#                             'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
#                         }

# # variables['jeteta1']  = {
# #                         'name': 'CleanJet_eta[0]',
# #                          'range' : (40,-5.0,5.0),
# #                          'xaxis' : '#eta 1st jet',
# #                          'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }

# # variables['jeteta2']  = {
# #                         'name': 'CleanJet_eta[1]',
# #                          'range' : (40,-5.0,5.0),
# #                          'xaxis' : '#eta 2nd jet',
# #                          'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }

# # variables['jetphi1']  = {
# #                         'name': 'CleanJet_phi[0]',
# #                          'range' : (40,-3.2,3.2),
# #                          'xaxis' : '#phi 1st jet',
# #                          'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }

# # variables['jetphi2']  = {
# #                         'name': 'CleanJet_phi[1]',
# #                          'range' : (40,-3.2,3.2),
# #                          'xaxis' : '#phi 2nd jet',
# #                          'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }

# variables['Zl1bin3'] = {   'name': 'Zl1',     
#                         'range' : (60,-3,3),   
#                         'xaxis' : 'Zl1',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
# }

# variables['Zl1bin4'] = {   'name': 'Zl1',     
#                         'range' : (20,-3,3),   
#                         'xaxis' : 'Zl1',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
# }


# # variables['DNNoutputSR_noQGLbin1'] = {   'name': 'DNNoutputSR_noQGL',     
# #                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 1.],), 
# #                         'xaxis' : 'DNNoutput',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'full',
# #                            'mu_SR' : 'full'
# #                          }
# # }

# # variables['DNNoutputSR_noQGLbin2'] = {   'name': 'DNNoutputSR_noQGL',     
# #                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 1.],), 
# #                         'xaxis' : 'DNNoutput',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'full',
# #                            'mu_SR' : 'full'
# #                          }
# # }

# # variables['DNNoutputSR_noQGLbin3'] = {   'name': 'DNNoutputSR_noQGL',     
# #                         'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 1.],), 
# #                         'xaxis' : 'DNNoutput',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'full',
# #                            'mu_SR' : 'full'
# #                          }
# # }

# # variables['DNNoutputSR_noQGLbin4'] = {   'name': 'DNNoutputSR_noQGL',     
# #                         'range' : (10,0,1), 
# #                         'xaxis' : 'DNNoutput',
# #                         'fold' : 3,
# #                         'blind': {
# #                            'ele_SR' : 'full',
# #                            'mu_SR' : 'full'
# #                          }
# # }


# # variables['mjj_bin1']      = {   'name': 'mjj',            #   variable name    
# #                             'range' : ([400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2500.],),    #   variable range
# #                             'xaxis' : 'm_{jj} [GeV]',  #   x axis name
# #                             'fold' : 3,
# #                             'blind': {
# #                               'ele_SR' : 'full',
# #                               'mu_SR' : 'full'
# #                             }
# #                         }

# #### leptons (l, nu, l+nu)

variables['DNN1ptW'] = {   'name': 'DNNoutputSR_noQGL:ptW',            #   variable name    
                            'range' : (30,0.,500.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : ptW [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1leppt'] = {   'name': 'DNNoutputSR_noQGL:Lepton_pt[0]',            #   variable name    
                            'range' : (35,0,200,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }   

variables['DNN1lepeta'] = {   'name': 'DNNoutputSR_noQGL:Lepton_eta[0]',            #   variable name    
                            'range' : (20,-2.,2.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta lepton',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }    


# ######## jets

variables['DNN1jet1pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[0]',            #   variable name    
                            'range' : (35,40.,350.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1jet1eta'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_eta[0]',            #   variable name    
                            'range' : (40,-5.0,5.0,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta 1st jet',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1jet2pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[1]',            #   variable name    
                            'range' : (25,30.,250.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1jet2eta'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_eta[1]',            #   variable name    
                            'range' : (40,-5.0,5.0,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta 2nd jet',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1mjj'] = {   'name': 'DNNoutputSR_noQGL:mjj',            #   variable name    
                            'range' : (27,300.,3000.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                            # 'blind': {
                            #   'ele_SR' : 'full',
                            #   'mu_SR' : 'full'
                            # }
                        }

variables['DNN1mjj2'] = {   'name': 'DNNoutputSR_noQGL:mjj',            #   variable name    
                            'range' : (10,300.,3000.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                            # 'blind': {
                            #   'ele_SR' : 'full',
                            #   'mu_SR' : 'full'
                            # }
                        }


variables['DNN1detajj'] = {   'name': 'DNNoutputSR_noQGL:detajj',            #   variable name    
                            'range' : (26,3.5,10.,10,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1nJet'] = {   'name': 'DNNoutputSR_noQGL:nCleanJet',            #   variable name    
                            'range' : ([1.5, 2.5, 3.5, 4.5, 5.5, 10.5],[0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 0.7, 0.8, 0.9, 1.],),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }