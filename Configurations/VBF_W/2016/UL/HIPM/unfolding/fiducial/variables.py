

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        }

variables['high0p5events'] = {   'name': 'mjj:DNNJoined',            #   variable name    
                            'range' : (1,0.5,1.,1,0.,100000.),    #   variable range
                            'xaxis' : 'DNNoutput : events [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['high0p8events'] = {   'name': 'mjj:DNNJoined',            #   variable name    
                            'range' : (1,0.8,1.,1,0.,100000.),    #   variable range
                            'xaxis' : 'DNNoutput : events [GeV]',  #   x axis name
                            'fold' :2 ,
                        }

variables['DNN0p5Joined5'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (5,0.5,1.),     #   variable range
                            'xaxis' : 'DNNoutput',  #   x axis name
                            'fold' :0 ,
                        }

variables['DNN0p5Joined10'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (10,0.5,1.),     #   variable range
                            'xaxis' : 'DNNoutput',  #   x axis name
                            'fold' :0 ,
                        }

variables['DNN0p5oined20'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (20,0.5,1.),     #   variable range
                            'xaxis' : 'DNNoutput',  #   x axis name
                            'fold' :0 ,
                        }

variables['DNN0p8Joined5'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (4,0.8,1.),     #   variable range
                            'xaxis' : 'DNNoutput',  #   x axis name
                            'fold' :0 ,
                        }

variables['DNN0p8Joined10'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (8,0.8,1.),     #   variable range
                            'xaxis' : 'DNNoutput',  #   x axis name
                            'fold' :0 ,
                        }

