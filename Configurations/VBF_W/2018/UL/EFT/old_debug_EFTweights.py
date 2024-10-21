samples['lin_cW'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[2] - LHEReweightingWeight[1]))',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHDD'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[40] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[4])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHWB'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[77] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[6])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[55] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[8])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[61] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[10])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[66] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[12])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[70] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[14])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[73] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[75] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[77] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[77] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cHDD'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[4] - LHEReweightingWeight[3]))',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHWB'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[41] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[6])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[34] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[8])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[35] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[10])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[36] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[12])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[37] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[14])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[38] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[39] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[40] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[41] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cHWB'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[6] - LHEReweightingWeight[5]))',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[56] + LHEReweightingWeight[0] - LHEReweightingWeight[6] - LHEReweightingWeight[8])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[62] + LHEReweightingWeight[0] - LHEReweightingWeight[6] - LHEReweightingWeight[10])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[67] + LHEReweightingWeight[0] - LHEReweightingWeight[6] - LHEReweightingWeight[12])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[71] + LHEReweightingWeight[0] - LHEReweightingWeight[6] - LHEReweightingWeight[14])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[74] + LHEReweightingWeight[0] - LHEReweightingWeight[6] - LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[76] + LHEReweightingWeight[0] - LHEReweightingWeight[6] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[77] + LHEReweightingWeight[0] - LHEReweightingWeight[6] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['mixed_cHWB_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[77] + LHEReweightingWeight[0] - LHEReweightingWeight[6] - LHEReweightingWeight[])',
    'FilesPerJob': 30,
}

samples['lin_cHj1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[8] - LHEReweightingWeight[7]))',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[50] + LHEReweightingWeight[0] - LHEReweightingWeight[8] - LHEReweightingWeight[10])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[51] + LHEReweightingWeight[0] - LHEReweightingWeight[8] - LHEReweightingWeight[12])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[52] + LHEReweightingWeight[0] - LHEReweightingWeight[8] - LHEReweightingWeight[14])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[53] + LHEReweightingWeight[0] - LHEReweightingWeight[8] - LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[54] + LHEReweightingWeight[0] - LHEReweightingWeight[8] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[55] + LHEReweightingWeight[0] - LHEReweightingWeight[8] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['mixed_cHj1_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[56] + LHEReweightingWeight[0] - LHEReweightingWeight[8] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cHQ1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[10] - LHEReweightingWeight[9]))',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[57] + LHEReweightingWeight[0] - LHEReweightingWeight[10] - LHEReweightingWeight[12])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[58] + LHEReweightingWeight[0] - LHEReweightingWeight[10] - LHEReweightingWeight[14])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[59] + LHEReweightingWeight[0] - LHEReweightingWeight[10] - LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[60] + LHEReweightingWeight[0] - LHEReweightingWeight[10] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[61] + LHEReweightingWeight[0] - LHEReweightingWeight[10] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ1_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[62] + LHEReweightingWeight[0] - LHEReweightingWeight[10] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cHj3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[12] - LHEReweightingWeight[11]))',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[63] + LHEReweightingWeight[0] - LHEReweightingWeight[12] - LHEReweightingWeight[14])',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[64] + LHEReweightingWeight[0] - LHEReweightingWeight[12] - LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[65] + LHEReweightingWeight[0] - LHEReweightingWeight[12] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[66] + LHEReweightingWeight[0] - LHEReweightingWeight[12] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['mixed_cHj3_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[67] + LHEReweightingWeight[0] - LHEReweightingWeight[12] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cHQ3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[14] - LHEReweightingWeight[13]))',
    'FilesPerJob': 30,
}

samples['mixed_cHQ3_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[68] + LHEReweightingWeight[0] - LHEReweightingWeight[14] - LHEReweightingWeight[16])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ3_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[69] + LHEReweightingWeight[0] - LHEReweightingWeight[14] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ3_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[70] + LHEReweightingWeight[0] - LHEReweightingWeight[14] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['mixed_cHQ3_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[71] + LHEReweightingWeight[0] - LHEReweightingWeight[14] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cHl3'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[16] - LHEReweightingWeight[15]))',
    'FilesPerJob': 30,
}

samples['mixed_cHl3_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[72] + LHEReweightingWeight[0] - LHEReweightingWeight[16] - LHEReweightingWeight[18])',
    'FilesPerJob': 30,
}

samples['mixed_cHl3_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[73] + LHEReweightingWeight[0] - LHEReweightingWeight[16] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['mixed_cHl3_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[74] + LHEReweightingWeight[0] - LHEReweightingWeight[16] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cll1'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[18] - LHEReweightingWeight[17]))',
    'FilesPerJob': 30,
}

samples['mixed_cll1_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[75] + LHEReweightingWeight[0] - LHEReweightingWeight[18] - LHEReweightingWeight[20])',
    'FilesPerJob': 30,
}

samples['mixed_cll1_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[76] + LHEReweightingWeight[0] - LHEReweightingWeight[18] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cWtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[20] - LHEReweightingWeight[19]))',
    'FilesPerJob': 30,
}

samples['mixed_cWtil_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(LHEReweightingWeight[77] + LHEReweightingWeight[0] - LHEReweightingWeight[20] - LHEReweightingWeight[22])',
    'FilesPerJob': 30,
}

samples['lin_cHWBtil'] = {
    'name': changeMEname,
    'weight': changeMEweight + '*' + '(0.5*(LHEReweightingWeight[22] - LHEReweightingWeight[21]))',
    'FilesPerJob': 30,
}

