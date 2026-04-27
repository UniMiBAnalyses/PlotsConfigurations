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

##########################################
############  BACKGROUNDS  ###############
##########################################


####### Wjets #########
Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
Total_correction = 'WJets_reweight'
# Total_correction = '1.'

samples['Wjets_HT_hardJets'] = { 'name' : nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100') 
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
                        'weight': CommonWeight+'*' + Wjets_photon_filter + '*' +Total_correction + '* hardJets',
                        # 'EventsPerJob' : 7000,
                        'FilesPerJob' : 2,
		                 }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu-LO', '(LHE_HT < 70)')
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO_ext1', '(LHE_HT < 70)')
# CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu-LO', 'WJetsToLNu-LO_ext1'])

addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT70To100', '1.21 * 0.9582') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT100To200',    '0.9525') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT200To400',    '0.9577') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT400To600',    '0.9613') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT600To800',    '1.0742') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT800To1200',   '1.1698') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT1200To2500',  '1.3046') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT2500ToInf',   '2.1910') 

###############################################
# # ####### WjetsPU #########


samples['Wjets_HT_PUJets'] = { 'name' : nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100') 
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
                        'weight': CommonWeight+'*' + Wjets_photon_filter  + '* PUJets',
                        # 'EventsPerJob' : 7000,
                        'FilesPerJob' : 2,
		                 }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu-LO', '(LHE_HT < 70)')

addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT70To100', '1.21 * 0.9582') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT100To200',    '0.9525') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT200To400',    '0.9577') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT400To600',    '0.9613') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT600To800',    '1.0742') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT800To1200',   '1.1698') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT1200To2500',  '1.3046') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT2500ToInf',   '2.1910') 

###############################################


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_top') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'TTToSemiLeptonic'),
                                #  + nanoGetSampleFiles(mcDirectory,'TTZjets')    ## missinglatino
                                #  + nanoGetSampleFiles(mcDirectory,'TTZjets_ext1')
                                #  + nanoGetSampleFiles(mcDirectory,'TTWjets')    ## only w/ pythia, non amcatnlo
                                #  + nanoGetSampleFiles(mcDirectory,'TTWjets_ext1'),
                      'weight': CommonWeight,
                      'FilesPerJob' : 3,
                      # 'EventsPerJob' : 7000,
                }


# CombineBaseW(samples, 'top', ['TTZjets', 'TTZjets_ext1'])
# CombineBaseW(samples, 'top', ['TTWjets', 'TTWjets_ext1'])

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')

addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")
###############################################
