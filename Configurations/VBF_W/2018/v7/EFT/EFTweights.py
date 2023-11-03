samples['lin_cW'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[3] - LHEReweightingWeight[2])',
    'FilesPerJob': 30,
}}

samples['quad_cW'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[3] + LHEReweightingWeight[2]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cHDD'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[41])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cHWB'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[78])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[56])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[62])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[67])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[71])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[74])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[76])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[78])',
    'FilesPerJob': 30,
}}

samples['mixed_cW_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[78])',
    'FilesPerJob': 30,
}}

samples['lin_cHDD'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[5] - LHEReweightingWeight[4])',
    'FilesPerJob': 30,
}}

samples['quad_cHDD'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[5] + LHEReweightingWeight[4]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cHWB'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[42])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[35])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[36])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[37])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[38])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[39])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[40])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[41])',
    'FilesPerJob': 30,
}}

samples['mixed_cHDD_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[42])',
    'FilesPerJob': 30,
}}

samples['lin_cHWB'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[7] - LHEReweightingWeight[6])',
    'FilesPerJob': 30,
}}

samples['quad_cHWB'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[7] + LHEReweightingWeight[6]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cHWB_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[57])',
    'FilesPerJob': 30,
}}

samples['mixed_cHWB_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[63])',
    'FilesPerJob': 30,
}}

samples['mixed_cHWB_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[68])',
    'FilesPerJob': 30,
}}

samples['mixed_cHWB_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[72])',
    'FilesPerJob': 30,
}}

samples['mixed_cHWB_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[75])',
    'FilesPerJob': 30,
}}

samples['mixed_cHWB_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}}

samples['mixed_cHWB_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[78])',
    'FilesPerJob': 30,
}}

samples['mixed_cHWB_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[78])',
    'FilesPerJob': 30,
}}

samples['lin_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[9] - LHEReweightingWeight[8])',
    'FilesPerJob': 30,
}}

samples['quad_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[9] + LHEReweightingWeight[8]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj1_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[51])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj1_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[52])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj1_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[53])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj1_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[54])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj1_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[55])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj1_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[56])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj1_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[57])',
    'FilesPerJob': 30,
}}

samples['lin_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[11] - LHEReweightingWeight[10])',
    'FilesPerJob': 30,
}}

samples['quad_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[11] + LHEReweightingWeight[10]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ1_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[58])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ1_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[59])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ1_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[60])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ1_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[61])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ1_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[62])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ1_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[63])',
    'FilesPerJob': 30,
}}

samples['lin_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[13] - LHEReweightingWeight[12])',
    'FilesPerJob': 30,
}}

samples['quad_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[13] + LHEReweightingWeight[12]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj3_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[64])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj3_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[65])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj3_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[66])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj3_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[67])',
    'FilesPerJob': 30,
}}

samples['mixed_cHj3_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[68])',
    'FilesPerJob': 30,
}}

samples['lin_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[15] - LHEReweightingWeight[14])',
    'FilesPerJob': 30,
}}

samples['quad_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[15] + LHEReweightingWeight[14]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ3_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[69])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ3_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[70])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ3_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[71])',
    'FilesPerJob': 30,
}}

samples['mixed_cHQ3_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[72])',
    'FilesPerJob': 30,
}}

samples['lin_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[17] - LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}}

samples['quad_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[17] + LHEReweightingWeight[16]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cHl3_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[73])',
    'FilesPerJob': 30,
}}

samples['mixed_cHl3_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[74])',
    'FilesPerJob': 30,
}}

samples['mixed_cHl3_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[75])',
    'FilesPerJob': 30,
}}

samples['lin_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[19] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}}

samples['quad_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[19] + LHEReweightingWeight[18]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cll1_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[76])',
    'FilesPerJob': 30,
}}

samples['mixed_cll1_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}}

samples['lin_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[21] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}}

samples['quad_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[21] + LHEReweightingWeight[20]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

samples['mixed_cWtil_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[78])',
    'FilesPerJob': 30,
}}

samples['lin_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[23] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}}

samples['quad_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '0.5*(LHEReweightingWeight[23] + LHEReweightingWeight[22]) -2*LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}}

