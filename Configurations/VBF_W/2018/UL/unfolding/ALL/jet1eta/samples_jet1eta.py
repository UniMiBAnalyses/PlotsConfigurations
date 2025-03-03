CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/samples_nobkg.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

samples['WLNuJJ_jet1eta1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs < 0.9)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.6)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 0.9) * (jeteta1_gen_abs < 1.3)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 1.3) * (jeteta1_gen_abs < 1.7)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 1.7) * (jeteta1_gen_abs < 2.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 2.0) * (jeteta1_gen_abs < 2.2)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 2.2) * (jeteta1_gen_abs < 2.4)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 2.4) * (jeteta1_gen_abs < 3.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.0) * (jeteta1_gen_abs < 3.3)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1eta9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.3) * (jeteta1_gen_abs < 3.6)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet1etaOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

