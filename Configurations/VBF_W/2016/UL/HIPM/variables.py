

##############################################
# now variables to plot
# Include also variables to be plotted

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}


variables['Dphijet1jet2PU']  = {   'name': 'Dphijet1jet2',     
                        'range' : (15, 0.,3.14),   
                        'xaxis' : ' Delta phi{J1, J2}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
                        }

variables['Dphilep1metPU']  = {   'name': 'Dphilep1met',     
                        'range' : (15, 0.,3.14),   
                        'xaxis' : 'Delta phi{l1, MET}PU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
                        }


variables['DNNJoinedDphijet1jet2PU'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
                            'range' : (5,0.,1.,5,0.,3.14),    #   variable range
                            'xaxis' : 'DNNoutput : Dphijet1jet2 [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }


variables['DNNJoinedDphijet1jet2PU2'] = {   'name': 'Dphijet1jet2:DNNJoined',            #   variable name    
                            'range' : (10,0.,1.,5,0.,3.14),   #   variable range
                            'xaxis' : 'DNNoutput : Dphijet1jet2 [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }



variables['DNNJoined'] = {   'name': 'DNNJoined',            #   variable name    
                            'range' : (10,0.,1.),     #   variable range
                            'xaxis' : 'DNNoutput',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }


  


# ######## lepton 1 ##########


variables['puppimet_phi']  = {  'name': 'PuppiMET_phi',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : 'phi MET',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full',
                            }
                        }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (40,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold' : 3,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }


variables['ptW']  = {   'name': 'ptW',     
                        'range' : (30,0,300),   
                        'xaxis' : 'pT(W) [GeV]',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
                        }


variables['jetpt1']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (70,40,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt1PU']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (20,40,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }


variables['detajj'] = {   'name': 'detajj',            #   variable name    
                            'range' : (40,2,10.),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }

variables['mjj'] = {   'name': 'mjj',            #   variable name    
                            'range' : (27,300.,3000.),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }

variables['R'] = {   'name': 'R_AN',     
                        'range' : (50,0,1),   
                        'xaxis' : 'R_AN',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}

variables['RPU'] = {   'name': 'R_AN',     
                        'range' : (20,0,1),   
                        'xaxis' : 'R_ANPU',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}


variables['leppt'] = {   'name': 'Lepton_pt[0]',            #   variable name    
                            'range' : (35,0,200),    #   variable range
                            'xaxis' : 'p_{T} lepton [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }   

variables['lepeta'] = {   'name': 'Lepton_eta[0]',            #   variable name    
                            'range' : (20,-2.5,2.5),    #   variable range
                            'xaxis' : 'Lepton eta',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }   

variables['lepphi'] = {   'name': 'Lepton_phi[0]',            #   variable name    
                            'range' : (20,-3.14,3.14),    #   variable range
                            'xaxis' : 'Lepton phi',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full', 
                              'mu_SR' : 'full', 
                            }
                        }   


variables['Zl1bin3'] = {   'name': 'Zl1',     
                        'range' : (60,-5,5),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}

variables['Zl1bin4'] = {   'name': 'Zl1',     
                        'range' : (20,-5,5),   
                        'xaxis' : 'Zl1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}


variables['leppt_eta'] = {   'name': 'Lepton_pt[0]:Lepton_eta[0]',       #   variable name    
                            'range' : ([-2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2.],[25., 30., 35., 40., 45., 60., 75., 120., 200.],),    #   variable range
                            'xaxis' : 'Lepton_pt : Lepton_eta [GeV]',  #   x axis name
                            'fold' :0 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }




###### jet 1 #########

variables['jetphi1'] = {   'name': 'CleanJet_phi[0]',     
                        'range' : (20,-3.14,3.14),   
                        'xaxis' : '#Phi J1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}

variables['jeteta1'] = {   'name': 'CleanJet_eta[0]',     
                        'range' : (20,-4.7,4.7),   
                        'xaxis' : '#eta J1',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}

variables['jetphi2'] = {   'name': 'CleanJet_phi[1]',     
                        'range' : (20,-3.14,3.14),   
                        'xaxis' : '#Phi J2',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}

variables['jeteta2'] = {   'name': 'CleanJet_eta[1]',     
                        'range' : (20,-4.7,4.7),   
                        'xaxis' : '#eta J2',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }
}


variables['jetpt2']  = {
                        'name': 'CleanJet_pt[0]',
                        'range' : (50,30,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        'blind': {
                           'ele_SR' : 'full', 
                           'mu_SR' : 'full', 
                         }   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }



  