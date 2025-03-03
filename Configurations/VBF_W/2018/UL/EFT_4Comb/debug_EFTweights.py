samples['lin_cW'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[2] - LHEReweightingWeight[1]))',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[24] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[4])',
    'FilesPerJob': 30,
}

samples['mixed_cW_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[24] + LHEReweightingWeight[0] - LHEReweightingWeight[2] - LHEReweightingWeight[6])',
    'FilesPerJob': 30,
}

samples['lin_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[4] - LHEReweightingWeight[3]))',
    'FilesPerJob': 30,
}

samples['mixed_cHDD_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[33] + LHEReweightingWeight[0] - LHEReweightingWeight[4] - LHEReweightingWeight[6])',
    'FilesPerJob': 30,
}

samples['lin_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[6] - LHEReweightingWeight[5]))',
    'FilesPerJob': 30,
}
