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


##############
# EFT samples

tapSamples = nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT')
tamSamples = nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT')
mupSamples = nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT')
mumSamples = nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT')
epSamples = nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT')
emSamples = nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT')

##############


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

########### DY ############

DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'

samples['DY'] = {    'name'   :   nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50') #Don't use LO(_ext0)! DYMVA Training!
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_ext2')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-10to50-LO_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-2500toInf')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-100to200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-200to400')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-400to600')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-600toInf'),
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter +'*btagSF_corr_DY',# missing ewkNLOW
                       'FilesPerJob' : 6,
                       'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                   }

CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext2'])
addSampleWeight(samples,'DY','DYJetsToLL_M-50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1','DY_LO_pTllrw') 
addSampleWeight(samples,'DY','DYJetsToLL_M-50',               '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',          '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1',   '(LHE_HT < 100)')   
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100',    'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',   'DY_LO_pTllrw * 1.000') #HT stitching correction
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',   'DY_LO_pTllrw * 0.999')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600',   'DY_LO_pTllrw * 0.990')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',   'DY_LO_pTllrw * 0.975')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',  'DY_LO_pTllrw * 0.907')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500', 'DY_LO_pTllrw * 0.833')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',  'DY_LO_pTllrw * 1.015')  
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-100to200','DY_LO_pTllrw') 
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-200to400','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf','DY_LO_pTllrw')


################################
############ Top ############

samples['top'] = {    'name'   :   nanoGetSampleFiles(directory_bkg,'TTTo2L2Nu')
                                 + nanoGetSampleFiles(directory_bkg,'ST_s-channel_ext1') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_tW_antitop_ext1') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_tW_top_ext1') 
                                 + nanoGetSampleFiles(directory_bkg,'TTToSemiLeptonic') 
                                 + nanoGetSampleFiles(directory_bkg,'TTWjets'),
                                #+  nanoGetSampleFiles(directory_bkg,'TTWJetsToLNu'), #also this is available
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC +'*btagSF_corr_top',
                     'FilesPerJob' : 4,
                     'EventsPerJob' : 70000,
                     'suppressNegative' :['all'],
                     'suppressNegativeNuisances' :['all'],
                 }
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
#addSampleWeight(samples,'top','TTZjets','Top_pTrw')
#addSampleWeight(samples,'top','TTWjets','Top_pTrw')

#Not corrected in baseW, so we should correct the XS here
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


################################
### Wjets samples

Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '

for iwboost, wjbin_boost in enumerate(wjets_boost_bins):
  samples[wjbin_boost] = { 'name' :   
            nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu-LO')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT70_100')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT100_200')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT200_400')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT400_600')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT600_800')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT800_1200')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT1200_2500')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_boost], 'WJetsToLNu_HT2500_inf'),
          'weight': "( fit_bin_boost == {} )*".format(iwboost+1) +XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + Wjets_photon_filter +  '* ewknloW * btagSF_corr_Wjets_HT',
          'FilesPerJob' : 10 #nfiles_wjets_boost[iwboost],   
      }

  # Fix Wjets binned + LO 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu-LO', '(LHE_HT < 70)') 
  ############
  # HT stiching corrections 2018
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT70_100',    '1.21 * 0.95148')  #adding also k-factor
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT100_200',   '0.9471') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT200_400',   '0.9515') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT400_600',   '0.9581') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT600_800',   '1.0582') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT800_1200',  '1.1285') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT1200_2500', '1.3268') 
  addSampleWeight(samples,wjbin_boost, 'WJetsToLNu_HT2500_inf',  '2.7948') 
  
###################################################3
for iwres, wjbin_res in enumerate(wjets_res_bins):
  samples[wjbin_res] = { 'name' :   
            nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu-LO')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT70_100')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT100_200')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT200_400')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT400_600')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT600_800')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT800_1200')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT1200_2500')
            + nanoGetSampleFiles(directory_wjets_bins[wjbin_res], 'WJetsToLNu_HT2500_inf'),
          'weight': "( fit_bin_res == {} )*".format(iwres+1) +XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + Wjets_photon_filter +  '* ewknloW * btagSF_corr_Wjets_HT',
          'FilesPerJob' : 10#files_wjets_res[iwres],   
      }

  # Fix Wjets binned + LO 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu-LO', '(LHE_HT < 70)') 
  ############
  # HT stiching corrections 2018
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT70_100',    '1.21 * 0.95148')  #adding also k-factor
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT100_200',   '0.9471') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT200_400',   '0.9515') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT400_600',   '0.9581') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT600_800',   '1.0582') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT800_1200',  '1.1285') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT1200_2500', '1.3268') 
  addSampleWeight(samples,wjbin_res, 'WJetsToLNu_HT2500_inf',  '2.7948') 
  

