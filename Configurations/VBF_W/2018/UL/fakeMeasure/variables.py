##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        }

variables['DNN1']  = {   'name': 'DNNJoined',      
                        'range' : (1,0.,0.25),  
                        'xaxis' : 'events', 
                        'fold' : 0,
}

variables['DNN2']  = {   'name': 'DNNJoined',      
                        'range' : (1,0.25,0.5),  
                        'xaxis' : 'events', 
                        'fold' : 0,
}

variables['DNN3']  = {   'name': 'DNNJoined',      
                        'range' : (1,0.5,0.75),  
                        'xaxis' : 'events', 
                        'fold' : 0,
}

variables['DNN4']  = {   'name': 'DNNJoined',      
                        'range' : (1,0.75,1.),  
                        'xaxis' : 'events', 
                        'fold' : 0,
}


variables['leppt_eta'] = {   'name': 'Lepton_pt[0]:Lepton_eta[0]',       #   variable name    
                            'range' : ([-2.5, -2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.,2.5],[25., 30., 35., 40., 45., 60., 75., 120., 200.],),    #   variable range
                            'xaxis' : 'Lepton_pt : Lepton_eta [GeV]',  #   x axis name
                            'fold' :0 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['leppt_eta_DNN1'] = {   'name': 'DNNJoined:Lepton_pt[0]:Lepton_eta[0]',       #   variable name    
                            'range' : ([-2.5, -2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.,2.5],[25., 30., 35., 40., 45., 60., 75., 120., 200.],[0.,0.25],),    #   variable range
                            'xaxis' : 'DNN : Lepton_pt : Lepton_eta [GeV]',  #   x axis name
                            'fold' :0 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['leppt_eta_DNN2'] = {   'name': 'DNNJoined:Lepton_pt[0]:Lepton_eta[0]',       #   variable name    
                            'range' : ([-2.5, -2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.,2.5],[25., 30., 35., 40., 45., 60., 75., 120., 200.],[0.25,0.5],),    #   variable range
                            'xaxis' : 'DNN : Lepton_pt : Lepton_eta [GeV]',  #   x axis name
                            'fold' :0 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['leppt_eta_DNN3'] = {   'name': 'DNNJoined:Lepton_pt[0]:Lepton_eta[0]',       #   variable name    
                            'range' : ([-2.5, -2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.,2.5],[25., 30., 35., 40., 45., 60., 75., 120., 200.],[0.5,0.75],),    #   variable range
                            'xaxis' : 'DNN : Lepton_pt : Lepton_eta [GeV]',  #   x axis name
                            'fold' :0 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['leppt_eta_DNN4'] = {   'name': 'DNNJoined:Lepton_pt[0]:Lepton_eta[0]',       #   variable name    
                            'range' : ([-2.5, -2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.,2.5],[25., 30., 35., 40., 45., 60., 75., 120., 200.],[0.75,1.0],),    #   variable range
                            'xaxis' : 'DNN : Lepton_pt : Lepton_eta [GeV]',  #   x axis name
                            'fold' :0 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }



variables['mll'] = {   'name': 'mll',     
                        'range' : (50,50,130),   
                        'xaxis' : 'mll',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['mll_DNN1'] = {   'name': 'DNNJoined:mll',     
                        'range' : ([ 50.,  58.,  66.,  74.,  82.,  90.,  98., 106., 114., 122., 130.] , [0., 0.25],), 
                        'xaxis' : 'DNN : mll',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['mll_DNN2'] = {   'name': 'DNNJoined:mll',     
                        'range' : ([ 50.,  58.,  66.,  74.,  82.,  90.,  98., 106., 114., 122., 130.] , [0.25, 0.5],), 
                        'xaxis' : 'DNN : mll',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['mll_DNN3'] = {   'name': 'DNNJoined:mll',     
                        'range' : ([ 50.,  58.,  66.,  74.,  82.,  90.,  98., 106., 114., 122., 130.] , [0.5, 0.75],), 
                        'xaxis' : 'DNN : mll',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}

variables['mll_DNN4'] = {   'name': 'DNNJoined:mll',     
                        'range' : ([ 50.,  58.,  66.,  74.,  82.,  90.,  98., 106., 114., 122., 130.] , [0.75, 1.0],), 
                        'xaxis' : 'DNN : mll',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full',
                           'mu_SR' : 'full'
                         }
}