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

samples['WLNuJJ_lepeta1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs < 0.15)',
}

samples['WLNuJJ_lepeta10'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.7)',
}

samples['WLNuJJ_lepeta2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.15) * (lepeta_gen_abs < 0.3)',
}

samples['WLNuJJ_lepeta3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.3) * (lepeta_gen_abs < 0.5)',
}

samples['WLNuJJ_lepeta4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.5) * (lepeta_gen_abs < 0.65)',
}

samples['WLNuJJ_lepeta5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.65) * (lepeta_gen_abs < 0.8)',
}

samples['WLNuJJ_lepeta6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 0.8) * (lepeta_gen_abs < 1.0)',
}

samples['WLNuJJ_lepeta7'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.0) * (lepeta_gen_abs < 1.2)',
}

samples['WLNuJJ_lepeta8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.2) * (lepeta_gen_abs < 1.4)',
}

samples['WLNuJJ_lepeta9'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(lepeta_gen_abs >= 1.4) * (lepeta_gen_abs < 1.7)',
}

samples['WLNuJJ_lepetaOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
}

