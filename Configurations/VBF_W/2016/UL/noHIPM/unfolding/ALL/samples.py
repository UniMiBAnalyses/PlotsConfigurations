CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/noHIPM/unfolding/samples.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

samples['WLNuJJ_detajj1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen < 4.12)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 6.1)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.12) * (detajj_gen < 4.27)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.27) * (detajj_gen < 4.42)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.42) * (detajj_gen < 4.59)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.59) * (detajj_gen < 4.79)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.79) * (detajj_gen < 5.03)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.03) * (detajj_gen < 5.28)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.28) * (detajj_gen < 5.57)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajj9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.57) * (detajj_gen < 6.1)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_detajjOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] < -3.32)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 3.32)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -3.32) * (CleanGenJet_eta[1] < -2.42)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -2.42) * (CleanGenJet_eta[1] < -1.96)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -1.96) * (CleanGenJet_eta[1] < -1.3)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -1.3) * (CleanGenJet_eta[1] < -0.04)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -0.04) * (CleanGenJet_eta[1] < 1.28)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 1.28) * (CleanGenJet_eta[1] < 1.94)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 1.94) * (CleanGenJet_eta[1] < 2.4)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1eta9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 2.4) * (CleanGenJet_eta[1] < 3.32)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1etaOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] < 88.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 235.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 88.0) * (CleanGenJet_pt[0] < 99.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 99.0) * (CleanGenJet_pt[0] < 110.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 110.0) * (CleanGenJet_pt[0] < 121.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 121.0) * (CleanGenJet_pt[0] < 133.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 133.0) * (CleanGenJet_pt[0] < 148.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 148.0) * (CleanGenJet_pt[0] < 165.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 165.0) * (CleanGenJet_pt[0] < 191.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1pt9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 191.0) * (CleanGenJet_pt[0] < 235.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet1ptOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] < -3.62)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 3.62)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -3.62) * (CleanGenJet_eta[1] < -3.24)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -3.24) * (CleanGenJet_eta[1] < -2.36)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -2.36) * (CleanGenJet_eta[1] < -1.78)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= -1.78) * (CleanGenJet_eta[1] < 0.16)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 0.16) * (CleanGenJet_eta[1] < 1.78)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 1.78) * (CleanGenJet_eta[1] < 2.36)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 2.36) * (CleanGenJet_eta[1] < 3.24)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2eta9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_eta[1] >= 3.24) * (CleanGenJet_eta[1] < 3.62)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2etaOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] < 68.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 149.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 68.0) * (CleanGenJet_pt[1] < 74.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 74.0) * (CleanGenJet_pt[1] < 79.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 79.0) * (CleanGenJet_pt[1] < 85.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 85.0) * (CleanGenJet_pt[1] < 91.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 91.0) * (CleanGenJet_pt[1] < 99.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 99.0) * (CleanGenJet_pt[1] < 109.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 109.0) * (CleanGenJet_pt[1] < 123.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2pt9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 123.0) * (CleanGenJet_pt[1] < 149.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_jet2ptOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] < -1.42)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= 1.41)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= -1.42) * (DressedLepton_eta[0] < -1.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= -1.0) * (DressedLepton_eta[0] < -0.64)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= -0.64) * (DressedLepton_eta[0] < -0.32)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= -0.32) * (DressedLepton_eta[0] < 0.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= 0.0) * (DressedLepton_eta[0] < 0.31)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= 0.31) * (DressedLepton_eta[0] < 0.64)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= 0.64) * (DressedLepton_eta[0] < 1.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepeta9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_eta[0] >= 1.0) * (DressedLepton_eta[0] < 1.41)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepetaOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] < 30.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 133.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 30.0) * (DressedLepton_pt[0] < 36.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 36.0) * (DressedLepton_pt[0] < 42.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 42.0) * (DressedLepton_pt[0] < 48.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 48.0) * (DressedLepton_pt[0] < 56.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 56.0) * (DressedLepton_pt[0] < 65.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 65.0) * (DressedLepton_pt[0] < 77.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 77.0) * (DressedLepton_pt[0] < 96.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_leppt9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 96.0) * (DressedLepton_pt[0] < 133.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_lepptOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen < 807.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 2637.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 807.0) * (mjj_gen < 951.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 951.0) * (mjj_gen < 1078.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1078.0) * (mjj_gen < 1216.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1216.0) * (mjj_gen < 1361.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1361.0) * (mjj_gen < 1535.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1535.0) * (mjj_gen < 1757.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1757.0) * (mjj_gen < 2071.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjj9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 2071.0) * (mjj_gen < 2637.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_mjjOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_nJet1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet < 2.5)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_nJet2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet >= 2.5) * (nCleanGenJet < 3.5)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_nJet3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet >= 3.5) * (nCleanGenJet < 4.5)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_nJet4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet >= 4.5) * (nCleanGenJet < 5.5)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_nJet5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet >= 5.5)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_nJetOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen < 23.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 198.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 23.0) * (ptW_gen < 35.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 35.0) * (ptW_gen < 47.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 47.0) * (ptW_gen < 59.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 59.0) * (ptW_gen < 73.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 73.0) * (ptW_gen < 90.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 90.0) * (ptW_gen < 111.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 111.0) * (ptW_gen < 143.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptW9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 143.0) * (ptW_gen < 198.0)',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

samples['WLNuJJ_ptWOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
        'suppressNegativeNuisances' :['all'],
}

## select only the samples we are interested in: the ones with "out" in the name
# samples = {k:v for k,v in samples.items() if 'Out' in k}