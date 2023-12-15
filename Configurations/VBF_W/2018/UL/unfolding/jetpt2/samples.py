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


samples['WLNuJJ_jet2pt1']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[1] < 80.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet2pt2']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[1] >= 80.0) * (CleanGenJet_pt[1] < 95.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet2pt3']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[1] >= 95.0) * (CleanGenJet_pt[1] < 115.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet2pt4']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[1] >= 115.0) * (CleanGenJet_pt[1] < 150.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet2pt5']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[1] >= 150.)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }