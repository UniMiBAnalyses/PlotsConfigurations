CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/samples.py"
if os.path.exists(CMSSW+'/src/'+samplesFile):
  handle = open(CMSSW+'/src/'+samplesFile)
  exec(handle)
  handle.close()

#########################################
######### MULTIPLE SIGNALS ##############
#########################################
###### W + jj EWK #######

samples['WLNuJJ_jet1eta1']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_eta[0] < -1.)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet1eta2']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_eta[0] >= -1.) * (CleanGenJet_eta[0] < 0.)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet1eta3']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_eta[0] >= 0.) * (CleanGenJet_eta[0] < 1.)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet1eta4']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_eta[0] >= 1.)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }