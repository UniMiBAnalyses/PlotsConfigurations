CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2017/UL/unfolding/samples_nobkg.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = "(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.5) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)"

fiducialw = fiducial.replace("&&","*")

samples['WLNuJJ_detajj1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen < 4.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 6.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.0) * (detajj_gen < 4.2)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.2) * (detajj_gen < 4.4)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.4) * (detajj_gen < 4.6)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.6) * (detajj_gen < 4.8)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.8) * (detajj_gen < 5.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.0) * (detajj_gen < 5.2)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.2) * (detajj_gen < 5.5)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajj9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.5) * (detajj_gen < 6.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_detajjOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

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

samples['WLNuJJ_jet2eta1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs < 1.3)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.85)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 1.3) * (jeteta2_gen_abs < 1.8)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 1.8) * (jeteta2_gen_abs < 2.1)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 2.1) * (jeteta2_gen_abs < 2.3)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 2.3) * (jeteta2_gen_abs < 3.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.0) * (jeteta2_gen_abs < 3.2)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.2) * (jeteta2_gen_abs < 3.4)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.4) * (jeteta2_gen_abs < 3.6)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2eta9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.6) * (jeteta2_gen_abs < 3.85)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2etaOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2pt1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] < 70.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2pt2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 70.0) * (CleanGenJet_pt[1] < 80.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2pt3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 80.0) * (CleanGenJet_pt[1] < 90.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2pt4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 90.0) * (CleanGenJet_pt[1] < 100.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2pt5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 100.0) * (CleanGenJet_pt[1] < 115.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2pt6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 115.0) * (CleanGenJet_pt[1] < 140.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2pt7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 140.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_jet2ptOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs < 0.15)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.7)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.15) * (lepeta_gen_abs < 0.3)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.3) * (lepeta_gen_abs < 0.5)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.5) * (lepeta_gen_abs < 0.65)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.65) * (lepeta_gen_abs < 0.8)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.8) * (lepeta_gen_abs < 1.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.0) * (lepeta_gen_abs < 1.2)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.2) * (lepeta_gen_abs < 1.4)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepeta9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.4) * (lepeta_gen_abs < 1.7)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepetaOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] < 30.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt10'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 150.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 30.0) * (DressedLepton_pt[0] < 35.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 35.0) * (DressedLepton_pt[0] < 40.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 40.0) * (DressedLepton_pt[0] < 50.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 50.0) * (DressedLepton_pt[0] < 60.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 60.0) * (DressedLepton_pt[0] < 65.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 65.0) * (DressedLepton_pt[0] < 80.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 80.0) * (DressedLepton_pt[0] < 100.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_leppt9'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 100.0) * (DressedLepton_pt[0] < 150.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_lepptOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjj1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen < 850.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjj2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 850.0) * (mjj_gen < 1000.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjj3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1000.0) * (mjj_gen < 1200.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjj4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1200.0) * (mjj_gen < 1400.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjj5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1400.0) * (mjj_gen < 1600.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjj6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1600.0) * (mjj_gen < 2000.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjj7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 2000.0) * (mjj_gen < 2500.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjj8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 2500.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_mjjOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_nJet1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet < 2.5)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_nJet2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet >= 2.5) * (nCleanGenJet < 3.5)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_nJet3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet >= 3.5)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_nJetOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptW1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen < 30.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptW2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 30.0) * (ptW_gen < 45.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptW3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 45.0) * (ptW_gen < 65.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptW4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 65.0) * (ptW_gen < 90.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptW5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 90.0) * (ptW_gen < 120.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptW6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 120.0) * (ptW_gen < 180.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptW7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 180.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptWOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjj1'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen < 30.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjj2'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 30.0) * (ptjj_gen < 45.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjj3'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 45.0) * (ptjj_gen < 60.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjj4'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 60.0) * (ptjj_gen < 75.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjj5'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 75.0) * (ptjj_gen < 100.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjj6'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 100.0) * (ptjj_gen < 130.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjj7'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 130.0) * (ptjj_gen < 180.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjj8'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 180.0)',
        'FilesPerJob' : 5,
}

samples['WLNuJJ_ptjjOut'] = { 
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'FilesPerJob' : 5,
}

