import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(directory_bkg, 'Summer16_102X_nAODv7_Full2016v7', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')

samples={}

# Steps
mcSteps   = 'MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016' 
dataSteps = 'DATAl1loose2016v7__DATACombJJLNu2016'
fakeSteps = 'DATAl1loose2016v7__DATACombJJLNu2016'

##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'

directory_bkg    = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7_skim/' + mcSteps
directory_mc    = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7_skim/' + mcSteps
directory_EFT    = treeBaseDir_SMP +  'Summer16_102X_nAODv7_Full2016v7/' + mcSteps
directory_signal = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7_skim/' + mcSteps
directory_fakes  = treeBaseDir_SMP + 'Run2016_102X_nAODv7_Full2016v7_skim/'  + fakeSteps
directory_data   = treeBaseDir_SMP + 'Run2016_102X_nAODv7_Full2016v7_skim/'  + dataSteps

wjets_res_bins = []
directory_wjets_res_bins = {}
nfiles_wjets = [4,4,5,6,8,8,4,4,5,6,8,8,5,5,6,8,8,8,8,8,8]
for i in range(1, 22):
  wjbin = "Wjets_res_{}".format(i)
  wjets_res_bins.append(wjbin)
  directory_wjets_res_bins[wjbin] = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7_WjetsBins_skim/res_bin_{}/'.format(i) + mcSteps

print "Wjets bins: ", wjets_res_bins
print directory_wjets_res_bins

###############################################
# EFT samples

tapSamples = nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT')
tamSamples = nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT')
mupSamples = nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT')
mumSamples = nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT')
epSamples = nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT')
emSamples = nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT')

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
              'btagSF', 'BoostedWtagSF_nominal']

SFweight = '*'.join(SFweight1l)
     
GenLepMatch   = 'Lepton_genmatched[0]'


####
# NVTX reweighting
#SFweight += '*nvtx_reweighting'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

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


###########################################
#############  BACKGROUNDS  ###############
###########################################

############ DY ############

# DY_photon_filter = '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))'
DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'


# samples['DY'] = {    'name'   :   #nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50-LO_ext1')
#                                   nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_ext2') 
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-10to50')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-10to50_ext1')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-70to100')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-100to200')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-100to200_ext1')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400_ext1')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-400to600')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-400to600_ext1')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-600to800')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-800to1200')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-1200to2500')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-2500toInf')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-70to100')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-100to200')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-200to400')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-200to400_ext1')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-400to600')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-400to600_ext1')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-600toinf')
#                                   + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-600toinf_ext1'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+DY_photon_filter+'*btagSF_corr_DY'  ,
#                        'FilesPerJob' : 6,
#                        'EventsPerJob' : 80000,
#                        'suppressNegative' :['all'],
#                        'suppressNegativeNuisances' :['all'],
#                    }
# #addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO-ext1','DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')

# CombineBaseW(samples, 'DY', ['DYJetsToLL_M-10to50', 'DYJetsToLL_M-10to50_ext1'])
# addSampleWeight(samples,'DY','DYJetsToLL_M-10to50','DY_NLO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-10to50_ext1','DY_NLO_pTllrw')

# CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-100to200', 'DYJetsToLL_M-50_HT-100to200_ext1'])
# CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-200to400', 'DYJetsToLL_M-50_HT-200to400_ext1'])
# CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-400to600', 'DYJetsToLL_M-50_HT-400to600_ext1'])
# CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-200to400', 'DYJetsToLL_M-5to50_HT-200to400_ext1'])
# CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-400to600', 'DYJetsToLL_M-5to50_HT-400to600_ext1'])
# CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-600toinf', 'DYJetsToLL_M-5to50_HT-600toinf_ext1'])

# #addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO_ext1',            '(LHE_HT < 70)')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',               '(LHE_HT < 70)') # last M50 HT bin is missing
# addSampleWeight(samples,'DY','DYJetsToLL_M-10to50',                '(LHE_HT < 70)')
# addSampleWeight(samples,'DY','DYJetsToLL_M-10to50_ext1',           '(LHE_HT < 70)')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100',         'DY_LO_pTllrw') # HT-binned are LO!
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',        'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200_ext1',   'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',        'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1',   'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600',        'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600_ext1',   'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',        'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',       'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500',      'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',       'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-70to100',      'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-100to200',     'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-200to400',     'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-200to400_ext1','DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-400to600',     'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-400to600_ext1','DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-600toinf',     'DY_LO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-600toinf_ext1','DY_LO_pTllrw')



