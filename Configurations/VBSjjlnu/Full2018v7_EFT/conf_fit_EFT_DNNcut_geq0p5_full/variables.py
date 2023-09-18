##############################################
# now variables to plot
# Include also variables to be plotted
res_cuts = [ c for c in cuts if 'res' in c]
boost_cuts = [ c for c in cuts if 'boost' in c]
sig_cuts =  [ c for c in cuts if 'sig' in c]

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

########################


variables['Mww'] = {   'name': 'Mww',
                        'range' : ([ 200., 400., 600., 800., 1000., 1200., 1500., 2000., 3000.],), #variable range  
                        'xaxis' : 'M_{WV} [GeV]',
                        'fold' : 3,
                        'cuts': sig_cuts,
                        # 'divideByBinWidth': True, 
                        'blind': [200. ,3000.]
                        }


variables['Mww_10'] = {   'name': 'Mww',
                        'range' : ([ 200., 300., 400., 500., 600., 800., 1000., 1200., 1500., 2000., 3000.],), #variable range  
                        'xaxis' : 'M_{WV} [GeV]',
                        'fold' : 3,
                        'cuts': sig_cuts,
                        # 'divideByBinWidth': True, 
                        'blind': [200. ,3000.]
                        }


variables['Mww_14'] = {   'name': 'Mww',
                        'range' : ([ 200., 300., 400., 500., 600., 700., 800., 900., 1000., 1200., 1400., 1600., 2000., 2500., 3000.],), #variable range  
                        'xaxis' : 'M_{WV} [GeV]',
                        'fold' : 3,
                        'cuts': sig_cuts,
                        # 'divideByBinWidth': True, 
                        'blind': [200. ,3000.]
                        }


variables['DNNoutput_res_v1'] = {
    'name': 'DNNoutput_resolved_v1',
    'range': (25,0.,1),
    'xaxis': 'DNN resolved',
    'fold': 3 ,
    'cuts':  res_cuts,
    'divideByBinWidth': True, 
    'blind': { c:[0.6,1] for c in cuts if "_sig_" in c},
}

variables['DNNoutput_boost'] = {
    'name': 'DNNoutput_boosted',
    'range': ([0., 0.05, 0.1, 0.15, 0.20, 0.25, 0.3, 0.35, 0.4, 0.55, 0.7, 0.85, 1.],),
    'xaxis': 'DNN boosted',
    'fold': 3 ,
    'cuts': boost_cuts,
    'divideByBinWidth': True,
    # 'blind': { c:[0.6,1] for c in cuts if "_sig_" in c} ,
}
#####################
#Fit variables

variables['fit_bins_res'] ={  'name' : 'fit_bin_res',
                            'range' : (21,1,22),
                            'xaxis' : 'Wjets resolved bin', 
                            'fold' : 0,
                            'cuts': res_cuts
}   

variables['fit_bins_boost'] ={  'name' : 'w_lep_pt',
                            'range' : ([0,50,100,150,200,300,400,600],),
                            'xaxis' : 'W leptonic Pt', 
                            'fold' : 3,
                            'cuts': boost_cuts
}   


######################


variables['vbs_0_eta'] = {   'name': 'vbs_0_eta',      
                        'range' : (10,-4.7,4.7),  
                        'xaxis' : 'VBS leading jet #eta', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }

variables['vbs_1_eta'] = {   'name': 'vbs_1_eta',      
                        'range' : (10,-4.7,4.7),  
                        'xaxis' : 'VBS trailing jet #eta', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }


variables['vbs_0_phi'] = {   'name': 'vbs_0_phi',      
                        'range' : (10,-3.14,3.14),  
                        'xaxis' : 'VBS leading jet #phi', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }

variables['vbs_1_phi'] = {   'name': 'vbs_1_phi',      
                        'range' : (10,-3.14,3.14),  
                        'xaxis' : 'VBS trailing jet #phi', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }


variables['vbs_0_E'] = {   'name': 'vbs_0_E',      
                        'range' : (10,0,1000),  
                        'xaxis' : 'VBS leading jet E', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }

variables['vbs_1_E'] = {   'name': 'vbs_1_E',      
                        'range' : (10,0,1000),  
                        'xaxis' : 'VBS trailing jet E', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }


#######################

variables['w_lep_pt'] = {   'name': 'w_lep_pt',      
                        'range' :  (10,0,400),  
                        'xaxis' : 'Pt W leptonic', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }


variables['Mtw_lep'] = {   'name': 'Mtw_lep',      
                        'range' :  (10,0,200),  
                        'xaxis' : 'Pt W leptonic', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }

variables['vbs_1_pt_res'] = {   'name': 'vbs_1_pt',      
                        'range' : (10,30,250),  
                        'xaxis' : 'trailing VBS jet pt', 
                        'fold' : 3,
                        'cuts': res_cuts
} 


