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

mcProduction = 'Fall2017_102X_nAODv7_Full2017v7'

dataReco = 'Run2017_102X_nAODv7_Full2017v7'

fakeReco = dataReco

#from VBS
mcSteps = 'MCl1loose2017v7__MCCorr2017v7__MCCombJJLNu2017' 

#from VBS
dataSteps = 'DATAl1loose2017v7__DATACombJJLNu2017'

skim = '2Jets1leptonW2017'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

# def makeMCDirectory(var=''):
#   if var:
#       return os.path.join(treeBaseDir, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
#   else:
#       return os.path.join(treeBaseDir, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectory = os.path.join(treeBaseDir,  mcProduction , mcSteps)
mcPrivateDirectory = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeRe
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + skim)

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(mcDirectory, 'Fall2017_102X_nAODv7_Full2017v7', samplelist)
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

eleWP='mvaFall17V1Iso_WP90'
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

XSWeight      = 'XSWeight'

# SFweight1l = [ 'puWeight_noeras[0]', 'SingleLepton_trigEff_corrected[0]',
#               'Lepton_RecoSF[0]','EMTFbug_veto', LepWPWeight_1l, LepWPCut_1l,
#               'PrefireWeight', 'PUJetIdSF',
#               'btagSF',  'BoostedWtagSF_nominal']
SFweight1l = [ 'puWeight_noeras[0]', 'SingleLepton_trigEff_corrected[0]',
              'Lepton_RecoSF[0]','EMTFbug_veto', LepWPWeight_1l, LepWPCut_1l,
              'PrefireWeight', 'PUJetIdSF',
              'btagSF']

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
            ['B','Run2017B-02Apr2020-v1'] ,
            ['C','Run2017C-02Apr2020-v1'] ,
            ['D','Run2017D-02Apr2020-v1'] ,
            ['E','Run2017E-02Apr2020-v1'] ,
            ['F','Run2017F-02Apr2020-v1']
          ]

DataSets = ['SingleMuon','SingleElectron']


DataTrig = {
    'SingleMuon'     : 'Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_sngMu && ele_passHLT',
}


#########################################
############### SIGNAL ##################
#########################################

###### W + jj EWK #######

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectory,'WLNuJJ_EWK'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        # 'weight': CommonWeight+'*btagSF_corr_Vg_VgS_VBFV',
                        'weight': CommonWeight,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                    }

# samples['WLNuJJ-dipole']  = {  'name'   :  nanoGetSampleFiles(mcDirectory,'EWK_LNuJJ_herwig'),
# #                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                         'weight': CommonWeight,
#                         'FilesPerJob' : 15,
#                         'EventsPerJob' : 70000,
#                     }

###########################################
#############  BACKGROUNDS  ###############
###########################################


####### Wjets #########
Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
# Total_correction = 'WJets_reweight'

samples['Wjets_HT'] = { 'name' : nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO')
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO_ext1')
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT70_100') 
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200')
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400')
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600')
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800')
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200')
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500')
                                  + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf'),
                        # 'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+ Wjets_photon_filter+'* ewknloW'+'* ewknloW * btagSF_corr_Wjets_HT',
                        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+ Wjets_photon_filter+'* ewknloW',
			                	'FilesPerJob' : 1, 
                        'subsamples': {
                          'hardJets'  : 'hardJets',
                          'PUJets'    : 'PUJets'
                                    }
		                 }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO', '(LHE_HT < 70)')
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO_ext1', '(LHE_HT < 70)')
CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu-LO', 'WJetsToLNu-LO_ext1'])

addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT70_100', '1.21 * 0.9582') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100_200',    '0.9525') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200_400',    '0.9577') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400_600',    '0.9613') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600_800',    '1.0742') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800_1200',   '1.1698') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200_2500',  '1.3046') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500_inf',   '2.1910') 

###############################################


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectory,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectory,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_tW_top') 
                                 + nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic') 
                                 + nanoGetSampleFiles(mcDirectory,'TTZjets')
                                 + nanoGetSampleFiles(mcDirectory,'TTZjets_ext1')
                                 + nanoGetSampleFiles(mcDirectory,'TTWjets')
                                 + nanoGetSampleFiles(mcDirectory,'TTWjets_ext1'),
                      'weight': CommonWeight,
                      'FilesPerJob' : 16,
                      'EventsPerJob' : 70000,
                }


CombineBaseW(samples, 'top', ['TTZjets', 'TTZjets_ext1'])
CombineBaseW(samples, 'top', ['TTWjets', 'TTWjets_ext1'])

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')

addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")
###############################################


############## VV ##################

samples['VV']  = { 'name' :  nanoGetSampleFiles(mcDirectory,'WmToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WmToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WmTo2J_ZTo2L_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpTo2J_WmToLNu_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpTo2J_ZTo2L_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpToLNu_WpTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'WpToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectory,'ZTo2L_ZTo2J_QCD'),
                   'weight': CommonWeight,
#                   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, # still missing EWKnlowW 
                   'FilesPerJob' : 17,
                   'EventsPerJob' : 70000,
                }


###############################################

############ VBS ############

samples['VBS']  = { 'name' :  nanoGetSampleFiles(mcDirectory,'WmToLNu_ZTo2J') 
                              + nanoGetSampleFiles(mcDirectory,'WmTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcDirectory,'WpTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcDirectory,'WpToLNu_ZTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WpToLNu_WpTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WmToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WpToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WpTo2J_WmToLNu')
                              + nanoGetSampleFiles(mcDirectory,'ZTo2L_ZTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WWToLNuQQ'),
                    'weight': CommonWeight,
#                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' :16,
                    'EventsPerJob' : 70000,
                }

########################################

# WminusToLNuWminusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# WminusToLNuZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# WplusToLNuWminusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# ZTo2LZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# WplusTo2JWminusToLNuJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# WminusTo2JZTo2LJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# WplusToLNuZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# WplusTo2JZTo2LJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# WplusToLNuWplusTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8
# WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8





################ ggWW ##################

samples['ggWW']  = {  'name'   :  
                                  nanoGetSampleFiles(mcDirectory,'GluGluWWToLNuQQ'),
                    'weight': CommonWeight,
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }


##VBF-Z has an updated k-factor but w/ different sample files
##################################################

########### Higgs Related #############

samples['Higgs']  = {   'name'   :  nanoGetSampleFiles(mcDirectory,'GluGluHToWWToLNuQQ_M125')
                                    + nanoGetSampleFiles(mcDirectory,'VBFHToWWToLNuQQ_M125'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }


########## DY ############

# DY_photons_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'
DY_photon_filter = '1'

samples['DY_M-50'] = {    'name'   : nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50') 
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_ext1')
                                  #+ nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200_newpmx') 
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600_newpmx') 
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-2500toInf'),
                        # 'weight': CommonWeight,
                      # 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter +'*btagSF_corr_DY',# missing ewkNLOW
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

CombineBaseW(samples, 'DY_M-50', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext1'])
CombineBaseW(samples, 'DY_M-50', ['DYJetsToLL_M-50_HT-200to400', 'DYJetsToLL_M-50_HT-200to400_ext1'])

addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext1','DY_NLO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-10to50-LO_ext1','DY_LO_pTllrw')

addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50',                      '(LHE_HT < 200)')  # To put 100 when HT100to200 is back
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext1',                 '(LHE_HT < 200)') # To put 100 when HT100to200 is back
#addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-100to200_newpmx',   'DY_LO_pTllrw * 1.00') # Added HT stitching  ##TO be added back
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-200to400',          'DY_LO_pTllrw * 0.999')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-200to400_ext1',     'DY_LO_pTllrw * 0.999')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-400to600_newpmx',   'DY_LO_pTllrw * 0.990')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-600to800',          'DY_LO_pTllrw * 0.975')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-800to1200',         'DY_LO_pTllrw * 0.907')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-1200to2500',        'DY_LO_pTllrw * 0.833')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-2500toInf',         'DY_LO_pTllrw * 1.015')

samples['DY_else'] = {    'name'   : nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-10to50-LO_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-100to200_newpmx')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-200to400_newpmx')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-600toInf')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-600toInf_ext1') ,
                        # 'weight': CommonWeight+ '*' + DY_photon_filter +'*btagSF_corr_DY',
                        'weight': CommonWeight+ '*' + DY_photon_filter,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }


CombineBaseW(samples, 'DY_M-50', ['DYJetsToLL_M-4to50_HT-400to600', 'DYJetsToLL_M-4to50_HT-400to600_ext1'])
CombineBaseW(samples, 'DY_M-50', ['DYJetsToLL_M-4to50_HT-600toInf', 'DYJetsToLL_M-4to50_HT-600toInf_ext1'])
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-10to50-LO_ext1',               '(LHE_HT < 100)')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-100to200_newpmx',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-200to400_newpmx',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-400to600',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-400to600_ext1',  'DY_LO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-600toInf',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-600toInf_ext1',  'DY_LO_pTllrw')

########## VBF - Z #############

samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcDirectory,'EWKZ2Jets_ZToLL_M-50_newpmx'),
                                  # + nanoGetSampleFiles(mcDirectory,'EWK_LLJJ_herwig')
                        # 'weight': CommonWeight+ '*btagSF_corr_Vg_VgS_VBFV_WLNuJJ',
                        'weight': CommonWeight,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }

##VBF-Z --> slighly different weight
###############################


############ Vg ##############

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'ZGToLLG'),
                    # 'weight':  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0) *btagSF_corr_Vg_VgS_VBFV_WLNuJJ',
                    'weight':  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
                    # 'weight': CommonWeight,
                    'FilesPerJob' : 16,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                }



############ VgS ############

# specialWeight1 = "(gstarLow * 0.94)"
# specialWeight2 = "(gstarHigh * 1.14)"
# weightTotal = 

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'ZGToLLG')
                                 + nanoGetSampleFiles(mcDirectory,'WZTo3LNu_mllmin01'),
                      # 'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14) * btagSF_corr_Vg_VgS_VBFV_WLNuJJ',
                      'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      'FilesPerJob' : 16,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
#0.448 needed in v5 and should be removed in v6
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') #*0.448
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')


############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'ZZZ')
                                + nanoGetSampleFiles(mcDirectory,'WZZ')
                                + nanoGetSampleFiles(mcDirectory,'WWZ')
                                + nanoGetSampleFiles(mcDirectory,'WWW'),
                    # 'weight': CommonWeight +'*btagSF_corr_VV_VVV_ggWW',
                    'weight': CommonWeight,
                                #+ nanoGetSampleFiles(mcDirectory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
                    'FilesPerJob' : 15,
                     'EventsPerJob' : 70000,
                  }


#########################################################################
fake_weight_corrected = "fakeWeight_35"

### Fakes
samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA+'*'+ fake_weight_corrected,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 45
}


#
for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataPrivateDirectory, pd + '_' + sd)
    # # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


##########################################
################# DATA ###################
##########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 45,
                  }


for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(dataPrivateDirectory,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                  samples['DATA']['name'].append(iFile)
                  samples['DATA']['weights'].append(DataTrig[DataSet])


# # #samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}

# # # mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s 2Jets1leptonW2017 -i MCl1loose2017v7__MCCorr2017v7__MCCombJJLNu2017 -b -Q workday -T WLNuJJ_EWK,EWK_LNuJJ_herwig,WJetsToLNu-LO,WJetsToLNu-LO_ext1,WJetsToLNu_HT70_100,WJetsToLNu_HT100_200,WJetsToLNu_HT200_400,WJetsToLNu_HT400_600,WJetsToLNu_HT600_800,WJetsToLNu_HT800_1200,WJetsToLNu_HT1200_2500,WJetsToLNu_HT2500_inf,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,TTZjets,TTZjets_ext1,TTWjets,TTWjets_ext1,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,VBFHToWWToLNuQQ_M125,DYJetsToLL_M-50,DYJetsToLL_M-50_ext1,DYJetsToLL_M-10to50-LO_ext1,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-400to600_newpmx,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-4to50_HT-100to200_newpmx,DYJetsToLL_M-4to50_HT-200to400_newpmx,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-400to600_ext1,DYJetsToLL_M-4to50_HT-600toInf,DYJetsToLL_M-4to50_HT-600toInf_ext1,EWKZ2Jets_ZToLL_M-50_newpmx,EWK_LLJJ_herwig,Wg_MADGRAPHMLM,ZGToLLG,WZTo3LNu_mllmin01,ZZZ,WWZ,WWW,WZZ

# # per il 2017 posso usare lo stesso step perche parto da uno step in piu (ereditato da davide) in cui i veti sul tight [0] e [1] sono gia applicati correttamente. Se cosi non fosse mi uscirebbero i fake sbagliati
# # # mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s 2Jets1leptonW2017 -i DATAl1loose2017v7__DATACombJJLNu2017 -b -Q workday

