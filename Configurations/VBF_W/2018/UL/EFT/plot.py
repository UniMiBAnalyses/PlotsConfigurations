# plot configuration

from ROOT import TColor
from itertools import product

# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used

colors = {
    # https://root.cern.ch/doc/master/classTColor.html#C02
    'kWhite'   : 0,
    'kBlack'   : 1,
    'kGray'    : 920,
    'kRed'     : 632,
    'kGreen'   : 416,
    'kBlue'    : 600,
    'kYellow'  : 400,
    'kMagenta' : 616,
    'kCyan'    : 432,
    'kOrange'  : 800,
    'kSpring'  : 820,
    'kTeal'    : 840,
    'kAzure'   : 860,
    'kViolet'  : 880,
    'kPink'    : 900, 
}

palette = {
    "FerrariRed": (255,40,0), #ff2800
    "Orange": (242, 108, 13), #f26c0d  
    "Yellow": (247, 195, 7), #f7c307
    "LightBlue": (153, 204, 255), #99ccff
    "MediumBlue": (72, 145, 234),  #4891ea
    "MediumBlue2": (56, 145, 224),    #3891e0
    "DarkBlue": (8, 103, 136), #086788
    "Green": (47, 181, 85), #2fb555
    "Green2": (55, 183, 76),  #37b74c
    "Green3": (16,235,52),#10eb34
    "Green4": (68, 175, 105), #44af69
    "Green5": (29,194,106),#1DC26A
    "Green6" : (27,177,97), #1BB161
    "Green7": (108, 198, 140), # 6CC68C
    "GreenLighter": (93, 192, 128),  #5DC080
    "GreenDarker": (14, 150, 78), # 14, 150, 78
    "LightGreen" : (82, 221, 135), #52dd87
    "Violet": (242, 67, 114), #f24372  
    "Pink": (247, 191, 223), #F7BFDF,
    "Peach": (255, 143, 133), #F7C59F
    "Peach2": (255, 146, 51), #FF9233
    "Peach3": (255, 157, 71), #
    "Pink2" : (253, 161, 155), #FD9BA1
    "Orange": (255,156, 51), #ff9c33
    "Orange2": (255,135, 31)
}

'''
    "Wjets_deta5": (247, 155, 7),#f79b07
    "Wjets_deta4": (247, 175, 7), #f7af07
    "Wjets_deta3": (247, 195, 7), #f7c307
    "Wjets_deta2": (247, 215, 7), #f7d707
    "Wjets_deta1": (247, 235, 7), #f7eb07
'''

jetbin_detabins = [3,3,2]
#wjets_palette = ['#FFF59D', '#FFEE58', '#FFD54F', '#FFB300', '#FF8F00', '#F57C00', '#E65100','#BF360C']
# wjets_palette = ['#DD2C00', '#FF3D00',  '#FF6D00','#F57C00', '#FFAB00', '#FFC400', '#FFEA00', '#FFFF00']
##fai una palette con verde chiaro, verde scuro, viola, rosa, arancione, giallo, nero
wjets_palette = ['#10eb34', '#37b74c', '#f24372', '#f7bfdf', '#ff9c33', '#b9f807', '#000000']



# wjets_bins = []
# for ir in range(1,7):
#     wjets_bins.append("Wjets_HT_res_"+str(ir))
# for ir in range(1,6):
#     wjets_bins.append("Wjets_HT_boost_"+str(ir))

# groupPlot['bkg'] = {
#     'nameHR': 'bkg',
#     'isSignal': 0,
#     'color': colors['kAzure']-9,
#     'samples': ['VV', 'VVV', 'VBS', 'VBF-Z', 'Vg', 'VgS', 'DY_M-50', 'DY_else', 'top', 'Wjets_HT_hardJets', 'Wjets_HT_PUJets', 'Fake']
# }


# groupPlot['Higgs']  = {  
#                 'nameHR' : "Higgs",
#                 'isSignal' : 0,
#                 'color'    : colors['kWhite'],
#                 'samples'  : ['Higgs'],
#                 'fill': 1001
#               }

# groupPlot['VV+VVV+VBS']  = {  
#                 'nameHR' : 'VV+VVV+VBS',
#                 'isSignal' : 0,
#                 'color': palette["Violet"], #palette["Peach3"],  
#                 'samples'  : ['VVV', 'VV','VBS'],
#                 'fill': 1001
#               }
              
# groupPlot['Others']  = {  
#                 'nameHR' : "Others",
#                 'isSignal' : 0,
#                 'color'    : palette["Orange"],
#                 'samples'  : ['VBF-Z', 'Vg', 'VgS'],
#                 'fill': 1001
#               }

# groupPlot['DY_else']  = {  
#                 'nameHR' : "DY_else",
#                 'isSignal' : 0,
#                 'color'    : palette["Pink"],
#                 'samples'  : ['DY_else'],
#                 'fill': 1001
#               }   

