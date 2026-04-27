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
variables["events"] = {'fold': 3, 'range': (1, 0, 2), 'name': '1', 'xaxis': 'events'}
variables["high0p5events"] = {'fold': 2, 'range': (1, 0.5, 1.0, 1, 0.0, 10000.0), 'name': 'ptjj:DNNJoined', 'xaxis': 'DNNoutput : events [GeV]'}
variables["high0p5DNN1ptW3_cut"] = {'fold': 2, 'range': ([0.5, 1.0], [0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 140.0, 155.0, 180.0, 235.0, 307.0, 10000.0]), 'name': 'ptW:DNNJoined', 'xaxis': 'DNNoutput : pT_{W} [GeV]'}
