

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        }

variables['high0p5events'] = {   'name': 'ptjj:DNNJoined',            #   variable name    
                            'range' : (1,0.5,1.,1,0.,10000.),    #   variable range
                            'xaxis' : 'DNNoutput : events [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

# # # #### leptons (l, nu, l+nu)

# variables['DNN1ptW'] = {   'name': 'ptW:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,0.,500.),    #   variable range
#                             'xaxis' : 'DNNoutput : ptW [GeV]',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1ptW2'] = {   'name': 'ptW:DNNJoined',            #   variable name    
                            'range' :  ([0.5, 1.],[0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0, 105.0, 120.0, 150.0, 180.0, 590.0, 1000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : pT_{W} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1ptW3'] = {   'name': 'ptW:DNNJoined',            #   variable name    
                            'range' :  ([0.5, 1.],[0., 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 140.0, 155.0, 180.0, 235.0, 307.0, 10000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : pT_{W} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1ptW3_old'] = {   'name': 'ptW:DNNJoined',            #   variable name    
                            'range' :  ([0.5, 1.],[0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 140.0, 160.0, 180.0, 453.333, 726.667, 1000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : pT_{W} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }


# variables['DNN1leppt'] = {   'name': 'Lepton_pt[0]:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,0,200),    #   variable range
#                             'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
#                             'fold' :3 ,
#                         }   

variables['high0p5DNN1leppt2'] = {   'name': 'Lepton_pt[0]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 90.0, 100.0, 125.0, 150.0, 575.0, 1000.0],),   #   variable range
                            'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
                            'fold' :2 ,
                        }   

variables['high0p5DNN1leppt3'] = {   'name': 'Lepton_pt[0]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[20.0, 26.0, 28.0, 30.0, 33.0, 37.0, 40.0, 43.0, 46.0, 50.0, 53.0, 56.0, 60.0, 63.0, 66.0, 70.0, 73.0, 76.0, 80.0, 85.0, 92.0, 100.0, 110.0, 130.0, 150.0, 177.0, 230.0, 1000.0],),   #   variable range
                            'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
                            'fold' :2 ,
                        }   

variables['high0p5DNN1leppt4'] = {   'name': 'Lepton_pt[0]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[20.0, 22.5, 25.0, 27.5, 30.0, 32.5, 35.0, 37.5, 40.0, 42.5, 45.0, 47.5, 50.0, 52.5, 55.0, 57.5, 60.0, 62.5, 65.0, 67.5, 70.0, 72.5, 75.0, 77.5, 80.0, 85.0, 90.0, 95.0, 100.0, 112.5, 125.0, 137.5, 150.0, 362.5, 575.0, 787.5, 1000.0],),   #   variable range
                            'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
                            'fold' :2 ,
                        }   


# variables['DNN1lepeta'] = {   'name': 'lepeta_abs:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,0,2.),    #   variable range
#                             'xaxis' : 'DNNoutput : |#eta| lepton',  #   x axis name
#                             'fold' :3 ,
#                         }   
 
variables['high0p5DNN1lepeta2'] = {   'name': 'lepeta_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.075, 0.15, 0.225, 0.3, 0.4, 0.5, 0.575, 0.65, 0.725, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.55, 1.7, 1.85, 2.0],),    #   variable range
                            'xaxis' : 'DNNoutput : |#eta| lepton',  #   x axis name
                            'fold' :2 ,
                        }    
variables['high0p5DNN1lepeta3'] = {   'name': 'lepeta_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.057, 0.1, 0.15, 0.2, 0.25, 0.3, 0.367, 0.433, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.867, 0.933, 1.0, 1.067, 1.133, 1.2, 1.267, 1.333, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0],),    #   variable range
                            'xaxis' : 'DNNoutput : |#eta| lepton',  #   x axis name
                            'fold' :2 ,
                        }    
variables['high0p5DNN1lepeta4'] = {   'name': 'lepeta_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.037, 0.075, 0.112, 0.15, 0.188, 0.225, 0.262, 0.3, 0.35, 0.4, 0.45, 0.5, 0.537, 0.575, 0.613, 0.65, 0.688, 0.725, 0.763, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.475, 1.55, 1.625, 1.7, 1.775, 1.85, 1.925, 2.0],),    #   variable range
                            'xaxis' : 'DNNoutput : |#eta| lepton',  #   x axis name
                            'fold' :2 ,
                        }    


# ######## jets

# variables['DNN1jet1pt'] = {   'name': 'CleanJet_pt[0]:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,40.,350.,),    #   variable range
#                             'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1jet1pt2'] = {   'name': 'CleanJet_pt[0]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[60.0, 85.0, 110.0, 125.0, 140.0, 160.0, 180.0, 205.0, 230.0, 265.0, 300.0, 650.0, 1000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1jet1pt3'] = {   'name': 'CleanJet_pt[0]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[60.0, 91.0, 100.0, 110.0, 120.0, 130.0, 140.0, 155.0, 166.0, 180.0, 197.0, 213.333, 230.0, 253.333, 272.0, 300.0, 350.0, 426.0, 10000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1jet1pt4'] = {   'name': 'CleanJet_pt[0]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[60.0, 72.5, 85.0, 97.5, 110.0, 117.5, 125.0, 132.5, 140.0, 150.0, 160.0, 170.0, 180.0, 192.5, 205.0, 217.5, 230.0, 247.5, 265.0, 282.5, 300.0, 475.0, 650.0, 825.0, 1000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
                            'fold' :2 ,
                        }


# variables['DNN1jet1eta'] = {   'name': 'jeteta1_abs:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,0,5.0,),    #   variable range
#                             'xaxis' : 'DNNoutput : |#eta| 1st jet',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1jet1eta2'] = {   'name': 'jeteta1_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.45, 0.9, 1.1, 1.3, 1.5, 1.7, 1.85, 2.0, 2.1, 2.2, 2.3, 2.4, 2.7, 3.0, 3.15, 3.3, 3.45, 3.6, 4.3, 5.0],),   #   variable range
                            'xaxis' : 'DNNoutput : |#eta| 1st jet',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1jet1eta3'] = {   'name': 'jeteta1_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.6, 0.77, 0.9, 1.04, 1.167, 1.3, 1.45, 1.567, 1.7, 1.8, 1.9, 2.0, 2.07, 2.133, 2.2, 2.267, 2.333, 2.4, 2.44, 3.0, 3.1, 3.2, 3.3, 3.4, 3.45, 3.6, 3.7, 3.9, 5.0],),   #   variable range
                            'xaxis' : 'DNNoutput : |#eta| 1st jet',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1jet1eta4'] = {   'name': 'jeteta1_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.225, 0.45, 0.675, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.775, 1.85, 1.925, 2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.55, 2.7, 2.85, 3.0, 3.075, 3.15, 3.225, 3.3, 3.375, 3.45, 3.525, 3.6, 3.95, 4.3, 4.65, 5.0],),   #   variable range
                            'xaxis' : 'DNNoutput : |#eta| 1st jet',  #   x axis name
                            'fold' :2 ,
                        }


