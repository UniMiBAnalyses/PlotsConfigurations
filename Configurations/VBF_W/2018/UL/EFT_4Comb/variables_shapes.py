

##############################################
# now variables to plot
# Include also variables to be plotted

# variables['events']  = {   'name': '1',      
#                         'range' : (1,0,2),  
#                         'xaxis' : 'events', 
#                         'fold' : 3,
#                         'blind': {
#                            'ele_SR' : 'full', 
#                            'ele_SR_highDNN' : 'full',
#                            'mu_SR' : 'full', 
#                            'mu_SR_highDNN' : 'full'
#                          }
#                         }


# ######## lepton 1 ##########

variables['jetpt1']  = {
                        'name': 'jetpt1',
                        'range' : (20,40,350),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 3,
                        }

variables['Dphilep1metPU']  = {   'name': 'Dphilep1met',     
                        'range' : (15, 0.,3.14),   
                        'xaxis' : '#Delta#phi{l1, MET}PU',
                        'fold' : 3,
                        }

variables['Dphijet1jet2PU']  = {   'name': 'Dphijet1jet2',     
                        'range' : (15, 0.,3.14),   
                        'xaxis' : '#Delta#phi{J1, J2}PU',
                        'fold' : 3,
                        }

variables['DNN1Dphijet1jet2PU'] = {   'name': 'DNNoutputSR_noQGL:Dphijet1jet2',            #   variable name    
                            'range' : (5,0.,3.14,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : Dphijet1jet2 [GeV]',  #   x axis name
                            'fold' :3 ,
                        }

variables['DNN1Dphilep1metPU'] = {   'name': 'DNNoutputSR_noQGL:Dphilep1met',            #   variable name    
                            'range' : (5,0.,3.14,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : Dphilep1met [GeV]',  #   x axis name
                            'fold' :3 ,
                        }

variables['DNNJoinedDphijet1jet2PU'] = {   'name': 'DNNJoined:Dphijet1jet2',            #   variable name    
                            'range' : (5,0.,3.14,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutputJ : Dphijet1jet2 [GeV]',  #   x axis name
                            'fold' :3 ,
                        }

variables['DNNJoinedDphilep1met'] = {   'name': 'DNNJoined:Dphilep1met',            #   variable name    
                            'range' : (5,0.,3.14,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutputJ : Dphilep1met [GeV]',  #   x axis name
                            'fold' :3 ,
                        }