# w1*wm1
samples['ciao1'] = {
    'name': EFTSamples,
    'weight':'LHEReweightingWeight[6] * LHEReweightingWeight[5]',
    'FilesPerJob': 30,
}

#w0w1
samples['ciao2'] = {
    'name': EFTSamples,
    'weight':'LHEReweightingWeight[0] * LHEReweightingWeight[5]',
    'FilesPerJob': 30,
}

#w0wm1
samples['ciao2'] = {
    'name': EFTSamples,
    'weight':'LHEReweightingWeight[0] * LHEReweightingWeight[6]',
    'FilesPerJob': 30,
}