# variables['DNN1jet2pt'] = {   'name': 'CleanJet_pt[1]:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,30.,250.),    #   variable range
#                             'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1jet2pt2'] = {   'name': 'CleanJet_pt[1]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[60.0, 70.0, 80.0, 90.0, 100.0, 115.0, 130.0, 150.0, 170.0, 200.0, 230.0, 615.0, 1000.0],),   #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1jet2pt3'] = {   'name': 'CleanJet_pt[1]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[60.0, 73.0, 76.0, 80.0, 86.667, 93.333, 100.0, 110.0, 120.0, 130.0, 143.333, 153.667, 170.0, 187.0, 203.0, 230.0, 262.0, 300.0, 1000.0],),   #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1jet2pt4'] = {   'name': 'CleanJet_pt[1]:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 107.5, 115.0, 122.5, 130.0, 140.0, 150.0, 160.0, 170.0, 185.0, 200.0, 215.0, 230.0, 422.5, 615.0, 807.5, 1000.0],),   #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
                            'fold' :2 ,
                        }


# variables['DNN1jet2eta'] = {   'name': 'jeteta2_abs:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,0,5.0),    #   variable range
#                             'xaxis' : 'DNNoutput : |#eta| 2nd jet',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1jet2eta2'] = {   'name': 'jeteta2_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.65, 1.3, 1.55, 1.8, 1.95, 2.1, 2.2, 2.3, 2.65, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.725, 3.85, 4.425, 5.0],),    #   variable range
                            'xaxis' : 'DNNoutput : |#eta| 2nd jet',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1jet2eta3'] = {   'name': 'jeteta2_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 1.15, 1.3, 1.52, 1.7, 1.8, 1.92, 2.02, 2.1, 2.17, 2.23, 2.3, 2.38, 2.44, 3.0, 3.08, 3.12, 3.2, 3.26, 3.3, 3.4, 3.45, 3.52, 3.6, 3.67, 3.77, 3.85, 3.97, 4.16, 5.0],),    #   variable range
                            'xaxis' : 'DNNoutput : |#eta| 2nd jet',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1jet2eta4'] = {   'name': 'jeteta2_abs:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.325, 0.65, 0.975, 1.3, 1.425, 1.55, 1.675, 1.8, 1.875, 1.95, 2.025, 2.1, 2.15, 2.2, 2.25, 2.3, 2.475, 2.65, 2.825, 3.0, 3.05, 3.1, 3.15, 3.2, 3.25, 3.3, 3.35, 3.4, 3.45, 3.5, 3.55, 3.6, 3.663, 3.725, 3.788, 3.85, 4.138, 4.425, 4.713, 5.0],),    #   variable range
                            'xaxis' : 'DNNoutput : |#eta| 2nd jet',  #   x axis name
                            'fold' :2 ,
                        }


