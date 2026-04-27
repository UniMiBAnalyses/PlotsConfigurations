import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # 2017
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

mcProduction = 'Summer20UL17_106x_nAODv9_Full2017v9'

dataReco = 'Run2017_UL2017_nAODv9_Full2017v9'

fakeReco = dataReco

#from VBS
mcSteps = 'MCl1loose2017v9__MCCorr2017v9NoJERInHorn' 

#from VBS
dataSteps = 'DATAl1loose2017v9'

MC_skim = '2Jets1leptonW2017'

DATA_skim = 'DATA2Jets1leptonW2017'


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

# def makeMCDirectory(var=''):
#   if var:
#       return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var='__' + var))
#   else:
#       return os.path.join(treeBaseDirPrivate, mcProduction, (mcSteps + '__' + skim).format(var=''))

mcDirectoryHWW = os.path.join(treeBaseDirHWW,  mcProduction , mcSteps)
mcDirectoryLat = os.path.join(treeBaseDirLat,  mcProduction , mcSteps)
mcDirectoryLatSig = os.path.join(treeBaseDirLat,  mcProduction , mcSteps+"__genStepVBFW2")
# mcDirectoryHWW = os.path.join(treeBaseDirPrivate,  mcProduction , mcSteps + '__' + MC_skim)
#fakeDirectory = os.path.join(treeBaseDir, fakeRe
dataDirectoryHWW = os.path.join(treeBaseDirHWW, dataReco, dataSteps)
dataDirectoryLat = os.path.join(treeBaseDirLat, dataReco, dataSteps)
# dataPrivateDirectory = os.path.join(treeBaseDirPrivate, dataReco, dataSteps + '__' + DATA_skim)

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(mcDirectory, 'Summer20UL17_106x_nAODv9_Full2017v9', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')
################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='1'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################


eleWP='mvaFall17V2Iso_WP90_tthmva_70'
muWP='cut_Tight_HWWW_tthmva_80'


LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF[0]'

trigg_MC = '( (abs(Lepton_pdgId[0])==13) * (HLT_IsoMu27 > 0.5) || (abs(Lepton_pdgId[0])==11) * (HLT_Ele35_WPTight_Gsf > 0.5) )'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################
#corrected trigger efficiency

XSWeight   = 'XSWeight'
SFweight1l = ['puWeight', 'Lepton_RecoSF[0]', LepWPWeight_1l, LepWPCut_1l, 'btagSF','PUJetIdSF', 'TriggerSFWeight_1l', trigg_MC, 'L1PreFiringWeight_Nom', 'EMTFbug_veto']

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
            ['B','Run2017B-UL2017-v1'] ,
            ['C','Run2017C-UL2017-v1'] ,
            ['D','Run2017D-UL2017-v1'] ,
            ['E','Run2017E-UL2017-v1'] ,
            ['F','Run2017F-UL2017-v1']
          ]

DataSets = ['SingleMuon','SingleElectron']

DataTrig = {
    'SingleMuon'     : 'Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl',
}


fiducial = '(((abs(Alt$(DressedLepton_pdgId[0],0))==11) + (abs(Alt$(DressedLepton_pdgId[0],0))==13))>0) \
            && (Alt$(DressedLepton_isPrompt[0],0)==1) \
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

samples['WLNuJJ'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'*'+fiducialw,
}

samples['WLNuJJ_Out'] = { 
        'FilesPerJob' : 5,
        'name' : nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')
               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK'),
        'weight' : CommonWeight+'* !('+fiducialw+')',
}


###########################################
#############  BACKGROUNDS  ###############
###########################################


####### Wjets #########
Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
Total_correction = 'WJets_reweight'
# Total_correction = '1.'

samples['Wjets_HT_hardJets'] = { 'name' : nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100') 
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
                        'weight': CommonWeight+'*' + Wjets_photon_filter + '*' +Total_correction + '* hardJets',
                        # 'EventsPerJob' : 7000,
                        'FilesPerJob' : 4
		                 }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu-LO', '(LHE_HT < 70)')
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO_ext1', '(LHE_HT < 70)')
# CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu-LO', 'WJetsToLNu-LO_ext1'])

addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT70To100', '1.21 * 0.9582') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT100To200',    '0.9525') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT200To400',    '0.9577') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT400To600',    '0.9613') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT600To800',    '1.0742') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT800To1200',   '1.1698') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT1200To2500',  '1.3046') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT2500ToInf',   '2.1910') 
###############################################
# # ####### WjetsPU #########

