samples['sm_lin_quad_cW'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[2])',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}

samples['quad_cW'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[2] + LHEReweightingWeight[1] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}

samples['sm_lin_quad_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[4])',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}

samples['quad_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[4] + LHEReweightingWeight[3] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}

samples['sm_lin_quad_mixed_cHDD_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[33])',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}

samples['sm_lin_quad_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[6])',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}

samples['quad_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(0.5*(LHEReweightingWeight[6] + LHEReweightingWeight[5] -2*LHEReweightingWeight[0]))',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}

samples['sm_lin_quad_mixed_cW_cHDD'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[23])',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}

samples['sm_lin_quad_mixed_cW_cHWB'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[24])',
    'FilesPerJob': 5,
    'EventsPerJob' : 5000,
}