# ######## dijet variables
# variables['DNN1ptjj'] = {   'name': 'ptjj:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,0.,400.),    #   variable range
#                             'xaxis' : 'DNNoutput : pT_{jj} [GeV]',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1ptjj2'] = {   'name': 'ptjj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 15.0, 30.0, 40.0, 50.0, 62.5, 75.0, 87.5, 100.0, 115.0, 130.0, 155.0, 180.0, 590.0, 1000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : pT_{jj} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1ptjj3'] = {   'name': 'ptjj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 15.0, 20.0, 30.0, 36.667, 43.333, 50.0, 58.333, 66.667, 75.0, 84.333, 91.667, 100.0, 110.0, 120.0, 130.0, 146.667, 163.333, 180.0, 229.0, 300.0, 10000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : pT_{jj} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1ptjj'] = {   'name': 'ptjj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 7.5, 15.0, 22.5, 30.0, 35.0, 40.0, 45.0, 50.0, 56.25, 62.5, 68.75, 75.0, 81.25, 87.5, 93.75, 100.0, 107.5, 115.0, 122.5, 130.0, 142.5, 155.0, 167.5, 180.0, 385.0, 590.0, 795.0, 1000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : pT_{jj} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }


# variables['DNN1mjj'] = {   'name': 'mjj:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,300.,3000.),    #   variable range
#                             'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1mjj2'] = {   'name': 'mjj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[300.0, 575.0, 850.0, 925.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1800.0, 2000.0, 2250.0, 2500.0, 6250.0, 10000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1mjj3'] = {   'name': 'mjj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[300.0, 850.0, 930.0, 950.0, 1000.0, 1100.667, 1150.333, 1200.0, 1288.667, 1333.333, 1400.0, 1473.667, 1538.333, 1600.0, 1750.333, 1866.667, 2000.0, 2197.667, 2343.333, 2500.0, 3000.0, 3600.0, 10000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1mjj4'] = {   'name': 'mjj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[300.0, 437.5, 575.0, 712.5, 850.0, 887.5, 925.0, 962.5, 1000.0, 1050.0, 1100.0, 1150.0, 1200.0, 1250.0, 1300.0, 1350.0, 1400.0, 1450.0, 1500.0, 1550.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2125.0, 2250.0, 2375.0, 2500.0, 4375.0, 6250.0, 8125.0, 10000.0],),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :2 ,
                        }



