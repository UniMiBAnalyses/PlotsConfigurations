CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2017/UL/unfolding/samples_nobkg.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()


fiducial = '(((abs(Alt$(DressedLepton_pdgId[0],0))==11) + (abs(Alt$(DressedLepton_pdgId[0],0))==13))>0) \
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

samples['WLNuJJ_ptjj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen < 30.0)',
}

samples['WLNuJJ_ptjj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 30.0) * (ptjj_gen < 50.0)',
}

samples['WLNuJJ_ptjj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 50.0) * (ptjj_gen < 75.0)',
}

samples['WLNuJJ_ptjj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 75.0) * (ptjj_gen < 100.0)',
}

samples['WLNuJJ_ptjj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 100.0) * (ptjj_gen < 130.0)',
}

samples['WLNuJJ_ptjj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 130.0) * (ptjj_gen < 180.0)',
}

samples['WLNuJJ_ptjj7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(ptjj_gen >= 180.0)',
}

samples['WLNuJJ_ptjjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
}

