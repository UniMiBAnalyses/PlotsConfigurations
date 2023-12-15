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
# mcDirectoryHWW = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + MC_skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeRe
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
fakeDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps+"__fakeW1l")
# dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + DATA_skim)


############################# PROVA
treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'
directory_data   = os.path.join(treeBaseDir_SMP, dataReco+ '_skim', dataSteps)

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

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################
#corrected trigger efficiency

XSWeight   = 'XSWeight'
SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF'] 
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

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLat,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLat,'Wp_LNuJJ_EWK'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'weight': CommonWeight,
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

###########################################
#############  BACKGROUNDS  ###############
###########################################


# # ####### Wjets #########
# Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
Wjets_photon_filter = '1.'
# Total_correction = 'WJets_reweight'
Total_correction = '1.'

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

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
############
# # HT stiching corrections 2018
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT70To100',    '1.21 * 0.95148')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100To200',   '0.9471') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200To400',   '0.9515') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400To600',   '0.9581') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600To800',   '1.0582') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800To1200',  '1.1285') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200To2500', '1.3268') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500ToInf',  '2.7948') 



# samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcDirectory, 'WJetsToLNu')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt50to100')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt100to250')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt250to400')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt400to600')
#                                    + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_Pt600toInf'),
#                         # 'weight': CommonWeight+'*' + Wjets_photon_filter +'* ewknloW',
#                         'weight': CommonWeight+'*' + Wjets_photon_filter,
#                         # 'weight' : '1',
# 			                  'FilesPerJob' : 15, 
#                         'subsamples': {
#                           'hardJets'  : 'hardJets',
#                           'PUJets'    : 'PUJets'
#                                     }
# 		                 }



###############################################


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectoryHWW,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectoryHWW,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectoryHWW,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryHWW,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectoryHWW,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryHWW,'ST_tW_top') 
                                 + nanoGetSampleFiles(mcDirectoryHWW,'TTToSemiLeptonic'),
                                #  + nanoGetSampleFiles(mcDirectoryHWW,'TTZjets')   have to do it
                                #  + nanoGetSampleFiles(mcDirectoryHWW,'TTWjets'),  same to do
                                 #+ nanoGetSampleFiles(mcDirectoryHWW,'TTWJetsToLNu'), #also this is available (was commented)
                      'weight': CommonWeight,
#                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                      'FilesPerJob' : 8,
                      # 'EventsPerJob' : 7000,
#                     'suppressNegative' :['all'],
#                     'suppressNegativeNuisances' :['all'],
                }

# !!!! TTToSemiLeptonic_ext3?


addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
# addSampleWeight(samples,'top','TTZjets','Top_pTrw')
# addSampleWeight(samples,'top','TTWjets','Top_pTrw')

#Not corrected in baseW, so we should correct the XS here
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


###############################################


############## VV ##################

samples['VV']  = { 'name' :  nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WmTo2J_ZTo2L_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_WmToLNu_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_ZTo2L_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WpTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'ZTo2L_ZTo2J_QCD'),
                   'weight': CommonWeight,
#                   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, # still missing EWKnlowW 
                   'FilesPerJob' : 10,
                  #  'EventsPerJob' : 70000,
                }


###############################################

############ VBS ############

samples['VBS']  = { 'name' :  nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_ZTo2J') 
                              + nanoGetSampleFiles(mcDirectoryLat,'WmTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_ZTo2J')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WpTo2J')
                              + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_WmToLNu')
                              + nanoGetSampleFiles(mcDirectoryLat,'ZTo2L_ZTo2J'),
                              # + nanoGetSampleFiles(mcDirectoryHWW,'WWToLNuQQ'),   missing from QCD and maybe also from DAS, ignore it for v9
                    'weight': CommonWeight,
#                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' :20,
                    # 'EventsPerJob' : 70000,
                }


# 2018

# WminusTo2JZTo2LJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8                    missing (lat)
# WminusToLNuWminusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8              missing (lat)
# WminusToLNuZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8                   missing (lat)
# WplusTo2JWminusToLNuJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8               missing (lat)
# WplusTo2JZTo2LJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8                     missing (lat)
# WplusToLNuWminusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8               missing (lat)
# WplusToLNuWplusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8                missing (lat)
# WplusToLNuZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8                    missing (lat)
# ZTo2LZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8                         missing (lat)
# WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8                                            missing (lat) maybe also DAS


# 2017
# WminusToLNuWminusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# WminusToLNuZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# WplusToLNuWminusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# ZTo2LZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# WplusTo2JWminusToLNuJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# WminusTo2JZTo2LJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# WplusToLNuZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# WplusTo2JZTo2LJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# WplusToLNuWplusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_Tune*_13TeV-madgraph-pythia8
# WWToLNuQQ_NNPDF31_Tune*_PSweights_13TeV-powheg-pythia8

