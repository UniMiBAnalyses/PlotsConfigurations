CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/noHIPM/unfolding/samples.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

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