############ Top ############

# samples['top'] = {    
#             'name'   :  
#                         nanoGetSampleFiles(directory_bkg,'ST_s-channel') 
#                       + nanoGetSampleFiles(directory_bkg,'ST_t-channel_antitop') 
#                       + nanoGetSampleFiles(directory_bkg,'ST_t-channel_top') 
#                       + nanoGetSampleFiles(directory_bkg,'ST_tW_antitop') 
#                       + nanoGetSampleFiles(directory_bkg,'ST_tW_top') 
#                       + nanoGetSampleFiles(directory_bkg,'TTToSemiLeptonic') 
#                       + nanoGetSampleFiles(directory_bkg,'TTTo2L2Nu') 
#                       + nanoGetSampleFiles(directory_bkg,'TTWJetsToLNu_ext2') 
#                       + nanoGetSampleFiles(directory_bkg,'TTZjets'),  
#             'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_top',
#             'FilesPerJob' : 5,
#             'EventsPerJob' : 80000,
#             'suppressNegative' :['all'],
#             'suppressNegativeNuisances' :['all'],
#       }

# addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
# addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
# #addSampleWeight(samples,'top','TTZjets','Top_pTrw')
# #addSampleWeight(samples,'top','TTWjets_ext1','Top_pTrw')

# addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
# addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


#######################################################
### W+jets treatment

Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '

# samples['Wjets_boost'] = { 'name' :   
#           #nanoGetSampleFiles(directory_bkg, 'WJetsToLNu')  #NLO inclusive samples
#           nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO_ext2')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT70_100')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT100_200')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT100_200_ext2')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT200_400')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT200_400_ext2')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT400_600')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT400_600_ext1')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT600_800')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT600_800_ext1')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT800_1200')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT800_1200_ext1')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT1200_2500')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT1200_2500_ext1')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT2500_inf')
#           + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT2500_inf_ext1')
#           ,
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*'+Wjets_photon_filter + '* EWKnloW * btagSF_corr_Wjets_HT', 
#         'FilesPerJob' : 4,
#          'subsamples': {
#             "1": '(VBS_category==0) && (w_lep_pt < 50)',
#             "2": '(VBS_category==0) && (w_lep_pt >= 50 && w_lep_pt < 100)',
#             "3": '(VBS_category==0) && (w_lep_pt >= 100 && w_lep_pt < 150)',
#             "4": '(VBS_category==0) && (w_lep_pt >= 150 && w_lep_pt < 200)',
#             "5": '(VBS_category==0) && (w_lep_pt >= 200 && w_lep_pt < 300)',
#             "6": '(VBS_category==0) && (w_lep_pt >= 300 && w_lep_pt < 400)',
#             "7": '(VBS_category==0) && (w_lep_pt >= 400)',
#         }
#        }
# # No needed HT stiching corrections
# #addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu', '(LHE_HT < 70)') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu-LO_ext2', '(LHE_HT < 70)') 
# CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu-LO','WJetsToLNu-LO_ext2'])

# CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT100_200','WJetsToLNu_HT100_200_ext2'])
# CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT200_400','WJetsToLNu_HT200_400_ext2'])
# CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT400_600','WJetsToLNu_HT400_600_ext1'])
# CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT600_800','WJetsToLNu_HT600_800_ext1'])
# CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT800_1200','WJetsToLNu_HT800_1200_ext1'])
# CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT1200_2500','WJetsToLNu_HT1200_2500_ext1'])
# CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT2500_inf','WJetsToLNu_HT2500_inf_ext1'])