# 2016
# WminusToLNuWminusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8
# WminusToLNuZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8
# ZTo2LZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8
# WplusTo2JWminusToLNuJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8
# WminusTo2JZTo2LJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8
# WplusToLNuZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8
# WplusTo2JZTo2LJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8
# WplusToLNuWplusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8
# WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1
########################################


# ################ ggWW ##################

# samples['ggWW']  = {  'name'   :  
#                                   nanoGetSampleFiles(mcDirectoryHWW,'GluGluWWToLNuQQ'),    #missing das
#                     'weight': CommonWeight,
# #                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                     'FilesPerJob' : 5,
#                     # 'EventsPerJob' : 70000,
#                   }


##VBF-Z has an updated k-factor but w/ different sample files
##################################################

########### Higgs Related #############

samples['Higgs']  = {   'name'   :  nanoGetSampleFiles(mcDirectoryLat,'GluGluHToWWToLNuQQ_M125')   #missing lat
                                    + nanoGetSampleFiles(mcDirectoryHWW,'HWminusJ_HToWWTo2L2Nu_WToLNu_M125')   #called HWminusJ_HToWWTo2L2Nu_WToLNu_M125
                                    + nanoGetSampleFiles(mcDirectoryHWW,'HWplusJ_HToWWTo2L2Nu_WToLNu_M125')     #called HWplusJ_HToWWTo2L2Nu_WToLNu_M125
                                    + nanoGetSampleFiles(mcDirectoryLat,'VBFHToWWToLNuQQ_M125'),   #missing lat
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 5,
                        # 'EventsPerJob' : 70000,
                  }


########### DY ############

DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'

samples['DY_M-50'] = {    'name'   :   nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50') #Don't use LO(_ext0)! DYMVA Training!
                                  # + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_ext2')
                                  + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-50_HT-2500toInf'),
                        'weight': CommonWeight+'*'+DY_photon_filter,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 15,
                        # 'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

# #VBF-Z does use less sample (only M-50 and applies dome different weights (but uses signal at higher energies))
# # CombineBaseW(samples, 'DY_M-50', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext2'])
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50','DY_NLO_pTllrw')
# # addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50',               '(LHE_HT < 70)')
# # addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext2',          '(LHE_HT < 70)') 
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-70to100',    'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-100to200',   'DY_LO_pTllrw * 1.000') #HT stitching correction
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-200to400',   'DY_LO_pTllrw * 0.999')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-400to600',   'DY_LO_pTllrw * 0.990')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-600to800',   'DY_LO_pTllrw * 0.975')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-800to1200',  'DY_LO_pTllrw * 0.907')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-1200to2500', 'DY_LO_pTllrw * 0.833')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-2500toInf',  'DY_LO_pTllrw * 1.015')  




samples['DY_else'] = {    'name'   : nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-10to50-LO')
                                  # + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-4to50_HT-100to200')   to do (or search..)
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-200to400') #missing (lat)
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-400to600'), #missing (lat)
                                  # + nanoGetSampleFiles(mcDirectoryHWW,'DYJetsToLL_M-4to50_HT-600toInf'),   missing.. search for it
                        'weight': CommonWeight+'*'+DY_photon_filter,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 5,
                        # 'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

addSampleWeight(samples,'DY_else','DYJetsToLL_M-10to50-LO', '(LHE_HT < 200)') 
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-100to200','DY_LO_pTllrw') 
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-200to400','DY_LO_pTllrw')
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-400to600','DY_LO_pTllrw')
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-600toInf','DY_LO_pTllrw')

################################

########## VBF - Z #############

samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcDirectoryHWW,'EWKZ2Jets_ZToLL_M-50'),
                        'weight': CommonWeight+ '*(lhe_mjj[0] > 120)',
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 5,
                        # 'EventsPerJob' : 70000,
                  }

##VBF-Z --> slighly different weight
###############################


############ Vg ##############

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryHWW,'WGToLNuG')   # this is called WGToLNuG in v9
                                 + nanoGetSampleFiles(mcDirectoryHWW,'ZGToLLG'),
                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
                    'FilesPerJob' : 5,
                    # 'EventsPerJob' : 70000,
#                    'suppressNegative' :['all'],
#                    'suppressNegativeNuisances' :['all'],
                }

# the following baseW correction is needed in both v5 and v6 (for Zg, Not for ZGToLLG)
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