# ###############################################

# samples['VV']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
#                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD',) +
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD',  ) ,
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }

############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'ZZZ')
                                + nanoGetSampleFiles(directory_bkg,'WZZ')
                                + nanoGetSampleFiles(directory_bkg,'WWZ')
                                + nanoGetSampleFiles(directory_bkg,'WWW'),
                                #+ nanoGetSampleFiles(directory_bkg,'WWG'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW',
                    'FilesPerJob' : 15,
                     'EventsPerJob' : 70000,
                  }

 ############## VBF-V ########

# samples['VBF-V']  = {  'name'   :  
#                                     nanoGetSampleFiles(directory_bkg,'WLNuJJ_EWK') +
#                                   nanoGetSampleFiles(directory_bkg,'EWKZ2Jets_ZToLL_M-50'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_Vg_VgS_VBFV',
#                     'FilesPerJob' : 15,
#                     'EventsPerJob' : 70000,
#                   }

samples['VBF-V_dipole']  = {  'name'   :  
                                    nanoGetSampleFiles(directory_bkg,'EWK_LNuJJ_herwig') +
                                  nanoGetSampleFiles(directory_bkg,'EWK_LLJJ_herwig'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_Vg_VgS_VBFV',
                    'FilesPerJob' : 8,
                    'EventsPerJob' : 70000,
                  }


################ ggWW ##################3

samples['ggWW']  = {  'name'   :  
                                  nanoGetSampleFiles(directory_bkg,'GluGluWWToLNuQQ'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VV_VVV_ggWW',
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }

##################################################
############ Vg ###################################

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(directory_bkg,'ZGToLLG'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0) *btagSF_corr_Vg_VgS_VBFV',
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }

# the following baseW correction is needed in both v5 and v6 (for Zg, Not for ZGToLLG)
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(directory_bkg,'ZGToLLG')
                                 + nanoGetSampleFiles(directory_bkg,'WZTo3LNu_mllmin01'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + ' * (gstarLow * 0.94 + gstarHigh * 1.14) *btagSF_corr_Vg_VgS_VBFV',
                      'FilesPerJob' : 15,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                      # 'subsamples': {
                      #   'L': 'gstarLow',
                      #   'H': 'gstarHigh'
                      # }
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') # *0.448 XS correction for Zg
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')



# Then corrected
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
    # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
    files = nanoGetSampleFiles(directory_data, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


#########################################
################ DATA ###################
#########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 40,         
            }

for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(directory_data,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])


# ##########################################
# ################ SIGNALS #################
# ##########################################

# # #
# # samples['VBS']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J',) + 
# #                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L', ) +
# #                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L', ) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J',) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J') +
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J') +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J') +
# #                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu') +
# #                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J',  ),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
# #        'FilesPerJob' :15,
# #        'EventsPerJob' : 70000,
# # }

samples['VBS_dipoleRecoil']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
       'FilesPerJob' :15,
       
}


# # samples['VBS_interf']  = { 'name' :  
# #                nanoGetSampleFiles(directory_interference,'WmToLNuWpTo2J_EWKQCD',) + 
# #                nanoGetSampleFiles(directory_interference,'WpToLNuWmTo2J_EWKQCD', ) +
# #                nanoGetSampleFiles(directory_interference,'WToJJZToLL_EWKQCD', ) +
# #                nanoGetSampleFiles(directory_interference,'WToLNuZTo2J_EWKQCD',) +
# #                nanoGetSampleFiles(directory_interference,'ZToLLZToJJ_EWKQCD') ,
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
# #        'FilesPerJob' :10,
# #        
# # }

# # samples['VBS_notop']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
# #               #  nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
# #               #  nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil'),
# #               #  nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil * (Sum$(abs(GenPart_pdgId)==6)==0)',
# #        'FilesPerJob' :16,
# #        
# # }

# # samples['VBS_top']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
# #               #  nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
# #               #  nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil') ,
# #               #  nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil * (Sum$(abs(GenPart_pdgId)==6)>0)',
# #        'FilesPerJob' :16,
# #        
# # }

# ####################################
# ####################################
# ### VV Samples splitting


# samples['ewk_WpWp']  = { 'name' :  nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil'),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
#        'FilesPerJob' :15,
#        
# }


# samples['ewk_WmWm']  = { 'name' :  nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil'),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
#        'FilesPerJob' :15,
#        
# }

# samples['ewk_WpWm']  = { 'name' :  
#             nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') + 
#             nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil'),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
#        'FilesPerJob' :15,
#        
# }

# samples['ewk_WpZ']  = { 'name' :  
#               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
#               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
#        'FilesPerJob' :15,
#        
# }

# samples['ewk_WmZ']  = { 'name' :  
#               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) +
#               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
#        'FilesPerJob' :15,
#        
# }

# samples['ewk_ZZ']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
#        'FilesPerJob' :15,
#        
# }

# ###############################################
# #############################################

# samples['VV_ssWW']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD'),
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         
# }


# samples['VV_osWW']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD'),
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         
# }


# samples['VV_WZjj']  = { 'name' :      
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD',) ,
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         
# }


# samples['VV_WZll']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ),
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         
# }


# samples['VV_ZZ']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD',  ) ,
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
#         'FilesPerJob' : 15,
#         
# }


###################################################################################

# EFT

###################################################################################

samples['quad_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[14] + LHEReweightingWeight[13] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[21]',
   'FilesPerJob': 1,
}

samples['lin_quad_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[8] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[19]',
   'FilesPerJob': 1,
}

samples['quad_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[6] + LHEReweightingWeight[5] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[12] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[32]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[28]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHW_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[37]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[10]',
   'FilesPerJob': 1,
}

samples['quad_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[10] + LHEReweightingWeight[9] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHB_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[43] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHW_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[38] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[2] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[20] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[23]',
   'FilesPerJob': 1,
}

samples['lin_quad_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[4] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[34]',
   'FilesPerJob': 1,
}

samples['lin_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[4] - LHEReweightingWeight[3])',
   'FilesPerJob': 1,
}

samples['quad_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[16] + LHEReweightingWeight[15] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[10] - LHEReweightingWeight[9])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHB_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[43]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHW_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[35] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[26]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHQ1_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[44]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHl1_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[39] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[18] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[17]',
   'FilesPerJob': 1,
}

