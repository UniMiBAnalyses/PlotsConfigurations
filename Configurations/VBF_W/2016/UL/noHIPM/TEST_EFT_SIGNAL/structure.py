# structure configuration for datacard
from itertools import product, chain
#structure = {}

mc_sm = ["sm", "WLNuJJ", "Wjets_HT_hardJets"]
mc_bkg = [c for c in mc_sm if "sm" not in c]
mc_eft = [c for c in samples if any(substring in c for substring in ["lin", "quad", "mixed"])]
signals = [c for c in samples if "sm" in c and c not in mc_eft]


# structure['Wjets_HT_hardJets']  = {  
#                   'isSignal' : 0,
#                   'isData'   : 0 
#               }

structure['sm']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['WLNuJJ']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }


# # data

structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }


# drop stat uncertainty (autoMCstat) for all 
# EFT components including the sm one

# for eft_sample in mc_eft+signals:
#    structure[eft_sample]["removeStatUnc"] = 1