variables['vbs_1_pt_boost'] = {   'name': 'vbs_1_pt',      
                        'range' : (10,30,200),  
                        'xaxis' : 'trailing VBS jet pt', 
                        'fold' : 3,
                        'cuts':  boost_cuts
                        }   

variables['deltaeta_vbs'] = {   'name': 'deltaeta_vbs',      
                        'range' : (10,2.5,8.5),  
                        'xaxis' : '#Delta#eta VBS jets', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }    

# variables['mjj_vjet_res'] = {   'name': 'mjj_vjet',      
#                         'range' : (15,65,105),  
#                         'xaxis' : 'Whad reco mass', 
#                         'fold' : 3,
#                         'cuts' : [c for c in res_cuts if 'wjetcr' not in c] 
#                         }

# variables['mjj_vjet_boost'] = {   'name': 'mjj_vjet',      
#                         'range' : (10,70,115),  
#                         'xaxis' : 'Whad reco mass', 
#                         'fold' : 3,
#                         'cuts' : [c for c in boost_cuts  if 'wjetcr' not in c] 
#                         }

# variables['mjj_vjet_wjetcr'] = {   'name': 'mjj_vjet',      
#                         'range' : (50,40,250),  
#                         'xaxis' : 'Whad reco mass', 
#                         'fold' : 3,
#                         'cuts' : [c for c in cuts if 'wjetcr' in c]
#                         }

variables['mjj_vbs'] = {   'name': 'mjj_vbs',      
                        'range' : (10,500,3500) , 
                        'xaxis' : 'M_{jj} VBS', 
                        'fold' : 3,
                        'cuts': sig_cuts,
                        #'blind':  { c: [1500,3000] for c in cuts if 'sig' in c} ,
                    }

variables['nJets_res'] = {   'name': 'nJets30',      
                        'range' : (6,4,10),  
                        'xaxis' : 'nJets cleaned from Ak8 >= 30 GeV', 
                        'fold' : 3,
                        'cuts': res_cuts
                        }

variables['nJets_boost'] = {   'name': 'nJets30',      
                        'range' : (6,2,8),  
                        'xaxis' : 'nJets cleaned from Ak8 >= 30 GeV', 
                        'fold' : 3,
                        'cuts':boost_cuts
                        }

variables['Zlep'] = {   'name': 'Zlep',      
                        'range' : (10,-1,1),  
                        'xaxis' : 'Zepp. lepton', 
                        'cuts': sig_cuts,
                        'fold' : 3
                        }

variables['Zvjets_0'] = {   'name': 'Zvjets_0',      
                        'range' : (10,-1,1),  
                        'xaxis' : 'Zepp. lepton', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }

variables['vbs_0_pt'] = {   'name': 'vbs_0_pt',      
                        'range' : (10,50,400),  
                        'xaxis' : 'leading VBS jet pt', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        } 

variables['vjet_0_pt'] = {   'name': 'vjet_0_pt',      
                        'range' : (10,30,180),  
                        'xaxis' : 'leading V-jet pt', 
                        'fold' : 3,
                        'cuts': [c for c in sig_cuts if "res" in c]
                        }
                        
variables['whad_pt_boost'] = {  'name': "w_had_pt",
                                'range': (8, 200, 600),
                                'xaxis': 'W hadronic Pt',
                                'fold': 3 ,
                                'cuts': [c for c in boost_cuts if 'sig' in c]
                            }

variables['vjet_1_pt'] = {   'name': 'vjet_1_pt',      
                        'range' : (10,30,100),  
                        'xaxis' : 'trailing V-jet pt', 
                        'fold' : 3,
                        'cuts': [c for c in sig_cuts if "res" in c]
                        }

variables['deltaphi_vbs'] = {   'name': 'deltaphi_vbs',      
                        'range' : (10,0,3.14),  
                        'xaxis' : '#Delta#phi VBS jets', 
                        'fold' : 3,
                        'cuts': sig_cuts,
                        }

variables['Lepton_eta'] = {   'name': 'Lepton_eta[0]',      
                        'range' : (10,-2.5,2.5),  
                        'xaxis' : 'Lepton #eta', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }

variables['Lepton_pt'] = {   'name': 'Lepton_pt[0]',      
                        'range' : (10,25,400),  
                        'xaxis' : 'Lepton pt', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }   

variables['Centr_ww'] = {   'name': 'Centr_ww',      
                        'range' : (10,-3,3),  
                        'xaxis' : 'W boson centrality', 
                        'fold' : 3,
                        'cuts': sig_cuts
                        }


variables['deltaeta_vjet'] = {   'name': 'deltaeta_vjet',      
                        'range' : (10,0,2),  
                        'xaxis' : '#Delta#eta V jets', 
                        'fold' : 3,
                        'cuts': [c for c in sig_cuts if "res" in c]
                        } 

variables = {i:k for i,k in variables.items() if i in ["Mww", "Mww_10", "Mww_14", "DNNoutput_res_v1", "DNNoutput_boost", "events", "fit_bins_res", "fit_bins_boost"]}
