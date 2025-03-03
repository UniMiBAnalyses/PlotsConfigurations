CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/samples_DNN.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

samples['WLNuJJ_detajj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen < 4.)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 6.)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.) * (detajj_gen < 4.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.2) * (detajj_gen < 4.4)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.4) * (detajj_gen < 4.6)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.6) * (detajj_gen < 4.8)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.8) * (detajj_gen < 5.)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.) * (detajj_gen < 5.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.2) * (detajj_gen < 5.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.5) * (detajj_gen < 6.)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen < 1.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 3.05)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 1.5) * (dphijj_gen < 2.)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.) * (dphijj_gen < 2.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.5) * (dphijj_gen < 2.6)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.6) * (dphijj_gen < 2.7)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.7) * (dphijj_gen < 2.8)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.8) * (dphijj_gen < 2.9)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.9) * (dphijj_gen < 3.)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 3.) * (dphijj_gen < 3.05)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs < 0.9)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.6)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 0.9) * (jeteta1_gen_abs < 1.3)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 1.3) * (jeteta1_gen_abs < 1.7)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 1.7) * (jeteta1_gen_abs < 2.)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 2.) * (jeteta1_gen_abs < 2.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 2.2) * (jeteta1_gen_abs < 2.4)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 2.4) * (jeteta1_gen_abs < 3.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.0) * (jeteta1_gen_abs < 3.3)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.3) * (jeteta1_gen_abs < 3.6)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1etaOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] < 95.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 95.0) * (CleanGenJet_pt[0] < 110.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 110.0) * (CleanGenJet_pt[0] < 130.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 130.0) * (CleanGenJet_pt[0] < 150.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 150.0) * (CleanGenJet_pt[0] < 175.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 175.0) * (CleanGenJet_pt[0] < 225.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 225.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1ptOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs < 1.3)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.85)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 1.3) * (jeteta2_gen_abs < 1.8)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 1.8) * (jeteta2_gen_abs < 2.1)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 2.1) * (jeteta2_gen_abs < 2.3)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 2.3) * (jeteta2_gen_abs < 3.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.0) * (jeteta2_gen_abs < 3.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.2) * (jeteta2_gen_abs < 3.4)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.4) * (jeteta2_gen_abs < 3.6)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.6) * (jeteta2_gen_abs < 3.85)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2etaOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] < 70.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 70.0) * (CleanGenJet_pt[1] < 80.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 80.0) * (CleanGenJet_pt[1] < 90.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 90.0) * (CleanGenJet_pt[1] < 100.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 100.0) * (CleanGenJet_pt[1] < 115.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 115.0) * (CleanGenJet_pt[1] < 140.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 140.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2ptOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs < 0.15)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.7)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.15) * (lepeta_gen_abs < 0.3)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.3) * (lepeta_gen_abs < 0.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.5) * (lepeta_gen_abs < 0.65)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.65) * (lepeta_gen_abs < 0.8)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.8) * (lepeta_gen_abs < 1.)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.) * (lepeta_gen_abs < 1.2)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.2) * (lepeta_gen_abs < 1.4)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.4) * (lepeta_gen_abs < 1.7)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepetaOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] < 30.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 150.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 30.0) * (DressedLepton_pt[0] < 35.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 35.0) * (DressedLepton_pt[0] < 40.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 40.0) * (DressedLepton_pt[0] < 50.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 50.0) * (DressedLepton_pt[0] < 60.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 60.0) * (DressedLepton_pt[0] < 65.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 65.0) * (DressedLepton_pt[0] < 80.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 80.0) * (DressedLepton_pt[0] < 100.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 100.0) * (DressedLepton_pt[0] < 150.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepptOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen < 850.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 850.0) * (mjj_gen < 1000.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1000.0) * (mjj_gen < 1200.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1200.0) * (mjj_gen < 1400.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1400.0) * (mjj_gen < 1600.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1600.0) * (mjj_gen < 2000.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 2000.0) * (mjj_gen < 2500.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 2500.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJet1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet < 2.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJet2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet >= 2.5) * (nCleanGenJet < 3.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJet3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet >= 3.5)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_nJetOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen < 30.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 30.0) * (ptW_gen < 45.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 45.0) * (ptW_gen < 65.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 65.0) * (ptW_gen < 90.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 90.0) * (ptW_gen < 120.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 120.0) * (ptW_gen < 180.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 180.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptWOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen < 30.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 30.0) * (ptjj_gen < 45.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 45.0) * (ptjj_gen < 60.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 60.0) * (ptjj_gen < 75.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 75.0) * (ptjj_gen < 100.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 100.0) * (ptjj_gen < 130.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 130.0) * (ptjj_gen < 180.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 180.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

