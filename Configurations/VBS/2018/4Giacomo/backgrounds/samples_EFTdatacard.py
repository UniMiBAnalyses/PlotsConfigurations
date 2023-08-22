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
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
MCDir = os.path.join(treeBaseDir,  mcProduction , mcSteps)



# MCDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'


################################################
################### WEIGHTS ####################
################################################

# ---------------------------------------- Basic MC weights
mcCommonWeightNoMatch = 'XSWeight*SFweight_mod*samesign_requirement'
mcCommonWeight = 'XSWeight*SFweight_mod*PromptGenLepMatch2l*samesign_requirement'
mcCommonWeight_EFT = 'XSWeight*SFweight_mod_EFT*PromptGenLepMatch2l*samesign_requirement'
mcCommonWeight_SMP = 'XSWeight*SFweight_mod_SMP*PromptGenLepMatch2l*samesign_requirement'
# ---------------------------------------- Number of leptons
Nlep='2'
#Nlep='3'
#Nlep='4'

# ---------------------------------------- Lepton WP
eleWP = 'mvaFall17V1Iso_WP90_SS_tthmva_70'
# eleWP = 'mvaFall17V1Iso_WP90_SS'
muWP  = 'cut_Tight_HWWW_tthmva_80'
#muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

# ---------------------------------------- MET filters
METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

# ---------------------------------------- fake weights
#fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
#fakeW = 'fakeW_ele_mvaFall17V1Iso_WP90_SS_tthmva_70_mu_cut_Tight_HWWW_2l2j'
fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2j'
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
# files = nanoGetSampleFiles(MCDir, 'WpWpJJ_EWK_madgraph') #WpWpJJ_EWK 
# samples['SSWW'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 4
# }

