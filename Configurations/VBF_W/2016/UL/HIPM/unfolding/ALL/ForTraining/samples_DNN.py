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
mcDirectoryLatSig = os.path.join(treeBaseDirLat,  mcProduction , mcSteps+"__genStepVBFW2")


################################################
############### Lepton WP ######################
################################################
  
eleWP='mvaFall17V2Iso_WP90'
muWP='cut_Tight80x'

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
SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF', 'PUJetIdSF','TriggerSFWeight_1l', trigg_MC, 'EMTFbug_veto', 'PrefireWeight']


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

###########################################
#############  BACKGROUNDS  ###############
###########################################


####### Wjets #########
Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
Total_correction = 'WJets_reweight'
# Total_correction = '1.'

samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu-LO')
                                   + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT70To100')
                                   + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT100To200')
                                   + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT200To400')
                                   + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT400To600')
                                   + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT600To800')
                                   + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT800To1200')
                                   + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT1200To2500')
                                   + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT2500ToInf'),
                        # 'weight': CommonWeight+'*' + Wjets_photon_filter +'* ewknloW' + '*' +Total_correction,
                        'weight': CommonWeight+'*' + Wjets_photon_filter + '*' +Total_correction,
			                	'FilesPerJob' : 6, 
                        'subsamples': {
                          'hardJets'  : 'hardJets',
                          'PUJets'    : 'PUJets'
                                    }
		                 }


# No needed HT stiching corrections

addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO', '(LHE_HT < 70)') 

# HT bins to LO factors 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT70To100',          '1.21 * 1.0346')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100To200',         '1.019') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200To400',         '1.012') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400To600',         '0.9945') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600To800',         '0.9537') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800To1200',        '0.8844') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200To2500',       '0.7643') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500ToInf',        '0.2422') 


###############################################

