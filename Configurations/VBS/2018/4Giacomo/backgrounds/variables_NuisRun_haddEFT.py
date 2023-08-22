# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['events']  = {   'name': '1',
'range' : (1,0,2),
'xaxis' : 'events',
'fold' : 3
}


variables['nJet']  = {   'name': 'nJet',
                         'range' : (6,0,6),
                         'xaxis' : 'njets',
                         'fold' : 3
                         }
variables['nJet_v2']  = {   'name': 'Sum$(CleanJet_pt>30)',
                            'range' : (4,0,4),
                            'xaxis' : 'njets',
                            'fold' : 3
                            }


variables['nLepton'] =  {
    'name': '1*(Alt$(Lepton_pt[0],0.)>20) + 1*(Alt$(Lepton_pt[1],0.)>20) + 1*(Alt$(Lepton_pt[2],0.)>20)+ 1*(Alt$(Lepton_pt[3],0.)>20) + 1*(Alt$(Lepton_pt[4],0.)>20)',
    'range': (5,0,5),
    'xaxis': '# leptons',
    'fold': 3
}

variables['mtw1']  = {   'name': 'mtw1',            #   variable name
                         'range' : ([10,20,30,40,50,60,70.75,80,85,90,100,110,120],),    #   variable range
                         'xaxis' : 'mtw1 [GeV]',  #   x axis name
                         'fold' : 3
                         }
    
variables['mtw2']  = {   'name': 'mtw2',            #   variable name
                         'range' : ([10,20,30,40,50,60,70.75,80,85,90,100,110,120],),    #   variable range
                         'xaxis' : 'mtw2 [GeV]',  #   x axis name
                         'fold' : 3
                         }

variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (15,50,300),
                           'xaxis' : 'p_{T} 1st clean jet',
                           'fold'  : 3
                           }

variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (15,50,300),
                           'xaxis' : 'p_{T} 2nd clean jet',
                           'fold'  : 3
                           }
variables['jetpt1_v2']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (30,50,300),
                           'xaxis' : 'p_{T} 1st clean jet',
                           'fold'  : 3
                           }

variables['jetpt2_v2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (30,50,300),
                           'xaxis' : 'p_{T} 2nd clean jet',
                           'fold'  : 3
                           }

variables['jetpt1_v3']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (10,50,400),
                           'xaxis' : 'p_{T} 1st clean jet',
                           'fold'  : 3
                           }

variables['jetpt2_v3']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (10,50,350),
                           'xaxis' : 'p_{T} 2nd clean jet',
                           'fold'  : 3
                           }


variables['met']  = {   'name': 'MET_pt',            #   variable name
                        'range' : (10,0,200),    #   variable range
                        'xaxis' : 'pfmet [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['etaj1'] = {  'name': 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'etaj1 cleanj',
                        'fold': 3
                        }

variables['etaj2'] = {         'name': 'Alt$(CleanJet_eta[1],-9999.)',
                               'range': (10,-5,5),
                               'xaxis': 'etaj2 cleanj',
                               'fold': 3
                               }

variables['etal1'] = {  'name': 'Alt$(Lepton_eta[0],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'etal1',
                        'fold': 3
                        }
variables['etal2'] = {         'name': 'Alt$(Lepton_eta[1],-9999.)',
                               'range': (10,-5,5),
                               'xaxis': 'etal2',
                               'fold': 3
                               }
variables['etal1_v2'] = {  'name': 'Alt$(Lepton_eta[0],-9999.)',
                        'range': (20,-5,5),
                        'xaxis': 'etal1',
                        'fold': 3
                        }
variables['etal2_v2'] = {         'name': 'Alt$(Lepton_eta[1],-9999.)',
                               'range': (20,-5,5),
                               'xaxis': 'etal2',
                               'fold': 3
                               }

variables['phij1'] = {  'name': 'Alt$(CleanJet_phi[0],-9999.)',
                        'range': (10,-3.15,3.15),
                        'xaxis': 'phij1 cleanj',
                        'fold': 3
                        }
variables['phij2'] = {  'name': 'Alt$(CleanJet_phi[1],-9999.)',
                        'range': (10,-3.15,3.15),
                        'xaxis': 'phij2 cleanj',
                        'fold': 3
                        }
variables['phil1'] = {  'name': 'Alt$(Lepton_phi[0],-9999.)',
                        'range': (10,-3.15,3.15),
                        'xaxis': 'phil1',
                        'fold': 3
                        }
variables['phil2'] = {  'name': 'Alt$(Lepton_phi[1],-9999.)',
                        'range': (10,-3.15,3.15),
                        'xaxis': 'phil2',
                        'fold': 3
                        }


variables['Zlep1']  = {  'name': '(Alt$(Lepton_eta[0],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{1}',
                         'fold': 3
                         }

variables['Zlep2']  = {  'name': '(Alt$(Lepton_eta[1],-9999.) - (Alt$(Jet_eta[0],-9999.)+Alt$(Jet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{2}',
                         'fold': 3
                         }

variables['detall']  = {  'name': 'detall',
                          'range': (16,0.0,8.0),
                          'xaxis': 'detall',
                          'fold': 3,
                          #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                          #'blind': { c:[0,8] for c in cuts if "ssww_tri_tauVeto" in c}
                          }
