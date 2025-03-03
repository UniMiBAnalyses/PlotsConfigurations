CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/HIPM/unfolding/samples_nobkg.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

samples['WLNuJJ_dphijj1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen < 1.5)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 3.05)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 1.5) * (dphijj_gen < 2.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.0) * (dphijj_gen < 2.5)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.5) * (dphijj_gen < 2.6)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.6) * (dphijj_gen < 2.7)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.7) * (dphijj_gen < 2.8)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.8) * (dphijj_gen < 2.9)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.9) * (dphijj_gen < 3.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijj9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 3.0) * (dphijj_gen < 3.05)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_dphijjOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