samples['lin_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[12] - LHEReweightingWeight[11])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[2]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[28] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[4]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[34] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[8] - LHEReweightingWeight[7])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHl1_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[41] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[27] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[18]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[25] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['quad_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[12] + LHEReweightingWeight[11] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[31] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['quad_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[8] + LHEReweightingWeight[7] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[16] - LHEReweightingWeight[15])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[20]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[33]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHl1_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[41]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[19] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cW_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[22]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[27]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHW_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[36]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[25]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[21] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[24] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHQ1_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[44] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[17] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[10] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[14]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHW_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[38]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[29]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHW_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[36] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[33] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['quad_cW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHl1_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[40]',
   'FilesPerJob': 1,
}

samples['lin_quad_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[6] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[8]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[6]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[12]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[29] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[14] - LHEReweightingWeight[13])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHl1_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[39]',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[30]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[22] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[14] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHB_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[42]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHl1_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[40] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[16]',
   'FilesPerJob': 1,
}

samples['quad_cHWB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[4] + LHEReweightingWeight[3] - 2*LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHW_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[35]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cW_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[23] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_cHj1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[16] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHbox_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[31]',
   'FilesPerJob': 1,
}

samples['lin_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[6] - LHEReweightingWeight[5])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHB'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[32] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHWB_cHl1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[26] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[0]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHB_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[42] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHbox_cHW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[30] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['sm_lin_quad_mixed_cHWB_cHbox'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + 'LHEReweightingWeight[24]',
   'FilesPerJob': 1,
}

samples['lin_quad_mixed_cHW_cHQ1'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '(LHEReweightingWeight[37] - LHEReweightingWeight[0])',
   'FilesPerJob': 1,
}

samples['lin_cW'] = {
   'name': nanoGetSampleFiles(directory_EFT,'epVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'emVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mupVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'mumVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tapVjj_ewk_dim6_EFT') + nanoGetSampleFiles(directory_EFT,'tamVjj_ewk_dim6_EFT') ,
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '0.5*(LHEReweightingWeight[2] - LHEReweightingWeight[1])',
   'FilesPerJob': 1,
}



EFT_samples = ['quad_cHQ1', 'sm_lin_quad_mixed_cW_cHB', 'lin_quad_cHW', 'sm_lin_quad_mixed_cW_cHW', 'quad_cHbox', 'lin_quad_cHB', 'sm_lin_quad_mixed_cHbox_cHB', 'sm_lin_quad_mixed_cHWB_cHQ1', 'sm_lin_quad_mixed_cHW_cHQ1', 'sm_lin_quad_cHl1', 'quad_cHl1', 'lin_quad_mixed_cHB_cHj1', 'lin_quad_mixed_cW_cHW', 'lin_quad_cW', 'lin_quad_mixed_cW_cHl1', 'sm_lin_quad_mixed_cW_cHj1', 'lin_quad_cHWB', 'sm_lin_quad_mixed_cHbox_cHj1', 'lin_cHWB', 'sm_lin_quad_cHWB', 'lin_cHl1', 'sm_lin_quad_mixed_cHB_cHj1', 'lin_quad_mixed_cHW_cHl1', 'lin_quad_mixed_cW_cHj1', 'sm_lin_quad_mixed_cHQ1_cHj1', 'lin_quad_mixed_cHl1_cHB', 'lin_quad_mixed_cW_cHbox', 'sm_lin_quad_mixed_cW_cHWB', 'lin_cHB', 'sm_lin_quad_cW', 'lin_quad_mixed_cHWB_cHQ1', 'quad_cHj1', 'lin_quad_mixed_cHbox_cHj1', 'lin_cHW', 'lin_quad_mixed_cHl1_cHj1', 'lin_quad_mixed_cHWB_cHB', 'sm_lin_quad_mixed_cW_cHbox', 'lin_quad_mixed_cHWB_cHW', 'quad_cHB', 'lin_quad_mixed_cHbox_cHl1', 'quad_cHW', 'lin_cHj1', 'sm_lin_quad_mixed_cW_cHl1', 'sm_lin_quad_mixed_cHbox_cHQ1', 'sm_lin_quad_mixed_cHl1_cHj1', 'lin_quad_mixed_cHW_cHj1', 'sm_lin_quad_mixed_cW_cHQ1', 'sm_lin_quad_mixed_cHWB_cHB', 'sm_lin_quad_mixed_cHW_cHB', 'sm_lin_quad_mixed_cHWB_cHW', 'lin_quad_mixed_cW_cHB', 'lin_quad_mixed_cHWB_cHbox', 'lin_quad_mixed_cHQ1_cHj1', 'lin_quad_mixed_cW_cHWB', 'lin_quad_cHl1', 'sm_lin_quad_cHQ1', 'sm_lin_quad_mixed_cHW_cHj1', 'sm_lin_quad_mixed_cHWB_cHj1', 'lin_quad_mixed_cHW_cHB', 'lin_quad_mixed_cHbox_cHQ1', 'quad_cW', 'sm_lin_quad_mixed_cHl1_cHQ1', 'lin_quad_cHbox', 'sm_lin_quad_cHW', 'sm_lin_quad_cHbox', 'sm_lin_quad_cHB', 'lin_quad_mixed_cHWB_cHj1', 'lin_cHQ1', 'sm_lin_quad_mixed_cHl1_cHB', 'sm_lin_quad_mixed_cHbox_cHW', 'lin_quad_mixed_cW_cHQ1', 'lin_quad_cHQ1', 'sm_lin_quad_mixed_cHB_cHQ1', 'lin_quad_mixed_cHl1_cHQ1', 'sm_lin_quad_cHj1', 'quad_cHWB', 'sm_lin_quad_mixed_cHW_cHl1', 'sm_lin_quad_mixed_cHWB_cHl1', 'lin_quad_cHj1', 'sm_lin_quad_mixed_cHbox_cHl1', 'lin_cHbox', 'lin_quad_mixed_cHbox_cHB', 'lin_quad_mixed_cHWB_cHl1', 'sm', 'lin_quad_mixed_cHB_cHQ1', 'lin_quad_mixed_cHbox_cHW', 'sm_lin_quad_mixed_cHWB_cHbox', 'lin_quad_mixed_cHW_cHQ1', 'lin_cW']

