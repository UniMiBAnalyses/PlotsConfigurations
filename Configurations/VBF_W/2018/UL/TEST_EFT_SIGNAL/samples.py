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
  treeBaseDirLat = '/eos/cms/store/group/phys_smp/ec/Latinos/HWWNano'


mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
dataDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps)

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V2Iso_WP90_tthmva_70'
muWP='cut_Tight_HWWW_tthmva_80'


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
SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'TriggerSFWeight_1l', trigg_MC, 'L1PreFiringWeight_Nom'] 
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


# #########################################
# ############### SIGNAL ##################
# #########################################
# ###### W + jj EWK #######

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLat,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLat,'Wp_LNuJJ_EWK'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'weight': CommonWeight+'*(lheEFTsel > 0.5)',
                        'FilesPerJob' : 3,
                        'EventsPerJob' : 5000,
                    }

# #########################################
# ############## EFT ###############
# #########################################

EFTSamples = nanoGetSampleFiles(mcDirectoryLat,'WLNuJJ_EWK_EFT2_crab')

samples['sm'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[0])' + '*(lheEFTsel > 0.5)',
    'FilesPerJob': 10,
}

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                      #  'weight' : METFilter_DATA,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 70,         
            }

for Run in DataRun :
  for DataSet in DataSets :
    version = 'v1'
    if "SingleMuon" in DataSet and any(k in Run[0] for k in ["A", "B", "C"]):
      version = 'v2'
    FileTarget = nanoGetSampleFiles(dataDirectoryHWW,DataSet+'_'+Run[1]+'-'+version)
    for iFile in FileTarget:
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])