samples['Wjets_HT_PUJets'] = { 'name' : nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100') 
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                  + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
                        'weight': CommonWeight+'*' + Wjets_photon_filter + '* PUJets',
                        # 'EventsPerJob' : 7000,
                        'FilesPerJob' : 4,
		                 }

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu-LO', '(LHE_HT < 70)')
# addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO_ext1', '(LHE_HT < 70)')
# CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu-LO', 'WJetsToLNu-LO_ext1'])

addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT70To100', '1.21 * 0.9582') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT100To200',    '0.9525') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT200To400',    '0.9577') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT400To600',    '0.9613') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT600To800',    '1.0742') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT800To1200',   '1.1698') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT1200To2500',  '1.3046') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT2500ToInf',   '2.1910') 

###############################################


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_top') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'TTToSemiLeptonic'),
                                #  + nanoGetSampleFiles(mcDirectory,'TTZjets')    ## missinglatino
                                #  + nanoGetSampleFiles(mcDirectory,'TTZjets_ext1')
                                #  + nanoGetSampleFiles(mcDirectory,'TTWjets')    ## only w/ pythia, non amcatnlo
                                #  + nanoGetSampleFiles(mcDirectory,'TTWjets_ext1'),
                      'weight': CommonWeight,
                      'FilesPerJob' : 3,
                      # 'EventsPerJob' : 7000,
                }


# CombineBaseW(samples, 'top', ['TTZjets', 'TTZjets_ext1'])
# CombineBaseW(samples, 'top', ['TTWjets', 'TTWjets_ext1'])

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')

addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")
###############################################

########## DY ############

# DY_photons_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'
DY_photon_filter = '1'

samples['DY_M-50'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50') 
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-100to200') 
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-400to600') 
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-2500toInf')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-10to50-LO')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-600toInf'),
                        # 'weight': CommonWeight,
                      # 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter +'*btagSF_corr_DY',# missing ewkNLOW
                      'weight': CommonWeight+'*'+DY_photon_filter,
                        'FilesPerJob' : 5,
                }

addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50',                      '(LHE_HT < 70)')  # To put 100 when HT100to200 is back
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-200to400',          '0.999')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-400to600',          '0.990')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-600to800',          '0.975')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-800to1200',         '0.907')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-1200to2500',        '0.833')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-2500toInf',         '1.015')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-10to50-LO',               '(LHE_HT < 100)')

# samples['DY_else'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-10to50-LO')
#                                   + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-100to200')
#                                   + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-200to400')
#                                   + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-400to600')
#                                   + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-600toInf'),
#                         # 'weight': CommonWeight+ '*' + DY_photon_filter +'*btagSF_corr_DY',
#                         'weight': CommonWeight+ '*' + DY_photon_filter,
# #                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
#                         'FilesPerJob' : 5,
#                         'EventsPerJob' : 70000,
#                       #  'suppressNegative' :['all'],
#                       #  'suppressNegativeNuisances' :['all'],
#                 }


# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-10to50-LO',               '(LHE_HT < 100)')
# # addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-100to200_newpmx',       'DY_LO_pTllrw')
# # addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-200to400_newpmx',       'DY_LO_pTllrw')
# # addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-400to600',       'DY_LO_pTllrw')
# # addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-400to600_ext1',  'DY_LO_pTllrw')
# # addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-600toInf',       'DY_LO_pTllrw')
# # addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-4to50_HT-600toInf_ext1',  'DY_LO_pTllrw')


# ############## VV ##################

# samples['VV']  = { 'name' :  nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_WmTo2J_QCD')
#                              + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_ZTo2J_QCD')
#                              + nanoGetSampleFiles(mcDirectoryLat,'WmTo2J_ZTo2L_QCD')
#                              + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_WmToLNu_QCD')
#                              + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_ZTo2L_QCD')
#                              + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WpTo2J_QCD')
#                              + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WmTo2J_QCD')
#                              + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_ZTo2J_QCD')
#                              + nanoGetSampleFiles(mcDirectoryLat,'ZTo2L_ZTo2J_QCD'),
#                    'weight': CommonWeight,
# #                   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, # still missing EWKnlowW 
#                    'FilesPerJob' : 10,
#                   #  'EventsPerJob' : 70000,
#                 }


# ##############################################

# ############ VBS ############

