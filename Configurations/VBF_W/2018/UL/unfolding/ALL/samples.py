CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/samples.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

samples['WLNuJJ_detajj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen < 4.06)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.69) * (detajj_gen < 4.79)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.79) * (detajj_gen < 4.9)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.9) * (detajj_gen < 5.03)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 5.03) * (detajj_gen < 5.16)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 5.16) * (detajj_gen < 5.28)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 5.28) * (detajj_gen < 5.42)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 5.42) * (detajj_gen < 5.57)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 5.57) * (detajj_gen < 5.77)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 5.77) * (detajj_gen < 6.1)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 6.1) * (detajj_gen < 6.64)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.06) * (detajj_gen < 4.12)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 6.64)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.12) * (detajj_gen < 4.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.2) * (detajj_gen < 4.27)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.27) * (detajj_gen < 4.34)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.34) * (detajj_gen < 4.42)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.42) * (detajj_gen < 4.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.5) * (detajj_gen < 4.59)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(detajj_gen >= 4.59) * (detajj_gen < 4.69)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_fiducialfiducial'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] < -3.6)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -0.92) * (CleanGenJet_eta[1] < -0.04)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -0.04) * (CleanGenJet_eta[1] < 0.9)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 0.9) * (CleanGenJet_eta[1] < 1.28)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 1.28) * (CleanGenJet_eta[1] < 1.66)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 1.66) * (CleanGenJet_eta[1] < 1.94)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 1.94) * (CleanGenJet_eta[1] < 2.18)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 2.18) * (CleanGenJet_eta[1] < 2.4)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 2.4) * (CleanGenJet_eta[1] < 3.1)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 3.1) * (CleanGenJet_eta[1] < 3.32)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 3.32) * (CleanGenJet_eta[1] < 3.58)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -3.6) * (CleanGenJet_eta[1] < -3.32)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 3.58)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -3.32) * (CleanGenJet_eta[1] < -3.12)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -3.12) * (CleanGenJet_eta[1] < -2.42)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -2.42) * (CleanGenJet_eta[1] < -2.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -2.2) * (CleanGenJet_eta[1] < -1.96)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -1.96) * (CleanGenJet_eta[1] < -1.68)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -1.68) * (CleanGenJet_eta[1] < -1.3)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -1.3) * (CleanGenJet_eta[1] < -0.92)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1etaOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] < 81.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 127.0) * (CleanGenJet_pt[0] < 133.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 133.0) * (CleanGenJet_pt[0] < 140.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 140.0) * (CleanGenJet_pt[0] < 148.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 148.0) * (CleanGenJet_pt[0] < 156.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 156.0) * (CleanGenJet_pt[0] < 165.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 165.0) * (CleanGenJet_pt[0] < 177.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 177.0) * (CleanGenJet_pt[0] < 191.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 191.0) * (CleanGenJet_pt[0] < 209.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 209.0) * (CleanGenJet_pt[0] < 235.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 235.0) * (CleanGenJet_pt[0] < 283.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 81.0) * (CleanGenJet_pt[0] < 88.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 283.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 88.0) * (CleanGenJet_pt[0] < 94.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 94.0) * (CleanGenJet_pt[0] < 99.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 99.0) * (CleanGenJet_pt[0] < 105.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 105.0) * (CleanGenJet_pt[0] < 110.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 110.0) * (CleanGenJet_pt[0] < 115.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 115.0) * (CleanGenJet_pt[0] < 121.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[0] >= 121.0) * (CleanGenJet_pt[0] < 127.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1ptOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] < -3.88)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -1.22) * (CleanGenJet_eta[1] < 0.16)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 0.16) * (CleanGenJet_eta[1] < 1.26)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 1.26) * (CleanGenJet_eta[1] < 1.78)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 1.78) * (CleanGenJet_eta[1] < 2.1)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 2.1) * (CleanGenJet_eta[1] < 2.36)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 2.36) * (CleanGenJet_eta[1] < 3.08)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 3.08) * (CleanGenJet_eta[1] < 3.24)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 3.24) * (CleanGenJet_eta[1] < 3.4)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 3.4) * (CleanGenJet_eta[1] < 3.62)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 3.62) * (CleanGenJet_eta[1] < 3.88)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -3.88) * (CleanGenJet_eta[1] < -3.62)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= 3.88)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -3.62) * (CleanGenJet_eta[1] < -3.42)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -3.42) * (CleanGenJet_eta[1] < -3.24)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -3.24) * (CleanGenJet_eta[1] < -3.08)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -3.08) * (CleanGenJet_eta[1] < -2.36)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -2.36) * (CleanGenJet_eta[1] < -2.12)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -2.12) * (CleanGenJet_eta[1] < -1.78)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_eta[1] >= -1.78) * (CleanGenJet_eta[1] < -1.22)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2etaOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] < 64.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 88.0) * (CleanGenJet_pt[1] < 91.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 91.0) * (CleanGenJet_pt[1] < 95.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 95.0) * (CleanGenJet_pt[1] < 99.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 99.0) * (CleanGenJet_pt[1] < 103.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 103.0) * (CleanGenJet_pt[1] < 109.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 109.0) * (CleanGenJet_pt[1] < 115.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 115.0) * (CleanGenJet_pt[1] < 123.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 123.0) * (CleanGenJet_pt[1] < 133.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 133.0) * (CleanGenJet_pt[1] < 149.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 149.0) * (CleanGenJet_pt[1] < 174.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 64.0) * (CleanGenJet_pt[1] < 68.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 174.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 68.0) * (CleanGenJet_pt[1] < 71.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 71.0) * (CleanGenJet_pt[1] < 74.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 74.0) * (CleanGenJet_pt[1] < 76.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 76.0) * (CleanGenJet_pt[1] < 79.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 79.0) * (CleanGenJet_pt[1] < 82.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 82.0) * (CleanGenJet_pt[1] < 85.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(CleanGenJet_pt[1] >= 85.0) * (CleanGenJet_pt[1] < 88.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2ptOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] < -1.7)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -0.16) * (DressedLepton_eta[0] < 0.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 0.0) * (DressedLepton_eta[0] < 0.15)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 0.15) * (DressedLepton_eta[0] < 0.31)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 0.31) * (DressedLepton_eta[0] < 0.48)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 0.48) * (DressedLepton_eta[0] < 0.64)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 0.64) * (DressedLepton_eta[0] < 0.82)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 0.82) * (DressedLepton_eta[0] < 1.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 1.0) * (DressedLepton_eta[0] < 1.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 1.2) * (DressedLepton_eta[0] < 1.41)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 1.41) * (DressedLepton_eta[0] < 1.69)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -1.7) * (DressedLepton_eta[0] < -1.42)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= 1.69)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -1.42) * (DressedLepton_eta[0] < -1.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -1.2) * (DressedLepton_eta[0] < -1.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -1.0) * (DressedLepton_eta[0] < -0.81)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -0.81) * (DressedLepton_eta[0] < -0.64)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -0.64) * (DressedLepton_eta[0] < -0.47)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -0.47) * (DressedLepton_eta[0] < -0.32)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_eta[0] >= -0.32) * (DressedLepton_eta[0] < -0.16)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepetaOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] < 28.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 52.0) * (DressedLepton_pt[0] < 56.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 56.0) * (DressedLepton_pt[0] < 60.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 60.0) * (DressedLepton_pt[0] < 65.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 65.0) * (DressedLepton_pt[0] < 70.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 70.0) * (DressedLepton_pt[0] < 77.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 77.0) * (DressedLepton_pt[0] < 85.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 85.0) * (DressedLepton_pt[0] < 96.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 96.0) * (DressedLepton_pt[0] < 111.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 111.0) * (DressedLepton_pt[0] < 133.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 133.0) * (DressedLepton_pt[0] < 173.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 28.0) * (DressedLepton_pt[0] < 30.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 173.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 30.0) * (DressedLepton_pt[0] < 33.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 33.0) * (DressedLepton_pt[0] < 36.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 36.0) * (DressedLepton_pt[0] < 39.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 39.0) * (DressedLepton_pt[0] < 42.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 42.0) * (DressedLepton_pt[0] < 45.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 45.0) * (DressedLepton_pt[0] < 48.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(DressedLepton_pt[0] >= 48.0) * (DressedLepton_pt[0] < 52.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepptOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen < 722.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1287.0) * (mjj_gen < 1361.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1361.0) * (mjj_gen < 1444.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1444.0) * (mjj_gen < 1535.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1535.0) * (mjj_gen < 1639.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1639.0) * (mjj_gen < 1757.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1757.0) * (mjj_gen < 1899.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1899.0) * (mjj_gen < 2071.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 2071.0) * (mjj_gen < 2312.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 2312.0) * (mjj_gen < 2637.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 2637.0) * (mjj_gen < 3211.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 722.0) * (mjj_gen < 807.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 3211.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 807.0) * (mjj_gen < 881.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 881.0) * (mjj_gen < 951.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 951.0) * (mjj_gen < 1013.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1013.0) * (mjj_gen < 1078.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1078.0) * (mjj_gen < 1147.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1147.0) * (mjj_gen < 1216.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(mjj_gen >= 1216.0) * (mjj_gen < 1287.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJet1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(nCleanGenJet < 2.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJet2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(nCleanGenJet >= 2.5) * (nCleanGenJet < 3.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJet3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(nCleanGenJet >= 3.5) * (nCleanGenJet < 4.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJet4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(nCleanGenJet >= 4.5) * (nCleanGenJet < 5.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJet5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(nCleanGenJet >= 5.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJetOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen < 16.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 66.0) * (ptW_gen < 73.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW11'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 73.0) * (ptW_gen < 81.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW12'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 81.0) * (ptW_gen < 90.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW13'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 90.0) * (ptW_gen < 100.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW14'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 100.0) * (ptW_gen < 111.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW15'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 111.0) * (ptW_gen < 126.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW16'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 126.0) * (ptW_gen < 143.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW17'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 143.0) * (ptW_gen < 165.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW18'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 165.0) * (ptW_gen < 198.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW19'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 198.0) * (ptW_gen < 253.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 16.0) * (ptW_gen < 23.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW20'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 253.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 23.0) * (ptW_gen < 29.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 29.0) * (ptW_gen < 35.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 35.0) * (ptW_gen < 41.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 41.0) * (ptW_gen < 47.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 47.0) * (ptW_gen < 53.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 53.0) * (ptW_gen < 59.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducial+'*'+'(ptW_gen >= 59.0) * (ptW_gen < 66.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptWOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducial+')',
        'EventsPerJob' : 7000,
}

