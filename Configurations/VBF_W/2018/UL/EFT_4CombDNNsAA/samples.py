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


# #########################################
# ############### SIGNAL ##################
# #########################################
# ###### W + jj EWK #######

# samples['WLNuJJ']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryLat,'Wm_LNuJJ_EWK')
#                                     + nanoGetSampleFiles(mcDirectoryLat,'Wp_LNuJJ_EWK'),
# #                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                         'weight': CommonWeight,
#                         'FilesPerJob' : 3,
#                         'EventsPerJob' : 5000,
#                     }

##########################################
############  BACKGROUNDS  ###############
##########################################


# samples['WLNuJJ_inter']  = {  'name'   :  nanoGetSampleFiles(mcDirectoryPrivate2,'WLNuJJ_EWK_QCD_interference2')
#                                           + nanoGetSampleFiles(mcDirectoryPrivate,'WLNuJJ_EWK_QCD_interference'),
# #                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#                         'weight': CommonWeight,
#                         'FilesPerJob' : 5,
#                         'EventsPerJob' : 7000,
#                     }


# # ####### Wjets #########
Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '
# Wjets_photon_filter = '1.'
Total_correction = 'WJets_reweight'
# Total_correction = '1.'

samples['Wjets_HT_hardJets'] = { 'name' :   nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                          + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
#				                'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
                                'weight': CommonWeight+'*' + Wjets_photon_filter + '*' + Total_correction + '* hardJets',
			                	'FilesPerJob' : 3,
		                 }

# # Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
# ############
# # HT stiching corrections 2018
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT70To100',    '1.21 * 0.95148')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT100To200',   '0.9471') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT200To400',   '0.9515') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT400To600',   '0.9581') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT600To800',   '1.0582') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT800To1200',  '1.1285') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT1200To2500', '1.3268') 
addSampleWeight(samples,'Wjets_HT_hardJets', 'WJetsToLNu_HT2500ToInf',  '2.7948') 

###############################################
# # ####### WjetsPU #########

samples['Wjets_HT_PUJets'] = { 'name' :   nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu-LO')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT70To100')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT100To200')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT200To400')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT400To600')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT600To800')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT800To1200')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT1200To2500')
                                   + nanoGetSampleFiles(mcDirectoryLat, 'WJetsToLNu_HT2500ToInf'),
#				                'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
                                'weight': CommonWeight+'*' + Wjets_photon_filter + '* PUJets',
			                	'FilesPerJob' : 3,
		                 }

# # Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
# ############
# # HT stiching corrections 2018
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT70To100',    '1.21 * 0.95148')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT100To200',   '0.9471') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT200To400',   '0.9515') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT400To600',   '0.9581') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT600To800',   '1.0582') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT800To1200',  '1.1285') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT1200To2500', '1.3268') 
addSampleWeight(samples,'Wjets_HT_PUJets', 'WJetsToLNu_HT2500ToInf',  '2.7948') 

###############################################


############ Top ############

samples['top'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'TTTo2L2Nu')  
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectoryLat,'ST_tW_top')
                                 + nanoGetSampleFiles(mcDirectoryLat,'TTToSemiLeptonic'),
                                #  + nanoGetSampleFiles(mcDirectoryLat,'TTZjets')   have to do it
                                #  + nanoGetSampleFiles(mcDirectoryLat,'TTWjets'),  same to do
                                 #+ nanoGetSampleFiles(mcDirectoryLat,'TTWJetsToLNu'), #also this is available (was commented)
                      'weight': CommonWeight,
                      'FilesPerJob' : 3,
                }

# !!!! TTToSemiLeptonic_ext3?


addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
# addSampleWeight(samples,'top','TTZjets','Top_pTrw')
# addSampleWeight(samples,'top','TTWjets','Top_pTrw')

#Not corrected in baseW, so we should correct the XS here
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


###############################################


########### DY ############

# DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'
DY_photon_filter = '1.'

samples['DY_M-50'] = {    'name'   :   nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50') #Don't use LO(_ext0)! DYMVA Training!
                                  # + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_ext2')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-50_HT-2500toInf')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-10to50-LO')
                                  # + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-100to200')   #missing (lat)
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-200to400')
                                  + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-400to600'),
                                  # + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-600toInf'),   missing.. search for it
                        'weight': CommonWeight+'*'+DY_photon_filter,
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                        'FilesPerJob' : 5,
                }

