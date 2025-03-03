

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        }

variables['ptW']  = {   'name': 'ptW_gen',     
                        'range' : (500,0,500),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        }
variables['ptW_flat']  = {   'name': 'ptW_gen',     
                        'range' : ([0.0, 35.0, 60.0, 90.0, 140.0, 500.0],),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        }
variables['ptW_div']  = {   'name': 'ptW_gen',     
                        'range' : ([0.0, 35.0, 60.0, 90.0, 140.0, 500.0],),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['leppt']  = {   'name': 'DressedLepton_pt[0]',     
                        'range' : (1000,0,1000),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3,
                        }
variables['leppt_flat']  = {   'name': 'DressedLepton_pt[0]',     
                        'range' : ([0.0, 40.0, 50.0, 65.0, 95.0, 1000.0],), 
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3,
                        }
variables['leppt_div']  = {   'name': 'DressedLepton_pt[0]',     
                        'range' : ([0.0, 40.0, 50.0, 65.0, 95.0, 1000.0],), 
                        'xaxis' : 'p_{T} 1st lep',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['lepeta']  = {   'name': 'lepeta_gen_abs',     
                        'range' : (400,0,2),   
                        'xaxis' : 'eta 1st lep',
                        'fold' : 3,
                        }
variables['lepeta_flat']  = {   'name': 'lepeta_gen_abs',     
                        'range' : ([-2.0, -1.0, -0.3, 0.3, 1., 2.],),   
                        'xaxis' : 'eta 1st lep',
                        'fold' : 3,
                        }
variables['lepeta_div']  = {   'name': 'lepeta_gen_abs',     
                        'range' : ([-2.0, -1.0, -0.3, 0.3, 1., 2.],),   
                        'xaxis' : 'eta 1st lep',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['jet1pt']  = {   'name': 'CleanGenJet_pt[0]',     
                        'range' : (1000,0,1000),   
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        }
variables['jet1pt_flat']  = {   'name': 'CleanGenJet_pt[0]',     
                        'range' : ([0.0, 100.0, 120.0, 150.0, 190.0, 1000.0],),   
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        }
variables['jet1pt_div']  = {   'name': 'CleanGenJet_pt[0]',     
                        'range' : ([0.0, 100.0, 120.0, 150.0, 190.0, 1000.0],),   
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['jet2pt']  = {   'name': 'CleanGenJet_pt[1]',     
                        'range' : (1000,0,1000),   
                        'xaxis' : 'p_{T} 2st jet',
                        'fold' : 3,
                        }
variables['jet2pt_flat']  = {   'name': 'CleanGenJet_pt[1]',     
                        'range' : ([0.0, 75.0, 85.0, 100.0, 120.0, 1000.0],),   
                        'xaxis' : 'p_{T} 2st jet',
                        'fold' : 3,
                        }
variables['jet2pt_div']  = {   'name': 'CleanGenJet_pt[1]',     
                        'range' : ([0.0, 75.0, 85.0, 100.0, 120.0, 1000.0],),   
                        'xaxis' : 'p_{T} 2st jet',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['jet1eta']  = {   'name': 'jeteta1_gen_abs',     
                        'range' : (500,0,5),   
                        'xaxis' : 'eta 1st jet',
                        'fold' : 3,
                        }
variables['jet1eta_flat']  = {   'name': 'jeteta1_gen_abs',     
                        'range' : ([-5.0, -2.4, -1.3, 1.3, 2.4, 5.],),   
                        'xaxis' : 'eta 1st jet',
                        'fold' : 3,
                        }
variables['jet1eta_div']  = {   'name': 'jeteta1_gen_abs',     
                        'range' : ([-5.0, -2.4, -1.3, 1.3, 2.4, 5.],),   
                        'xaxis' : 'eta 1st jet',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['jet2eta']  = {   'name': 'jeteta2_gen_abs',     
                        'range' : (500,0,5),   
                        'xaxis' : 'eta 2nd jet',
                        'fold' : 3,
                        }
variables['jet2eta_flat']  = {   'name': 'jeteta2_gen_abs',     
                        'range' : ([-5.0, -3.2, -1.8, 1.8, 3.2, 5.],),   
                        'xaxis' : 'eta 2nd jet',
                        'fold' : 3,
                        }
variables['jet2eta_div']  = {   'name': 'jeteta2_gen_abs',     
                        'range' : ([-5.0, -3.2, -1.8, 1.8, 3.2, 5.],),   
                        'xaxis' : 'eta 2nd jet',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['dphijj']  = {   'name': 'dphijj_gen',     
                        'range' : (314,0,3.14),   
                        'xaxis' : 'dphijj_gen',
                        'fold' : 2,
                        }
variables['dphijj_flat']  = {   'name': 'dphijj_gen',     
                        'range' : ([-5.0, -3.2, -1.8, 1.8, 3.2, 5.],),   
                        'xaxis' : 'dphijj_gen',
                        'fold' : 2,
                        }
variables['dphijj_div']  = {   'name': 'dphijj_gen',     
                        'range' : ([-5.0, -3.2, -1.8, 1.8, 3.2, 5.],),   
                        'xaxis' : 'dphijj_gen',
                        'fold' : 2,
                        'divideByBinWidth': 1,
                        }

variables['detajj']  = {   'name': 'detajj_gen',     
                        'range' : (700,3,10),   
                        'xaxis' : 'detajj',
                        'fold' : 3,
                        }
variables['detajj_flat']  = {   'name': 'detajj_gen',     
                        'range' : ([3.0, 4.3, 4.6, 5.0, 5.5, 10.],),   
                        'xaxis' : 'detajj',
                        'fold' : 3,
                        }
variables['detajj_div']  = {   'name': 'detajj_gen',     
                        'range' : ([3.0, 4.3, 4.6, 5.0, 5.5, 10.],),   
                        'xaxis' : 'detajj',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['mjj']  = {   'name': 'mjj_gen',     
                        'range' : (5000,0,5000),   
                        'xaxis' : 'detajj',
                        'fold' : 3,
                        }
variables['mjj_flat']  = {   'name': 'mjj_gen',     
                        'range' : ([0.0, 950.0, 1200.0, 1500.0, 2000.0, 5000.0],),   
                        'xaxis' : 'detajj',
                        'fold' : 3,
                        }
variables['mjj_div']  = {   'name': 'mjj_gen',     
                        'range' : ([0.0, 950.0, 1200.0, 1500.0, 2000.0, 5000.0],),   
                        'xaxis' : 'detajj',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['ptjj']  = {   'name': 'ptjj_gen',     
                        'range' : (500,0,500),   
                        'xaxis' : 'ptjj',
                        'fold' : 3,
                        }
variables['ptjj_flat']  = {   'name': 'ptjj_gen',     
                        'range' : ([0.0, 950.0, 1200.0, 1500.0, 2000.0, 5000.0],),   
                        'xaxis' : 'ptjj',
                        'fold' : 3,
                        }
variables['ptjj_div']  = {   'name': 'ptjj_gen',     
                        'range' : ([0.0, 950.0, 1200.0, 1500.0, 2000.0, 5000.0],),   
                        'xaxis' : 'ptjj',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }

variables['nJet']  = {   'name': 'nCleanGenJet',     
                        'range' : (10,0,10),   
                        'xaxis' : 'nCleanGenJet',
                        'fold' : 3,
                        }
variables['nJet_flat']  = {   'name': 'nCleanGenJet',     
                        'range' : ([1.5, 2.5, 4.5, 10.5],),   
                        'xaxis' : 'nCleanGenJet',
                        'fold' : 3,
                        }
variables['nJet_div']  = {   'name': 'nCleanGenJet',     
                        'range' : ([1.5, 2.5, 4.5, 10.5],),      
                        'xaxis' : 'nCleanGenJet',
                        'fold' : 3,
                        'divideByBinWidth': 1,
                        }