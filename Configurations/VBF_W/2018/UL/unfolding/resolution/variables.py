

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


variables['ratio_mjj'] = {   'name': 'ratio_mjj',            #   variable name    
                            'range' : (100,0,2),    #   variable range
                            'xaxis' : 'ratio_mjj',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_detajj'] = {   'name': 'ratio_detajj',            #   variable name    
                            'range' : (100,0.9,1.1),    #   variable range
                            'xaxis' : 'ratio_detajj',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_dphijj'] = {   'name': 'ratio_dphijj',            #   variable name    
                            'range' : (100,0.,3),    #   variable range
                            'xaxis' : 'ratio_dphijj',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_ptjj'] = {   'name': 'ratio_ptjj',            #   variable name    
                            'range' : (100,0,3),    #   variable range
                            'xaxis' : 'ratio_ptjj',  #   x axis name
                            'fold' :0,
                        }


variables['ratio_ptj1'] = {   'name': 'ratio_ptj1',            #   variable name    
                            'range' : (100,0,2),    #   variable range
                            'xaxis' : 'ratio_ptj1',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_ptj2'] = {   'name': 'ratio_ptj2',            #   variable name    
                            'range' : (100,0,2),    #   variable range
                            'xaxis' : 'ratio_ptj2',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_etaj1'] = {   'name': 'ratio_etaj1',            #   variable name    
                            'range' : (100,0.9,1.1),    #   variable range
                            'xaxis' : 'ratio_etaj1',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_etaj2'] = {   'name': 'ratio_etaj2',            #   variable name    
                            'range' : (100,0.9,1.1),    #   variable range
                            'xaxis' : 'ratio_etaj2',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_ptl'] = {   'name': 'ratio_ptl',            #   variable name    
                            'range' : (100,0.8,1.2),    #   variable range
                            'xaxis' : 'ratio_ptl',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_etal'] = {   'name': 'ratio_etal',            #   variable name    
                            'range' : (100,0.98,1.02),    #   variable range
                            'xaxis' : 'ratio_etal',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_ptW'] = {   'name': 'ratio_ptW',            #   variable name    
                            'range' : (100,0,3),    #   variable range
                            'xaxis' : 'ratio_ptW',  #   x axis name
                            'fold' :0,
                        }

variables['ratio_nJet'] = {   'name': 'ratio_nJet',            #   variable name    
                            'range' : (4,0,4),    #   variable range
                            'xaxis' : 'ratio_nJet',  #   x axis name
                            'fold' :0,
                        }
