# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py
#
structure['sm']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
############################
op = ["cW", "cHDD", "cHW", "cHWB", "cHbox", "cHj1", "cHj3", "cHl1", "cHl3", "cll1", "cjj11", "cjj31", "cjj18", "cjj38"]
#op = ["cW", "cHbox"]
# the following (ls) contains the operators in the same order as in the LHEReweightingWeight vector
ls = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38']
# the following (mix) contains all the operators with mixed terms as well, in the LHEReweightingWeight order
mix = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38', 'cW_cHDD', 'cW_cHW', 'cW_cHWB', 'cW_cHbox', 'cW_cHj1', 'cW_cHj3', 'cW_cHl1', 'cW_cHl3', 'cW_cll1', 'cW_cjj11', 'cW_cjj31', 'cW_cjj18', 'cW_cjj38', 'cHDD_cHW', 'cHDD_cHWB', 'cHDD_cHbox', 'cHDD_cHj1', 'cHDD_cHj3', 'cHDD_cHl1', 'cHDD_cHl3', 'cHDD_cll1', 'cHDD_cjj11', 'cHDD_cjj31', 'cHDD_cjj18', 'cHDD_cjj38', 'cHW_cHWB', 'cHW_cHbox', 'cHW_cHj1', 'cHW_cHj3', 'cHW_cHl1', 'cHW_cHl3', 'cHW_cll1', 'cHW_cjj11', 'cHW_cjj31', 'cHW_cjj18', 'cHW_cjj38', 'cHWB_cHbox', 'cHWB_cHj1', 'cHWB_cHj3', 'cHWB_cHl1', 'cHWB_cHl3', 'cHWB_cll1', 'cHWB_cjj11', 'cHWB_cjj31', 'cHWB_cjj18', 'cHWB_cjj38', 'cHbox_cHj1', 'cHbox_cHj3', 'cHbox_cHl1', 'cHbox_cHl3', 'cHbox_cll1', 'cHbox_cjj11', 'cHbox_cjj31', 'cHbox_cjj18', 'cHbox_cjj38', 'cHj1_cHj3', 'cHj1_cHl1', 'cHj1_cHl3', 'cHj1_cll1', 'cHj1_cjj11', 'cHj1_cjj31', 'cHj1_cjj18', 'cHj1_cjj38', 'cHj3_cHl1', 'cHj3_cHl3', 'cHj3_cll1', 'cHj3_cjj11', 'cHj3_cjj31', 'cHj3_cjj18', 'cHj3_cjj38', 'cHl1_cHl3', 'cHl1_cll1', 'cHl1_cjj11', 'cHl1_cjj31', 'cHl1_cjj18', 'cHl1_cjj38', 'cHl3_cll1', 'cHl3_cjj11', 'cHl3_cjj31', 'cHl3_cjj18', 'cHl3_cjj38', 'cll1_cjj11', 'cll1_cjj31', 'cll1_cjj18', 'cll1_cjj38', 'cjj11_cjj31', 'cjj11_cjj18', 'cjj11_cjj38', 'cjj31_cjj18', 'cjj31_cjj38', 'cjj18_cjj38']

for o in op:
    ip = ls.index(o)
    im = ls.index(o+'_m1')
    structure['quad_'+o] = {
                  'isSignal' : 1,
                  'isData'   : 0
    }
    structure['sm_lin_quad_'+o] = {
                  'isSignal' : 1,
                  'isData'   : 0
    }

for i in range(len(op)):
    for j in range(len(op)):
        if j > i:
            term = op[i]+'_'+op[j]
            structure['sm_lin_quad_mixed_'+term] = {
                  'isSignal' : 1,
                  'isData'   : 0
            }
############################
structure['WZ_EWK']  = {
                  'isSignal' : 0, # boh 
                  'isData'   : 0
                  }
structure['WpWp_QCD']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['WZ_QCD']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['ZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['tVx']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['Vg']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['VgS1_H']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['VgS1_L']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['WW']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['Top']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['DY']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['Higgs']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['DPS']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['VVV']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

#Fake
structure['Fake_lep']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }
structure['Fake_lep_m']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }
structure['Fake_lep_e']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

# data
structure['DATA']  = {
                  'isSignal' : 0,
                  'isData'   : 1
              }



