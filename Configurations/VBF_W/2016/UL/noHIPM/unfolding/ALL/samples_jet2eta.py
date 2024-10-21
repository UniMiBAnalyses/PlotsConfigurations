CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/noHIPM/unfolding/samples.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

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
