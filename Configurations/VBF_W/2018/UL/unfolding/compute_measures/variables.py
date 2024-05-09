

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        }

# variables['ptW']  = {   'name': 'ptW_gen',     
#                         'range' : (500,0,500),   
#                         'xaxis' : 'pT(W) [GeV]',
#                         'fold' : 3,
#                         }
# variables['ptW_flat']  = {   'name': 'ptW_gen',     
#                         'range' : ([0.0, 25.0, 40.0, 55.0, 70.0, 90.0, 110.0, 140.0, 170.0, 240.0, 500.0],),   
#                         'xaxis' : 'pT(W) [GeV]',
#                         'fold' : 3,
#                         }
# variables['ptW_div']  = {   'name': 'ptW_gen',     
#                         'range' : ([0.0, 25.0, 40.0, 55.0, 70.0, 90.0, 110.0, 140.0, 170.0, 240.0, 500.0],),   
#                         'xaxis' : 'pT(W) [GeV]',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['leppt']  = {   'name': 'DressedLepton_pt[0]',     
#                         'range' : (1000,0,1000),   
#                         'xaxis' : 'p_{T} 1st lep',
#                         'fold' : 3,
#                         }
# variables['leppt_flat']  = {   'name': 'DressedLepton_pt[0]',     
#                         'range' : ([20.0, 25.0, 35.0, 40.0, 45.0, 55.0, 65.0, 80.0, 100.0, 150.0, 1000.0],), 
#                         'xaxis' : 'p_{T} 1st lep',
#                         'fold' : 3,
#                         }
# variables['leppt_div']  = {   'name': 'DressedLepton_pt[0]',     
#                         'range' : ([20.0, 25.0, 35.0, 40.0, 45.0, 55.0, 65.0, 80.0, 100.0, 150.0, 1000.0],), 
#                         'xaxis' : 'p_{T} 1st lep',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['lepeta']  = {   'name': 'DressedLepton_eta[0]',     
#                         'range' : (400,-2,2),   
#                         'xaxis' : 'eta 1st lep',
#                         'fold' : 3,
#                         }
# variables['lepeta_flat']  = {   'name': 'DressedLepton_eta[0]',     
#                         'range' : ([-2.0, -1.50, -1.00, -0.6, -0.3, 0.0, 0.3, 0.6, 1.0, 1.5, 2],),   
#                         'xaxis' : 'eta 1st lep',
#                         'fold' : 3,
#                         }
# variables['lepeta_div']  = {   'name': 'DressedLepton_eta[0]',     
#                         'range' : ([-2.0, -1.50, -1.00, -0.6, -0.3, 0.0, 0.3, 0.6, 1.0, 1.5, 2],),   
#                         'xaxis' : 'eta 1st lep',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['jet1pt']  = {   'name': 'CleanGenJet_pt[0]',     
#                         'range' : (1000,0,1000),   
#                         'xaxis' : 'p_{T} 1st jet',
#                         'fold' : 3,
#                         }
# variables['jet1pt_flat']  = {   'name': 'CleanGenJet_pt[0]',     
#                         'range' : ([60.0, 85.0, 95.0, 105.0, 120.0, 135.0, 150.0, 170.0, 200.0, 260.0, 1000.0],),   
#                         'xaxis' : 'p_{T} 1st jet',
#                         'fold' : 3,
#                         }
# variables['jet1pt_div']  = {   'name': 'CleanGenJet_pt[0]',     
#                         'range' : ([60.0, 85.0, 95.0, 105.0, 120.0, 135.0, 150.0, 170.0, 200.0, 260.0, 1000.0],),   
#                         'xaxis' : 'p_{T} 1st jet',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['jet2pt']  = {   'name': 'CleanGenJet_pt[1]',     
#                         'range' : (1000,0,1000),   
#                         'xaxis' : 'p_{T} 2st jet',
#                         'fold' : 3,
#                         }
# variables['jet2pt_flat']  = {   'name': 'CleanGenJet_pt[1]',     
#                         'range' : ([60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 95.0, 105.0, 125.0, 155.0, 1000.0],),   
#                         'xaxis' : 'p_{T} 2st jet',
#                         'fold' : 3,
#                         }
# variables['jet2pt_div']  = {   'name': 'CleanGenJet_pt[1]',     
#                         'range' : ([60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 95.0, 105.0, 125.0, 155.0, 1000.0],),   
#                         'xaxis' : 'p_{T} 2st jet',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['jeteta1']  = {   'name': 'CleanGenJet_eta[0]',     
#                         'range' : (500,-5,5),   
#                         'xaxis' : 'eta 1st jet',
#                         'fold' : 3,
#                         }
# variables['jeteta1_flat']  = {   'name': 'CleanGenJet_eta[0]',     
#                         'range' : ([-5.0, -3.0, -2.5, -2.0, -1.25, 0.0, 1.25, 2.0, 2.5, 3.0, 5.0],),   
#                         'xaxis' : 'eta 1st jet',
#                         'fold' : 3,
#                         }
# variables['jeteta1_div']  = {   'name': 'CleanGenJet_eta[0]',     
#                         'range' : ([-5.0, -3.0, -2.5, -2.0, -1.25, 0.0, 1.25, 2.0, 2.5, 3.0, 5.0],),   
#                         'xaxis' : 'eta 1st jet',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['jeteta2']  = {   'name': 'CleanGenJet_eta[1]',     
#                         'range' : (500,-5,5),   
#                         'xaxis' : 'eta 2nd jet',
#                         'fold' : 3,
#                         }
# variables['jeteta2_flat']  = {   'name': 'CleanGenJet_eta[1]',     
#                         'range' : ([-5.0, -3.3, -2.8, -2.3, -1.5, 0.0, 1.5, 2.3, 2.8, 3.3, 5.0],),   
#                         'xaxis' : 'eta 2nd jet',
#                         'fold' : 3,
#                         }
# variables['jeteta2_div']  = {   'name': 'CleanGenJet_eta[1]',     
#                         'range' : ([-5.0, -3.3, -2.8, -2.3, -1.5, 0.0, 1.5, 2.3, 2.8, 3.3, 5.0],),   
#                         'xaxis' : 'eta 2nd jet',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['detajj']  = {   'name': 'detajj_gen',     
#                         'range' : (700,3,10),   
#                         'xaxis' : 'detajj',
#                         'fold' : 3,
#                         }
# variables['detajj_flat']  = {   'name': 'detajj_gen',     
#                         'range' : ([3.5, 3.7, 3.8, 4.0, 4.2, 4.4, 4.6, 5.0, 5.5, 6.0, 10.],),   
#                         'xaxis' : 'detajj',
#                         'fold' : 3,
#                         }
# variables['detajj_div']  = {   'name': 'detajj_gen',     
#                         'range' : ([3.5, 3.7, 3.8, 4.0, 4.2, 4.4, 4.6, 5.0, 5.5, 6.0, 10.],),   
#                         'xaxis' : 'detajj',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['mjj']  = {   'name': 'mjj_gen',     
#                         'range' : (5000,0,5000),   
#                         'xaxis' : 'detajj',
#                         'fold' : 3,
#                         }
# variables['mjj_flat']  = {   'name': 'mjj_gen',     
#                         'range' : ([300.0, 650.0, 750.0, 850.0, 1000.0, 1150.0, 1300.0, 1500.0, 1800.0, 2350.0, 5000.0],),   
#                         'xaxis' : 'detajj',
#                         'fold' : 3,
#                         }
# variables['mjj_div']  = {   'name': 'mjj_gen',     
#                         'range' : ([300.0, 650.0, 750.0, 850.0, 1000.0, 1150.0, 1300.0, 1500.0, 1800.0, 2350.0, 5000.0],),   
#                         'xaxis' : 'detajj',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }

# variables['nJet']  = {   'name': 'nCleanGenJet',     
#                         'range' : (10,0,10),   
#                         'xaxis' : 'nCleanGenJet',
#                         'fold' : 3,
#                         }
# variables['nJet_flat']  = {   'name': 'nCleanGenJet',     
#                         'range' : ([1.5, 2.5, 3.5, 4.5, 5.5, 10.5],),   
#                         'xaxis' : 'nCleanGenJet',
#                         'fold' : 3,
#                         }
# variables['nJet_div']  = {   'name': 'nCleanGenJet',     
#                         'range' : ([1.5, 2.5, 3.5, 4.5, 5.5, 10.5],),      
#                         'xaxis' : 'nCleanGenJet',
#                         'fold' : 3,
#                         'divideByBinWidth': 1,
#                         }