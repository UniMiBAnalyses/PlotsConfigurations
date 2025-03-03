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
  treeBaseDirPrivate2 = '/eos/user/a/abulla/nanoAOD/interference/reco_inter2/hadd/'
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/interference/reco_inter/'

def makeMCDirectory(var=''):
  if var:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
  else:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)

mcDirectoryPrivate2 = os.path.join(treeBaseDirPrivate2,  mcProduction , mcSteps)
mcDirectoryPrivate = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps)

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


#########################################
############### SIGNAL ##################
#########################################
###### W + jj EWK #######

# samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLat,'Wm_LNuJJ_EWK')
#                                     + nanoGetSampleFiles(mcDirectoryLat,'Wp_LNuJJ_EWK'),
# #                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                         'weight': CommonWeight,
#                         'FilesPerJob' : 5,
#                         'EventsPerJob' : 7000,
#                     }

##########################################
############  BACKGROUNDS  ###############
##########################################


# samples['WLNuJJ_inter']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryPrivate2,'WLNuJJ_EWK_QCD_interference2')
#                                           + nanoGetSampleFiles(mcDirectoryPrivate,'WLNuJJ_EWK_QCD_interference'),
# #                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                         'weight': CommonWeight,
#                         'FilesPerJob' : 5,
#                         'EventsPerJob' : 7000,
#                     }


# # ####### Wjets #########
Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
# Wjets_photon_filter = '1.'
Total_correction = 'WJets_reweight'
# Total_correction = '1.'

samples['Wjets_HT_hardJets'] = { 'name' :   nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
#				                'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
                                'weight': CommonWeight+'*' + Wjets_photon_filter + '*' + Total_correction + '* hardJets',
			                	'FilesPerJob' : 4,
		                 }

# # Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
# ############
# # HT stiching corrections 2018
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT70To100',    '1.21 * 0.95148')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT100To200',   '0.9471') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT200To400',   '0.9515') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT400To600',   '0.9581') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT600To800',   '1.0582') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT800To1200',  '1.1285') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT1200To2500', '1.3268') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT2500ToInf',  '2.7948') 

###############################################

samples['Wjets_HT_PUJets'] = { 'name' :   nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
#				                'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
                                'weight': CommonWeight+'*' + Wjets_photon_filter + '* PUJets',
			                	'FilesPerJob' : 4,
		                 }

# # Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
# ############
# # HT stiching corrections 2018
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT70To100',    '1.21 * 0.95148')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT100To200',   '0.9471') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT200To400',   '0.9515') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT400To600',   '0.9581') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT600To800',   '1.0582') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT800To1200',  '1.1285') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT1200To2500', '1.3268') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT2500ToInf',  '2.7948') 

###############################################


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_top')
                                 + nanoGetSampleFiles(mcDirectoryLat,'TTToSemiLeptonic'),
                                #  + nanoGetSampleFiles(mcDirectoryLat,'TTZjets')   have to do it
                                #  + nanoGetSampleFiles(mcDirectoryLat,'TTWjets'),  same to do
                                 #+ nanoGetSampleFiles(mcDirectoryLat,'TTWJetsToLNu'), #also this is available (was commented)
                      'weight': CommonWeight,
                      'FilesPerJob' : 8,
                }

# !!!! TTToSemiLeptonic_ext3?


addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
# addSampleWeight(samples,'top','TTZjets','Top_pTrw')
# addSampleWeight(samples,'top','TTWjets','Top_pTrw')

#Not corrected in baseW, so we should correct the XS here
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


# ###############################################
