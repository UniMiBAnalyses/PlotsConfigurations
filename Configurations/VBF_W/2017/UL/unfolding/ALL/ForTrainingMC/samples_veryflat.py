CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2017/UL/unfolding/samples_DNN.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = '(((abs(Alt$(DressedLepton_pdgId[0],0))==11) + (abs(Alt$(DressedLepton_pdgId[0],0))==13))>0) \
        && (Alt$(DressedLepton_isPrompt[0],0)==1) \
        && (Alt$(DressedLepton_pt[0],0)>=20.) \
        && (Alt$(CleanGenJet_pt[0],0)>=60.) \
        && (Alt$(CleanGenJet_pt[1],0)>=60.) \
        && (Alt$(mjj_gen,0)>=300.) \
        && (Alt$(detajj_gen,0)>=4.) \
        && (Alt$(abs(DressedLepton_eta[0]),999.)<2.) \
        && (Alt$(abs(CleanGenJet_eta[0]),999.)<4.7) \
        && (Alt$(abs(CleanGenJet_eta[1]),999.)<4.7) \
        && (Alt$(nCleanGenJet20,0)>=2)'
        
fiducialw = fiducial.replace("&&","*")

samples['WLNuJJ_detajj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen < 4.11)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.95)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.11) * (detajj_gen < 4.24)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.24) * (detajj_gen < 4.38)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.38) * (detajj_gen < 4.54)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.54) * (detajj_gen < 4.73)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.73) * (detajj_gen < 4.96)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 4.96) * (detajj_gen < 5.22)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.22) * (detajj_gen < 5.51)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_detajj9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(detajj_gen >= 5.51) * (detajj_gen < 5.95)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen < 1.63)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 3.06)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 1.63) * (dphijj_gen < 2.15)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.15) * (dphijj_gen < 2.41)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.41) * (dphijj_gen < 2.58)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.58) * (dphijj_gen < 2.71)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.71) * (dphijj_gen < 2.82)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.82) * (dphijj_gen < 2.91)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.91) * (dphijj_gen < 2.99)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_dphijj9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(dphijj_gen >= 2.99) * (dphijj_gen < 3.06)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs < 0.93)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.55)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 0.93) * (jeteta1_gen_abs < 1.33)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 1.33) * (jeteta1_gen_abs < 1.7)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 1.7) * (jeteta1_gen_abs < 1.96)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 1.96) * (jeteta1_gen_abs < 2.17)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 2.17) * (jeteta1_gen_abs < 2.36)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 2.36) * (jeteta1_gen_abs < 3.05)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.05) * (jeteta1_gen_abs < 3.26)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1eta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta1_gen_abs >= 3.26) * (jeteta1_gen_abs < 3.55)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] < 94.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 94.0) * (CleanGenJet_pt[0] < 111.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 111.0) * (CleanGenJet_pt[0] < 128.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 128.0) * (CleanGenJet_pt[0] < 148.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 148.0) * (CleanGenJet_pt[0] < 175.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 175.0) * (CleanGenJet_pt[0] < 224.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet1pt7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[0] >= 224.0)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs < 1.29)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 1.29) * (jeteta2_gen_abs < 1.81)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 1.81) * (jeteta2_gen_abs < 2.1)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 2.1) * (jeteta2_gen_abs < 2.32)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 2.32) * (jeteta2_gen_abs < 3.01)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.01) * (jeteta2_gen_abs < 3.19)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.19) * (jeteta2_gen_abs < 3.37)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.37) * (jeteta2_gen_abs < 3.58)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2eta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(jeteta2_gen_abs >= 3.58) * (jeteta2_gen_abs < 3.85)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] < 71.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 71.0) * (CleanGenJet_pt[1] < 79.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 79.0) * (CleanGenJet_pt[1] < 88.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 88.0) * (CleanGenJet_pt[1] < 98.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 98.0) * (CleanGenJet_pt[1] < 113.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_jet2pt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(CleanGenJet_pt[1] >= 113.0) * (CleanGenJet_pt[1] < 140.0)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.69)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.15) * (lepeta_gen_abs < 0.31)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.31) * (lepeta_gen_abs < 0.47)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.47) * (lepeta_gen_abs < 0.64)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.64) * (lepeta_gen_abs < 0.81)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.81) * (lepeta_gen_abs < 0.99)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.99) * (lepeta_gen_abs < 1.19)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.19) * (lepeta_gen_abs < 1.41)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_lepeta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.41) * (lepeta_gen_abs < 1.69)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] < 31.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 139.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 31.0) * (DressedLepton_pt[0] < 36.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 36.0) * (DressedLepton_pt[0] < 42.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 42.0) * (DressedLepton_pt[0] < 49.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 49.0) * (DressedLepton_pt[0] < 57.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 57.0) * (DressedLepton_pt[0] < 66.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 66.0) * (DressedLepton_pt[0] < 79.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 79.0) * (DressedLepton_pt[0] < 99.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_leppt9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(DressedLepton_pt[0] >= 99.0) * (DressedLepton_pt[0] < 139.0)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen < 848.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 848.0) * (mjj_gen < 1016.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1016.0) * (mjj_gen < 1184.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1184.0) * (mjj_gen < 1364.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1364.0) * (mjj_gen < 1588.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1588.0) * (mjj_gen < 1894.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 1894.0) * (mjj_gen < 2428.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_mjj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(mjj_gen >= 2428.0)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen < 29.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 29.0) * (ptW_gen < 46.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 46.0) * (ptW_gen < 65.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 65.0) * (ptW_gen < 87.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 87.0) * (ptW_gen < 120.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 120.0) * (ptW_gen < 176.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptW7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptW_gen >= 176.0)',
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
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen < 27.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 27.0) * (ptjj_gen < 42.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 42.0) * (ptjj_gen < 57.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 57.0) * (ptjj_gen < 74.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 74.0) * (ptjj_gen < 96.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 96.0) * (ptjj_gen < 127.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 127.0) * (ptjj_gen < 181.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjj8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 181.0)',
        'EventsPerJob' : 7000,
}

samples['WLNuJJ_ptjjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
        'EventsPerJob' : 7000,
}