variables['dphijj']  = {  'name': 'dphijj',
                          'range': (16,0.0,8.0),
                          'xaxis': 'dphijj',
                          'fold': 3,
                          #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                          #'Blind': { c:[0,8] for c in cuts if "ssww_tri_tauVeto" in c}
                          }
variables['dphill']  = {  'name': 'dphill',
                          'range': (16,0.0,8.0),
                          'xaxis': 'dphill',
                          'fold': 3,
                          #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                          #'blind': { c:[0,8] for c in cuts if "ssww_tri_tauVeto" in c}
                          }


###############################################################################
variables['mjj']  = {  'name': 'mjj', # for comparison with paper (ww)
                       'range': ([500,650,800, 1000,1200, 1500, 1800, 2300, 3000],),
                       'xaxis': 'mjj [GeV]',
                       #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                       'fold': 3,
                       #'blind': { c:[1200,3000] for c in cuts if "ssww_tri_tauVeto" in c}
                       }
variables['mjj_v2']  = {  'name': 'mjj', # I used it at some point for 1D fitting but the previous one looks better
                          'range': ([500,800,1200,1500,1800,2200,2600,3000],), 
                          'xaxis': 'mjj [GeV]',
                          #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                          'fold': 3,
                          #'blind': { c:[1200,3000] for c in cuts if "ssww_tri_tauVeto" in c}
                          }
variables['mjj_v3']  = {  'name': 'mjj', # for comparison with paper (btag cr)
                          'range': ([500,800,1200,1800,3000],),
                          'xaxis': 'mjj [GeV]',
                          'fold': 3,
                          #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                          #'blind': { c:[1200,3000] for c in cuts if "ssww_tri_tauVeto" in c}
                          }

variables['mll']  = {   'name': 'mll',
                        'range' : ([20,80,140,240,500],),
                        'xaxis' : 'mll [GeV]',
                        'fold' : 3,
                        }
variables['mll_zwindow']  = {   'name': 'mll',
                                'range' : ([20,60,120,140,240,500],),
                        'xaxis' : 'mll [GeV]', 
                        'fold' : 3,
                        }
variables['mll_zwindow_v2']  = {   'name': 'mll',
                                'range' : ([20,60,120,140,240,400,500],),
                        'xaxis' : 'mll [GeV]', 
                        'fold' : 3,
                        }

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : ([20,50,70,80,100,120,150,200,300],),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3,
                        #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                        #'blind': { c:[20,300] for c in cuts if "ssww_tri_tauVeto" in c}
                        }
variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : ([20,50,70,80,100,120,150,200,300],),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3,
                        #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                        #'blind': { c:[20,300] for c in cuts if "ssww_tri_tauVeto" in c}
                        }

variables['detajj']  = {  'name': 'detajj',
                          'range': (16,0.0,8.0),
                          'xaxis': 'detajj',
                          'fold': 3,
                          #'cuts': ['ssww_tri_tauVeto','ssww_tri_btag_tauVeto'],
                          #'blind': { c:[0,8] for c in cuts if "ssww_tri_tauVeto" in c}
                          }

variables['mll_mjj']  = {   'name': 'mll:mjj',
                            'range' : ([500,800,1200,1800,3000],[20,80,140,240,600]),
                            'xaxis' : 'mll:mjj [GeV]',
                            'fold' : 3,
                            'doWeight' : 1,
                            'binX'     : 4,
                            'binY'     : 4
                            }
variables['mll_mjj_v2']  = {   'name': 'mll:mjj', # same as the paper for 2D fitting
                               'range' : ([500,650,800, 1000,1200, 1500, 1800, 2300, 3000],[20,80,140,240,600]),
                               'xaxis' : 'mll:mjj [GeV]',
                               'fold' : 3,
                               'doWeight' : 1,
                               'binX'     : 4,
                               'binY'     : 4
                               }

variables['mjj_detajj']  = {   'name': 'mjj:detajj',
                               'range' : ([2.5,4,5,8],[500,1000,1500,2000,3500]),
                            'xaxis' : 'mjj:detajj [GeV]',
                            'fold' : 3,
                            }


###############################################################################


#variables = {k:v for k,v in variables.items() if k in ["events", "mjj", "pt2", "pt1", "mll", "detajj", "mtw1", "mtw2"]} #["events", "mjj", "pt2", "pt1", "mll", "detajj", "mtw1", "mtw2"]
#variables = {k:v for k,v in variables.items() if k in ['events', 'mjj', 'mjj_v2', 'mll_mjj', 'mll_mjj_v2','mjj_detajj']}
# variables = {k:v for k,v in variables.items() if k in ['events', 'mjj', 'mjj_v2', 'mjj_v3', 'mll', 'pt1', 'pt2', 'detajj', 'mll_mjj', 'mll_mjj_v2', 'mjj_detajj']}
#variables = {k:v for k,v in variables.items() if k in ['events', 'mjj', 'mjj_v2', 'mjj_v3', 'mll','mll_zwindow','mll_zwindow_v2', 'pt1', 'pt2','jetpt1','jetpt2','jetpt1_v2','jetpt2_v2','jetpt1_v3','jetpt2_v3','etaj1','etaj2','detajj','detall','dphijj','dphill', 'mll_mjj','etal1','etal2','etal1_v2','etal2_v2','phil1','phil2','phij1','phij2','mll_mjj_v2', 'mjj_detajj']}
variables = {k:v for k,v in variables.items() if k in ['mjj_v3', 'mll_mjj_v2']}
