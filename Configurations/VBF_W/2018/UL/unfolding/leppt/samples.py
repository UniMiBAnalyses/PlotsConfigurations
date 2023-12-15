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


samples['WLNuJJ_pt1']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(DressedLepton_pt[0] < 50.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_pt2']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(DressedLepton_pt[0] >= 50.0) * (DressedLepton_pt[0] < 75.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_pt3']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(DressedLepton_pt[0] >= 75.0) * (DressedLepton_pt[0] < 100.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_pt4']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(DressedLepton_pt[0] >= 100.0) * (DressedLepton_pt[0] < 200.0)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

samples['WLNuJJ_pt5']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight+'*'+'(DressedLepton_pt[0] >= 200.)',
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }