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
treeBaseDirEFT = "/eos/user/g/glavizza/nanoAOD/WWjjTolnulnu_SS_EFTdim6/postProc"
MCDir = os.path.join(treeBaseDir,  mcProduction , mcSteps)
MCDirEFT = os.path.join(treeBaseDirEFT,  mcProduction , mcSteps)



# MCDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'


################################################
################### WEIGHTS ####################
################################################

# ---------------------------------------- Basic MC weights
mcCommonWeightNoMatch = 'XSWeight*SFweight_mod_SMP*samesign_requirement'
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
files = nanoGetSampleFiles(MCDir, 'WpWpJJ_EWK_madgraph') #WpWpJJ_EWK 
samples['SSWW_SM'] = {
    'name': files,
    'weight': mcCommonWeight_SMP,
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(MCDirEFT, 'WWjjTolnulnu_SS_EFTdim6')  

samples['SSWW_EFT_sm'] = {
    'name': files,
    'weight': mcCommonWeight_EFT,
    'FilesPerJob': 4
}

op = ["cW", "cHDD", "cHW", "cHWB", "cHbox", "cHj1", "cHj3", "cHl1", "cHl3", "cll1", "cjj11", "cjj31", "cjj18", "cjj38"]
# the following (ls) contains the operators in the same order as in the LHEReweightingWeight vector
ls = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38']

### lin and quad components
for o in op:
    ip = ls.index(o)
    im = ls.index(o+'_m1')
    print (o, ip, im)
    samples['SSWW_EFT_lin_'+o] = {
        'name': files,
        'weight': mcCommonWeight_EFT+'*0.5*(LHEReweightingWeight['+str(ip)+'] - LHEReweightingWeight['+str(im)+'])',
        'FilesPerJob': 4
    }
    samples['SSWW_EFT_quad_'+o] = {
        'name': files,
        'weight': mcCommonWeight_EFT+'*0.5*(LHEReweightingWeight['+str(ip)+'] + LHEReweightingWeight['+str(im)+'] - 2*LHEReweightingWeight[0])',
        'FilesPerJob': 4
    }

# for o in mix:
#     ix = ls.index(o)
#     print (o, ix)
#     samples['SSWW_EFT_mix_'+o] = {
#         'name': files,
#         'weight': mcCommonWeight_EFT+'*(LHEReweightingWeight['+str(ix)+'] - LHEReweightingWeight[0])',
#         'FilesPerJob': 4
#     }
