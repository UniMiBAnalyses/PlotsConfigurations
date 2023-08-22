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
# files = nanoGetSampleFiles(MCDir, 'WpWpJJ_EWK_madgraph') #WpWpJJ_EWK 
# samples['SSWW_SM'] = {
#     'name': files,
#     'weight': mcCommonWeight_SMP,
#     'FilesPerJob': 4
# }

files = nanoGetSampleFiles(MCDirEFT, 'WWjjTolnulnu_SS_EFTdim6')  

samples['sm'] = {
    'name': files,
    'weight': mcCommonWeight_EFT+'*rw_SM',
    'FilesPerJob': 20
}

op = ["cW", "cHDD", "cHW", "cHWB", "cHbox", "cHj1", "cHj3", "cHl1", "cHl3", "cll1", "cjj11", "cjj31", "cjj18", "cjj38"]
#op = ["cW", "cHbox"]
# the following (ls) contains the operators in the same order as in the LHEReweightingWeight vector
ls = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38']
# the following (mix) contains all the operators with mixed terms as well, in the LHEReweightingWeight order
mix = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38', 'cW_cHDD', 'cW_cHW', 'cW_cHWB', 'cW_cHbox', 'cW_cHj1', 'cW_cHj3', 'cW_cHl1', 'cW_cHl3', 'cW_cll1', 'cW_cjj11', 'cW_cjj31', 'cW_cjj18', 'cW_cjj38', 'cHDD_cHW', 'cHDD_cHWB', 'cHDD_cHbox', 'cHDD_cHj1', 'cHDD_cHj3', 'cHDD_cHl1', 'cHDD_cHl3', 'cHDD_cll1', 'cHDD_cjj11', 'cHDD_cjj31', 'cHDD_cjj18', 'cHDD_cjj38', 'cHW_cHWB', 'cHW_cHbox', 'cHW_cHj1', 'cHW_cHj3', 'cHW_cHl1', 'cHW_cHl3', 'cHW_cll1', 'cHW_cjj11', 'cHW_cjj31', 'cHW_cjj18', 'cHW_cjj38', 'cHWB_cHbox', 'cHWB_cHj1', 'cHWB_cHj3', 'cHWB_cHl1', 'cHWB_cHl3', 'cHWB_cll1', 'cHWB_cjj11', 'cHWB_cjj31', 'cHWB_cjj18', 'cHWB_cjj38', 'cHbox_cHj1', 'cHbox_cHj3', 'cHbox_cHl1', 'cHbox_cHl3', 'cHbox_cll1', 'cHbox_cjj11', 'cHbox_cjj31', 'cHbox_cjj18', 'cHbox_cjj38', 'cHj1_cHj3', 'cHj1_cHl1', 'cHj1_cHl3', 'cHj1_cll1', 'cHj1_cjj11', 'cHj1_cjj31', 'cHj1_cjj18', 'cHj1_cjj38', 'cHj3_cHl1', 'cHj3_cHl3', 'cHj3_cll1', 'cHj3_cjj11', 'cHj3_cjj31', 'cHj3_cjj18', 'cHj3_cjj38', 'cHl1_cHl3', 'cHl1_cll1', 'cHl1_cjj11', 'cHl1_cjj31', 'cHl1_cjj18', 'cHl1_cjj38', 'cHl3_cll1', 'cHl3_cjj11', 'cHl3_cjj31', 'cHl3_cjj18', 'cHl3_cjj38', 'cll1_cjj11', 'cll1_cjj31', 'cll1_cjj18', 'cll1_cjj38', 'cjj11_cjj31', 'cjj11_cjj18', 'cjj11_cjj38', 'cjj31_cjj18', 'cjj31_cjj38', 'cjj18_cjj38']

for o in op:
    ip = ls.index(o)
    im = ls.index(o+'_m1')
    samples['lin_'+o] = {
        'name': files,
        'weight': mcCommonWeight_EFT+'*rw_LIN_'+o,
        'FilesPerJob': 20
    }
    samples['quad_'+o] = {
        'name': files,
        'weight': mcCommonWeight_EFT+'*rw_QUAD_'+o,
        'FilesPerJob': 20
    }
    samples['lin_quad_'+o] = {
        'name': files,
        'weight': mcCommonWeight_EFT+'*(LHEReweightingWeight['+str(ip)+'] - rw_SM)',
        #'weight': mcCommonWeight_EFT+'*(rw_LIN_'+o+' + rw_QUAD_'+o+')',
        'FilesPerJob': 20
    }
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