# samples['VBS']  = { 'name' :  nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_ZTo2J') 
#                               + nanoGetSampleFiles(mcDirectoryLat,'WmTo2J_ZTo2L')
#                               + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_ZTo2L')
#                               + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_ZTo2J')
#                               + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WpTo2J')
#                               + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_WmTo2J')
#                               + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WmTo2J')
#                               + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_WmToLNu')
#                               + nanoGetSampleFiles(mcDirectoryLat,'ZTo2L_ZTo2J'),
#                               # + nanoGetSampleFiles(mcDirectory,'WWToLNuQQ'),   #no in das UL, who cares
#                     'weight': CommonWeight,
# #                    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                     'FilesPerJob' : 20,
#                     # 'EventsPerJob' : 70000,
#                 }


# #################################################

# ########### Higgs Related #############

# samples['Higgs']  = {   'name'   :  nanoGetSampleFiles(mcDirectoryLat,'GluGluHToWWToLNuQQ_M125')
#                                     + nanoGetSampleFiles(mcDirectoryLat,'VBFHToWWToLNuQQ_M125'),
#                         'weight': CommonWeight,
# #                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                         'FilesPerJob' : 5,
#                         # 'EventsPerJob' : 70000,
#                   }

# ######### VBF - Z #############

# samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcDirectoryLat,'EWKZ2Jets_ZToLL_M-50_MJJ-120'),
#                                   # + nanoGetSampleFiles(mcDirectory,'EWK_LLJJ_herwig')
#                         # 'weight': CommonWeight+ '*btagSF_corr_Vg_VgS_VBFV_WLNuJJ',
#                         'weight': CommonWeight+ '*(lhe_mjj[0] > 120)',
#                         'FilesPerJob' : 10,
#                         'EventsPerJob' : 70000,
#                   }


# ############ VgS ############

# # specialWeight1 = "(gstarLow * 0.94)"
# # specialWeight2 = "(gstarHigh * 1.14)"
# # weightTotal = 

# samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'WGToLNuG')
#                                  + nanoGetSampleFiles(mcDirectoryLat,'ZGToLLG')
#                                  + nanoGetSampleFiles(mcDirectoryLat,'WZTo3LNu_mllmin0p1'),    ## called WZTo3LNu_mllmin0p1
#                       # 'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14) * btagSF_corr_Vg_VgS_VBFV_WLNuJJ',
#                       'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#                       'FilesPerJob' : 15,
#                       # 'EventsPerJob' : 70000,
#                       # 'suppressNegative' :['all'],
#                       # 'suppressNegativeNuisances' :['all'],
#                    }

# # addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
# #0.448 needed in v5 and should be removed in v6
# addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') #*0.448
# addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')


# ############ VVV ############
  
# samples['VVV']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'ZZZ')
#                                 + nanoGetSampleFiles(mcDirectoryLat,'WZZ')
#                                 + nanoGetSampleFiles(mcDirectoryLat,'WWZ')
#                                 + nanoGetSampleFiles(mcDirectoryLat,'WWW'),
#                     # 'weight': CommonWeight +'*btagSF_corr_VV_VVV_ggWW',
#                     'weight': CommonWeight,
#                                 #+ nanoGetSampleFiles(mcDirectory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
# #                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
#                     'FilesPerJob' : 5,
#                     #  'EventsPerJob' : 70000,
#                   }


# #########################################################################


##### trying to group:
samples['Others']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'ZZZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WZZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WWZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WWW')
                                # + nanoGetSampleFiles(mcDirectoryLat,'ZGToLLG')
                                # + nanoGetSampleFiles(mcDirectoryLat,'WZTo3LNu_mllmin0p1')
                                + nanoGetSampleFiles(mcDirectoryLat,'EWKZ2Jets_ZToLL_M-50_MJJ-120')
                                + nanoGetSampleFiles(mcDirectoryLat,'GluGluHToWWToLNuQQ_M125')
                                + nanoGetSampleFiles(mcDirectoryLat,'VBFHToWWToLNuQQ_M125')
                                + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_ZTo2J') 
                                + nanoGetSampleFiles(mcDirectoryLat,'WmTo2J_ZTo2L')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_ZTo2L')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_ZTo2J')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WpTo2J')
                                + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_WmTo2J')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WmTo2J')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_WmToLNu')
                                + nanoGetSampleFiles(mcDirectoryLat,'ZTo2L_ZTo2J')
                                + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_WmTo2J_QCD')
                                + nanoGetSampleFiles(mcDirectoryLat,'WmToLNu_ZTo2J_QCD')
                                + nanoGetSampleFiles(mcDirectoryLat,'WmTo2J_ZTo2L_QCD')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_WmToLNu_QCD')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpTo2J_ZTo2L_QCD')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WpTo2J_QCD')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_WmTo2J_QCD')
                                + nanoGetSampleFiles(mcDirectoryLat,'WpToLNu_ZTo2J_QCD')
                                + nanoGetSampleFiles(mcDirectoryLat,'ZTo2L_ZTo2J_QCD'),
                    'weight': CommonWeight,
                    'FilesPerJob' : 2,
                  }

