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

mcProduction = 'Summer16_102X_nAODv7_Full2016v7'

dataReco = 'Run2016_102X_nAODv7_Full2016v7'

fakeReco = dataReco

#from VBS
mcSteps = 'MCl1loose2016v7__MCCorr2016v7' 

#from VBS
dataSteps = 'DATAl1loose2016v7__DATACombJJLNu2016'

skim = '2Jets1leptonW2016'


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


############################# PROVA
treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'
directory_data   = os.path.join(treeBaseDir_SMP, dataReco+ '_skim', dataSteps)

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(mcDirectory, 'Summer16_102X_nAODv7_Full2016v7', samplelist)
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
  
eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'

LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight   = 'XSWeight'
SFweight1l = [ 'puWeight', 'SingleLepton_trigEff_corrected[0]',
              'Lepton_RecoSF[0]', 'EMTFbug_veto', 
              LepWPWeight_1l, LepWPCut_1l,
              'PrefireWeight','PUJetIdSF', 
              'btagSF']
              
# SFweight1l = [ 'puWeight', 'SingleLepton_trigEff_corrected[0]',
#               'Lepton_RecoSF[0]', 'EMTFbug_veto', 
#               LepWPWeight_1l, LepWPCut_1l,
#               'PrefireWeight','PUJetIdSF', 
#               'btagSF', 'BoostedWtagSF_nominal']

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
    ['B','Run2016B-02Apr2020_ver2-v1'],
    ['C','Run2016C-02Apr2020-v1'],
    ['D','Run2016D-02Apr2020-v1'],
    ['E','Run2016E-02Apr2020-v1'],
    ['F','Run2016F-02Apr2020-v1'],
    ['G','Run2016G-02Apr2020-v1'],
    ['H','Run2016H-02Apr2020-v1']
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

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectory,'EWK_LNuJJ'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'weight': CommonWeight,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                    }

###########################################
#############  BACKGROUNDS  ###############
###########################################


####### Wjets #########
# Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
# Total_correction = 'WJets_reweight'

samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO_ext2')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200_ext2')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400_ext2')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600_ext1')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800_ext1')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200_ext1')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500_ext1')
                                   + nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf_ext1'),
                        'weight': CommonWeight,
			                	'FilesPerJob' : 1, 
                        'subsamples': {
                          'hardJets'  : 'hardJets',
                          'PUJets'    : 'PUJets'
                                    }
		                 }

# Missing (wrt 2018)
# WJetsToLNu-LO
# WJetsToLNu_HT70_100
# WJetsToLNu_HT100_200
# WJetsToLNu_HT200_400
# .. tutti non ext

# No needed HT stiching corrections
#addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu', '(LHE_HT < 70)') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu-LO_ext2', '(LHE_HT < 70)') 
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu-LO','WJetsToLNu-LO_ext2'])

CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT100_200','WJetsToLNu_HT100_200_ext2'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT200_400','WJetsToLNu_HT200_400_ext2'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT400_600','WJetsToLNu_HT400_600_ext1'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT600_800','WJetsToLNu_HT600_800_ext1'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT800_1200','WJetsToLNu_HT800_1200_ext1'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT1200_2500','WJetsToLNu_HT1200_2500_ext1'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT2500_inf','WJetsToLNu_HT2500_inf_ext1'])

# HT bins to LO factors 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT70_100',          '1.21 * 1.0346')  #adding also k-factor
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT100_200',         '1.019') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT100_200_ext2',    '1.019') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT200_400',         '1.012') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT200_400_ext2',    '1.012') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT400_600',         '0.9945') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT400_600_ext1',    '0.9945')
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT600_800',         '0.9537') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT600_800_ext1',    '0.9537') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT800_1200',        '0.8844') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT800_1200_ext1',   '0.8844')
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT1200_2500',       '0.7643') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT1200_2500_ext1',  '0.7643') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT2500_inf',        '0.2422') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT2500_inf_ext1',   '0.2422') 


###############################################


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectory,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectory,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_tW_top') 
                                 + nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic') #to be add (not present in pvt)
                                 + nanoGetSampleFiles(mcDirectory,'TTZjets')
                                 + nanoGetSampleFiles(mcDirectory,'TTWJetsToLNu_ext1')
                                 + nanoGetSampleFiles(mcDirectory,'TTWJetsToLNu_ext2')
                                 + nanoGetSampleFiles(mcDirectory,'TTWJetsToQQ'),
                      'weight': CommonWeight,
                      'FilesPerJob' : 16,
                      'EventsPerJob' : 70000,
                }

CombineBaseW(samples, 'top', ['TTWJetsToLNu_ext1', 'TTWJetsToLNu_ext2'])

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
#addSampleWeight(samples,'top','TTZjets','Top_pTrw')
#addSampleWeight(samples,'top','TTWjets_ext1','Top_pTrw')

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
#                             + nanoGetSampleFiles(mcDirectory,'WpToLNu_WmTo2J') solo QCD
                              + nanoGetSampleFiles(mcDirectory,'WpTo2J_WmToLNu')
                              + nanoGetSampleFiles(mcDirectory,'ZTo2L_ZTo2J')
                              + nanoGetSampleFiles(mcDirectory,'WWToLNuQQ'),
                    'weight': CommonWeight,
