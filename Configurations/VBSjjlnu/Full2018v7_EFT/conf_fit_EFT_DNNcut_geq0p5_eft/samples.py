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
  treeBaseDir_EFT = '/eos/user/g/gboldrin/nanoLatino/'

directory_bkg    = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_signal = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_mc     = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_EFT     = os.path.join(treeBaseDir_SMP ,  mcProduction_EFT , mcSteps)
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

# Dropping corrupted files 

emSamples = [i for i in emSamples if "nanoLatino_emVjj_ewk_dim6_EFT__part30.root" not in i]
tamSamples = [i for i in tamSamples if "nanoLatino_tamVjj_ewk_dim6_EFT__part77.root" not in i] 

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

######################################

samples['quad_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[14] + LHEReweightingWeight[13] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[21]',
   'FilesPerJob': 30,
}

samples['lin_quad_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[8] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[19]',
   'FilesPerJob': 30,
}

samples['quad_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[6] + LHEReweightingWeight[5] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[12] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHbox_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[32]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[28]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHW_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[37]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[10]',
   'FilesPerJob': 30,
}

samples['quad_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[10] + LHEReweightingWeight[9] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHB_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[43] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHW_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[38] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_cW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[2] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cW_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[20] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[23]',
   'FilesPerJob': 30,
}

samples['lin_quad_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[4] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHbox_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[34]',
   'FilesPerJob': 30,
}

samples['lin_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[4] - LHEReweightingWeight[3])',
   'FilesPerJob': 30,
}

samples['quad_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[16] + LHEReweightingWeight[15] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[10] - LHEReweightingWeight[9])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHB_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[43]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHW_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[35] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[26]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHQ1_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[44]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHl1_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[39] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cW_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[18] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[17]',
   'FilesPerJob': 30,
}

samples['lin_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[12] - LHEReweightingWeight[11])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_cW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[2]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHWB_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[28] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[4]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHbox_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[34] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[8] - LHEReweightingWeight[7])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHl1_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[41] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHWB_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[27] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[18]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHWB_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[25] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['quad_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[12] + LHEReweightingWeight[11] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHbox_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[31] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['quad_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[8] + LHEReweightingWeight[7] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[16] - LHEReweightingWeight[15])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[20]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHbox_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[33]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHl1_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[41]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cW_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[19] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cW_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[22]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[27]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHW_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[36]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[25]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cW_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[21] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHWB_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[24] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHQ1_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[44] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cW_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[17] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[10] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[14]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHW_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[38]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[29]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHW_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[36] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHbox_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[33] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['quad_cW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHl1_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[40]',
   'FilesPerJob': 30,
}

samples['lin_quad_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[6] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[8]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[6]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[12]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHWB_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[29] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[14] - LHEReweightingWeight[13])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHl1_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[39]',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHbox_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[30]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cW_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[22] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[14] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHB_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[42]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHl1_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[40] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[16]',
   'FilesPerJob': 30,
}

samples['quad_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[4] + LHEReweightingWeight[3] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHW_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[35]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cW_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[23] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[16] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHbox_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[31]',
   'FilesPerJob': 30,
}

samples['lin_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[6] - LHEReweightingWeight[5])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHbox_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[32] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHWB_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[26] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHB_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[42] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHbox_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[30] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['sm_lin_quad_mixed_cHWB_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[24]',
   'FilesPerJob': 30,
}

samples['lin_quad_mixed_cHW_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[37] - LHEReweightingWeight[0])',
   'FilesPerJob': 30,
}

samples['lin_cW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[2] - LHEReweightingWeight[1])',
   'FilesPerJob': 30,
}

#########################################

VBS_samples = ["ewk_WpZ", "ewk_WmZ", "ewk_ZZ", "ewk_WpWm", "ewk_WpWp", "ewk_WmWm"]
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]

