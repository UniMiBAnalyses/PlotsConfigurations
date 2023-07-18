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
if  'cern' in SITE or 'hercules' in SITE:
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'

directory_bkg    = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_signal = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_mc     = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_EFT     = os.path.join(treeBaseDir_SMP ,  mcProduction_EFT , mcSteps)
directory_data   = os.path.join(treeBaseDir_SMP,       dataProduction, dataSteps)
directory_interference = '/eos/user/g/govoni/valsecchi/LatinosSamples/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018'

###############################################

wjets_res_bins = []
wjets_boost_bins = []
directory_wjets_bins = {}
nfiles_wjets_res = [4,4,5,6,8,8,4,4,5,6,8,8,5,5,6,8,8,8,8,8,8]
nfiles_wjets_boost = [6,6,6,6,7,8,8]
for i in range(1, 22):
  wjbin = "Wjets_res_{}".format(i)
  wjets_res_bins.append(wjbin)
  directory_wjets_bins[wjbin] = treeBaseDir_SMP + 'Autumn18_102X_nAODv7_Full2018v7_WjetsBins_skim/res_bin_{}/'.format(i) + mcSteps
for i in range(1, 8):
  wjbin = "Wjets_boost_{}".format(i)
  wjets_boost_bins.append(wjbin)
  directory_wjets_bins[wjbin] = treeBaseDir_SMP + 'Autumn18_102X_nAODv7_Full2018v7_WjetsBins_skim/boost_bin_{}/'.format(i) + mcSteps

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


############## VBF-V ########

samples['VBF-V']  = {  'name'   :  
                                    nanoGetSampleFiles(directory_bkg,'WLNuJJ_EWK') +
                                  nanoGetSampleFiles(directory_bkg,'EWKZ2Jets_ZToLL_M-50'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_Vg_VgS_VBFV',
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }

# samples['VBF-V_dipole']  = {  'name'   :  
#                                     nanoGetSampleFiles(directory_bkg,'EWK_LNuJJ_herwig') +
#                                   nanoGetSampleFiles(directory_bkg,'EWK_LLJJ_herwig'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_Vg_VgS_VBFV',
#                     'FilesPerJob' : 8,
#                     'EventsPerJob' : 70000,
#                   }

######################################

#########################################
