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


#########################################
############### SIGNAL ##################
#########################################
###### W + jj EWK #######

# samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLat,'Wm_LNuJJ_EWK')
#                                   + nanoGetSampleFiles(mcDirectoryLat,'Wp_LNuJJ_EWK'),
# #                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                         'weight': CommonWeight,
#                         'FilesPerJob' : 5,
#                         'EventsPerJob' : 70000,
#                     }

###########################################
#############  BACKGROUNDS  ###############
###########################################


####### Wjets #########
Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
Total_correction = 'WJets_reweight'
# Total_correction = '1.'

samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
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


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_top') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'TTToSemiLeptonic') #to be add (not present in pvt)
                                 + nanoGetSampleFiles(mcDirectoryLat,'TTZjets')         ## only LO (no NLO)
                                 + nanoGetSampleFiles(mcDirectoryLat,'TTWjets-LO'),
                                #  + nanoGetSampleFiles(mcDirectoryLat,'TTWjets-NLO')   ## use one of them (or NLO or LO)
                      'weight': CommonWeight,
                      'FilesPerJob' : 10,
                      # 'EventsPerJob' : 70000,
                }


addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','TTZjets','Top_pTrw')
addSampleWeight(samples,'top','TTWjets-LO','Top_pTrw')

addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")
###############################################


############## VV ##################

samples['VV']  = { 'name' :  nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WmTo2J_ZTo2L_QCD')
                            #  + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_WmToLNu_QCD') ## missing
                             + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_ZTo2L_QCD')
                            #  + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WpTo2J_QCD') ## missing
                             + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WmTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_ZTo2J_QCD')
                             + nanoGetSampleFiles(mcDirectoryLat,'ZTo2L_ZTo2J_QCD'),
                   'weight': CommonWeight,
#                   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, # still missing EWKnlowW 
                   'FilesPerJob' : 25,
                  #  'EventsPerJob' : 70000,
                }


###############################################

############ VBS ############

samples['VBS']  = { 'name' :  nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_ZTo2J') 
                              + nanoGetSampleFiles(mcDirectoryLat,'WmTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_ZTo2L')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_ZTo2J')
                              # + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WpTo2J') ## missing
                              + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WmTo2J')
                              + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_WmToLNu')
                              + nanoGetSampleFiles(mcDirectoryLat,'ZTo2L_ZTo2J'),
                    'weight': CommonWeight,
#                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' :20,
                    # 'EventsPerJob' : 70000,
                }

########################################


##VBF-Z has an updated k-factor but w/ different sample files
##################################################

########### Higgs Related #############

samples['Higgs']  = {   'name'   :  nanoGetSampleFiles(mcDirectoryLat,'GluGluHToWWToLNuQQ_M125')
                                    + nanoGetSampleFiles(mcDirectoryLat,'VBFHToWWToLNuQQ_M125'),
                        'weight': CommonWeight,
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 5,
                        # 'EventsPerJob' : 70000,
                  }


######### DY ############

DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'
# DY_photon_filter = '1.'

samples['DY_M-50'] = {  'name'  : nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50') 
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-2500toInf'),
                        'weight': CommonWeight+'*'+DY_photon_filter,
                      # 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW --> it is avaible
                        'FilesPerJob' : 15,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                }

#addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO-ext1','DY_LO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')

#addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50-LO_ext1',            '(LHE_HT < 70)')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50',               '(LHE_HT < 70)') # last M50 HT bin is missing
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-70to100',         'DY_LO_pTllrw') # HT-binned are LO!
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-100to200',        'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-200to400',        'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-400to600',        'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-600to800',        'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-800to1200',       'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-1200to2500',      'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-2500toInf',       'DY_LO_pTllrw')


samples['DY_else'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-10to50') ##also NLO exists
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-70to100')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-600toInf'),
                        'weight': CommonWeight+'*'+DY_photon_filter,
                      # 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 5,
                        # 'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all,,
                      #  'suppressNegativeNuisances' :['all,,
                }




# addSampleWeight(samples,'DY_else','DYJetsToLL_M-10to50','DY_NLO_pTllrw')
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-10to50_ext1','DY_NLO_pTllrw')

addSampleWeight(samples,'DY_else','DYJetsToLL_M-10to50',                '(LHE_HT < 70)')
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-5to50_HT-70to100',      'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-5to50_HT-100to200',     'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-5to50_HT-200to400',     'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-5to50_HT-400to600',     'DY_LO_pTllrw')
# addSampleWeight(samples,'DY_else','DYJetsToLL_M-5to50_HT-600toInf',     'DY_LO_pTllrw')


########## VBF - Z #############


samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcDirectoryLat,'EWKZ2Jets_ZToLL_M-50_MJJ-120'),    #called EWKZ2Jets_ZToLL_M-50
                        'weight': CommonWeight+ '*(lhe_mjj[0] > 120)',
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                        'FilesPerJob' : 5,
                        # 'EventsPerJob' : 70000,
                  }

###############################


############ Vg ##############

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'WGToLNuG')   #called WGToLNuG
                                 + nanoGetSampleFiles(mcDirectoryLat,'ZGToLLG'),        ## not found in das
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(!(Gen_ZGstar_mass > 0))',
                    # 'weight': CommonWeight,
                    'FilesPerJob' : 15,
                    # 'EventsPerJob' : 70000,
#                    'suppressNegative' :['all,,
#                    'suppressNegativeNuisances' :['all,,
                }



