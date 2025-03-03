# structure configuration for datacard
from itertools import product, chain
#structure = {}

mc_eft = ["sm", "sm_lin_quad_cW", "sm_lin_quad_mixed_cW_cHDD", "sm_lin_quad_mixed_cW_cHWB", "sm_lin_quad_mixed_cW_cHj1", "sm_lin_quad_mixed_cW_cHQ1", "sm_lin_quad_mixed_cW_cHj3", "sm_lin_quad_mixed_cW_cWtil", "sm_lin_quad_mixed_cW_cHWBtil", "sm_lin_quad_cHDD", "sm_lin_quad_mixed_cHDD_cHWB", "sm_lin_quad_mixed_cHDD_cHj1", "sm_lin_quad_mixed_cHDD_cHQ1", "sm_lin_quad_mixed_cHDD_cHj3", "sm_lin_quad_mixed_cHDD_cWtil", "sm_lin_quad_mixed_cHDD_cHWBtil", "sm_lin_quad_cHWB", "sm_lin_quad_mixed_cHWB_cHj1", "sm_lin_quad_mixed_cHWB_cHQ1", "sm_lin_quad_mixed_cHWB_cHj3", "sm_lin_quad_mixed_cHWB_cWtil", "sm_lin_quad_mixed_cHWB_cHWBtil", "sm_lin_quad_cHj1", "sm_lin_quad_mixed_cHj1_cHQ1", "sm_lin_quad_mixed_cHj1_cHj3", "sm_lin_quad_mixed_cHj1_cWtil", "sm_lin_quad_mixed_cHj1_cHWBtil", "sm_lin_quad_cHQ1", "sm_lin_quad_mixed_cHQ1_cHj3", "sm_lin_quad_mixed_cHQ1_cWtil", "sm_lin_quad_mixed_cHQ1_cHWBtil", "sm_lin_quad_cHj3", "sm_lin_quad_mixed_cHj3_cWtil", "sm_lin_quad_mixed_cHj3_cHWBtil", "sm_lin_quad_cWtil", "sm_lin_quad_mixed_cWtil_cHWBtil", "sm_lin_quad_cHWBtil", "quad_cW", "quad_cHDD", "quad_cHWB", "quad_cHj1", "quad_cHQ1", "quad_cHj3", "quad_cWtil", "quad_cHWBtil"]

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

structure['VV']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['VBS']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Higgs']  = { 
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

structure['VBF-Z']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['Vg']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['VgS']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }


structure['VVV']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

# structure['WLNuJJ']  = {  
#                   'isSignal' : 1,
#                   'isData'   : 0 
#               }


structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }



# data

structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }


#eft 

# EFTs
for eft_sample in mc_eft:
    structure[eft_sample]  = {  
                    'isSignal' : 1,
                    'isData'   : 0 
                }

# drop stat uncertainty (autoMCstat) for all 
# EFT components except for the sm one

for eft_sample in mc_eft:
   if eft_sample != "sm": structure[eft_sample]["removeStatUnc"] = 1