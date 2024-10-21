

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,

                        }


######## lepton 1 ##########

variables['pt1_gen']  = {   'name': 'DressedLepton_pt[0]',     
                        'range' : (35,0,175),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3,

                        }

variables['pt1bin2_gen']  = {   'name': 'DressedLepton_pt[0]',     
                        'range' : (20,20,50),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 0,

                        }

variables['pt1bin3_gen']  = {   'name': 'DressedLepton_pt[0]',     
                        'range' : (6,25,75),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 0,

                        }

variables['eta1_gen']  = {  'name': 'DressedLepton_eta[0]',     
                        'range' : (24,-2.4,2.4),   
                        'xaxis' : '#eta 1st lep',
                        'fold' : 3,
                         
                        }
variables['eta1binHEM_gen']  = {  'name': 'DressedLepton_eta[0]',     
                        'range' : (30,-2.,-1.),   
                        'xaxis' : '#eta 1st lep',
                        'fold' : 3,
                         
                        }
                        
variables['phi1_gen']  = {  'name': 'DressedLepton_phi[0]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold' : 3,

                        }

# variables['puppimet_phi']  = {  'name': 'PuppiMET_phi',
#                         'range' : (40,-3.2,3.2),
#                         'xaxis' : '#phi MET',
#                         'fold' : 3,

#                         }

# variables['puppimet_phiPU']  = {  'name': 'PuppiMET_phi',
#                         'range' : (20,-3.2,3.2),
#                         'xaxis' : '#phi METPU',
#                         'fold' : 3,

#                         }

variables['mW']  = {   'name': 'mW',
                        'range' : (50,0,200),
                         'xaxis' : 'm(l1+v) [GeV]',
                        'fold' : 3,
                       }

# variables['mtw1bin2']  = {   'name': 'mtw1',
#                         'range' : (100,0,200),
#                          'xaxis' : 'm_{T}^{l1+MET} [GeV]',
#                         'fold' : 3,

#                        }

# variables['mtw1bin1']  = {   'name': 'mtw1',
#                         'range' : (50,0,50),
#                          'xaxis' : 'm_{T}^{l1+MET} [GeV]',
#                         'fold' : 3,

#                        }

variables['NeutrinoGen_pt']  = {
                        'name': 'NeutrinoGen_pt',
                        'range' : (40,0,200),
                        'xaxis' : 'NeutrinoGen_pt [GeV]',
                        'fold' : 3,

                        }

variables['NeutrinoGen_pt_bin1']  = {
                        'name': 'NeutrinoGen_pt',
                        'range' : (60,0,60),
                        'xaxis' : 'NeutrinoGen_pt [GeV]',
                        'fold' : 3,

                        }

# variables['met']  = {
#                         'name': 'MET_pt',
#                         'range' : (40,0,200),
#                         'xaxis' : 'MET_pt [GeV]',
#                         'fold' : 3,

#                         }

# variables['metbin1']  = {
#                         'name': 'MET_pt',
#                         'range' : (60,0,60),
#                         'xaxis' : 'MET_pt [GeV]',
#                         'fold' : 3,

#                         }


# variables['Dphilep1met']  = {   'name': 'Dphilep1met',     
#                         'range' : (60,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi_{L1, MET}',
#                         'fold' : 3,

#                         }

# variables['Dphilep1metPU']  = {   'name': 'Dphilep1met',     
#                         'range' : (30,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi_{L1, MET}PU',
#                         'fold' : 3,

#                         }

variables['ptW_gen']  = {   'name': 'ptW_gen',     
                        'range' : (30,0,300),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,

                        }

# ############# getti ###################
# variables['njet_30']  = {
#                          'name': 'Sum$(CleanJet_pt>30)',     
#                          'range' : (8,0,8),   
#                          'xaxis' : 'Number of jets w/ pt>30 GeV',
#                          'fold' : 3,
#    # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                          }

variables['jetpt1_gen']  = {
                        'name': 'CleanGenJet_pt[0]',
                        'range' : (70,0,200),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }



variables['jetpt1_gen_PU']  = {
                        'name': 'CleanGenJet_pt[0]',
                        'range' : (25,0,150),
                        'xaxis' : 'p_{T}PU 1st jet',
                        'fold' : 3,
   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt2_gen']  = {
                        'name': 'CleanGenJet_pt[1]',
                        'range' : (50,0,200),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 3,
   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['jetpt2_gen_PU']  = {
                        'name': 'CleanGenJet_pt[1]',
                        'range' : (10,0,150),
                        'xaxis' : 'p_{T}PU 2nd jet',
                        'fold' : 3,
   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jeteta1_gen']  = {
                        'name': 'CleanGenJet_eta[0]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 1st jet',
                         'fold' : 3,

                        }

variables['jeteta2_gen']  = {
                        'name': 'CleanGenJet_eta[1]',
                         'range' : (40,-5.0,5.0),
                         'xaxis' : '#eta 2nd jet',
                         'fold' : 3,

                        }


variables['mjj_gen']      = {   'name': 'mjj_gen',            #   variable name    
                            'range' : (40,0,1500),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,

                        }

variables['mjj_gen_PU']      = {   'name': 'mjj_gen',            #   variable name    
                            'range' : (40,120,2000),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]PU',  #   x axis name
                            'fold' : 3,

                        }