# variables['DNN1detajj'] = {   'name': 'detajj:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,3.5,10.),    #   variable range
#                             'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1detajj2'] = {   'name': 'detajj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.35, 5.5, 5.75, 6.0, 8.0, 10.0],),     #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1detajj3'] = {   'name': 'detajj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[4.0, 4.067, 4.133, 4.2, 4.267, 4.333, 4.4, 4.467, 4.533, 4.6, 4.667, 4.733, 4.8, 4.867, 4.933, 5.0, 5.067, 5.133, 5.2, 5.3, 5.4, 5.5, 5.667, 5.773, 6.0, 6.383, 6.85, 10.0],),     #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1detajj4'] = {   'name': 'detajj:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[4.0, 4.05, 4.1, 4.15, 4.2, 4.25, 4.3, 4.35, 4.4, 4.45, 4.5, 4.55, 4.6, 4.65, 4.7, 4.75, 4.8, 4.85, 4.9, 4.95, 5.0, 5.05, 5.1, 5.15, 5.2, 5.275, 5.35, 5.425, 5.5, 5.625, 5.75, 5.875, 6.0, 7.0, 8.0, 9.0, 10.0],),     #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :2 ,
                        }


# variables['DNN1nJet'] = {   'name': 'nCleanJet30:DNNJoined',            #   variable name    
#                             'range' : ([0., 0.2, 0.4, 0.6, 0.8, 1.],[1.5, 2.5, 3.5, 10.5],),    #   variable range
#                             'xaxis' : 'DNNoutput : nJets',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1nJet'] = {   'name': 'nCleanJet30:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[1.5, 2.5, 3.5, 10.5],),    #   variable range
                            'xaxis' : 'DNNoutput : nJets',  #   x axis name
                            'fold' :2 ,
                        }


# variables['DNN1dphijj'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
#                             'range' : (5,0.,1.,10,0,3.14,),    #   variable range
#                             'xaxis' : 'DNNoutput : #Delta#phi_{jj}',  #   x axis name
#                             'fold' :3 ,
#                         }

variables['high0p5DNN1dphijj2'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 1.0, 2.0, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.07, 3.14],),     #   variable range
                            'xaxis' : 'DNNoutput : #Delta#phi_{jj}',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1dphijj3'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 1.11, 1.69, 2.0, 2.173, 2.267, 2.4, 2.467, 2.533, 2.6, 2.667, 2.733, 2.8, 2.867, 2.933, 3.0, 3.047, 3.099, 3.14],),     #   variable range
                            'xaxis' : 'DNNoutput : #Delta#phi_{jj}',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p5DNN1dphijj4'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
                            'range' : ([0.5, 1.],[0.0, 0.5, 1.0, 1.5, 2.0, 2.1, 2.2, 2.3, 2.4, 2.45, 2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95, 3.0, 3.035, 3.07, 3.105, 3.14],),     #   variable range
                            'xaxis' : 'DNNoutput : #Delta#phi_{jj}',  #   x axis name
                            'fold' :2 ,
                        }



