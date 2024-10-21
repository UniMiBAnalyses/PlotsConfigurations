CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/noHIPM/unfolding/samples.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

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
