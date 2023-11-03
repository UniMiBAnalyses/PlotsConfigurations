samples['lin_cW'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[2] - LHEReweightingWeight[1]))',
    'FilesPerJob': 30,
}

samples['quad_cW'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[2] + LHEReweightingWeight[1] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[40])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[55])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[61])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[66])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[70])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[73])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[75])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}

samples['lin_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[4] - LHEReweightingWeight[3]))',
    'FilesPerJob': 30,
}

samples['quad_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[4] + LHEReweightingWeight[3] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[41])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[34])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[35])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[36])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[37])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[38])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[39])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[40])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[41])',
    'FilesPerJob': 30,
}

samples['lin_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[6] - LHEReweightingWeight[5]))',
    'FilesPerJob': 30,
}

samples['quad_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[6] + LHEReweightingWeight[5] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[56])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[62])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[67])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[71])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[74])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[76])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}

samples['lin_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[8] - LHEReweightingWeight[7]))',
    'FilesPerJob': 30,
}

samples['quad_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[8] + LHEReweightingWeight[7] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[50])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[51])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[52])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[53])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[54])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[55])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[56])',
    'FilesPerJob': 30,
}

samples['lin_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[10] - LHEReweightingWeight[9]))',
    'FilesPerJob': 30,
}

samples['quad_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[10] + LHEReweightingWeight[9] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[57])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[58])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[59])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[60])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[61])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[62])',
    'FilesPerJob': 30,
}

samples['lin_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[12] - LHEReweightingWeight[11]))',
    'FilesPerJob': 30,
}

samples['quad_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[12] + LHEReweightingWeight[11] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[63])',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[64])',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[65])',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[66])',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[67])',
    'FilesPerJob': 30,
}

samples['lin_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[14] - LHEReweightingWeight[13]))',
    'FilesPerJob': 30,
}

samples['quad_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[14] + LHEReweightingWeight[13] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cHQ3_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[68])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ3_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[69])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ3_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[70])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ3_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[71])',
    'FilesPerJob': 30,
}

samples['lin_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[16] - LHEReweightingWeight[15]))',
    'FilesPerJob': 30,
}

samples['quad_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[16] + LHEReweightingWeight[15] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cHl3_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[72])',
    'FilesPerJob': 30,
}

samples['mixed_cHl3_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[73])',
    'FilesPerJob': 30,
}

samples['mixed_cHl3_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[74])',
    'FilesPerJob': 30,
}

samples['lin_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[18] - LHEReweightingWeight[17]))',
    'FilesPerJob': 30,
}

samples['quad_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[18] + LHEReweightingWeight[17] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cll1_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[75])',
    'FilesPerJob': 30,
}

samples['mixed_cll1_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[76])',
    'FilesPerJob': 30,
}

samples['lin_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[20] - LHEReweightingWeight[19]))',
    'FilesPerJob': 30,
}

samples['quad_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[20] + LHEReweightingWeight[19] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['mixed_cWtil_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}

samples['lin_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[22] - LHEReweightingWeight[21]))',
    'FilesPerJob': 30,
}

samples['quad_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[22] + LHEReweightingWeight[21] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

