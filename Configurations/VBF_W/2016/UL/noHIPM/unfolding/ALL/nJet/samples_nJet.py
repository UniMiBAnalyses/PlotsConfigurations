CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/noHIPM/unfolding/samples_nobkg.py"
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

samples['WLNuJJ_nJet1'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet20 < 2.5)',
}

samples['WLNuJJ_nJet2'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet20 >= 2.5) * (nCleanGenJet20 < 3.5)',
}

samples['WLNuJJ_nJet3'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw+'*'+'(nCleanGenJet20 >= 3.5)',
}

samples['WLNuJJ_nJetOut'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
}

