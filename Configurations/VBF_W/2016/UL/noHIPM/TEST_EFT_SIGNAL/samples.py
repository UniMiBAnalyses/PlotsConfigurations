import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2016
configurations = os.path.dirname(configurations) # VBF_W
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, getBaseWnAOD, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction = 'Summer20UL16_106x_nAODv9_noHIPM_Full2016v9'

dataReco = 'Run2016_UL2016_nAODv9_noHIPM_Full2016v9'

fakeReco = dataReco

#from VBS
mcSteps = 'MCl1loose2016v9__MCCorr2016v9NoJERInHorn' 

#from VBS
dataSteps = 'DATAl1loose2016v9'

MC_skim = '2Jets1leptonW2016'

DATA_skim = 'DATA2Jets1leptonW2016'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDirHWW = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirLat = '/eos/cms/store/group/phys_smp/ec/Latinos/HWWNano'

def makeMCDirectory(var=''):
  if var:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
  else:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
dataDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps)

################################################
############### Lepton WP ######################
################################################
  
eleWP='mvaFall17V2Iso_WP90_tthmva_70'
muWP='cut_Tight80x_tthmva_80'

LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'

trigg_MC = '( (abs(Lepton_pdgId[0])==13) * (HLT_IsoTkMu24 > 0.5 || HLT_IsoMu24 > 0.5 ) || (abs(Lepton_pdgId[0])==11) * (HLT_Ele27_WPTight_Gsf > 0.5 || HLT_Ele25_eta2p1_WPTight_Gsf > 0.5) )'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight   = 'XSWeight'         
SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF', 'PUJetIdSF','TriggerSFWeight_1l', trigg_MC, 'EMTFbug_veto', 'L1PreFiringWeight_Nom']


SFweight = '*'.join(SFweight1l)
     
GenLepMatch   = 'Lepton_genmatched[0]'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

CommonWeight = XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch
# CommonWeight = XSWeight

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['F','Run2016F-UL2016-v1'],
    ['G','Run2016G_UL2016-v1'],
    ['H','Run2016H_UL2016-v1']
]

DataSets = ['SingleMuon','SingleElectron']


DataTrig = {
    'SingleMuon'     : 'Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl',
}


# #########################################
# ############### SIGNAL ##################
# #########################################
# ###### W + jj EWK #######

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLat,'Wm_LNuJJ_EWK')
                                  + nanoGetSampleFiles(mcDirectoryLat,'Wp_LNuJJ_EWK'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'weight': CommonWeight+'*(lheEFTsel > 0.5)',
                        'FilesPerJob' : 5,
                    }


# # # # # #########################################
# # # # ############## EFT ###############
# # # # #########################################

EFTSamples = nanoGetSampleFiles(mcDirectoryLat,'WLNuJJ_EWK_EFT2_crab')

samples['sm'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[0])' + '*(lheEFTsel > 0.5)',
    'FilesPerJob': 10,
}

# CMSSW=os.environ["CMSSW_BASE"]
# sampleEFTFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT/EFTweights.py"
# if os.path.exists(CMSSW+'/src/'+sampleEFTFile):
#   handle = open(CMSSW+'/src/'+sampleEFTFile)
#   exec(handle)
#   handle.close()

# # ## fatti ma non usati per datacard
# # # ######################################### debug weightssss ############################
# sampleEFTFileDebug = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT/debug_EFTweights.py"
# if os.path.exists(CMSSW+'/src/'+sampleEFTFileDebug):
#   handle = open(CMSSW+'/src/'+sampleEFTFileDebug)
#   exec(handle)
#   handle.close()

# ######################################
# ########### Fakesss ###############
# ######################################


# # Then corrected
# # fakeW = 'fakeWeight_35'
# fakeW = '(fakeWeight_0p9 * (fakeWeight_0p9<=20) + 0.*(fakeWeight_0p9>20))'

# ### Fakes
# samples['Fake'] = {
#   'name': [],
#   'weight': METFilter_DATA+'*'+fakeW,
#   'weights': [],
#   'isData': ['all'],
#   'FilesPerJob' : 30,
#   # 'suppressNegative' :['ele_SR','mu_SR'],
#   # 'suppressNegativeNuisances' :['ele_SR','mu_SR'],
# }

# for _, sd in DataRun:
#   for pd in DataSets:
#     files = nanoGetSampleFiles(dataDirectoryHWW, pd + '_' + sd)
#     samples['Fake']['name'].extend(files)
#     samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

    

# # #########################################
# # ################ DATA ###################
# # #########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 60,         
            }

for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(dataDirectoryHWW,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])


# # #samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}


# # # # mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s 2Jets1leptonW2016 -i MCl1loose2016v7__MCCorr2016v7 -b -Q workday -T EWK_LNuJJ,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWW_LNu_M125,HWplusJ_HToWW_LNu_M125,VBFHToWWToLNuQQ_M125,EWK_LLJJ_MLL-50_MJJ-120,Wg_MADGRAPHMLM,Zg,WZTo3LNu_mllmin01,ZZZ,WZZ,WWZ,WWW,WJetsToLNu-LO,WJetsToLNu-LO_ext2,WJetsToLNu_HT70_100,WJetsToLNu_HT100_200,WJetsToLNu_HT100_200_ext2,WJetsToLNu_HT200_400,WJetsToLNu_HT200_400_ext2,WJetsToLNu_HT400_600,WJetsToLNu_HT400_600_ext1,WJetsToLNu_HT600_800,WJetsToLNu_HT600_800_ext1,WJetsToLNu_HT800_1200,WJetsToLNu_HT800_1200_ext1,WJetsToLNu_HT1200_2500,WJetsToLNu_HT1200_2500_ext1,WJetsToLNu_HT2500_inf,WJetsToLNu_HT2500_inf_ext1,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,TTZjets,TTWJetsToLNu_ext1,TTWJetsToLNu_ext2,TTWJetsToQQ,DYJetsToLL_M-50_ext2,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-100to200_ext1,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-400to600_ext1,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-10to50,DYJetsToLL_M-10to50_ext1,DYJetsToLL_M-5to50_HT-70to100,DYJetsToLL_M-5to50_HT-100to200,DYJetsToLL_M-5to50_HT-200to400,DYJetsToLL_M-5to50_HT-200to400_ext1,DYJetsToLL_M-5to50_HT-400to600,DYJetsToLL_M-5to50_HT-400to600_ext1,DYJetsToLL_M-5to50_HT-600toinf,DYJetsToLL_M-5to50_HT-600toinf_ext1

# # # # mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s DATA2Jets1leptonW2016 -i DATAl1loose2016v7__DATACombJJLNu2016 -b -Q workday