variables['mjj_gen_H']      = {   'name': 'mjj_gen',            #   variable name    
                            'range' : (30,100,1000),    #   variable range
                            'xaxis' : 'm_{jj}H [GeV]',  #   x axis name
                            'fold' : 3,

                        }

variables['detajj_gen'] = {   'name': 'detajj_gen',            #   variable name    
                            'range' : (80,-1,10),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}',  #   x axis name
                            'fold' : 3,

                        }
variables['njet10'] = {   'name': 'njet10',            #   variable name    
                            'range' : (7,0,7),    #   variable range
                            'xaxis' : 'njet10',  #   x axis name
                            'fold' : 3,
                        }
variables['njet20'] = {   'name': 'njet20',            #   variable name    
                            'range' : (7,0,7),    #   variable range
                            'xaxis' : 'njet20',  #   x axis name
                            'fold' : 3,
                        }


# variables['Dphijet1met']  = {   'name': 'Dphijet1met',     
#                         'range' : (60,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{J1, MET}',
#                         'fold' : 3,

#                         }

# variables['Dphijet1metPU']  = {   'name': 'Dphijet1met',     
#                         'range' : (30,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{J1, MET}PU',
#                         'fold' : 3,

#                         }

# variables['Dphijet2met']  = {   'name': 'Dphijet2met',     
#                         'range' : (60,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{J2, MET}',
#                         'fold' : 3,

#                         }

# variables['Dphijet2metPU']  = {   'name': 'Dphijet2met',     
#                         'range' : (30,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{J2, MET}PU',
#                         'fold' : 3,

#                         }

# variables['Dphijet1jet2']  = {   'name': 'Dphijet1jet2',     
#                         'range' : (60,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{J1, J2}',
#                         'fold' : 3,

#                         }

# variables['Dphijet1jet2PU']  = {   'name': 'Dphijet1jet2',     
#                         'range' : (30,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{J1, J2}PU',
#                         'fold' : 3,

#                         }

# variables['Dphilep1jet1']  = {   'name': 'Dphilep1jet1',     
#                         'range' : (60,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{L1, J1}',
#                         'fold' : 3,

#                         }

# variables['Dphilep1jet1PU']  = {   'name': 'Dphilep1jet1',     
#                         'range' : (30,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{L1, J1}PU',
#                         'fold' : 3,

#                         }

# variables['Dphilep1jet2']  = {   'name': 'Dphilep1jet2',     
#                         'range' : (60,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{L1, J2}',
#                         'fold' : 3,

#                         }

# variables['Dphilep1jet2PU']  = {   'name': 'Dphilep1jet2',     
#                         'range' : (30,-3.14,3.14),   
#                         'xaxis' : '#Delta#phi{L1, J2}PU',
#                         'fold' : 3,

#                         }

# variables['R'] = {   'name': 'R_AN',     
#                         'range' : (50,0,1),   
#                         'xaxis' : 'R_AN',
#                         'fold' : 3,

# }

# variables['RPU'] = {   'name': 'R_AN',     
#                         'range' : (20,0,1),   
#                         'xaxis' : 'R_ANPU',
#                         'fold' : 3,

# }

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


# variables['DeepBj1'] = {   'name': 'Jet_btagDeepB[CleanJet_jetIdx[0]]',     
#                         'range' : (10,0,1),   
#                         'xaxis' : 'BJet1',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
# }

# variables['DeepBj2'] = {   'name': 'Jet_btagDeepB[CleanJet_jetIdx[1]]',     
#                         'range' : (10,0,1),   
#                         'xaxis' : 'BJet2',
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full',
#                            'mu_SR' : 'full'
#                          }
# }

variables['DNNoutput_ALLbin1'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,

}

variables['DNNoutput_ALLbin2'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,

}

variables['DNNoutput_ALLbin3'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : ([0., 0.10, 0.20, 0.30, 0.40, 0.50, 0.6, 1.],), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,

}

variables['DNNoutput_ALLbin4'] = {   'name': 'DNNoutputSR_noQGL',     
                        'range' : (10,0,1), 
                        'xaxis' : 'DNNoutput',
                        'fold' : 3,

}


variables['mjj_gen_bin1']      = {   'name': 'mjj_gen',            #   variable name    
                            'range' : ([400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2500.],),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' : 3,

                        }


# variables['CleanJetNS_mjj']      = {   'name': 'CleanJetNS_mjj',            #   variable name    
#                             'range' : ([400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800., 1900., 2000., 2500.],),    #   variable range
#                             'xaxis' : 'm_{jj} [GeV]',  #   x axis name
#                             'fold' : 3,
#                             'blind': {
#                               'ele_SR' : 'full',
#                               'mu_SR' : 'full'
#                             }
#                         }

# variables['leppt_eta'] = {   'name': 'Lepton_pt[0]:Lepton_eta[0]',            #   variable name    
#                             'range' : ([-2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.],[25., 30., 35., 40., 45., 60., 75.,],),    #   variable range
#                             'xaxis' : 'Lepton_pt : Lepton_eta [GeV]',  #   x axis name
#                             'fold' :0 ,
#                             'blind': {
#                               'ele_SR' : 'full',
#                               'mu_SR' : 'full'
#                             }
#                         }

