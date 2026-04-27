import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2017
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

mcProduction = 'Summer20UL17_106x_nAODv9_Full2017v9'

dataReco = 'Run2017_UL2017_nAODv9_Full2017v9'

fakeReco = dataReco

#from VBS
mcSteps = 'MCl1loose2017v9__MCCorr2017v9NoJERInHorn' 

#from VBS
dataSteps = 'DATAl1loose2017v9'

MC_skim = '2Jets1leptonW2017'

DATA_skim = 'DATA2Jets1leptonW2017'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDirHWW = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirLat = '/eos/cms/store/group/phys_smp/ec/Latinos/HWWNano'
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

# def makeMCDirectory(var=''):
#   if var:
#       return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
#   else:
#       return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectoryHWW = os.path.join(treeBaseDirHWW,  mcProduction , mcSteps)
mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
# mcDirectoryHWW = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + MC_skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeRe
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
fakeDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps+"__fakeW1l")
# dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + DATA_skim)

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(mcDirectory, 'Summer20UL17_106x_nAODv9_Full2017v9', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')
################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='1'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V2Iso_WP90_tthmva_70'
muWP='cut_Tight_HWWW_tthmva_80'


LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF[0]'

trigg_MC = '( (abs(Lepton_pdgId[0])==13) * (HLT_IsoMu27 > 0.5) || (abs(Lepton_pdgId[0])==11) * (HLT_Ele35_WPTight_Gsf > 0.5) )'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################
#corrected trigger efficiency

XSWeight   = 'XSWeight'
SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'TriggerSFWeight_1l', trigg_MC, 'L1PreFiringWeight_Nom', 'EMTFbug_veto']

SFweight = '*'.join(SFweight1l)
     
GenLepMatch   = 'Lepton_genmatched[0]'


################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

CommonWeight = XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['B','Run2017B-UL2017-v1'] ,
            ['C','Run2017C-UL2017-v1'] ,
            ['D','Run2017D-UL2017-v1'] ,
            ['E','Run2017E-UL2017-v1'] ,
            ['F','Run2017F-UL2017-v1']
          ]

DataSets = ['SingleMuon','SingleElectron']


DataTrig = {
    'SingleMuon'     : 'Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl',
}


samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLat,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLat,'Wp_LNuJJ_EWK'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        # 'weight': CommonWeight+'*btagSF_corr_Vg_VgS_VBFV',
                        'weight': CommonWeight+'*(lheEFTsel > 0.5)',
                        'FilesPerJob' : 5,
                        # 'EventsPerJob' : 7000,
                    }

# # # # #########################################
# # # # ############## EFT ###############
# # # # #########################################

EFTSamples = nanoGetSampleFiles(mcDirectoryLat,'WLNuJJ_EWK_EFT2_crab')

samples['sm'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[0])' + '*(lheEFTsel > 0.5)',
    'FilesPerJob': 5,
}

# CMSSW=os.environ["CMSSW_BASE"]
# sampleEFTFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT/EFTweights.py"
# if os.path.exists(CMSSW+'/src/'+sampleEFTFile):
#   handle = open(CMSSW+'/src/'+sampleEFTFile)
#   exec(handle)
#   handle.close()

# ## haddato, ma non nelle datacard
# ######################################### debug weightssss ############################
# sampleEFTFileDebug = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT/debug_EFTweights.py"
# if os.path.exists(CMSSW+'/src/'+sampleEFTFileDebug):
#   handle = open(CMSSW+'/src/'+sampleEFTFileDebug)
#   exec(handle)
#   handle.close()

# ########################################################################

# # Then corrected
# fakeW = '(fakeWeight_0p9 * (fakeWeight_0p9 <= 20) + 0.*(fakeWeight_0p9>20))'
# # fakeW = 'fakeWeight_0p8'