#VBF-Z does use less sample (only M-50 and applies dome different weights (but uses signal at higher energies))
# CombineBaseW(samples, 'DY_M-50', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext2'])
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50','DY_NLO_pTllrw')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50',               '(LHE_HT < 70)')
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_ext2',          '(LHE_HT < 70)') 
# addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-70to100',    'DY_LO_pTllrw')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-100to200',   '1.000') #HT stitching correction
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-200to400',   '0.999')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-400to600',   '0.990')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-600to800',   '0.975')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-800to1200',  '0.907')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-1200to2500', '0.833')
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-50_HT-2500toInf',  '1.015')  
addSampleWeight(samples,'DY_M-50','DYJetsToLL_M-10to50-LO', '(LHE_HT < 200)') 


# samples['DY_else'] = {    'name'   : nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-10to50-LO')
#                                   # + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-100to200')   to do (or search..)
#                                   + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-200to400') #missing (lat)
#                                   + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-400to600'), #missing (lat)
#                                   # + nanoGetSampleFiles(mcDirectoryLat,'DYJetsToLL_M-4to50_HT-600toInf'),   missing.. search for it
#                         'weight': CommonWeight+'*'+DY_photon_filter,
# #                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
#                         'FilesPerJob' : 5,
#                 }

# addSampleWeight(samples,'DY_else','DYJetsToLL_M-10to50-LO', '(LHE_HT < 200)') 
# # addSampleWeight(samples,'DY_else','DYJetsToLL_M-10to50-LO', '(LHE_HT > 600)') 
# # addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-100to200','DY_LO_pTllrw') 
# # addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-200to400','DY_LO_pTllrw')
# # addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-400to600','DY_LO_pTllrw')
# # addSampleWeight(samples,'DY_else','DYJetsToLL_M-4to50_HT-600toInf','DY_LO_pTllrw')


# # ############# VV ##################

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
#                 }


# ###############################################

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
#                               # + nanoGetSampleFiles(mcDirectoryLat,'WWToLNuQQ'),   missing from QCD and maybe also from DAS, ignore it for v9
#                     'weight': CommonWeight,
#                     'FilesPerJob' :10,
#                 }


# ########### Higgs Related #############

# samples['Higgs']  = {   'name'   :  nanoGetSampleFiles(mcDirectoryLat,'GluGluHToWWToLNuQQ_M125')   #missing lat
#                                     + nanoGetSampleFiles(mcDirectoryLat,'HWminusJ_HToWWTo2L2Nu_WToLNu_M125')   #called HWminusJ_HToWWTo2L2Nu_WToLNu_M125
#                                     + nanoGetSampleFiles(mcDirectoryLat,'HWplusJ_HToWWTo2L2Nu_WToLNu_M125')     #called HWplusJ_HToWWTo2L2Nu_WToLNu_M125
#                                     + nanoGetSampleFiles(mcDirectoryLat,'VBFHToWWToLNuQQ_M125'),   #missing lat
#                         'weight': CommonWeight,
#                         'FilesPerJob' : 5,
#                   }


################################

# ########## VBF - Z #############

# samples['VBF-Z']  = {   'name'   :  nanoGetSampleFiles(mcDirectoryLat,'EWKZ2Jets_ZToLL_M-50'),
#                         'weight': CommonWeight+ '*(lhe_mjj[0] > 120)',
#                         'FilesPerJob' : 20,
#                   }

# # ##VBF-Z --> slighly different weight
# # ###############################


# ############ Vg ##############

# samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'WGToLNuG')   # this is called WGToLNuG in v9
#                                  + nanoGetSampleFiles(mcDirectoryLat,'ZGToLLG'),
#                     'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
#                     'FilesPerJob' : 10,
#                 }

# # the following baseW correction is needed in both v5 and v6 (for Zg, Not for ZGToLLG)
# #addSampleWeight(samples, 'Vg', 'Zg', '0.448')

# ##VBF-Z has different weights (common)+genstar
# ###############################


# ############ VgS ############

# samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'WGToLNuG')
#                                  + nanoGetSampleFiles(mcDirectoryLat,'ZGToLLG')
#                                  + nanoGetSampleFiles(mcDirectoryLat,'WZTo3LNu_mllmin0p1'),
#                       'weight' : CommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#                       'FilesPerJob' : 10,
#                    }

# addSampleWeight(samples,'VgS','WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
# addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') # *0.448 XS correction for Zg
# addSampleWeight(samples,'VgS','WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1)')

