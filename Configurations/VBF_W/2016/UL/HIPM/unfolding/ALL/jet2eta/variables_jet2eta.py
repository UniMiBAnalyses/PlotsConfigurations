variables["events"] = {'fold': 3, 'range': (1, 0, 2), 'name': '1', 'xaxis': 'events'}
variables["high0p5events"] = {'fold': 2, 'range': (1, 0.5, 1.0, 1, 0.0, 10000.0), 'name': 'ptjj:DNNJoined', 'xaxis': 'DNNoutput : events [GeV]'}
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