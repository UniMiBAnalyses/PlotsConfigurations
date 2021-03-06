# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    

## Reducible Bkg
structure['ChMisId']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['ttbar'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['ZZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['WZ_strong']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['DPS']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0,
                  #'removeFromCuts' : ['hww2l2v_13TeV_dytt_of2j_vbf'],
                  } 
##Irreducible Bkg

structure['WW_strong']  = {
                      'isSignal' : 0,
                      'isData'   : 0
                      }

##Signal

structure['WpWp_EWK']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }

structure['WmWm_EWK']  = {
                      'isSignal' : 1,
                      'isData'   : 0
                      }
                      
structure['WZ_EWK']  = { 
                  'isSignal' : 1,
                  'isData'   : 0 
                  }

#Fake
structure['Fake_lep']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
              }

structure['DY_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['lep_TT_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['singleTop_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['singleAntiTop_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['ggWWTo2L2Nu_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['WWTo2L2Nu_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Vg_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['ZZ_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['WpWpJJ_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['WmWmJJ_promptSubtr']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['WpWpJJ_QCD_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['VVV_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['DPS_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['WZ_promptSubtr']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }
# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }







