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

mcProduction = 'Summer20UL16_106x_nAODv9_HIPM_Full2016v9'

dataReco = 'Run2016_UL2016_nAODv9_HIPM_Full2016v9'

fakeReco = dataReco

#from VBS
# mcSteps = 'MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016' 
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
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

def makeMCDirectory(var=''):
  if var:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
  else:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectoryHWW = os.path.join(treeBaseDirHWW,  mcProduction , mcSteps)
mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
# mcDirectoryHWW = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + MC_skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeRe
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
fakeDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps+"__fakeW1l")
# dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + DATA_skim)


############################# PROVA
treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'
directory_data   = os.path.join(treeBaseDir_SMP, dataReco+ '_skim', dataSteps)

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(mcDirectory, 'Summer20UL16_106x_nAODv9_HIPM_Full2016v9', samplelist)
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
    ['B','Run2016B-ver2_HIPM_UL2016-v2'],
    ['C','Run2016C-HIPM_UL2016-v2'],
    ['D','Run2016D-HIPM_UL2016-v2'],
    ['E','Run2016E-HIPM_UL2016-v2'],
    ['F','Run2016F-HIPM_UL2016-v2'],
]

DataSets = ['SingleMuon','SingleElectron']


DataTrig = {
    'SingleMuon'     : 'Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl',
}


#########################################
############### SIGNAL ##################
#########################################
###### W + jj EWK #######

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLat,'Wm_LNuJJ_EWK')
                                  + nanoGetSampleFiles(mcDirectoryLat,'Wp_LNuJJ_EWK'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'weight': CommonWeight+'*(lhesel>0.5)',
                        'FilesPerJob' : 5,
                    }
