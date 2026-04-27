CMSSW=os.environ["CMSSW_BASE"]
aliasesFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/aliases_noDNNs.py"
if os.path.exists(CMSSW+"/src/"+aliasesFile):
  handle = open(CMSSW+"/src/"+aliasesFile)
  exec(handle)
  handle.close()


aliases["MultiClass_lepeta"] = {'args': ('/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations//VBF_W/utils/2018/NN/multiclassCONDOR_newWP_geninfo//lepeta_even/', '/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations//VBF_W/utils/2018/NN/multiclassCONDOR_newWP_geninfo//lepeta_even/cumulative_distributions.root', '/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations//VBF_W/utils/2018/NN/multiclassCONDOR_newWP_geninfo//lepeta_odd/', '/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations//VBF_W/utils/2018/NN/multiclassCONDOR_newWP_geninfo//lepeta_even/cumulative_distributions.root', False), 'class': 'MVAReaderDNNMultiRatioSingle', 'linesToAdd': ['gSystem->Load("libLatinoAnalysisMultiDraw.so")', 'gSystem->Load("libDNNEvaluator.so")', '.L /afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations//VBF_W/utils/macros/multiclassmva_reader_DNN_ratioSingle.cc+']}