# ############ VVV ############
  
# samples['VVV']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'ZZZ')
#                                 + nanoGetSampleFiles(mcDirectoryLat,'WZZ')
#                                 + nanoGetSampleFiles(mcDirectoryLat,'WWZ')
#                                 + nanoGetSampleFiles(mcDirectoryLat,'WWW'),
#                     'weight': CommonWeight,
#                                 #+ nanoGetSampleFiles(mcDirectory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
#                     'FilesPerJob' : 20,
#                   }


##### trying to group:
samples['Others']  = {  'name'   :   nanoGetSampleFiles(mcDirectoryLat,'ZZZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WZZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WWZ')
                                + nanoGetSampleFiles(mcDirectoryLat,'WWW')
                                # + nanoGetSampleFiles(mcDirectoryLat,'WGToLNuG')
                                # + nanoGetSampleFiles(mcDirectoryLat,'ZGToLLG')
                                # + nanoGetSampleFiles(mcDirectoryLat,'WZTo3LNu_mllmin0p1')
                                + nanoGetSampleFiles(mcDirectoryLat,'EWKZ2Jets_ZToLL_M-50')
                                + nanoGetSampleFiles(mcDirectoryLat,'GluGluHToWWToLNuQQ_M125')
                                + nanoGetSampleFiles(mcDirectoryLat,'HWminusJ_HToWWTo2L2Nu_WToLNu_M125') 
                                + nanoGetSampleFiles(mcDirectoryLat,'HWplusJ_HToWWTo2L2Nu_WToLNu_M125')   
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
                    'FilesPerJob' : 5,
                  }

# addSampleWeight(samples,'Others','WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1) * (gstarLow * 0.94 + gstarHigh * 1.14)')
# addSampleWeight(samples,'Others','ZGToLLG', '(Gen_ZGstar_mass > 0) * (gstarLow * 0.94 + gstarHigh * 1.14)') # *0.448 XS correction for Zg
# addSampleWeight(samples,'Others','WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1) * (gstarLow * 0.94 + gstarHigh * 1.14)')
addSampleWeight(samples,'Others','EWKZ2Jets_ZToLL_M-50', 'lhe_mjj[0] > 120')


#########################################
############## EFT ###############
#########################################

EFTSamples = nanoGetSampleFiles(mcDirectoryLat,'WLNuJJ_EWK_EFT2_crab')

samples['sm'] = {
    'name': EFTSamples,
    'weight': CommonWeight + '*' + '(LHEReweightingWeight[0])',
    'FilesPerJob': 10,
}

CMSSW=os.environ["CMSSW_BASE"]
sampleEFTFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT_4CombDNNsAA/EFTweights.py"
if os.path.exists(CMSSW+'/src/'+sampleEFTFile):
  handle = open(CMSSW+'/src/'+sampleEFTFile)
  exec(handle)
  handle.close()

# # ## fatti ma non usati per datacard
# ######################################### debug weightssss ############################
sampleEFTFileDebug = "PlotsConfigurations/Configurations/VBF_W/2018/UL/EFT_4CombDNNsAA/debug_EFTweights.py"
if os.path.exists(CMSSW+'/src/'+sampleEFTFileDebug):
  handle = open(CMSSW+'/src/'+sampleEFTFileDebug)
  exec(handle)
  handle.close()

# # #########################################
# # ############## DATAA ###############
# # #########################################


# Then corrected
fakeW = '((fakeWeight_0p9 * (fakeWeight_0p9 <= 20)) + 0. * (fakeWeight_0p9>20))'
# fakeW = 'fakeWeight_0p8'

# # ## Fakes
samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA +'*'+ fakeW +'* fakes_correction',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 30
}

for Run in DataRun :
  for DataSet in DataSets :
    version = 'v1'
    if "SingleMuon" in DataSet and any(k in Run[0] for k in ["A", "B", "C"]):
      version = 'v2'
    # # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
    files = nanoGetSampleFiles(dataDirectoryHWW, DataSet+'_'+Run[1]+'-'+version)
    for iFile in files:
      samples['Fake']['name'].append(iFile)
      samples['Fake']['weights'].append(DataTrig[DataSet])

    

########################################
############### DATA ###################
########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                      #  'weight' : METFilter_DATA,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 70,         
            }

