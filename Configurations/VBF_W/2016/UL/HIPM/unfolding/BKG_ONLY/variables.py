

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


# # #### leptons (l, nu, l+nu)

variables['DNN1ptW'] = {   'name': 'DNNoutputSR_noQGL:ptW',            #   variable name    
                            'range' : (10,0.,500.,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : ptW [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1leppt'] = {   'name': 'DNNoutputSR_noQGL:Lepton_pt[0]',            #   variable name    
                            'range' : (10,0,200,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} lepton [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }   

variables['DNN1lepeta'] = {   'name': 'DNNoutputSR_noQGL:lepeta_abs',            #   variable name    
                            'range' : (10,0,2.,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta lepton',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }    


# ######## jets

variables['DNN1jet1pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[0]',            #   variable name    
                            'range' : (10,40.,350.,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 1st jet [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1jet1eta'] = {   'name': 'DNNoutputSR_noQGL:jeteta1_abs',            #   variable name    
                            'range' : (10,0,5.0,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta 1st jet',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1jet2pt'] = {   'name': 'DNNoutputSR_noQGL:CleanJet_pt[1]',            #   variable name    
                            'range' : (10,30.,250.,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : p_{T} 2nd jet [GeV]',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1jet2eta'] = {   'name': 'DNNoutputSR_noQGL:jeteta2_abs',            #   variable name    
                            'range' : (10,0,5.0,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #eta 2nd jet',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }

variables['DNN1ptjj'] = {   'name': 'DNNoutputSR_noQGL:ptjj',            #   variable name    
                            'range' : (10,0.,400.,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                            # 'blind': {
                            #   'ele_SR' : 'full',
                            #   'mu_SR' : 'full'
                            # }
                        }

variables['DNN1mjj'] = {   'name': 'DNNoutputSR_noQGL:mjj',            #   variable name    
                            'range' : (10,300.,3000.,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : m_{jj} [GeV]',  #   x axis name
                            'fold' :3 ,
                            # 'blind': {
                            #   'ele_SR' : 'full',
                            #   'mu_SR' : 'full'
                            # }
                        }


variables['DNN1detajj'] = {   'name': 'DNNoutputSR_noQGL:detajj',            #   variable name    
                            'range' : (10,3.5,10.,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }


variables['DNN1nJet'] = {   'name': 'DNNoutputSR_noQGL:nCleanJet',            #   variable name    
                            'range' : ([1.5, 2.5, 5.5, 10.5],[0., 0.20, 0.40, 0.6, 0.8, 1.],),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :3 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }


variables['DNN1dphijj'] = {   'name': 'DNNoutputSR_noQGL:dphijj',            #   variable name    
                            'range' : (10,0,3.14,5,0.,1.),    #   variable range
                            'xaxis' : 'DNNoutput : #Delta#eta_{jj}',  #   x axis name
                            'fold' :2 ,
                            'blind': {
                              'ele_SR' : 'full',
                              'mu_SR' : 'full'
                            }
                        }


bin_map = {
  'ptW' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'leppt' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'lepeta' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'nJet' : [5,5,2],
  'jet1pt' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'jet1eta' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'jet2pt' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'jet2eta' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'detajj' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'mjj' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'ptjj' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1],
  'dphijj' : [10, 10, 8, 8, 5, 5, 5, 4, 4, 2, 1]
}

####### multiclass shit, the map_multiclass -> binning is defined in aliases.py so should be available
for var in ["ptW", "leppt", "lepeta", "nJet", "jet1pt", "jet1eta", "jet2pt", "jet2eta", "detajj", "mjj", "ptjj", "dphijj"]:
# for var in ["mjj"]:
  for bin in range(1, map_multiclass[var]+1):
      variables['MultiClass_{}_class{}'.format(var,bin)] = {'name': 'MultiClass_{}_class{}'.format(var,bin),
          'range' : (bin_map[var][bin-1],0.,1.), 
          'xaxis' : 'MultiClass_{}_class{}'.format(var,bin),  #   x axis name
          'fold' :3 ,
          'blind': {
            'ele_SR' : 'full',
            'mu_SR' : 'full'
          }
      }