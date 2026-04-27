samples['quad_cW'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[2] + LHEReweightingWeight[1] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[4] + LHEReweightingWeight[3] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[6] + LHEReweightingWeight[5] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[8] + LHEReweightingWeight[7] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[10] + LHEReweightingWeight[9] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[12] + LHEReweightingWeight[11] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[14] + LHEReweightingWeight[13] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[16] + LHEReweightingWeight[15] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[18] + LHEReweightingWeight[17] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[20] + LHEReweightingWeight[19] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['quad_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[22] + LHEReweightingWeight[21] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cW'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[2])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[23])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[24])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[25])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[26])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[27])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[28])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[29])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[30])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[31])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[32])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[4])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[33])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[34])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[35])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[36])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[37])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[38])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[39])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[40])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHDD_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[41])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[6])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[42])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[43])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[44])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[45])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[46])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[47])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[48])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[49])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cHj1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[8])',
    'FilesPerJob': 30,
}


samples['sm_lin_quad_mixed_cHj1_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[50])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj1_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[51])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj1_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[52])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj1_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[53])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj1_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[54])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj1_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[55])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj1_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[56])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cHQ1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[10])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ1_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[57])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ1_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[58])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ1_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[59])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ1_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[60])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ1_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[61])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ1_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[62])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cHj3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[12])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj3_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[63])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj3_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[64])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj3_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[65])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj3_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[66])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHj3_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[67])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cHQ3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[14])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ3_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[68])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ3_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[69])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ3_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[70])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ3_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[71])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cHl3'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHl3_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[72])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHl3_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[73])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHl3_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[74])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cll1'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cll1_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[75])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cll1_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[76])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cWtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cWtil_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[77])',
    'FilesPerJob': 30,
}

samples['sm_lin_quad_cHWBtil'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}