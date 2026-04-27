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


signals = [c for c in samples if "WLNuJJ" in c and "Out" not in c]
for i in signals:
    structure['{}'.format(i)] = {
                    'isSignal' : 1,
                    'isData'   : 0 
             }

out = [c for c in samples if "WLNuJJ" in c and "Out" in c]
for i in out:
    structure['{}'.format(i)] = {
                    'isSignal' : 0,
                    'isData'   : 0 
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