##VBF-Z has different weights (common)+genstar
###############################


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectoryHWW,'WGToLNuG')
                                 + nanoGetSampleFiles(mcDirectoryHWW,'ZGToLLG')
                                 + nanoGetSampleFiles(mcDirectoryHWW,'WZTo3LNu_mllmin0p1'),
                      'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      'FilesPerJob' : 15,
                      # 'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                      # 'subsamples': {
                      #   'L': 'gstarLow',
                      #   'H': 'gstarHigh'
                      # }
                   }

addSampleWeight(samples,'VgS','WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') # *0.448 XS correction for Zg
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1)')

############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryHWW,'ZZZ')
                                + nanoGetSampleFiles(mcDirectoryHWW,'WZZ')
                                + nanoGetSampleFiles(mcDirectoryHWW,'WWZ')
                                + nanoGetSampleFiles(mcDirectoryHWW,'WWW'),
                    'weight': CommonWeight,
                                #+ nanoGetSampleFiles(mcDirectory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
                    'FilesPerJob' : 20,
                    #  'EventsPerJob' : 70000,
                  }


##########################################
############### VBS ###############
##########################################

#samples['WWewk'] = {
#    'name': nanoGetSampleFiles(mcDirectoryHWW, 'WpWmJJ_EWK_noTop_dipoleRecoil_private'),
#    'weight': CommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs
#     'FilesPerJob': 4
#}

# Then corrected
fakeW = 'fakeWeight_35'
# Fake_correction = '((abs(Lepton_pdgId[0])==11)*((Lepton_phi[0]<-1.)*(Lepton_phi[0]>-1.5)*(0.4)+((Lepton_phi[0]>=-1.)*(Lepton_phi[0]<=-1.5)*(1))) + ((abs(Lepton_pdgId[0])==13)*((Lepton_phi[0]>0.3)*(Lepton_phi[0]<1.)*(0.5)+((Lepton_phi[0]<=0.3)*(Lepton_phi[0]>=1.)*(1)))))'
# Fake_correction = '1.'

# Fake_ele_corr = ((abs(Lepton_pdgId[0]) == 11) * (((Lepton_phi[0]<-1.)*(Lepton_phi[0]>-1.5)*(0.4)) + ((Lepton_phi[0]>-1.)*(1.) + (Lepton_phi[0]<1.5)*(1.))))
# Fake_corr = '(((abs(Lepton_pdgId[0]) == 11) * (1. + ((Lepton_phi[0]<-1.)*(Lepton_phi[0]>-1.5)*(-0.6)))) + ((abs(Lepton_pdgId[0]) == 13 ) * 1.))'
Fake_corr = '1.'


## MISSING DATAAA!!!!!!!!!!!!!!

### Fakes
samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA+'*'+fakeW,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 70,
}

for Run in DataRun :
  for DataSet in DataSets :
    version = 'v1'
    if "SingleMuon" in DataSet and any(k in Run[0] for k in ["A", "B", "C"]):
      version = 'v2'
    # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
    files = nanoGetSampleFiles(dataDirectoryHWW, DataSet+'_'+Run[1]+'-'+version)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[DataSet]] * len(files))

    

# #########################################
# ################ DATA ###################
# #########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
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


#samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}

# mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s 2Jets1leptonW2018 -i MCl1loose2018v7__MCCorr2018v7 -b -Q workday -T  WLNuJJ_EWK,WJetsToLNu-LO,WJetsToLNu_HT70_100,WJetsToLNu_HT100_200,WJetsToLNu_HT200_400,WJetsToLNu_HT400_600,WJetsToLNu_HT600_800,WJetsToLNu_HT800_1200,WJetsToLNu_HT1200_2500,WJetsToLNu_HT2500_inf,WJetsToLNu,WJetsToLNu_Pt50to100,WJetsToLNu_Pt100to250,WJetsToLNu_Pt250to400,WJetsToLNu_Pt400to600,WJetsToLNu_Pt600toInf,TTTo2L2Nu,ST_s-channel_ext1,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop_ext1,ST_tW_top_ext1,TTToSemiLeptonic,TTZjets,TTWjets,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWW_LNu_M125,HWplusJ_HToWW_LNu_M125,VBFHToWWToLNuQQ_M125,DYJetsToLL_M-50,DYJetsToLL_M-50_ext2,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-10to50-LO_ext1,DYJetsToLL_M-4to50_HT-100to200,DYJetsToLL_M-4to50_HT-200to400,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-600toInf,EWKZ2Jets_ZToLL_M-50,Wg_MADGRAPHMLM,ZGToLLG,ZZZ,WZZ,WWZ,WWW,WJetsToLNu-0J,WJetsToLNu-1J,WJetsToLNu-2J

# # mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s DATA2Jets1leptonW2018 -i DATAl1loose