# groupPlot['DY_M-50']  = {  
#                 'nameHR' : "DY_M-50",
#                 'isSignal' : 0,
#                 'color'    : palette["DarkBlue"],
#                 'samples'  : ['DY_M-50'],
#                 'fill': 1001
#               }            

# groupPlot['Top']  = {  
#                 'nameHR' : "Top",
#                 'isSignal' : 0,
#                 'color':palette["GreenDarker"],# palette["Green5"],    #Green2
#                 'samples'  : ['top' ],
#                 'fill': 1001
#             }

# groupPlot['Wjets_HT_hardJets']  = {  
#                 'nameHR' : 'WJets_hardJets',
#                 'isSignal' : 0,
#                 'color':   palette["Yellow"],
#                 'samples'  : ['Wjets_HT_hardJets'],
#                 'fill': 1001
#                 }

# groupPlot['Wjets_HT_PUJets']  = {  
#                 'nameHR' : 'WJets_PUJets',
#                 'isSignal' : 0,
#                 'color':   palette["MediumBlue"],
#                 'samples'  : ['Wjets_HT_PUJets'],
#                 'fill': 1001
#                 }

# groupPlot['Fake']  = {  
#                'nameHR' : "Non-prompt",
#                'isSignal' : 0,
#                'color': palette["LightBlue"],   
#               'samples'  : ['Fake'],
#               'fill': 1001
#           }

# groupPlot['sm']  = {  
#                'nameHR' : "sm/20",
#             #    'nameHR' : "sm/1000",
#                'isSignal' : 2,
#                'color': palette["LightBlue"],   
#               'samples'  : ['sm'],
#               'fill': 1001
#           }

cHl3 = [c for c in samples if "quad_cHl3" in c or "lin_cHl3" in c]
cll1 = [c for c in samples if "quad_cll1" in c or "lin_cll1" in c]
mixed = [c for c in samples if "mixed_cHl3_cll1" in c or "mixed_cll1_cHl3" in c]
uno = [c for c in cHl3 + cll1 if "sm_lin_quad" not in c]

cHWB = [c for c in samples if "quad_cHWB" in c or "lin_cHWB" in c]
cHDD = [c for c in samples if "quad_cHDD" in c or "lin_cHDD" in c]
mixed = [c for c in samples if "mixed_cHWB_cHDD" in c or "mixed_cHDD_cHWB" in c]
due = [c for c in cHWB + cHDD + mixed if "sm_lin_quad" not in c and "til" not in c]

for i,s in enumerate(due):
    groupPlot['{}'.format(s)] = {
                'nameHR' : '{}'.format(s),
                'isSignal' : 0,
                'color':   wjets_palette[i],
                'samples'  : [s],
                'fill': 1001
                }


#plot = {}

# keys here must match keys in samples.py

for i,s in enumerate(due):
    plot['{}'.format(s)] = {   
                    'color': colors['kAzure']-1,
                    'isSignal' : 1,
                    'isData'   : 0, 
                    'scale'    : 1.              
                }

# plot['Wjets_HT_hardJets'] = {   
#                  'color': colors['kAzure']-1,
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                 }

# plot['Wjets_HT_PUJets'] = {   
#                  'color': colors['kAzure']-1,
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0
#                 }

# plot['top'] = {   
#                  'color': colors['kAzure']-1,
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0 
#                  }
    
# plot['VV']  = {
#                   'color': colors['kGreen']+3,  
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.   ,
#               }   
    
# plot['VBS']  = { 
#                   'color': colors["kAzure"]-3,    
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.0
#                   }


# plot['Higgs'] = {   
#                  'color': colors['kAzure']-1,
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0 
#                 }
    
# plot['DY_M-50']  = {  
#                 'color': colors['kMagenta']+1,
#                 'isSignal' : 0,
#                 'isData'   : 0, 
#                 'scale'    : 1.0,
#             }

# plot['DY_else']  = {  
#                 'color': colors['kMagenta']+1,
#                 'isSignal' : 0,
#                 'isData'   : 0, 
#                 'scale'    : 1.0,
#             }

# plot['VBF-Z']  = {
#                   'color': colors['kYellow']+3,  
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.   ,
#               }

# plot['Vg']  = {
#                   'color': colors['kGreen']+3,  
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.   ,
#               }   

# plot['VgS'] = {   
#                  'color': colors['kAzure']-1,
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0 
#                 }

# plot['VVV'] = {   
#                  'color': colors['kAzure']-1,
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0 
#                 }


# plot['Fake'] = {   
#                 'color': colors['kAzure']-1,
#                 'isSignal' : 0,
#                 'isData'   : 0, 
#                 'scale'    : 1.              
#                }

# plot['sm'] = {   
#                 'color': colors['kAzure']-1,
#                 'isSignal' : 0,
#                 'isData'   : 0, 
#                 'scale'    : 0.05,              
#                 # 'scale'    : 0.0001,              
#                }



# plot['DATA']  = { 
#                   'nameHR' : 'Data',
#                   'color': 1 ,  
#                   'isSignal' : 0,
#                   'isData'   : 1 ,
#                   'isBlind'  : 0
#               }


# additional options

legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
