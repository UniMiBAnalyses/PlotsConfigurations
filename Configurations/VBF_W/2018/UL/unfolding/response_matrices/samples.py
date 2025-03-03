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
MC_skim = 'genStepVBFW2'



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
mcDirectoryLatSig = os.path.join(treeBaseDirLat,  mcProduction , mcSteps + "__" + MC_skim)

mcDirectoryPrivate2 = os.path.join(treeBaseDirPrivate2,  mcProduction , mcSteps)
mcDirectoryPrivate = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps)

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
CommonWeight = XSWeight

fiducial  = '(Alt$(DressedLepton_pt[0],0) >= 20.) && (Alt$(CleanGenJet_pt[1],0) >= 60.) && (Alt$(CleanGenJet_pt[0],0) >= 60.) && (Alt$(mjj_gen,0) >= 300.) && (Alt$(detajj_gen,0) >= 3.9) && (Alt$(abs(DressedLepton_eta[0]), 10) < 2) && (Alt$(abs(CleanGenJet_eta[0]), 100) < 10) && (Alt$(abs(CleanGenJet_eta[1]), 100) < 10) && (Alt$(nCleanGenJet,-1) >= 0.)'
#########################################
######### MULTIPLE SIGNALS ##############
#########################################
###### W + jj EWK #######

samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
                                    + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
                        'weight': CommonWeight,
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

# samples['WLNuJJ_inter']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryPrivate2,'WLNuJJ_EWK_QCD_interference2')
#                                           + nanoGetSampleFiles(mcDirectoryPrivate,'WLNuJJ_EWK_QCD_interference'),
# #                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                         'weight': CommonWeight,
#                         'FilesPerJob' : 5,
#                         'EventsPerJob' : 7000,
#                     }


# EFTSamples = nanoGetSampleFiles(mcDirectoryLat,'WLNuJJ_EWK_EFT')

# samples['sm'] = {
#     'name': EFTSamples,
#     'weight': CommonWeight + '*' + '(LHEReweightingWeight[0])',
#     'FilesPerJob': 30,
# }

# CMSSW=os.environ["CMSSW_BASE"]
# sampleEFTFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT_4Comb/EFTweights.py"
# if os.path.exists(CMSSW+'/src/'+sampleEFTFile):
#   handle = open(CMSSW+'/src/'+sampleEFTFile)
#   exec(handle)
#   handle.close()

# # ## fatti ma non usati per datacard
# # ######################################### debug weightssss ############################
# sampleEFTFileDebug = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT_4Comb/debug_EFTweights.py"
# if os.path.exists(CMSSW+'/src/'+sampleEFTFileDebug):
#   handle = open(CMSSW+'/src/'+sampleEFTFileDebug)
#   exec(handle)
#   handle.close()