# addSampleWeight(samples,'Others','ZGToLLG', '(Gen_ZGstar_mass > 0)') # *0.448 XS correction for Zg
# addSampleWeight(samples,'Others','WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1)')
addSampleWeight(samples,'Others','EWKZ2Jets_ZToLL_M-50_MJJ-120', 'lhe_mjj[0] > 120')


##########################################

# Then corrected
fakeW = '(fakeWeight_0p9 * (fakeWeight_0p9 <= 20) + 0.*(fakeWeight_0p9>20))'


# ## Fakes
samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA+'*'+fakeW,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 30,
}


#
for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectoryHWW, pd + '_' + sd)
    # # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


##########################################
################# DATA ###################
##########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 60,
                  }


for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(dataDirectoryHWW,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                  samples['DATA']['name'].append(iFile)
                  samples['DATA']['weights'].append(DataTrig[DataSet])


# # # #samples = {   key:v for key,v in samples.items() if key  in ["VBS_dipoleRecoil"]}

# # # # mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s 2Jets1leptonW2017 -i MCl1loose2017v7__MCCorr2017v7__MCCombJJLNu2017 -b -Q workday -T WLNuJJ_EWK,EWK_LNuJJ_herwig,WJetsToLNu-LO,WJetsToLNu-LO_ext1,WJetsToLNu_HT70_100,WJetsToLNu_HT100_200,WJetsToLNu_HT200_400,WJetsToLNu_HT400_600,WJetsToLNu_HT600_800,WJetsToLNu_HT800_1200,WJetsToLNu_HT1200_2500,WJetsToLNu_HT2500_inf,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,TTZjets,TTZjets_ext1,TTWjets,TTWjets_ext1,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,VBFHToWWToLNuQQ_M125,DYJetsToLL_M-50,DYJetsToLL_M-50_ext1,DYJetsToLL_M-10to50-LO_ext1,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-400to600_newpmx,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-4to50_HT-100to200_newpmx,DYJetsToLL_M-4to50_HT-200to400_newpmx,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-400to600_ext1,DYJetsToLL_M-4to50_HT-600toInf,DYJetsToLL_M-4to50_HT-600toInf_ext1,EWKZ2Jets_ZToLL_M-50_newpmx,EWK_LLJJ_herwig,Wg_MADGRAPHMLM,ZGToLLG,WZTo3LNu_mllmin01,ZZZ,WWZ,WWW,WZZ

# # # per il 2017 posso usare lo stesso step perche parto da uno step in piu (ereditato da davide) in cui i veti sul tight [0] e [1] sono gia applicati correttamente. Se cosi non fosse mi uscirebbero i fake sbagliati
# # # # mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s 2Jets1leptonW2017 -i DATAl1loose2017v7__DATACombJJLNu2017 -b -Q workday

# # mkPostProc.py -p Summer20UL17_106x_nAODv9_Full2017v9 -s $iSyst -i MCl1loose2017v9__MCCorr2017v9NoJERInHorn -b -Q nextweek -T Wm_LNuJJ_EWK,Wp_LNuJJ_EWK,EWKZ2Jets_ZToLL_M-50_MJJ-120,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,GluGluHToWWToLNuQQ_M125,VBFHToWWToLNuQQ_M125,ZZZ,WZZ,WWZ,WWW,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,WGToLNuG,ZGToLLG,DYJetsToLL_M-10to50-LO,DYJetsToLL_M-4to50_HT-100to200,DYJetsToLL_M-4to50_HT-200to400,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-600toInf,WJetsToLNu-LO,WJetsToLNu_HT70To100,WJetsToLNu_HT100To200,WJetsToLNu_HT200To400,WJetsToLNu_HT400To600,WJetsToLNu_HT600To800,WJetsToLNu_HT800To1200,WJetsToLNu_HT1200To2500,WJetsToLNu_HT2500ToInf,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,DYJetsToLL_M-50,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,WGToLNuG,ZGToLLG,WZTo3LNu_mllmin0p1