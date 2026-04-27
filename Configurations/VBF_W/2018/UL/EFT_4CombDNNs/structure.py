# structure configuration for datacard
from itertools import product, chain
#structure = {}

mc_sm = ["sm", "Wjets_HT", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
mc_bkg = [c for c in mc_sm if "sm" not in c]
mc_eft = [c for c in samples if any(substring in c for substring in ["lin", "quad", "mixed"])]
signals = [c for c in samples if "sm" in c and c not in mc_eft]


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

structure['sm']  = {  
                  'isSignal' : 1,
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


# EFTs
for eft_sample in mc_eft:
    structure[eft_sample]  = {  
                    'isSignal' : 1,
                    'isData'   : 0 
                }

# drop stat uncertainty (autoMCstat) for all 
# EFT components including the sm one

for eft_sample in mc_eft+signals:
   structure[eft_sample]["removeStatUnc"] = 1