#                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' :16,
                    'EventsPerJob' : 70000,
                }

########################################


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
                                    + nanoGetSampleFiles(mcDirectory,'HWminusJ_HToWW_LNu_M125')
                                    + nanoGetSampleFiles(mcDirectory,'HWplusJ_HToWW_LNu_M125')
                                    + nanoGetSampleFiles(mcDirectory,'VBFHToWWToLNuQQ_M125'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }


######### DY ############

# DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )' --> does not work
DY_photon_filter = '1.'

samples['DY_M-50'] = {    'name'  : nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_ext2') 
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-2500toInf'),
                        # 'weight': CommonWeight,
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

#addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO-ext1','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')

CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-100to200', 'DYJetsToLL_M-50_HT-100to200_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-200to400', 'DYJetsToLL_M-50_HT-200to400_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-400to600', 'DYJetsToLL_M-50_HT-400to600_ext1'])

#addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO_ext1',            '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',               '(LHE_HT < 70)') # last M50 HT bin is missing
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100',         'DY_LO_pTllrw') # HT-binned are LO!
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',        'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200_ext1',   'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',        'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1',   'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600',        'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600_ext1',   'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',        'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500',      'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',       'DY_LO_pTllrw')


samples['DY_else'] = {    'name'   : nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-10to50')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-10to50_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-70to100')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-600toinf')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-600toinf_ext1'),
                        # 'weight': CommonWeight,
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 16,
                        'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }




CombineBaseW(samples, 'DY', ['DYJetsToLL_M-10to50', 'DYJetsToLL_M-10to50_ext1'])
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50_ext1','DY_NLO_pTllrw')

CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-200to400', 'DYJetsToLL_M-5to50_HT-200to400_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-400to600', 'DYJetsToLL_M-5to50_HT-400to600_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-600toinf', 'DYJetsToLL_M-5to50_HT-600toinf_ext1'])

addSampleWeight(samples,'DY','DYJetsToLL_M-10to50',                '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50_ext1',           '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-70to100',      'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-100to200',     'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-200to400',     'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-200to400_ext1','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-400to600',     'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-400to600_ext1','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-600toinf',     'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-600toinf_ext1','DY_LO_pTllrw')


########## VBF - Z #############

samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcDirectory,'EWK_LLJJ'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 15,
                        'EventsPerJob' : 70000,
                  }

##VBF-Z --> slighly different weight
###############################


############ Vg ##############

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'Zg'),
                    # 'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(!(Gen_ZGstar_mass > 0))
                    'weight': CommonWeight,
                    'FilesPerJob' : 16,
                    'EventsPerJob' : 70000,
#                    'suppressNegative' :['all'],
#                    'suppressNegativeNuisances' :['all'],
                }



############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(directory_bkg,'Zg')
                                 + nanoGetSampleFiles(directory_bkg,'WZTo3LNu_mllmin01'),
                      # 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + ' * (gstarLow * 0.94 + gstarHigh * 1.14)
                      'weight' : CommonWeight,
                      'FilesPerJob' : 15,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                      # 'subsamples': {
                      #   'L': 'gstarLow',
                      #   'H': 'gstarHigh'
                      # }
                   }

# 14.02.2020: Changed Vg treatment
addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')
#addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01_ext1', '(Gen_ZGstar_mass > 0.1)')

############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'ZZZ')
                                + nanoGetSampleFiles(mcDirectory,'WZZ')
                                + nanoGetSampleFiles(mcDirectory,'WWZ')
                                + nanoGetSampleFiles(mcDirectory,'WWW'),
                    'weight': CommonWeight,
                                #+ nanoGetSampleFiles(mcDirectory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
                    'FilesPerJob' : 15,
                     'EventsPerJob' : 70000,
                  }


# Then corrected
# fakeW = 'fakeWeight_35'
fakeW = 'fakeWeight_35'

### Fakes
samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA+'*'+fakeW,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 40,
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

    

#########################################
################ DATA ###################
#########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 60,         
            }

for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(dataDirectory,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])


#samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}


# mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s 2Jets1leptonW2016 -i MCl1loose2016v7__MCCorr2016v7 -b -Q workday -T EWK_LNuJJ,WJetsToLNu-LO_ext2,WJetsToLNu_HT100_200_ext2,WJetsToLNu_HT200_400_ext2,WJetsToLNu_HT400_600_ext1,WJetsToLNu_HT600_800_ext1,WJetsToLNu_HT800_1200_ext1,WJetsToLNu_HT1200_2500_ext1,WJetsToLNu_HT2500_inf_ext1,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTZjets,TTWJetsToLNu_ext1,TTWJetsToLNu_ext2,TTWJetsToQQ,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWW_LNu_M125,HWplusJ_HToWW_LNu_M125,VBFHToWWToLNuQQ_M125,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200_ext1,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-400to600_ext1,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-5to50_HT-70to100,DYJetsToLL_M-5to50_HT-100to200,DYJetsToLL_M-5to50_HT-200to400_ext1,DYJetsToLL_M-5to50_HT-400to600_ext1,DYJetsToLL_M-5to50_HT-600toinf_ext1,DYJetsToLL_M-10to50,EWK_LLJJ_MLL-50_MJJ-120,Wg_MADGRAPHMLM,ZZZ,WZZ,WWZ,WWW