EFT_samples = ['quad_cHQ1', 'sm_lin_quad_mixed_cW_cHB', 'lin_quad_cHW', 'sm_lin_quad_mixed_cW_cHW', 'quad_cHbox', 'lin_quad_cHB', 'sm_lin_quad_mixed_cHbox_cHB', 'sm_lin_quad_mixed_cHWB_cHQ1', 'sm_lin_quad_mixed_cHW_cHQ1', 'sm_lin_quad_cHl1', 'quad_cHl1', 'lin_quad_mixed_cHB_cHj1', 'lin_quad_mixed_cW_cHW', 'lin_quad_cW', 'lin_quad_mixed_cW_cHl1', 'sm_lin_quad_mixed_cW_cHj1', 'lin_quad_cHWB', 'sm_lin_quad_mixed_cHbox_cHj1', 'lin_cHWB', 'sm_lin_quad_cHWB', 'lin_cHl1', 'sm_lin_quad_mixed_cHB_cHj1', 'lin_quad_mixed_cHW_cHl1', 'lin_quad_mixed_cW_cHj1', 'sm_lin_quad_mixed_cHQ1_cHj1', 'lin_quad_mixed_cHl1_cHB', 'lin_quad_mixed_cW_cHbox', 'sm_lin_quad_mixed_cW_cHWB', 'lin_cHB', 'sm_lin_quad_cW', 'lin_quad_mixed_cHWB_cHQ1', 'quad_cHj1', 'lin_quad_mixed_cHbox_cHj1', 'lin_cHW', 'lin_quad_mixed_cHl1_cHj1', 'lin_quad_mixed_cHWB_cHB', 'sm_lin_quad_mixed_cW_cHbox', 'lin_quad_mixed_cHWB_cHW', 'quad_cHB', 'lin_quad_mixed_cHbox_cHl1', 'quad_cHW', 'lin_cHj1', 'sm_lin_quad_mixed_cW_cHl1', 'sm_lin_quad_mixed_cHbox_cHQ1', 'sm_lin_quad_mixed_cHl1_cHj1', 'lin_quad_mixed_cHW_cHj1', 'sm_lin_quad_mixed_cW_cHQ1', 'sm_lin_quad_mixed_cHWB_cHB', 'sm_lin_quad_mixed_cHW_cHB', 'sm_lin_quad_mixed_cHWB_cHW', 'lin_quad_mixed_cW_cHB', 'lin_quad_mixed_cHWB_cHbox', 'lin_quad_mixed_cHQ1_cHj1', 'lin_quad_mixed_cW_cHWB', 'lin_quad_cHl1', 'sm_lin_quad_cHQ1', 'sm_lin_quad_mixed_cHW_cHj1', 'sm_lin_quad_mixed_cHWB_cHj1', 'lin_quad_mixed_cHW_cHB', 'lin_quad_mixed_cHbox_cHQ1', 'quad_cW', 'sm_lin_quad_mixed_cHl1_cHQ1', 'lin_quad_cHbox', 'sm_lin_quad_cHW', 'sm_lin_quad_cHbox', 'sm_lin_quad_cHB', 'lin_quad_mixed_cHWB_cHj1', 'lin_cHQ1', 'sm_lin_quad_mixed_cHl1_cHB', 'sm_lin_quad_mixed_cHbox_cHW', 'lin_quad_mixed_cW_cHQ1', 'lin_quad_cHQ1', 'sm_lin_quad_mixed_cHB_cHQ1', 'lin_quad_mixed_cHl1_cHQ1', 'sm_lin_quad_cHj1', 'quad_cHWB', 'sm_lin_quad_mixed_cHW_cHl1', 'sm_lin_quad_mixed_cHWB_cHl1', 'lin_quad_cHj1', 'sm_lin_quad_mixed_cHbox_cHl1', 'lin_cHbox', 'lin_quad_mixed_cHbox_cHB', 'lin_quad_mixed_cHWB_cHl1', 'sm', 'lin_quad_mixed_cHB_cHQ1', 'lin_quad_mixed_cHbox_cHW', 'sm_lin_quad_mixed_cHWB_cHbox', 'lin_quad_mixed_cHW_cHQ1', 'lin_cW']
EFT_samples_datacard = [i for i in EFT_samples if not i.startswith("lin")]

EFT_samples_dropped = [i for i in EFT_samples if i not in EFT_samples_datacard]

# uncomment for mkDatacard
# samples = {k: j for k,j in samples.items() if k not in EFT_samples_dropped}

# Only EFT
samples = {k: j for k,j in samples.items() if k in EFT_samples}

#########################################