# # HT bins to LO factors 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT70_100',          '1.21 * 1.0346')  #adding also k-factor
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT100_200',         '1.019') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT100_200_ext2',    '1.019') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT200_400',         '1.012') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT200_400_ext2',    '1.012') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT400_600',         '0.9945') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT400_600_ext1',    '0.9945')
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT600_800',         '0.9537') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT600_800_ext1',    '0.9537') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT800_1200',        '0.8844') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT800_1200_ext1',   '0.8844')
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT1200_2500',       '0.7643') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT1200_2500_ext1',  '0.7643') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT2500_inf',        '0.2422') 
# addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT2500_inf_ext1',   '0.2422') 

# ####################
# #Resolved bin 
# for iw, wjetbin in enumerate(wjets_res_bins):
#   samples[wjetbin] = { 'name' :   
#             #nanoGetSampleFiles(directory_bkg, 'WJetsToLNu')  #NLO inclusive samples
#             nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu-LO')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu-LO_ext2')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT70_100')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT100_200')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT100_200_ext2')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT200_400')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT200_400_ext2')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT400_600')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT400_600_ext1')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT600_800')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT600_800_ext1')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT800_1200')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT800_1200_ext1')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT1200_2500')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT1200_2500_ext1')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT2500_inf')
#             + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT2500_inf_ext1')
#             ,
#           'weight': "( fit_bin_res == {} )*".format(iw+1) + XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*'+Wjets_photon_filter + '* EWKnloW * btagSF_corr_Wjets_HT', 
#           'FilesPerJob' : nfiles_wjets[iw],
#         }
#   # No needed HT stiching corrections
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu-LO', '(LHE_HT < 70)') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu-LO_ext2', '(LHE_HT < 70)') 
#   CombineBaseW(samples, wjetbin, ['WJetsToLNu-LO','WJetsToLNu-LO_ext2'])

#   CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT100_200','WJetsToLNu_HT100_200_ext2'])
#   CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT200_400','WJetsToLNu_HT200_400_ext2'])
#   CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT400_600','WJetsToLNu_HT400_600_ext1'])
#   CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT600_800','WJetsToLNu_HT600_800_ext1'])
#   CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT800_1200','WJetsToLNu_HT800_1200_ext1'])
#   CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT1200_2500','WJetsToLNu_HT1200_2500_ext1'])
#   CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT2500_inf','WJetsToLNu_HT2500_inf_ext1'])

#   # HT bins to LO factors 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT70_100',          '1.21 * 1.0346')  #adding also k-factor
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT100_200',         '1.019') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT100_200_ext2',    '1.019') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT200_400',         '1.012') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT200_400_ext2',    '1.012') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT400_600',         '0.9945') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT400_600_ext1',    '0.9945')
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT600_800',         '0.9537') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT600_800_ext1',    '0.9537') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT800_1200',        '0.8844') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT800_1200_ext1',   '0.8844')
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT1200_2500',       '0.7643') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT1200_2500_ext1',  '0.7643') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT2500_inf',        '0.2422') 
#   addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT2500_inf_ext1',   '0.2422') 

# #############################################################################
# ###########################################################################


# samples['VV']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD') ,
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VV_VVV_ggWW',
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }

############ VVV ############

# samples['VVV']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'ZZZ')
#                                 + nanoGetSampleFiles(directory_bkg,'WZZ')
#                                 + nanoGetSampleFiles(directory_bkg,'WWZ')
#                                 + nanoGetSampleFiles(directory_bkg,'WWW'),
#                                 #+ nanoGetSampleFiles(directory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VV_VVV_ggWW'  ,
#                     'FilesPerJob' : 12,
#                     'EventsPerJob' : 70000,
#                   }

############## VBF-V ########

# samples['VBF-V']  = {  'name'   : nanoGetSampleFiles(directory_signal,'EWK_LNuJJ')
#                                 + nanoGetSampleFiles(directory_signal,'EWK_LLJJ'), 
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_Vg_VgS_VBFV',
#                     'FilesPerJob' : 15
#                   }

# samples['VBF-V_dipole']  = {  'name'   : nanoGetSampleFiles(directory_signal,'EWK_LNuJJ_herwig')
#                                        + nanoGetSampleFiles(directory_signal,'EWK_LLJJ_herwig'), 
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_Vg_VgS_VBFV',
#                     'FilesPerJob' : 6
#                   }