# # Fake_ele_corr = ((abs(Lepton_pdgId[0]) == 11) * (((Lepton_phi[0]<-1.)*(Lepton_phi[0]>-1.5)*(0.4)) + ((Lepton_phi[0]>-1.)*(1.) + (Lepton_phi[0]<1.5)*(1.))))
# # Fake_corr = '(((abs(Lepton_pdgId[0]) == 11) * (1. + ((Lepton_phi[0]<-1.)*(Lepton_phi[0]>-1.5)*(-0.6)))) + ((abs(Lepton_pdgId[0]) == 13 ) * 1.))'
# # Fake_corr = '1.'


# # ## Fakes
# samples['Fake'] = {
#   'name': [],
#   'weight': METFilter_DATA+'*'+fakeW,
#   'weights': [],
#   'isData': ['all'],
#   'FilesPerJob' : 30,
# }


# #
# for _, sd in DataRun:
#   for pd in DataSets:
#     files = nanoGetSampleFiles(dataDirectoryHWW, pd + '_' + sd)
#     # # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
#     samples['Fake']['name'].extend(files)
#     samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


# ##########################################
# ################# DATA ###################
# ##########################################

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


# # # #samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}

# # # # mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s 2Jets1leptonW2017 -i MCl1loose2017v7__MCCorr2017v7__MCCombJJLNu2017 -b -Q workday -T WLNuJJ_EWK,EWK_LNuJJ_herwig,WJetsToLNu-LO,WJetsToLNu-LO_ext1,WJetsToLNu_HT70_100,WJetsToLNu_HT100_200,WJetsToLNu_HT200_400,WJetsToLNu_HT400_600,WJetsToLNu_HT600_800,WJetsToLNu_HT800_1200,WJetsToLNu_HT1200_2500,WJetsToLNu_HT2500_inf,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,TTZjets,TTZjets_ext1,TTWjets,TTWjets_ext1,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,VBFHToWWToLNuQQ_M125,DYJetsToLL_M-50,DYJetsToLL_M-50_ext1,DYJetsToLL_M-10to50-LO_ext1,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-400to600_newpmx,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-4to50_HT-100to200_newpmx,DYJetsToLL_M-4to50_HT-200to400_newpmx,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-400to600_ext1,DYJetsToLL_M-4to50_HT-600toInf,DYJetsToLL_M-4to50_HT-600toInf_ext1,EWKZ2Jets_ZToLL_M-50_newpmx,EWK_LLJJ_herwig,Wg_MADGRAPHMLM,ZGToLLG,WZTo3LNu_mllmin01,ZZZ,WWZ,WWW,WZZ

# # # per il 2017 posso usare lo stesso step perche parto da uno step in piu (ereditato da davide) in cui i veti sul tight [0] e [1] sono gia applicati correttamente. Se cosi non fosse mi uscirebbero i fake sbagliati
# # # # mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s 2Jets1leptonW2017 -i DATAl1loose2017v7__DATACombJJLNu2017 -b -Q workday

# # mkPostProc.py -p Summer20UL17_106x_nAODv9_Full2017v9 -s $iSyst -i MCl1loose2017v9__MCCorr2017v9NoJERInHorn -b -Q nextweek -T Wm_LNuJJ_EWK,Wp_LNuJJ_EWK,EWKZ2Jets_ZToLL_M-50_MJJ-120,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,GluGluHToWWToLNuQQ_M125,VBFHToWWToLNuQQ_M125,ZZZ,WZZ,WWZ,WWW,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,WGToLNuG,ZGToLLG,DYJetsToLL_M-10to50-LO,DYJetsToLL_M-4to50_HT-100to200,DYJetsToLL_M-4to50_HT-200to400,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-600toInf,WJetsToLNu-LO,WJetsToLNu_HT70To100,WJetsToLNu_HT100To200,WJetsToLNu_HT200To400,WJetsToLNu_HT400To600,WJetsToLNu_HT600To800,WJetsToLNu_HT800To1200,WJetsToLNu_HT1200To2500,WJetsToLNu_HT2500ToInf,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,DYJetsToLL_M-50,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,WGToLNuG,ZGToLLG,WZTo3LNu_mllmin0p1