for Run in DataRun :
  for DataSet in DataSets :
    version = 'v1'
    if "SingleMuon" in DataSet and any(k in Run[0] for k in ["A", "B", "C"]):
      version = 'v2'
    FileTarget = nanoGetSampleFiles(dataDirectoryHWW,DataSet+'_'+Run[1]+'-'+version)
    for iFile in FileTarget:
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])


# # mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s 2Jets1leptonW2018 -i MCl1loose2018v7__MCCorr2018v7 -b -Q workday -T  WLNuJJ_EWK,WJetsToLNu-LO,WJetsToLNu_HT70_100,WJetsToLNu_HT100_200,WJetsToLNu_HT200_400,WJetsToLNu_HT400_600,WJetsToLNu_HT600_800,WJetsToLNu_HT800_1200,WJetsToLNu_HT1200_2500,WJetsToLNu_HT2500_inf,WJetsToLNu,WJetsToLNu_Pt50to100,WJetsToLNu_Pt100to250,WJetsToLNu_Pt250to400,WJetsToLNu_Pt400to600,WJetsToLNu_Pt600toInf,TTTo2L2Nu,ST_s-channel_ext1,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop_ext1,ST_tW_top_ext1,TTToSemiLeptonic,TTZjets,TTWjets,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,WWToLNuQQ,GluGluWWToLNuQQ,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWW_LNu_M125,HWplusJ_HToWW_LNu_M125,VBFHToWWToLNuQQ_M125,DYJetsToLL_M-50,DYJetsToLL_M-50_ext2,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,DYJetsToLL_M-10to50-LO_ext1,DYJetsToLL_M-4to50_HT-100to200,DYJetsToLL_M-4to50_HT-200to400,DYJetsToLL_M-4to50_HT-400to600,DYJetsToLL_M-4to50_HT-600toInf,EWKZ2Jets_ZToLL_M-50,Wg_MADGRAPHMLM,ZGToLLG,ZZZ,WZZ,WWZ,WWW,WJetsToLNu-0J,WJetsToLNu-1J,WJetsToLNu-2J


# # mkPostProc.py -p Summer20UL18_106x_nAODv9_Full2018v9 -s $iSyst -i MCl1loose2018v9__MCCorr2018v9NoJERInHorn -b -Q nextweek -T Wm_LNuJJ_EWK,Wp_LNuJJ_EWK,EWKZ2Jets_ZToLL_M-50,WmToLNu_WmTo2J_QCD,WmToLNu_ZTo2J_QCD,WmTo2J_ZTo2L_QCD,WpTo2J_WmToLNu_QCD,WpTo2J_ZTo2L_QCD,WpToLNu_WpTo2J_QCD,WpToLNu_WmTo2J_QCD,WpToLNu_ZTo2J_QCD,ZTo2L_ZTo2J_QCD,GluGluHToWWToLNuQQ_M125,HWminusJ_HToWWTo2L2Nu_WToLNu_M125,HWplusJ_HToWWTo2L2Nu_WToLNu_M125,VBFHToWWToLNuQQ_M125,ZZZ,WZZ,WWZ,WWW,TTTo2L2Nu,ST_s-channel,ST_t-channel_antitop,ST_t-channel_top,ST_tW_antitop,ST_tW_top,TTToSemiLeptonic,WGToLNuG,ZGToLLG,DYJetsToLL_M-10to50-LO,DYJetsToLL_M-4to50_HT-200to400,DYJetsToLL_M-4to50_HT-400to600,WJetsToLNu-LO,WJetsToLNu_HT70To100,WJetsToLNu_HT100To200,WJetsToLNu_HT200To400,WJetsToLNu_HT400To600,WJetsToLNu_HT600To800,WJetsToLNu_HT800To1200,WJetsToLNu_HT1200To2500,WJetsToLNu_HT2500ToInf,WmToLNu_ZTo2J,WmTo2J_ZTo2L,WpTo2J_ZTo2L,WpToLNu_ZTo2J,WpToLNu_WpTo2J,WmToLNu_WmTo2J,WpToLNu_WmTo2J,WpTo2J_WmToLNu,ZTo2L_ZTo2J,DYJetsToLL_M-50,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400,DYJetsToLL_M-50_HT-400to600,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-800to1200,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-2500toInf,WGToLNuG,ZGToLLG,WZTo3LNu_mllmin0p1

# # mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s DATA2Jets1leptonW2018 -i DATAl1loose2018v7__DATACombJJLNu2018 -b -Q workday