################ ggWW ##################3

# samples['ggWW']  = {  'name'   :  
#                                   nanoGetSampleFiles(directory_bkg,'GluGluWWToLNuQQ'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VV_VVV_ggWW',
#                     'FilesPerJob' : 15,
#                     'EventsPerJob' : 70000,
#                   }

########################

# samples['Vg']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
#                                + nanoGetSampleFiles(directory_bkg,'Zg'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(!(Gen_ZGstar_mass > 0))*btagSF_corr_Vg_VgS_VBFV', # 14.02.2020: Changed Vg treatment
#                     'FilesPerJob' : 15,
#                     'EventsPerJob' : 70000,
#                     'suppressNegative' :['all'],
#                     'suppressNegativeNuisances' :['all'],
#                   }

#addSampleWeight(samples,'Vg','Zg','(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')


############ VgS ############

# samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
#                                  + nanoGetSampleFiles(directory_bkg,'Zg')
#                                  + nanoGetSampleFiles(directory_bkg,'WZTo3LNu_mllmin01'),
#                                  #+ nanoGetSampleFiles(directory_bkg,'WZTo3LNu_mllmin01_ext1'),
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + ' * (gstarLow * 0.94 + gstarHigh * 1.14) *btagSF_corr_Vg_VgS_VBFV',
#                       'FilesPerJob' : 15,
#                       'EventsPerJob' : 80000,
#                       'suppressNegative' :['all'],
#                       'suppressNegativeNuisances' :['all'],
                
#                    }
#CombineBaseW(samples, 'VgS', ['WZTo3LNu_mllmin01', 'WZTo3LNu_mllmin01_ext1'])

# # 14.02.2020: Changed Vg treatment
# addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
# addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass > 0)')
# addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')
# #addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01_ext1', '(Gen_ZGstar_mass > 0.1)')

# #fakeW = 'fakeW_ele_' + eleWP + '_mu_' +muWP+ '_1l_mu35_ele35'
# # from alias
# fakeW = 'fakeWeight_35'
# #### Fakes
# samples['Fake'] = {
#   'name': [],
#   'weight': METFilter_DATA+'*'+fakeW,
#   'weights': [],
#   'isData': ['all'],
#   'FilesPerJob' : 40
# }

# for _, sd in DataRun:
#   for pd in DataSets:
#     files = nanoGetSampleFiles(directory_data, pd + '_' + sd)
#     samples['Fake']['name'].extend(files)
#     samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


##########################################
################# DATA ###################
##########################################

# samples['DATA']  = {   'name': [ ] ,
#                        'weight' : METFilter_DATA+'*'+LepWPCut,
#                        'weights' : [ ],
#                        'isData': ['all'],
#                        'FilesPerJob' : 40,
#                   }

# for Run in DataRun :
#         for DataSet in DataSets :
#                 FileTarget = nanoGetSampleFiles(directory_data,DataSet+'_'+Run[1])
#                 for iFile in FileTarget:
#                         samples['DATA']['name'].append(iFile)
#                         samples['DATA']['weights'].append(DataTrig[DataSet])


##########################################
################ SIGNALS #################
##########################################

# samples['VBS_ssWW']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil'),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
#        'FilesPerJob' :10,
#        'EventsPerJob' : 70000,
# }

# samples['VBS_osWW']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil'),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
#        'FilesPerJob' :10,
#        'EventsPerJob' : 70000,
# }


# samples['VBS_WZjj']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
#        'FilesPerJob' :10,
#        'EventsPerJob' : 70000,
# }

# samples['VBS_WZll']  = { 'name' :   
#                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
#        'FilesPerJob' :10,
#        'EventsPerJob' : 70000,
# }


# samples['VBS_ZZ']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
#        'FilesPerJob' :10,
#        'EventsPerJob' : 70000,
# }



###############################################
#############################################

# samples['VV_ssWW']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD'),
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }


# samples['VV_osWW']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD'),
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }


# samples['VV_WZjj']  = { 'name' :      
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD',) ,
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }


# samples['VV_WZll']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ),
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }


# samples['VV_ZZ']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD',  ) ,
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }


####################################

samples['quad_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[14] + LHEReweightingWeight[13] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cW_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[21]',
   'FilesPerJob': 60,
}

samples['lin_quad_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[8] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cW_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[19]',
   'FilesPerJob': 60,
}

samples['quad_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[6] + LHEReweightingWeight[5] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[12] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHbox_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[32]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHWB_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[28]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHW_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[37]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[10]',
   'FilesPerJob': 60,
}

samples['quad_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[10] + LHEReweightingWeight[9] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHB_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[43] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHW_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[38] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_cW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[2] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cW_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[20] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cW_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[23]',
   'FilesPerJob': 60,
}

samples['lin_quad_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[4] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHbox_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[34]',
   'FilesPerJob': 60,
}

samples['lin_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[4] - LHEReweightingWeight[3])',
   'FilesPerJob': 60,
}

samples['quad_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[16] + LHEReweightingWeight[15] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[10] - LHEReweightingWeight[9])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHB_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[43]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHW_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[35] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHWB_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[26]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHQ1_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[44]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHl1_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[39] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cW_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[18] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cW_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[17]',
   'FilesPerJob': 60,
}

samples['lin_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[12] - LHEReweightingWeight[11])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_cW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[2]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHWB_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[28] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[4]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHbox_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[34] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[8] - LHEReweightingWeight[7])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHl1_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[41] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHWB_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[27] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cW_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[18]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHWB_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[25] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['quad_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[12] + LHEReweightingWeight[11] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHbox_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[31] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['quad_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[8] + LHEReweightingWeight[7] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[16] - LHEReweightingWeight[15])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cW_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[20]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHbox_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[33]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHl1_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[41]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cW_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[19] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cW_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[22]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHWB_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[27]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHW_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[36]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHWB_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[25]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cW_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[21] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHWB_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[24] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHQ1_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[44] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cW_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[17] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[10] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[14]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHW_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[38]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHWB_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[29]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHW_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[36] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHbox_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[33] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['quad_cW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHl1_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[40]',
   'FilesPerJob': 60,
}

samples['lin_quad_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[6] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[8]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[6]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[12]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHWB_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[29] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[14] - LHEReweightingWeight[13])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHl1_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[39]',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHbox_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[30]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cW_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[22] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[14] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHB_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[42]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHl1_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[40] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[16]',
   'FilesPerJob': 60,
}

samples['quad_cHWB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[4] + LHEReweightingWeight[3] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHW_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[35]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cW_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[23] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_cHj1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[16] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHbox_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[31]',
   'FilesPerJob': 60,
}

samples['lin_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[6] - LHEReweightingWeight[5])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHbox_cHB'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[32] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHWB_cHl1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[26] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[0]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHB_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[42] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHbox_cHW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[30] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['sm_lin_quad_mixed_cHWB_cHbox'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + 'LHEReweightingWeight[24]',
   'FilesPerJob': 60,
}

samples['lin_quad_mixed_cHW_cHQ1'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '(LHEReweightingWeight[37] - LHEReweightingWeight[0])',
   'FilesPerJob': 60,
}

samples['lin_cW'] = {
   'name': tapSamples + tamSamples + mupSamples + mumSamples + epSamples + emSamples    ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS' + '*' + '0.5*(LHEReweightingWeight[2] - LHEReweightingWeight[1])',
   'FilesPerJob': 60,
}

#########################################

VBS_samples = ["ewk_WpZ", "ewk_WmZ", "ewk_ZZ", "ewk_WpWm", "ewk_WpWp", "ewk_WmWm"]
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]

EFT_samples = ['quad_cHQ1', 'sm_lin_quad_mixed_cW_cHB', 'lin_quad_cHW', 'sm_lin_quad_mixed_cW_cHW', 'quad_cHbox', 'lin_quad_cHB', 'sm_lin_quad_mixed_cHbox_cHB', 'sm_lin_quad_mixed_cHWB_cHQ1', 'sm_lin_quad_mixed_cHW_cHQ1', 'sm_lin_quad_cHl1', 'quad_cHl1', 'lin_quad_mixed_cHB_cHj1', 'lin_quad_mixed_cW_cHW', 'lin_quad_cW', 'lin_quad_mixed_cW_cHl1', 'sm_lin_quad_mixed_cW_cHj1', 'lin_quad_cHWB', 'sm_lin_quad_mixed_cHbox_cHj1', 'lin_cHWB', 'sm_lin_quad_cHWB', 'lin_cHl1', 'sm_lin_quad_mixed_cHB_cHj1', 'lin_quad_mixed_cHW_cHl1', 'lin_quad_mixed_cW_cHj1', 'sm_lin_quad_mixed_cHQ1_cHj1', 'lin_quad_mixed_cHl1_cHB', 'lin_quad_mixed_cW_cHbox', 'sm_lin_quad_mixed_cW_cHWB', 'lin_cHB', 'sm_lin_quad_cW', 'lin_quad_mixed_cHWB_cHQ1', 'quad_cHj1', 'lin_quad_mixed_cHbox_cHj1', 'lin_cHW', 'lin_quad_mixed_cHl1_cHj1', 'lin_quad_mixed_cHWB_cHB', 'sm_lin_quad_mixed_cW_cHbox', 'lin_quad_mixed_cHWB_cHW', 'quad_cHB', 'lin_quad_mixed_cHbox_cHl1', 'quad_cHW', 'lin_cHj1', 'sm_lin_quad_mixed_cW_cHl1', 'sm_lin_quad_mixed_cHbox_cHQ1', 'sm_lin_quad_mixed_cHl1_cHj1', 'lin_quad_mixed_cHW_cHj1', 'sm_lin_quad_mixed_cW_cHQ1', 'sm_lin_quad_mixed_cHWB_cHB', 'sm_lin_quad_mixed_cHW_cHB', 'sm_lin_quad_mixed_cHWB_cHW', 'lin_quad_mixed_cW_cHB', 'lin_quad_mixed_cHWB_cHbox', 'lin_quad_mixed_cHQ1_cHj1', 'lin_quad_mixed_cW_cHWB', 'lin_quad_cHl1', 'sm_lin_quad_cHQ1', 'sm_lin_quad_mixed_cHW_cHj1', 'sm_lin_quad_mixed_cHWB_cHj1', 'lin_quad_mixed_cHW_cHB', 'lin_quad_mixed_cHbox_cHQ1', 'quad_cW', 'sm_lin_quad_mixed_cHl1_cHQ1', 'lin_quad_cHbox', 'sm_lin_quad_cHW', 'sm_lin_quad_cHbox', 'sm_lin_quad_cHB', 'lin_quad_mixed_cHWB_cHj1', 'lin_cHQ1', 'sm_lin_quad_mixed_cHl1_cHB', 'sm_lin_quad_mixed_cHbox_cHW', 'lin_quad_mixed_cW_cHQ1', 'lin_quad_cHQ1', 'sm_lin_quad_mixed_cHB_cHQ1', 'lin_quad_mixed_cHl1_cHQ1', 'sm_lin_quad_cHj1', 'quad_cHWB', 'sm_lin_quad_mixed_cHW_cHl1', 'sm_lin_quad_mixed_cHWB_cHl1', 'lin_quad_cHj1', 'sm_lin_quad_mixed_cHbox_cHl1', 'lin_cHbox', 'lin_quad_mixed_cHbox_cHB', 'lin_quad_mixed_cHWB_cHl1', 'sm', 'lin_quad_mixed_cHB_cHQ1', 'lin_quad_mixed_cHbox_cHW', 'sm_lin_quad_mixed_cHWB_cHbox', 'lin_quad_mixed_cHW_cHQ1', 'lin_cW']
EFT_samples_datacard = [i for i in EFT_samples if not i.startswith("lin")]

EFT_samples_dropped = [i for i in EFT_samples if i not in EFT_samples_datacard]

samples = {k: j for k,j in samples.items() if k == "sm"}

# samples = {   key:v for key,v in samples.items() if key in VBS_samples}