files = nanoGetSampleFiles(MCDir, 'WLLJJ_WToLNu_EWK')
samples['WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight_EFT+'*LHEReweightingWeight[0]',
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
# TTZToLLNuNu_M-10
# TTWJetsToLNu
files = nanoGetSampleFiles(MCDir, 'TTZjets') + \
        nanoGetSampleFiles(MCDir, 'TTWjets') + \
        nanoGetSampleFiles(MCDir, 'tZq_ll')
samples['tVx'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

# ---------------------------------------- tZq
# files = nanoGetSampleFiles(MCDir, 'tZq_ll')
# samples['tZq'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 4
# }

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

samples['Fake_lep']['subsamples'] = {
  'e': 'abs(Lepton_pdgId[1]) == 11',
  'm': 'abs(Lepton_pdgId[1]) == 13'
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


# samples = {k:i for k, i in samples.items() if k in ["tVx"]}


op = ["cW", "cHDD", "cHW", "cHWB", "cHbox", "cHj1", "cHj3", "cHl1", "cHl3", "cll1", "cjj11", "cjj31", "cjj18", "cjj38"]
#op = ["cW", "cHbox"]
# the following (ls) contains the operators in the same order as in the LHEReweightingWeight vector
ls = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38']
# the following (mix) contains all the operators with mixed terms as well, in the LHEReweightingWeight order
mix = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38', 'cW_cHDD', 'cW_cHW', 'cW_cHWB', 'cW_cHbox', 'cW_cHj1', 'cW_cHj3', 'cW_cHl1', 'cW_cHl3', 'cW_cll1', 'cW_cjj11', 'cW_cjj31', 'cW_cjj18', 'cW_cjj38', 'cHDD_cHW', 'cHDD_cHWB', 'cHDD_cHbox', 'cHDD_cHj1', 'cHDD_cHj3', 'cHDD_cHl1', 'cHDD_cHl3', 'cHDD_cll1', 'cHDD_cjj11', 'cHDD_cjj31', 'cHDD_cjj18', 'cHDD_cjj38', 'cHW_cHWB', 'cHW_cHbox', 'cHW_cHj1', 'cHW_cHj3', 'cHW_cHl1', 'cHW_cHl3', 'cHW_cll1', 'cHW_cjj11', 'cHW_cjj31', 'cHW_cjj18', 'cHW_cjj38', 'cHWB_cHbox', 'cHWB_cHj1', 'cHWB_cHj3', 'cHWB_cHl1', 'cHWB_cHl3', 'cHWB_cll1', 'cHWB_cjj11', 'cHWB_cjj31', 'cHWB_cjj18', 'cHWB_cjj38', 'cHbox_cHj1', 'cHbox_cHj3', 'cHbox_cHl1', 'cHbox_cHl3', 'cHbox_cll1', 'cHbox_cjj11', 'cHbox_cjj31', 'cHbox_cjj18', 'cHbox_cjj38', 'cHj1_cHj3', 'cHj1_cHl1', 'cHj1_cHl3', 'cHj1_cll1', 'cHj1_cjj11', 'cHj1_cjj31', 'cHj1_cjj18', 'cHj1_cjj38', 'cHj3_cHl1', 'cHj3_cHl3', 'cHj3_cll1', 'cHj3_cjj11', 'cHj3_cjj31', 'cHj3_cjj18', 'cHj3_cjj38', 'cHl1_cHl3', 'cHl1_cll1', 'cHl1_cjj11', 'cHl1_cjj31', 'cHl1_cjj18', 'cHl1_cjj38', 'cHl3_cll1', 'cHl3_cjj11', 'cHl3_cjj31', 'cHl3_cjj18', 'cHl3_cjj38', 'cll1_cjj11', 'cll1_cjj31', 'cll1_cjj18', 'cll1_cjj38', 'cjj11_cjj31', 'cjj11_cjj18', 'cjj11_cjj38', 'cjj31_cjj18', 'cjj31_cjj38', 'cjj18_cjj38']

##################################
##### for PLOTTING
# for o in op:
#     ip = ls.index(o)
#     im = ls.index(o+'_m1')
#     samples['lin_'+o] = {
#         'name': files,
#         'weight': mcCommonWeight_EFT+'*rw_LIN_'+o,
#         'FilesPerJob': 4
#     }
#     samples['quad_'+o] = {
#         'name': files,
#         'weight': mcCommonWeight_EFT+'*rw_QUAD_'+o,
#         'FilesPerJob': 20
#     }
#     samples['linm1_'+o] = {
#         'name': files,
#         'weight': mcCommonWeight_EFT+'*rw_LIN_'+o,
#         'FilesPerJob': 4
#     }
#     samples['quadm1_'+o] = {
#         'name': files,
#         'weight': mcCommonWeight_EFT+'*rw_QUAD_'+o,
#         'FilesPerJob': 20
#     }

    # samples['SSWW_EFT_linquad_'+o] = {
    #     'name': files,
    #     'weight': mcCommonWeight_EFT+'*(LHEReweightingWeight['+str(ip)+'] - rw_SM)',
    #     #'weight': mcCommonWeight_EFT+'*(rw_LIN_'+o+' + rw_QUAD_'+o+')',
    #     'FilesPerJob': 20
    # }
    # samples['sm_lin_quad_'+o] = {
    #     'name': files,
    #     'weight': mcCommonWeight_EFT+'*LHEReweightingWeight['+str(ip)+']',
    #     #'weight': mcCommonWeight_EFT+'*(rw_SM + rw_LIN_'+o+' + rw_QUAD_'+o+')',
    #     'FilesPerJob': 20
    # }



##################################
########## for DATACARD
for o in op:
    ip = ls.index(o)
    im = ls.index(o+'_m1')
    # samples['SSWW_EFT_lin_'+o] = {
    #     'name': files,
    #     'weight': mcCommonWeight_EFT+'*rw_LIN_'+o,
    #     'FilesPerJob': 4
    # }
    samples['quad_'+o] = {
        'name': files,
        'weight': mcCommonWeight_EFT+'*rw_QUAD_'+o,
        'FilesPerJob': 20
    }
    # samples['SSWW_EFT_linquad_'+o] = {
    #     'name': files,
    #     'weight': mcCommonWeight_EFT+'*(LHEReweightingWeight['+str(ip)+'] - rw_SM)',
    #     #'weight': mcCommonWeight_EFT+'*(rw_LIN_'+o+' + rw_QUAD_'+o+')',
    #     'FilesPerJob': 20
    # }
    samples['sm_lin_quad_'+o] = {
        'name': files,
        'weight': mcCommonWeight_EFT+'*LHEReweightingWeight['+str(ip)+']',
        #'weight': mcCommonWeight_EFT+'*(rw_SM + rw_LIN_'+o+' + rw_QUAD_'+o+')',
        'FilesPerJob': 20
    }


for i in range(len(op)):
    for j in range(len(op)):
        if j > i:
            term = op[i]+'_'+op[j]
            samples['sm_lin_quad_mixed_'+term] = {
                'name': files,
                'weight': mcCommonWeight_EFT+'*rw_MIX_'+term,
                'FilesPerJob': 20
            }
            # samples['SSWW_EFT_smmix_'+term] = {
            #     'name': files,
            #     'weight': mcCommonWeight_EFT+'*(rw_SM + rw_LIN_'+op[i]+'*rw_LIN_'+op[i]+' + rw_QUAD_'+op[i]+'*rw_QUAD_'+op[i]+' + rw_LIN_'+op[j]+'*rw_LIN_'+op[j]+' + rw_QUAD_'+op[j]+'*rw_QUAD_'+op[j]+' + rw_MIX_'+term+')',
            #     'FilesPerJob': 4
            # }
