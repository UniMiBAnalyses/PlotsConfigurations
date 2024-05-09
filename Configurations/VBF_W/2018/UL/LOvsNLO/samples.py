import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2018
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

mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'

dataReco = 'Run2018_UL2018_nAODv9_Full2018v9'

fakeReco = dataReco

#from VBS
mcSteps = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn' 

#from VBS
dataSteps = 'DATAl1loose2018v9'

MC_skim = '2Jets1leptonW2018'

DATA_skim = 'DATA2Jets1leptonW2018'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDirHWW = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirLat = '/eos/cms/store/group/phys_smp/Latinos/vbfw'
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

def makeMCDirectory(var=''):
  if var:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
  else:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectoryHWW = os.path.join(treeBaseDirHWW,  mcProduction , mcSteps)
mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
# mcDirectoryLat = mcDirectoryHWW
# mcDirectoryHWW = mcDirectoryLat
# mcDirectoryHWW = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + MC_skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeRe
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
# fakeDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps+"__fakeW1l")
# dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + DATA_skim)


############################# PROVA
# def CombineBaseW(samples, proc, samplelist):
#   newbaseW = getBaseWnAOD(mcDirectoryHWW, 'Autumn18_102X_nAODv7_Full2018v7', samplelist)
#   for s in samplelist:
#     addSampleWeight(samples, proc, s, newbaseW+'/baseW')
################################################
############ NUMBER OF LEPTONS #################
################################################

#Nlep='1'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V2Iso_WP90'
muWP='cut_Tight_HWWW'


LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF[0]'

trigg_MC = '( (abs(Lepton_pdgId[0])==13) * (HLT_IsoMu24 > 0.5) || (abs(Lepton_pdgId[0])==11) * (HLT_Ele32_WPTight_Gsf > 0.5) )'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################
#corrected trigger efficiency

XSWeight   = 'XSWeight'
SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'TriggerSFWeight_1l', trigg_MC] 
# SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', 'btagSF','PUJetIdSF', 'TriggerSFWeight_1l', trigg_MC] 
# SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'SingleLepton_trigEff_corrected[0]'] 
# SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'TriggerEffWeight_1l'] 
# SFweight1l = ['puWeight', 'SingleLepton_trigEff_corrected[0]',
#               'Lepton_RecoSF[0]',LepWPWeight_1l, LepWPCut_1l,
#               'btagSF','PUJetIdSF'] 

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
            ['A','Run2018A-UL2018'] ,
            ['B','Run2018B-UL2018'] ,
            ['C','Run2018C-UL2018'] ,
            ['D','Run2018D-UL2018'] ,
          ]

DataSets = ['SingleMuon','EGamma']

DataTrig = {
            'SingleMuon' : 'Trigger_sngMu' ,
            'EGamma'     : '!Trigger_sngMu && Trigger_sngEl' 
}


##########################################
############  BACKGROUNDS  ###############
##########################################


# # ####### Wjets #########
# Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
Wjets_photon_filter = '1.'
Total_correction = 'WJets_reweight'
# Total_correction = '1.'

samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu-LO')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_HT70To100')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_HT100To200')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_HT200To400')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_HT400To600')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_HT600To800')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_HT800To1200')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_HT1200To2500')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_HT2500ToInf'),
#				                'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
                        # 'weight': CommonWeight+'*' + Wjets_photon_filter +'* ewknloW' + '*' +Total_correction,
                        'weight': CommonWeight+'*' + Wjets_photon_filter + '*' + Total_correction,
			                	'FilesPerJob' : 6, 
                        'subsamples': {
                          'hardJets'  : 'hardJets',
                          'PUJets'    : 'PUJets'
                                    }
		                 }

# # Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
# ############
# # HT stiching corrections 2018
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT70To100',    '1.21 * 0.95148')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100To200',   '0.9471') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200To400',   '0.9515') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400To600',   '0.9581') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600To800',   '1.0582') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800To1200',  '1.1285') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200To2500', '1.3268') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500ToInf',  '2.7948') 

###############################################

            
# samples['Wjets_NLO_pt'] = { 'name' :   nanoGetSampleFiles(mcDirectory, 'WJetsToLNu')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt50to100')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt100to250')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt250to400')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt400to600')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt600toInf'),
#                         # 'weight': CommonWeight+'*' + Wjets_photon_filter +'* ewknloW',
#                         # 'weight': CommonWeight+'*'+'EWKnloW[0]',
#                         'weight': CommonWeight,
#                         # 'weight' : '1',
# 			                  'FilesPerJob' : 15
#                         # 'subsamples': {
#                         #   'hardJets'  : 'hardJets',
#                         #   'PUJets'    : 'PUJets'
#                                     # }
# 		                 }


# addSampleWeight(samples, 'Wjets_NLO_pt', 'WJetsToLNu',   '(LHE_Vpt > 120)')
# addSampleWeight(samples, 'Wjets_NLO_pt', 'WJetsToLNu_Pt50to100',   '(LHE_Vpt > 120)')
# addSampleWeight(samples, 'Wjets_NLO_pt', 'WJetsToLNu_Pt100to250',   '(LHE_Vpt > 120)')
# addSampleWeight(samples, 'Wjets_NLO_pt', 'WJetsToLNu_Pt250to400',   '(LHE_Vpt > 120)')
# addSampleWeight(samples, 'Wjets_NLO_pt', 'WJetsToLNu_Pt400to600',   '(LHE_Vpt > 120)')
# addSampleWeight(samples, 'Wjets_NLO_pt', 'WJetsToLNu_Pt600toInf',   '(LHE_Vpt > 120)')

samples['Wjets_NLO_J'] = { 'name' :  nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_0J')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_1J')
                                   + nanoGetSampleFiles(mcDirectoryHWW, 'WJetsToLNu_2J'),
                        # 'weight': CommonWeight+'*' + Wjets_photon_filter +'* ewknloW',
                        # 'weight': CommonWeight+'*'+'EWKnloW[0]',
                        'weight': CommonWeight,
                        # 'weight' : '1',
			                  'FilesPerJob' : 15
                        # 'subsamples': {
                        #   'hardJets'  : 'hardJets',
                        #   'PUJets'    : 'PUJets'
                                    # }
		                 }


# addSampleWeight(samples, 'Wjets_NLO_J', 'WJetsToLNu-0J',   '(LHE_Vpt < 120)')
# addSampleWeight(samples, 'Wjets_NLO_J', 'WJetsToLNu-1J',   '(LHE_Vpt < 120)')
# addSampleWeight(samples, 'Wjets_NLO_J', 'WJetsToLNu-2J',   '(LHE_Vpt < 120)')