bin_map = {
    "leppt": [1.0, 1.17, 1.33, 1.5, 1.67, 1.83, 2.0, 2.17, 2.33, 2.5, 2.67, 2.83, 3.0, 3.17, 3.33, 3.5, 3.67, 3.83, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.33, 8.67, 9.0, 9.33, 9.67, 10.0],
    "lepeta": [1.0, 1.17, 1.33, 1.5, 1.67, 1.83, 2.0, 2.17, 2.33, 2.5, 2.67, 2.83, 3.0, 3.17, 3.33, 3.5, 3.67, 3.83, 4.0, 4.17, 4.33, 4.5, 4.67, 4.83, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.33, 9.67, 10.0, 10.33, 10.67, 11.0],
    "jet1pt": [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.33, 5.67, 6.0, 6.33, 6.67, 7.0],
    "jet1eta": [1.0, 1.17, 1.33, 1.5, 1.67, 1.83, 2.0, 2.17, 2.33, 2.5, 2.67, 2.83, 3.0, 3.17, 3.33, 3.5, 3.67, 3.83, 4.0, 4.17, 4.33, 4.5, 4.67, 4.83, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.33, 9.67, 10.0, 10.33, 10.67, 11.0],
    "jet2pt": [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.33, 5.67, 6.0, 6.33, 6.67, 7.0],
    "jet2eta": [1.0, 1.17, 1.33, 1.5, 1.67, 1.83, 2.0, 2.17, 2.33, 2.5, 2.67, 2.83, 3.0, 3.17, 3.33, 3.5, 3.67, 3.83, 4.0, 4.17, 4.33, 4.5, 4.67, 4.83, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.33, 9.67, 10.0, 10.33, 10.67, 11.0],
    "mjj": [1.0, 1.17, 1.33, 1.5, 1.67, 1.83, 2.0, 2.17, 2.33, 2.5, 2.67, 2.83, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.33, 7.67, 8.0, 8.33, 8.67, 9.0],
    "detajj": [1.0, 1.17, 1.33, 1.5, 1.67, 1.83, 2.0, 2.17, 2.33, 2.5, 2.67, 2.83, 3.0, 3.17, 3.33, 3.5, 3.67, 3.83, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.33, 8.67, 9.0, 9.33, 9.67, 10.0],
    "ptjj": [1.0, 1.17, 1.33, 1.5, 1.67, 1.83, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.33, 6.67, 7.0, 7.33, 7.67, 8.0],
    "dphijj": [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.33, 5.67, 6.0, 6.33, 6.67, 7.0],
    "ptW": [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.33, 5.67, 6.0, 6.33, 6.67, 7.0],
    "nJet": [1.0, 1.25, 1.5, 1.75, 2.0, 2.33, 2.67, 3.0, 3.33, 3.67, 4.0],
}

####### multiclass shit, the map_multiclass -> binning is defined in aliases.py so should be available
# for var in ["ptW", "leppt", "lepeta", "nJet", "jet1pt", "jet1eta", "jet2pt", "jet2eta", "detajj", "mjj", "ptjj", "dphijj"]:
for var in ["mjj", "nJet"]:
# for var in ["ptjj"]:
    n_classes = map_multiclass[var]
    variables['MultiClass_{}_3bin'.format(var)] = {'name': 'MultiClass_{}'.format(var),
        'range' : (n_classes * 3, 1., n_classes+1.0), 
        'xaxis' : 'MultiClass_{}'.format(var), 
        'fold' :0 ,
    }
    # variables['MultiClass_{}_1bin'.format(var)] = {'name': 'MultiClass_{}'.format(var),
    #     'range' : (n_classes, 1., n_classes+1.0), 
    #     'xaxis' : 'MultiClass_{}'.format(var),  #   x axis name
    #     'fold' :0 ,
    # }
    # variables['MultiClass_{}_Varbin'.format(var)] = {'name': 'MultiClass_{}'.format(var),
    #     'range' : (n_classes*2, 1., n_classes+1.0), 
    #     'xaxis' : 'MultiClass_{}'.format(var),  #   x axis name
    #     'fold' :0 ,
    # }
    variables['MultiClass_{}_class0'.format(var)] = {'name': 'MultiClass_{}'.format(var),
        # 'range' : (bin_map[var][bin-1],0.,1.), 
        'range' : (1,0.,1.), 
        'xaxis' : 'MultiClass_{}_class0'.format(var),  #   x axis name
        'fold' :0 ,
    }