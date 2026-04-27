CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/samples_nobkg.py"
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

samples['WLNuJJ_dphijj1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(Dphijet1jet2_gen < 2.0)',
}

samples['WLNuJJ_dphijj2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(Dphijet1jet2_gen >= 2.0) * (Dphijet1jet2_gen < 2.4)',
}

samples['WLNuJJ_dphijj3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(Dphijet1jet2_gen >= 2.4) * (Dphijet1jet2_gen < 2.6)',
}

samples['WLNuJJ_dphijj4'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(Dphijet1jet2_gen >= 2.6) * (Dphijet1jet2_gen < 2.8)',
}

samples['WLNuJJ_dphijj5'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(Dphijet1jet2_gen >= 2.8) * (Dphijet1jet2_gen < 3.0)',
}

samples['WLNuJJ_dphijj6'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(Dphijet1jet2_gen >= 3.0)',
}

samples['WLNuJJ_dphijjOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
}

