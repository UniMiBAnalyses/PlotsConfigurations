import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

############################################
############ MORE MC STAT ##################
############################################

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(directory_bkg, 'Autumn18_102X_nAODv7_Full2018v7', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')

##############################################
###### Tree Directory according to site ######
##############################################

samples={}

# Steps
mcSteps   = 'MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018'
dataSteps = 'DATAl1loose2018v7__DATACombJJLNu2018'

mcProduction =   'Autumn18_102X_nAODv7_Full2018v7_skim'
mcProduction_EFT =   'Autumn18_102X_nAODv7_Full2018v7'
dataProduction = 'Run2018_102X_nAODv7_Full2018v7_skim'

SITE=os.uname()[1]
xrootdPath=''
if  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'
  treeBaseDir_EFT = '/eos/user/g/gboldrin/nanoLatino/'

directory_bkg    = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_signal = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_mc     = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_EFT     = os.path.join(treeBaseDir_EFT ,  mcProduction_EFT , mcSteps)
directory_data   = os.path.join(treeBaseDir_SMP,       dataProduction, dataSteps)
directory_interference = '/eos/user/g/govoni/valsecchi/LatinosSamples/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018'

###############################################
# EFT samples

tapSamples = nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT')
tamSamples = nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT')
mupSamples = nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT')
mumSamples = nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT')
epSamples = nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT')
emSamples = nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT')
###############################################

directory_wjets_bins = {}
wjets_res_bins = []
wjets_boost_bins = []
nfiles_wjets_res = [4,4,5,6,8,8,4,4,5,6,8,8,5,5,6,8,8,8,8,8,8]
nfiles_wjets_boost = [6,6,6,6,7,8,8]
for i in range(1, 22):
  if i == 5 or i == 9 or i == 10 or i == 13 or i == 17 or i == 19 or i == 21: continue
  wjbin = "Wjets_res_{}".format(i)
  wjets_res_bins.append(wjbin)
  directory_wjets_bins[wjbin] = treeBaseDir_EFT + 'Autumn18_102X_nAODv7_Full2018v7_skim/res_bin_{}/'.format(i) + mcSteps
for i in range(1, 8):
  wjbin = "Wjets_boost_{}".format(i)
  wjets_boost_bins.append(wjbin)
  directory_wjets_bins[wjbin] = treeBaseDir_EFT + 'Autumn18_102X_nAODv7_Full2018v7_skim/boost_bin_{}/'.format(i) + mcSteps

wjets_all_bins = wjets_res_bins + wjets_boost_bins

# print "Wjets bins: ", wjets_res_bins, wjets_boost_bins

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

XSWeight   = 'XSWeight'
SFweight1l = [ 'puWeight', 'SingleLepton_trigEff_corrected[0]',
              'Lepton_RecoSF[0]',LepWPWeight_1l, LepWPCut_1l,
              'btagSF','PUJetIdSF', 'BoostedWtagSF_nominal']

SFweight = '*'.join(SFweight1l)

GenLepMatch   = 'Lepton_genmatched[0]'



################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['SingleMuon','EGamma']

DataTrig = {
            'SingleMuon' : 'Trigger_sngMu' ,
            'EGamma'     : '!Trigger_sngMu && Trigger_sngEl' 
}

###########################################
#############  BACKGROUNDS  ###############
##########################################

################################
### Wjets samples

Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '

for iwboost, wjbin_boost in enumerate(wjets_boost_bins):
  samples[wjbin_boost] = { 'name' :   
            nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu-LO')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT70_100')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT100_200')
            # + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT200_400')
            # + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT400_600')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT600_800')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT800_1200')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT1200_2500'),
            # + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT2500_inf'),
          'weight': "( fit_bin_boost == {} )*".format(iwboost+1) +XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + Wjets_photon_filter +  '* ewknloW * btagSF_corr_Wjets_HT',
          'FilesPerJob' : 5 ,   
      }

  # Fix Wjets binned + LO 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu-LO', '(LHE_HT < 70)') 
  ############
  # HT stiching corrections 2018
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT70_100',    '1.21 * 0.95148')  #adding also k-factor
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT100_200',   '0.9471') 
  # addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT200_400',   '0.9515') 
  # addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT400_600',   '0.9581') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT600_800',   '1.0582') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT800_1200',  '1.1285') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT1200_2500', '1.3268') 
  # addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT2500_inf',  '2.7948') 
  
###################################################3
for iwres, wjbin_res in enumerate(wjets_res_bins):
  samples[wjbin_res] = { 'name' :   
            nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu-LO')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT70_100')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT100_200')
            # + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT200_400')
            # + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT400_600')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT600_800')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT800_1200')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT1200_2500'),
            # + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT2500_inf'),
          'weight': "( fit_bin_res == {} )*".format(iwres+1) +XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + Wjets_photon_filter +  '* ewknloW * btagSF_corr_Wjets_HT',
          'FilesPerJob' : 5,   
      }

  # Fix Wjets binned + LO 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu-LO', '(LHE_HT < 70)') 
  ############
  # HT stiching corrections 2018
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT70_100',    '1.21 * 0.95148')  #adding also k-factor
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT100_200',   '0.9471') 
  # addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT200_400',   '0.9515') 
  # addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT400_600',   '0.9581') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT600_800',   '1.0582') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT800_1200',  '1.1285') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT1200_2500', '1.3268') 
  # addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT2500_inf',  '2.7948') 


#########################################

VBS_samples = ["ewk_WpZ", "ewk_WmZ", "ewk_ZZ", "ewk_WpWm", "ewk_WpWp", "ewk_WmWm"]
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]
EFT_samples = []
# uncomment for mkDatacard
# samples = {k: j for k,j in samples.items() if k not in EFT_samples_dropped}

# Only EFT
# samples = {k: j for k,j in samples.items() if in EFT_samples}
