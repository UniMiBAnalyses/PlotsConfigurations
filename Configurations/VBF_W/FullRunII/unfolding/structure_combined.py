# structure configuration for datacard
from itertools import product, chain
#structure = {}

structure['Wjets_HT_hardJets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Wjets_HT_PUJets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['top']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['DY_M-50']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['DY_else']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

# structure['VV']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0
#               }

# structure['VBS']  = { 
#                   'isSignal' : 0,
#                   'isData'   : 0 
#               }

# structure['Higgs']  = { 
#                   'isSignal' : 0,
#                   'isData'   : 0 
#               }

# structure['VBF-Z']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0
#               }

# structure['Vg']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0 
#               }

# structure['VgS']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0 
#               }


# structure['VVV']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0 
#               }

structure['Others']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }


var = "mjj"
n_bins = 8

# Bin di segnale WLNuJJ_mjj1 ... WLNuJJ_mjj8
for i in range(1, n_bins+1):
    s = "WLNuJJ_{}{}".format(var, i)
    structure[s] = {
        'isSignal': 1,
        'isData': 0
    }

# Bin di output WLNuJJ_mjj1Out ... WLNuJJ_mjj8Out
out_s = "WLNuJJ_{}Out".format(var)
structure[out_s] = {
    'isSignal': 0,
    'isData': 0
}

structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }



# data

structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }

