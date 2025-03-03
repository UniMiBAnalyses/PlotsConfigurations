CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/HIPM/unfolding/samples_nobkg.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

samples['WLNuJJ_jet1pt1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] < 95.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1pt2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 95.0) * (CleanGenJet_pt[0] < 110.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1pt3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 110.0) * (CleanGenJet_pt[0] < 130.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1pt4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 130.0) * (CleanGenJet_pt[0] < 150.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1pt5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 150.0) * (CleanGenJet_pt[0] < 175.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1pt6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 175.0) * (CleanGenJet_pt[0] < 225.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1pt7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 225.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1ptOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

