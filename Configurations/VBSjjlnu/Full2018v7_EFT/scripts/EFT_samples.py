samples['quad_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[14] + LHEReweightingWeight[13] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[21]',
   'FilesPerJob': 1,
}

samples['lin_quad_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[8] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[19]',
   'FilesPerJob': 1,
}

samples['quad_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[6] + LHEReweightingWeight[5] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[12] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[32]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[28]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHW_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[37]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[10]',
   'FilesPerJob': 1,
}

samples['quad_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[10] + LHEReweightingWeight[9] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHB_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[43] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHW_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[38] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[2] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[20] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[23]',
   'FilesPerJob': 1,
}

samples['lin_quad_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[4] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[34]',
   'FilesPerJob': 1,
}

samples['lin_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[4] - LHEReweightingWeight[3])',
   'FilesPerJob': 1,
}

samples['quad_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[16] + LHEReweightingWeight[15] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[10] - LHEReweightingWeight[9])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHB_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[43]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHW_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[35] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[26]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHQ1_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[44]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHl1_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[39] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[18] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[17]',
   'FilesPerJob': 1,
}

samples['lin_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[12] - LHEReweightingWeight[11])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[2]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[28] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[4]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[34] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[8] - LHEReweightingWeight[7])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHl1_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[41] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[27] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[18]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[25] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['quad_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[12] + LHEReweightingWeight[11] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[31] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['quad_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[8] + LHEReweightingWeight[7] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[16] - LHEReweightingWeight[15])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[20]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[33]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHl1_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[41]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[19] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[22]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[27]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHW_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[36]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[25]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[21] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[24] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHQ1_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[44] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[17] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[10] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[14]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHW_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[38]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[29]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHW_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[36] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[33] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['quad_cW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHl1_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[40]',
   'FilesPerJob': 1,
}

samples['lin_quad_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[6] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[8]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[6]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[12]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[29] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[14] - LHEReweightingWeight[13])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHl1_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[39]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[30]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[22] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[14] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHB_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[42]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHl1_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[40] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[16]',
   'FilesPerJob': 1,
}

samples['quad_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[4] + LHEReweightingWeight[3] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHW_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[35]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[23] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[16] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[31]',
   'FilesPerJob': 1,
}

samples['lin_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[6] - LHEReweightingWeight[5])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[32] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[26] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[0]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHB_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[42] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[30] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[24]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHW_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[37] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[2] - LHEReweightingWeight[1])',
   'FilesPerJob': 1,
}

