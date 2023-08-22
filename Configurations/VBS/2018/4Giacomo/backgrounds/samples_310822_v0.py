import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # WWSS
configurations = os.path.dirname(configurations) # 2018
configurations = os.path.dirname(configurations) # VBS
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseWnAOD, addSampleWeight

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

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

MCDir = makeMCDirectory()


# MCDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'


################################################
################### WEIGHTS ####################
################################################

# ---------------------------------------- Basic MC weights
mcCommonWeightNoMatch = 'XSWeight*SFweight_mod*samesign_requirement'
mcCommonWeight = 'XSWeight*SFweight_mod*PromptGenLepMatch2l*samesign_requirement'

# ---------------------------------------- Number of leptons
Nlep='2'
#Nlep='3'
#Nlep='4'

# ---------------------------------------- Lepton WP
eleWP = 'mvaFall17V1Iso_WP90_tthmva_70'
# eleWP = 'mvaFall17V1Iso_WP90_SS'
muWP  = 'cut_Tight_HWWW_tthmva_80'
#muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

# ---------------------------------------- MET filters
METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

# ---------------------------------------- fake weights
fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP

# ---------------------------------------- Basic MC weights
XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'

################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}


################################################
################ MC SAMPLES ####################
################################################

# ---------------------------------------- SSWW - WZ
files = nanoGetSampleFiles(MCDir, 'WpWpJJ_EWK')
samples['SSWW'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(MCDir, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# ---------------------------------------- WW QCD
files = nanoGetSampleFiles(MCDir, 'WpWpJJ_QCD')
samples['WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# ---------------------------------------- WZ QCD
# samples['WZ_QCD'] = {
#     'name': nanoGetSampleFiles(MCDir, 'WLLJJToLNu_M-50_QCD_0Jet') + \
#             nanoGetSampleFiles(MCDir, 'WLLJJToLNu_M-50_QCD_1Jet') + \
#             nanoGetSampleFiles(MCDir, 'WLLJJToLNu_M-50_QCD_3Jet') + \
#             nanoGetSampleFiles(MCDir, 'WLLJJToLNu_M-4To50_QCD_0Jet') + \
#             nanoGetSampleFiles(MCDir, 'WLLJJToLNu_M-4To50_QCD_2Jet') + \
#             nanoGetSampleFiles(MCDir, 'WLLJJToLNu_M-4To50_QCD_3Jet'),
#     'weight': mcCommonWeight+'*1.2',
#     'FilesPerJob': 4
# }
files = nanoGetSampleFiles(MCDir, 'WZTo3LNu')
samples['WZ_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# ---------------------------------------- ZZ 
samples['ZZ'] = {  'name'  :   nanoGetSampleFiles(MCDir,'ZZTo2L2Nu_ext1')
                             + nanoGetSampleFiles(MCDir,'ZZTo2L2Nu_ext2')
                             + nanoGetSampleFiles(MCDir,'ZZTo2L2Q')
                             + nanoGetSampleFiles(MCDir,'ZZTo4L_ext1')
                             + nanoGetSampleFiles(MCDir,'ZZTo4L_ext2')
                             + nanoGetSampleFiles(MCDir,'ggZZ4m')
                             + nanoGetSampleFiles(MCDir,'ggZZ4m_ext1')
                             + nanoGetSampleFiles(MCDir,'ggZZ4t')
                             + nanoGetSampleFiles(MCDir,'ggZZ2e2t')
                             + nanoGetSampleFiles(MCDir,'ggZZ2m2t')
                             + nanoGetSampleFiles(MCDir,'ggZZ2e2m'),
                    'weight' :  XSWeight+'*samesign_requirement*'+SFweight+'*((nLepton==2)*PromptGenLepMatch2l + (nLepton==3)*PromptGenLepMatch3l + (nLepton>3)*PromptGenLepMatch4l)*'+METFilter_MC,
                    'FilesPerJob' : 3,
                 }

ZZ2LbaseW   = getBaseWnAOD(MCDir,'Autumn18_102X_nAODv7_Full2018v7',['ZZTo2L2Nu_ext1','ZZTo2L2Nu_ext2'])
ZZ4LbaseW   = getBaseWnAOD(MCDir,'Autumn18_102X_nAODv7_Full2018v7',['ZZTo4L_ext1',   'ZZTo4L_ext2'])
ggZZbaseW   = getBaseWnAOD(MCDir,'Autumn18_102X_nAODv7_Full2018v7',['ggZZ4m',        'ggZZ4m_ext1'])

addSampleWeight(samples,'ZZ','ZZTo2L2Nu_ext1',"1.07*"+ZZ2LbaseW+"/baseW") ## The non-ggZZ NNLO/NLO k-factor, cited from https://arxiv.org/abs/1405.2219v1 
addSampleWeight(samples,'ZZ','ZZTo2L2Nu_ext2',"1.07*"+ZZ2LbaseW+"/baseW") 
addSampleWeight(samples,'ZZ','ZZTo2L2Q',      "1.07") 
addSampleWeight(samples,'ZZ','ZZTo4L_ext1',   "1.07*"+ZZ4LbaseW+"/baseW")
addSampleWeight(samples,'ZZ','ZZTo4L_ext2',   "1.07*"+ZZ4LbaseW+"/baseW") 
addSampleWeight(samples,'ZZ','ggZZ2e2t',      "1.68") ## The NLO/LO k-factor, cited from https://arxiv.org/abs/1509.06734v1
addSampleWeight(samples,'ZZ','ggZZ2m2t',      "1.68")
addSampleWeight(samples,'ZZ','ggZZ2e2m',      "1.68")
addSampleWeight(samples,'ZZ','ggZZ4m',        "1.68*"+ggZZbaseW+"/baseW")
addSampleWeight(samples,'ZZ','ggZZ4m_ext1',   "1.68*"+ggZZbaseW+"/baseW")
addSampleWeight(samples,'ZZ','ggZZ4t',        "1.68")

# files = nanoGetSampleFiles(MCDir, 'ZZTo4L_ext2')
# samples['ZZ4L'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 4
# }

# files = nanoGetSampleFiles(MCDir, 'ggZZ2m2t_CP5') + \
#         nanoGetSampleFiles(MCDir, 'ggZZ2e2t') + \
#         nanoGetSampleFiles(MCDir, 'ggZZ2e2m') + \
#         nanoGetSampleFiles(MCDir, 'ggZZ4t_CP5') + \
#         nanoGetSampleFiles(MCDir, 'ggZZ4m_ext1')
#         #nanoGetSampleFiles(MCDir, 'ggZZ4e')
# samples['ggZZ'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 4
# }

# ---------------------------------------- TTV
files = nanoGetSampleFiles(MCDir, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(MCDir, 'TTWJetsToLNu')
samples['TTV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# ---------------------------------------- tZq
files = nanoGetSampleFiles(MCDir, 'tZq_ll')
samples['tZq'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# ---------------------------------------- Vg
# need: 
# LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# old: WGJJ Zg
files = nanoGetSampleFiles(MCDir, 'ZGToLLG') + \
        nanoGetSampleFiles(MCDir, 'WGJJ')
samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 10
}
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

# ---------------------------------------- VgS1
files = nanoGetSampleFiles(MCDir, 'ZGToLLG') + \
        nanoGetSampleFiles(MCDir, 'WGJJ') + \
        nanoGetSampleFiles(MCDir, 'WZTo3LNu_mllmin01')
samples['VgS1'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS1', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS1', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS1', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1 && Gen_ZGstar_mass<4)')

# ---------------------------------------- Wrong-sign
files = nanoGetSampleFiles(MCDir, 'WWTo2L2Nu') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToENEN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToENMN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToENTN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToMNEN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToMNMN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToMNTN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToTNEN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToTNMN') + \
        nanoGetSampleFiles(MCDir, 'GluGluToWWToTNTN')
samples['WW'] = {
    'name': files,
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

# ---------------------------------------- Top
samples['Top'] = {
    'name': nanoGetSampleFiles(MCDir, 'TTTo2L2Nu') + \
            nanoGetSampleFiles(MCDir, 'ST_tW_top_ext1') + \
            nanoGetSampleFiles(MCDir, 'ST_tW_antitop_ext1'),
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 3,
}

# ---------------------------------------- DY
ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'
samples['DY'] = {
    'name': nanoGetSampleFiles(MCDir, 'DYJetsToLL_M-50_ext2') + \
            nanoGetSampleFiles(MCDir, 'DYJetsToLL_M-10to50-LO_ext1'),
    'weight':  'mcCommonWeight_os*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 3,
}

# ---------------------------------------- Higgs
samples['Higgs'] = {
    'name': nanoGetSampleFiles(MCDir, 'GluGluHToWWTo2L2Nu_M125') + \
            nanoGetSampleFiles(MCDir, 'GluGluHToTauTau_M125') + \
            nanoGetSampleFiles(MCDir, 'VBFHToWWTo2L2Nu_M125') + \
            nanoGetSampleFiles(MCDir, 'VBFHToTauTau_M125') + \
            nanoGetSampleFiles(MCDir, 'ttHToNonbb_M125'),
    'weight': 'mcCommonWeight_os',
    'FilesPerJob': 17,
}

# ---------------------------------------- others
samples['DPS'] = {
    'name': nanoGetSampleFiles(MCDir, 'WWTo2L2Nu_DoubleScattering'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
 
samples['VVV'] = {
    'name': nanoGetSampleFiles(MCDir, 'ZZZ') + \
            nanoGetSampleFiles(MCDir, 'WZZ') + \
            nanoGetSampleFiles(MCDir, 'WWZ') + \
            nanoGetSampleFiles(MCDir, 'WWW') + \
            nanoGetSampleFiles(MCDir, 'WWG'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

###########################################
################## FAKE ###################
###########################################

samples['Fake_lep']={'name': [ ] ,
                       'weight' :METFilter_DATA+'*'+fakeW+'*samesign_requirement',
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
					}


for Run in DataRun :
  FakeDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__fakeW'
  for DataSet in DataSets :
    FileTarget = getSampleFiles(FakeDir,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
      samples['Fake_lep']['name'].append(iFile)
      samples['Fake_lep']['weights'].append(DataTrig[DataSet])

###########################################
################## DATA ###################
###########################################

samples['DATA']  = 	{  'name': [ ] ,
                       'weight' :METFilter_DATA+'*'+LepWPCut+'*samesign_requirement',
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
					}

for Run in DataRun :
  #DataDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv4_14Dec_Full2018v4/DATAl1loose2018__l2loose__l2tightOR2018v4/'
  DataDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7'
  for DataSet in DataSets :
    FileTarget = getSampleFiles(DataDir,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])


# samples = {k:i for k, i in sampes.items() if k in ["VBSSSWW, DATA, Fake"]}
