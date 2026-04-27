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
mcSteps = 'iniGENStep__iniGENStep2' 

#from VBS
dataSteps = 'DATAl1loose2018v9'

MC_skim = '2Jets1leptonW2018'

DATA_skim = 'DATA2Jets1leptonW2018'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDirHWW = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirLat = '/eos/cms/store/group/phys_smp/ec/Latinos/HWWNano'
  treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

def makeMCDirectory(var=''):
  if var:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
  else:
      return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectoryHWW = os.path.join(treeBaseDirHWW,  mcProduction , mcSteps)
mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
mcDirectoryLatSig = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
# mcDirectoryLat = mcDirectoryHWW
# mcDirectoryHWW = mcDirectoryLat
# mcDirectoryHWW = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + MC_skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeRe
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
dataDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps)
# dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + DATA_skim)


################################################
############ BASIC MC WEIGHTS ##################
################################################
#corrected trigger efficiency

XSWeight   = 'XSWeight'

# # ##########################################
# # ############  BACKGROUNDS  ###############
# # ##########################################


fiducial = '(((abs(Alt$(DressedLepton_pdgId[0],0))==11) + (abs(Alt$(DressedLepton_pdgId[0],0))==13))>0) \
            && (Alt$(DressedLepton_pt[0],0)>=20.) \
            && (Alt$(CleanGenJet_pt[0],0)>=60.) \
            && (Alt$(CleanGenJet_pt[1],0)>=60.) \
            && (Alt$(mjj_gen,0)>=300.) \
            && (Alt$(detajj_gen,0)>=4.) \
            && (Alt$(abs(DressedLepton_eta[0]),999.)<2.) \
            && (Alt$(abs(CleanGenJet_eta[0]),999.)<4.7) \
            && (Alt$(abs(CleanGenJet_eta[1]),999.)<4.7) \
            && (Alt$(nCleanGenJet20,0)>=2)'
            
fiducialw = fiducial.replace("&&","*")

samples['WLNuJJ_MG_LO_PY8_NANOAOD'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : XSWeight+'*'+fiducialw
}

samples['WLNuJJ_SHERPA_LO_J'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wewk_SHERPA_LO_J'),
        'weight' : XSWeight+'*'+fiducialw
}

samples['WLNuJJ_POWHEG_PY8'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wewk_POWHEG_PYTHIA_NLO_Wpe')
                + nanoGetSampleFiles(mcDirectoryLatSig,'Wewk_POWHEG_PYTHIA_NLO_Wpm')
                + nanoGetSampleFiles(mcDirectoryLatSig,'Wewk_POWHEG_PYTHIA_NLO_Wme')
                + nanoGetSampleFiles(mcDirectoryLatSig,'Wewk_POWHEG_PYTHIA_NLO_Wmm'),
        'weight' : XSWeight+'*'+fiducialw
}

samples['WLNuJJ_MG_LO_PY8_NANOGEN'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wewk_MG_PYTHIA_LO_Wp')
                + nanoGetSampleFiles(mcDirectoryLatSig,'Wewk_MG_PYTHIA_LO_Wm'),
        'weight' : XSWeight+'*'+fiducialw
}