############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'WGToLNuG')
                                 + nanoGetSampleFiles(mcDirectoryLat,'ZGToLLG')       ## called ZGToLLG
                                 + nanoGetSampleFiles(mcDirectoryLat,'WZTo3LNu_mllmin0p1'),     #called WZTo3LNu_mllmin0p1
                      'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      # 'weight' : CommonWeight,
                      'FilesPerJob' : 5,
                      # 'EventsPerJob' : 70000,
                      # 'suppressNegative' :['all'],
                      # 'suppressNegativeNuisances' :['all'],
                   }

# 14.02.2020: Changed Vg treatment
addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')
#addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01_ext1,(Gen_ZGstar_mass > 0.1)')

############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'ZZZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WZZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WWZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WWW'),
                    'weight': CommonWeight,
                                #+ nanoGetSampleFiles(mcDirectory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
#                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
                    'FilesPerJob' : 20,
                    #  'EventsPerJob' : 70000,
                  }


# # # #########################################
# # # ############## EFT ###############
# # # #########################################

EFTSamples = nanoGetSampleFiles(mcDirectoryLat,'WLNuJJ_EWK_EFT')

samples['sm'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[0])',
    'FilesPerJob': 30,
}

CMSSW=os.environ["CMSSW_BASE"]
sampleEFTFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT_4Comb/EFTweights.py"
if os.path.exists(CMSSW+'/src/'+sampleEFTFile):
  handle = open(CMSSW+'/src/'+sampleEFTFile)
  exec(handle)
  handle.close()

# # # fatti ma non usati per hadd
# # ######################################### debug weightssss ############################
# sampleEFTFileDebug = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT_4Comb/debug_EFTweights.py"
# if os.path.exists(CMSSW+'/src/'+sampleEFTFileDebug):
#   handle = open(CMSSW+'/src/'+sampleEFTFileDebug)
#   exec(handle)
#   handle.close()

#########################################
############## DATAA ###############
#########################################


# Then corrected
# fakeW = 'fakeWeight_35'
fakeW = 'fakeWeight_1p3'

### Fakes
samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA+'*'+fakeW,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 70,
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectoryHWW, pd + '_' + sd)
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
                FileTarget = nanoGetSampleFiles(dataDirectoryHWW,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])


#samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}


# # mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s 2Jets1leptonW2016 -i MCl1loose2016v7__MCCorr2016v7 -b -Q workday -T EWK_LNuJJ,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWW_LNu_M125,HWplusJ_HToWW_LNu_M125,VBFHToWWToLNuQQ_M125,EWK_LLJJ_MLL-50_MJJ-120,Wg_MADGRAPHMLM,Zg,WZTo3LNu_mllmin01,ZZZ,WZZ,WWZ,WWW,WJetsToLNu-LO,WJetsToLNu-LO_ext2,WJetsToLNu_HT70_100,WJetsToLNu_HT100_200,WJetsToLNu_HT100_200_ext2,WJetsToLNu_HT200_400,WJetsToLNu_HT200_400_ext2,WJetsToLNu_HT400_600,WJetsToLNu_HT400_600_ext1,WJetsToLNu_HT600_800,WJetsToLNu_HT600_800_ext1,WJetsToLNu_HT800_1200,WJetsToLNu_HT800_1200_ext1,WJetsToLNu_HT1200_2500,WJetsToLNu_HT1200_2500_ext1,WJetsToLNu_HT2500_inf,WJetsToLNu_HT2500_inf_ext1,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,TTZjets,TTWJetsToLNu_ext1,TTWJetsToLNu_ext2,TTWJetsToQQ,DYJetsToLL_M-50_ext2,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-100to200_ext1,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-400to600_ext1,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-10to50,DYJetsToLL_M-10to50_ext1,DYJetsToLL_M-5to50_HT-70to100,DYJetsToLL_M-5to50_HT-100to200,DYJetsToLL_M-5to50_HT-200to400,DYJetsToLL_M-5to50_HT-200to400_ext1,DYJetsToLL_M-5to50_HT-400to600,DYJetsToLL_M-5to50_HT-400to600_ext1,DYJetsToLL_M-5to50_HT-600toinf,DYJetsToLL_M-5to50_HT-600toinf_ext1

# # mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s DATA2Jets1leptonW2016 -i DATAl1loose2016v7__DATACombJJLNu2016 -b -Q workday



# mkPostProc.py -p Summer20UL16_106x_nAODv9_HIPM_Full2016v9 -s $iSyst -i MCl1loose2016v9__MCCorr2016v9NoJERInHorn -b -Q nextweek -T Wm_LNuJJ_EWK,Wp_LNuJJ_EWK,EWKZ2Jets_ZToLL_M-50_MJJ-120,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,GluGluHToWWToLNuQQ_M125,VBFHToWWToLNuQQ_M125,ZZZ,WZZ,WWZ,WWW,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,WGToLNuG,ZGToLLG,DYJetsToLL_M-10to50-LO,DYJetsToLL_M-4to50_HT-100to200,DYJetsToLL_M-4to50_HT-200to400,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-600toInf,WJetsToLNu-LO,WJetsToLNu_HT70To100,WJetsToLNu_HT100To200,WJetsToLNu_HT200To400,WJetsToLNu_HT400To600,WJetsToLNu_HT600To800,WJetsToLNu_HT800To1200,WJetsToLNu_HT1200To2500,WJetsToLNu_HT2500ToInf,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,DYJetsToLL_M-50,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,WGToLNuG,ZGToLLG,WZTo3LNu_mllmin0p1