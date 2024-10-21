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

def makeMCDirectory(var=''):
  if var:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
  else:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
mcDirectoryLatSig = os.path.join(treeBaseDirLat,  mcProduction , mcSteps + "__" + MC_skim)
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

# # Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
# Wjets_photon_filter = '1.'
# Total_correction = 'WJets_reweight'
# # Total_correction = '1.'

# samples['Wjets_HT'] = { 'name' :   nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu-LO')
#                                    + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT70To100')
#                                    + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT100To200')
#                                    + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT200To400')
#                                    + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT400To600')
#                                    + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT600To800')
#                                    + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT800To1200')
#                                    + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT1200To2500')
#                                    + nanoGetSampleFiles(mcDirectoryLatSig, 'WJetsToLNu_HT2500ToInf'),
# #				                'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
#                         # 'weight': CommonWeight+'*' + Wjets_photon_filter +'* ewknloW' + '*' +Total_correction,
#                         'weight': CommonWeight+'*' + Wjets_photon_filter + '*' + Total_correction,
# 			                	'FilesPerJob' : 6, 
#                         'subsamples': {
#                           'hardJets'  : 'hardJets',
#                           'PUJets'    : 'PUJets'
#                                     }
# 		                 }

# # # Fix Wjets binned + LO 
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
# # ############
# # # HT stiching corrections 2018
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT70To100',    '1.21 * 0.95148')  #adding also k-factor
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100To200',   '0.9471') 
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200To400',   '0.9515') 
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400To600',   '0.9581') 
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600To800',   '1.0582') 
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800To1200',  '1.1285') 
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200To2500', '1.3268') 
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500ToInf',  '2.7948') 
