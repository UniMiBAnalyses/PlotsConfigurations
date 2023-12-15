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


samples['WLNuJJ_jet1pt1']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[0] < 90.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet1pt2']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[0] >= 90.0) * (CleanGenJet_pt[0] < 110.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet1pt3']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[0] >= 110.0) * (CleanGenJet_pt[0] < 140.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet1pt4']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[0] >= 140.0) * (CleanGenJet_pt[0] < 180.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_jet1pt5']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(CleanGenJet_pt[0] >= 180.)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }