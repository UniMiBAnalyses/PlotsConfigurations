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


mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
dataDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps)

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V2Iso_WP90_tthmva_70'
muWP='cut_Tight_HWWW_tthmva_80'


LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF[0]'

trigg_MC = '( (abs(Lepton_pdgId[0])==13) * (HLT_IsoMu24 > 0.5) || (abs(Lepton_pdgId[0])==11) * (HLT_Ele32_WPTight_Gsf > 0.5) )'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################
#corrected trigger efficiency

XSWeight   = 'XSWeight'
SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'TriggerSFWeight_1l', trigg_MC, 'L1PreFiringWeight_Nom'] 
# SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', 'btagSF','PUJetIdSF', 'TriggerSFWeight_1l', trigg_MC] 
# SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'SingleLepton_trigEff_corrected[0]'] 
# SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'TriggerEffWeight_1l'] 
# SFweight1l = ['puWeight', 'SingleLepton_trigEff_corrected[0]',
#               'Lepton_RecoSF[0]',LepWPWeight_1l, LepWPCut_1l,
#               'btagSF','PUJetIdSF'] 

SFweight = '*'.join(SFweight1l)

GenLepMatch   = 'Lepton_genmatched[0]'


################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

CommonWeight = XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-UL2018'] ,
            ['B','Run2018B-UL2018'] ,
            ['C','Run2018C-UL2018'] ,
            ['D','Run2018D-UL2018'] ,
          ]

DataSets = ['SingleMuon','EGamma']

DataTrig = {
            'SingleMuon' : 'Trigger_sngMu' ,
            'EGamma'     : '!Trigger_sngMu && Trigger_sngEl' 
}


# helper to init a data sample dict
def _init_data_sample():
  return {
    'name': [],
    'weight': METFilter_DATA + '*' + LepWPCut,
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 70,
  }

# 1) per-run samples
for Run in DataRun:
  runTag  = Run[0]      # 'A', 'B', ...
  runName = Run[1]      # 'Run2018A-UL2018', ...

  key = 'DATA_2018{}'.format(runTag)
  samples[key] = _init_data_sample()

  for DataSet in DataSets:
    version = 'v1'
    if DataSet == "SingleMuon" and runTag in ["A", "B", "C"]:
      version = 'v2'

    FileTarget = nanoGetSampleFiles(dataDirectoryHWW, '{}_{}-{}'.format(DataSet, runName, version))
    for iFile in FileTarget:
      samples[key]['name'].append(iFile)
      samples[key]['weights'].append(DataTrig[DataSet])

# 2) all-runs combined sample
samples['DATA'] = _init_data_sample()

for Run in DataRun:
  runTag  = Run[0]
  runName = Run[1]

  for DataSet in DataSets:
    version = 'v1'
    if DataSet == "SingleMuon" and runTag in ["A", "B", "C"]:
      version = 'v2'

    FileTarget = nanoGetSampleFiles(dataDirectoryHWW, '{}_{}-{}'.format(DataSet, runName, version))
    for iFile in FileTarget:
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])


# # #samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}

# # # mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s 2Jets1leptonW2018 -i MCl1loose2018v7__MCCorr2018v7 -b -Q workday -T  WLNuJJ_EWK,WJetsToLNu-LO,WJetsToLNu_HT70_100,WJetsToLNu_HT100_200,WJetsToLNu_HT200_400,WJetsToLNu_HT400_600,WJetsToLNu_HT600_800,WJetsToLNu_HT800_1200,WJetsToLNu_HT1200_2500,WJetsToLNu_HT2500_inf,WJetsToLNu,WJetsToLNu_Pt50to100,WJetsToLNu_Pt100to250,WJetsToLNu_Pt250to400,WJetsToLNu_Pt400to600,WJetsToLNu_Pt600toInf,TTTo2L2Nu,ST_s-channel_ext1,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop_ext1,ST_tW_top_ext1,TTToSemiLeptonic,TTZjets,TTWjets,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWW_LNu_M125,HWplusJ_HToWW_LNu_M125,VBFHToWWToLNuQQ_M125,DYJetsToLL_M-50,DYJetsToLL_M-50_ext2,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-10to50-LO_ext1,DYJetsToLL_M-4to50_HT-100to200,DYJetsToLL_M-4to50_HT-200to400,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-600toInf,EWKZ2Jets_ZToLL_M-50,Wg_MADGRAPHMLM,ZGToLLG,ZZZ,WZZ,WWZ,WWW,WJetsToLNu-0J,WJetsToLNu-1J,WJetsToLNu-2J


# # mkPostProc.py -p Summer20UL18_106x_nAODv9_Full2018v9 -s $iSyst -i MCl1loose2018v9__MCCorr2018v9NoJERInHorn -b -Q nextweek -T Wm_LNuJJ_EWK,Wp_LNuJJ_EWK,EWKZ2Jets_ZToLL_M-50,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWWTo2L2Nu_WToLNu_M125,HWplusJ_HToWWTo2L2Nu_WToLNu_M125,VBFHToWWToLNuQQ_M125,ZZZ,WZZ,WWZ,WWW,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,WGToLNuG,ZGToLLG,DYJetsToLL_M-10to50-LO,DYJetsToLL_M-4to50_HT-200to400,DYJetsToLL_M-4to50_HT-400to600,WJetsToLNu-LO,WJetsToLNu_HT70To100,WJetsToLNu_HT100To200,WJetsToLNu_HT200To400,WJetsToLNu_HT400To600,WJetsToLNu_HT600To800,WJetsToLNu_HT800To1200,WJetsToLNu_HT1200To2500,WJetsToLNu_HT2500ToInf,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,DYJetsToLL_M-50,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,WGToLNuG,ZGToLLG,WZTo3LNu_mllmin0p1

# # # # mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s DATA2Jets1leptonW2018 -i DATAl1loose2018v7__DATACombJJLNu2018 -b -Q workday