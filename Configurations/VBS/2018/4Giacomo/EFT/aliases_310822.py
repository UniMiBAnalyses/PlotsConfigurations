import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017
configurations = os.path.dirname(configurations) # ggH
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}
bAlgo = 'DeepB'
bWP = '0.4184'

eleWP = 'mvaFall17V1Iso_WP90_SS_tthmva_70'
muWP  = 'cut_Tight_HWWW_tthmva_80'

mc = [skey for skey in samples if skey not in ('Fake_lep','DATA')]
mcSMP = [skey for skey in samples if skey in ('SSWW_SM')] # funge solo se no bkg
mcEFT = [skey for skey in samples if skey not in ('SSWW_SM')] # funge solo se no bkg
SSsamples = [skey for skey in samples if skey not in ('WW','Top','DY','Higgs')]
# DNN reader WW
# dnn_reader_path = os.getenv('CMSSW_BASE') + '/src/PlotsConfigurations/Configurations/ssww/l2_2018/dnn/'
# models_path_WW = '/eos/user/j/jixiao/latino/2018_WW/'
# aliases['DNNScore_WW'] = {
#     'class': 'DNNScore',
#     'args': ( models_path_WW +'ssww_leppt1_jetpt30/models/v2/', False),
#     'linesToAdd':[
#         'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#         'gSystem->Load("libDNNEvaluator.so")',
#         '.L ' + dnn_reader_path + 'dnn_score.cc+',
#         ],
# }
# # DNN reader PP
# models_path_VBS = '/eos/user/j/jixiao/latino/vbs/'
# aliases['DNNScore_VBS'] = {
#     'class': 'DNNScoreVBS',
#     'args': ( models_path_VBS +'ssww_leppt1_jetpt30/models/v8/', False),
#     'linesToAdd':[
#         '.L ' + dnn_reader_path + 'dnn_score_VBS.cc+',
#         ],
# }
# models_path_nonVBS = '/eos/user/j/jixiao/latino/nonvbs_mc/'
# aliases['DNNScore_nonVBS'] = {
#     'class': 'DNNScorenonVBS',
#     'args': ( models_path_nonVBS +'ssww_leppt1_jetpt30/models/v8/', False),
#     'linesToAdd':[
#         '.L ' + dnn_reader_path + 'dnn_score_nonVBS_mc.cc+',
#         ],
# }
# tau veto
aliases['tauVeto_ww'] = {
    'expr': '(Sum$(Tau_pt > 18 && abs(Tau_eta)<2.3 && (Tau_idMVAoldDM2017v2 > 1) && Tau_idDecayMode &&sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(abs(abs(Tau_phi - Lepton_phi[0])-pi)-pi, 2) ) >= 0.4 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(abs(abs(Tau_phi - Lepton_phi[1])-pi)-pi, 2) ) >= 0.4) == 0)'
}

aliases['tauVeto_wz'] = {
    'expr': '(Sum$(Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)>20 && Alt$(Lepton_pt[3],0.)<10 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[2],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[2],-9999.))-pi)-pi, 2) ) > 0.4) == 0)'
}

aliases['tauVeto_zz'] = {
    'expr': '(Sum$(Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)>10 && Alt$(Lepton_pt[3],0.)>10 && Alt$(Lepton_pt[4],0.)<10 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[2],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[2],-9999.))-pi)-pi, 2) ) > 0.4 && sqrt( pow(Tau_eta - Alt$(Lepton_eta[3],-9999.), 2) + pow(abs(abs(Tau_phi - Alt$(Lepton_phi[3],-9999.))-pi)-pi, 2) ) > 0.4) == 0)'
}

aliases['softmuon_veto']={
    'expr':'(Sum$(abs(Muon_dxy)<0.02 && abs(Muon_dz)<0.1 && Muon_softId && Muon_pt>5 && abs(Muon_eta)<2.4 && sqrt( pow(Muon_eta - Lepton_eta[0], 2) + pow(abs(abs(Muon_phi - Lepton_phi[0])-pi)-pi, 2) ) >= 0.4 && sqrt( pow(Muon_eta - Lepton_eta[1], 2) + pow(abs(abs(Muon_phi - Lepton_phi[1])-pi)-pi, 2) ) >= 0.4)==0)'
}
# fiducial
# print('.L %s/2018/WWSR/fiducial.cc+' % configurations)
# aliases['fid'] = {
#     'linesToAdd': ['.L %s/2018/WWSR/fiducial.cc+' % configurations],
#     'class': 'FiducialRegion',
#     'samples': mc,
# }
# chargeflip
aliases['chargeflip_w'] = {
    'linesToAdd': ['.L %s/2018/WWSR/mischarge_sf.cc+' % configurations],
    'class': 'misID_sf',
    'samples': mc,
}
# chargeflip
# lepton sf
#eleWP = 'mvaFall17V2Iso_WP90_SS'

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': ['VgS','VgS1','VgS2']
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': ['VgS','VgS1','VgS2']
}
# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'2l2j',
    #'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l',
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jElUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jElDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jMuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jMuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jstatElUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jstatElDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jstatMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_2l2jstatMuDown',
    'samples': ['Fake']
}
# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

aliases['PromptGenLepMatch3l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]*Lepton_promptgenmatched[2], 0)',
    'samples': mc
}

aliases['PromptGenLepMatch4l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]*Lepton_promptgenmatched[2]*Lepton_promptgenmatched[3], 0)',
    'samples': mc
}


aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

#aliases['topGenPtOTF'] = {
#    'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#    'samples': ['top']
#}

#aliases['antitopGenPtOTF'] = {
#    'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#    'samples': ['top']
#}

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPtOTF) * TMath::Exp(0.0615 - 0.0005 * antitopGenPtOTF))) + isSingleTop',
    'samples': ['top']
}




############################################
# B tagging
#loose 0.1241
# medium 0.4184
# tight 0.7527
aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1)'
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
    'samples': mcSMP
}
aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mcSMP
}
aliases['btagSF'] = {
    'expr': 'bVeto*bVetoSF + bReq*bReqSF',
    'samples': mcSMP
}

aliases['bVetoSF_EFT'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
    'samples': mcEFT
}
aliases['bReqSF_EFT'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mcEFT
}
aliases['btagSF_EFT'] = {
    'expr': 'bVeto*bVetoSF_EFT + bReq*bReqSF_EFT',
    'samples': mcEFT
}

##############################
#### qui inizia la parte buona

# systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

# for s in systs:
#   aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }
#   aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc }


# aliases['nJetsBtag']= {
#     'expr' : 'Sum$(CleanJet_pt > 20 && abs(CleanJet_eta)<2.5)'
# }



systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:
  aliases['btagSF_EFT'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF_EFT']['expr'].replace('shape','shape_up_'+s)+'+bReq*'+aliases['bReqSF_EFT']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mcEFT  }
  aliases['btagSF_EFT'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF_EFT']['expr'].replace('shape','shape_down_'+s)+'+bReq*'+aliases['bReqSF_EFT']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mcEFT }



#### qui finisce la parte buona
#################################

# btagSF_corr_samples_groups = {
#     'VBS': ['VBS','VBS_ZLL'],
#     'VBS_dipoleRecoil': ['VBS_dipoleRecoil',"VBS_top","VBS_notop"] + VBS_samples,
#     'Wjets_HT': wjets_res_bins  + wjets_boost_bins,
#     'Vg_VgS_VBFV':['Vg','VgS','VBF-V','VBF-V_dipole'] ,
#     'VV_VVV_ggWW':['VVV','VV','ggWW']+ VV_samples ,
#     'top':['top'],
#     'DY': ['DY']
# }

# for sgroup_name, sgroup in btagSF_corr_samples_groups.items():
#     aliases['btagSF_corr_'+sgroup_name] = {
#         'class': 'BtagSFNormCorrection',
#         'args': ('{}/VBSjjlnu/weights_files/btagsf_correction/btagsf_corr_2018.root'.format(configurations), sgroup_name),
#         'linesToAdd' : [
#             'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#             '.L {}/VBSjjlnu/macros/btagsf_norm_correction.cc+'.format(configurations)
#         ],     
#         'samples' : sgroup
#     }

# ################################################################################################





# # #bjet
# # # No jet with pt > 30 GeV
# aliases['zeroJet'] = {
#     'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
# }




# # # ==1 jet with pt > 30 GeV
# aliases['oneJet'] = {
#     'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) < 30.'
# }

# # # ==2 jets with pt > 30 GeV
# aliases['twoJet'] = {
#     'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) >= 30. && Alt$(CleanJet_pt[2], 0) < 30.'
# }

# # # >=2 jets with pt > 30 GeV
# aliases['twoJetOrMore'] = {
#     'expr': 'Alt$(CleanJet_pt[0], 0) >= 30. && Alt$(CleanJet_pt[1], 0) >= 30.'
# }

# aliases['bVeto'] = {
#     'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) == 0'
# }

# aliases['bReq'] = {
#     'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184) >= 1'
# }

# aliases['btag0'] = {
#     'expr': 'zeroJet && !bVeto'
# }

# aliases['btag1'] = {
#     'expr': 'oneJet && bReq'
# }

# aliases['btag2'] = {
#     'expr': 'twoJet && bReq'
# }


# lepton eta range
aliases['lep0eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[0],-9999))==11 && abs(Alt$(Lepton_eta[0],-9999.)) <2.5) || (abs(Alt$(Lepton_pdgId[0],-9999))==13 && abs(Alt$(Lepton_eta[0],-9999.)) <2.4))'
}
aliases['lep1eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[1],-9999))==11 && abs(Alt$(Lepton_eta[1],-9999.)) <2.5) || (abs(Alt$(Lepton_pdgId[1],-9999))==13 && abs(Alt$(Lepton_eta[1],-9999.)) <2.4))'
}
aliases['jetpt30']={
    'expr': 'Alt$(CleanJet_pt[0],-9999.) >30 && Alt$(CleanJet_pt[1],-9999.) >30'
}
aliases['jetpt50']={
    'expr': 'Alt$(CleanJet_pt[0],-9999.) >50 && Alt$(CleanJet_pt[1],-9999.) >50'
}
aliases['leppt0']={
    'expr': 'Alt$(Lepton_pt[0],-9999.) >25 && Alt$(Lepton_pt[1],-9999.) >20'
}
aliases['leppt1']={
    'expr': 'Alt$(Lepton_pt[0],-9999.) >30 && Alt$(Lepton_pt[1],-9999.) >30'
}
# -3.2<eta<-1.3 and -1.57<phi< -0.87
aliases['HEM']={
    'expr': '(Alt$(CleanJet_eta[0],-9999.)>-3.2 && Alt$(CleanJet_eta[0],-9999.)<-1.3 && Alt$(CleanJet_phi[0],-9999.)>-1.57 && Alt$(CleanJet_phi[0],-9999.)<-0.87) || \
        (Alt$(CleanJet_eta[1],-9999.)>-3.2 && Alt$(CleanJet_eta[1],-9999.)<-1.3 && Alt$(CleanJet_phi[1],-9999.)>-1.57 && Alt$(CleanJet_phi[1],-9999.)<-0.87)'
}
# ssww region
aliases['zlep_ww']={
    'expr': 'abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75 && abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75'
}
aliases['zveto_ww']={
    'expr': '(abs(Alt$(Lepton_pdgId[0],-9999)) * abs(Alt$(Lepton_pdgId[1],-9999)) != 11*11 || abs(mll - 91.1876) > 15)'
}
#aliases['ssww_region']={
#    'expr': 'nLepton>1 && nCleanJet >1 && Alt$(Lepton_pt[2],0.)<10 && MET_pt>30 && mll > 20 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 && tauVeto_ww && zveto_ww && lep0eta && lep1eta'  # pt zlep mjj detajj
#}

# B tag scale factors

#btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')
#
#aliases['Jet_btagSF_shapeFix'] = {
#    'linesToAdd': [
#        'gSystem->Load("libCondFormatsBTauObjects.so");',
#        'gSystem->Load("libCondToolsBTau.so");',
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#        '.L %s/patches/btagsfpatch.cc+' % configurations
#    ],
#    'class': 'BtagSF',
#    'args': (btagSFSource,),
#    'samples': mc
#}
# aliases['bVetoSF'] = {
#     'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
#     'samples': mc
# }

# aliases['btag0SF'] = {
#     'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5))))',
#     'samples': mc
# }

# aliases['btagnSF'] = {
#     'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx] + (CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
#     'samples': mc
# }

# aliases['btagSF'] = {
#     'expr': 'bVetoSF*bVeto + btag0SF*btag0 + btagnSF*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)',
#     'samples': mc
# }

# systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

# for s in systs:
#   aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }
#   aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc }



# for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
#     #aliases['Jet_btagSF_deepcsv_shape_up_%s' % shift] = {
#     #    'class': 'BtagSF',
#     #    'args': (btagSFSource, 'up_' + shift),
#     #    'samples': mc
#     #}
#     #aliases['Jet_btagSF_deepcsv_shape_down_%s' % shift] = {
#     #    'class': 'BtagSF',
#     #    'args': (btagSFSource, 'down_' + shift),
#     #    'samples': mc
#     #}

#     for targ in ['bVeto', 'btag0', 'btagn']:
#         alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#         alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)

#         alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#         alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)

#     aliases['btagSF%sup' % shift] = {
#         'expr': 'bVetoSF{shift}up*bVeto + btag0SF{shift}up*btag0 + btagnSF{shift}up*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)'.format(shift = shift),
#         'samples': mc
#     }

#     aliases['btagSF%sdown' % shift] = {
#         'expr': 'bVetoSF{shift}down*bVeto + btag0SF{shift}down*btag0 + btagnSF{shift}down*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)'.format(shift = shift),
#         'samples': mc
#     }

#data/MC scale factors
aliases['SFweight_mod_SMP'] = {
    'expr': ' * '.join(['SFweight2l','LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut','METFilter_MC','btagSF']), #bveto_sf*lep_sf*trig_sf*mu_roc_sf
    'samples': mcSMP
}
aliases['SFweight_mod_EFT'] = {
    'expr': ' * '.join(['SFweight2l','LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut','METFilter_MC','btagSF_EFT']), #bveto_sf*lep_sf*trig_sf*mu_roc_sf
    'samples': mcEFT
}


# aliases['mcCommonWeight_os'] = {
#     'expr': 'SFweight2l*XSWeight*PromptGenLepMatch2l*chargeflip_w*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) < 0)',
#     'samples':mc
# }
aliases['mcCommonWeight_os'] = {
    'expr': 'XSWeight*SFweight_mod_SMP*PromptGenLepMatch2l*chargeflip_w*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) < 0)',
    'samples':mcSMP
}

aliases['samesign_requirement'] = {
    'expr': '(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) > 0)',
    'samples':SSsamples
}

# # variations
# aliases['SFweightEleUp'] = {
#     'expr': 'LepSF2l__ele_'+eleWP+'__Up',
#     'samples': mc
# }
# aliases['SFweightEleDown'] = {
#     'expr': 'LepSF2l__ele_'+eleWP+'__Do',
#     'samples': mc
# }
# aliases['SFweightMuUp'] = {
#     'expr': 'LepSF2l__mu_'+muWP+'__Up',
#     'samples': mc
# }
# aliases['SFweightMuDown'] = {
#     'expr': 'LepSF2l__mu_'+muWP+'__Do',
#     'samples': mc
# }
aliases['zlep1'] = {'expr' : '(Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj'}
aliases['zlep2'] = {'expr' : '(Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj'}










########################################################################## 
############### my own weights for the nuisances #########################

aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}



# for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
#       for targ in ['bVeto', 'bReq']:
#           alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#           alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_up_%s' % shift)

#           alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#           alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_down_%s' % shift)

#       aliases['btagSF%sup' % shift] = {
#           'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
#           'samples': mc
#       }

#       aliases['btagSF%sdown' % shift] = {
#           'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
#           'samples': mc
#       }


aliases['Jet_PUIDSF'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))',
  'samples': mc
}

aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_up)))',
  'samples': mc
}

aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_down)))',
  'samples': mc
}



##########################################################################
################## EFT reweighting weights ###############################

op = ["cW", "cHDD", "cHW", "cHWB", "cHbox", "cHj1", "cHj3", "cHl1", "cHl3", "cll1", "cjj11", "cjj31", "cjj18", "cjj38"]
# the following (ls) contains the operators in the same order as in the LHEReweightingWeight vector
ls = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38']
# te following (mix) contains all the operators with mixed terms as well, in the LHEReweightingWeight order
mix = ['SM', 'cW_m1', 'cW', 'cHDD_m1', 'cHDD', 'cHW_m1', 'cHW', 'cHWB_m1', 'cHWB', 'cHbox_m1', 'cHbox', 'cHj1_m1', 'cHj1', 'cHj3_m1', 'cHj3', 'cHl1_m1', 'cHl1', 'cHl3_m1', 'cHl3', 'cll1_m1', 'cll1', 'cjj11_m1', 'cjj11', 'cjj31_m1', 'cjj31', 'cjj18_m1', 'cjj18', 'cjj38_m1', 'cjj38', 'cW_cHDD', 'cW_cHW', 'cW_cHWB', 'cW_cHbox', 'cW_cHj1', 'cW_cHj3', 'cW_cHl1', 'cW_cHl3', 'cW_cll1', 'cW_cjj11', 'cW_cjj31', 'cW_cjj18', 'cW_cjj38', 'cHDD_cHW', 'cHDD_cHWB', 'cHDD_cHbox', 'cHDD_cHj1', 'cHDD_cHj3', 'cHDD_cHl1', 'cHDD_cHl3', 'cHDD_cll1', 'cHDD_cjj11', 'cHDD_cjj31', 'cHDD_cjj18', 'cHDD_cjj38', 'cHW_cHWB', 'cHW_cHbox', 'cHW_cHj1', 'cHW_cHj3', 'cHW_cHl1', 'cHW_cHl3', 'cHW_cll1', 'cHW_cjj11', 'cHW_cjj31', 'cHW_cjj18', 'cHW_cjj38', 'cHWB_cHbox', 'cHWB_cHj1', 'cHWB_cHj3', 'cHWB_cHl1', 'cHWB_cHl3', 'cHWB_cll1', 'cHWB_cjj11', 'cHWB_cjj31', 'cHWB_cjj18', 'cHWB_cjj38', 'cHbox_cHj1', 'cHbox_cHj3', 'cHbox_cHl1', 'cHbox_cHl3', 'cHbox_cll1', 'cHbox_cjj11', 'cHbox_cjj31', 'cHbox_cjj18', 'cHbox_cjj38', 'cHj1_cHj3', 'cHj1_cHl1', 'cHj1_cHl3', 'cHj1_cll1', 'cHj1_cjj11', 'cHj1_cjj31', 'cHj1_cjj18', 'cHj1_cjj38', 'cHj3_cHl1', 'cHj3_cHl3', 'cHj3_cll1', 'cHj3_cjj11', 'cHj3_cjj31', 'cHj3_cjj18', 'cHj3_cjj38', 'cHl1_cHl3', 'cHl1_cll1', 'cHl1_cjj11', 'cHl1_cjj31', 'cHl1_cjj18', 'cHl1_cjj38', 'cHl3_cll1', 'cHl3_cjj11', 'cHl3_cjj31', 'cHl3_cjj18', 'cHl3_cjj38', 'cll1_cjj11', 'cll1_cjj31', 'cll1_cjj18', 'cll1_cjj38', 'cjj11_cjj31', 'cjj11_cjj18', 'cjj11_cjj38', 'cjj31_cjj18', 'cjj31_cjj38', 'cjj18_cjj38']


### lin and quad components
aliases['rw_SM'] = {
    'expr' : 'LHEReweightingWeight[0]',
    'samples': mcEFT
}

for o in op:
    ip = ls.index(o)
    im = ls.index(o+'_m1')
    print (o, ip, im)

    aliases['rw_LIN_'+o] = {
        'expr' : '0.5*(LHEReweightingWeight['+str(ip)+'] - LHEReweightingWeight['+str(im)+'])',
        'samples': mcEFT
    }
    aliases['rw_QUAD_'+o] = {
        'expr' : '0.5*(LHEReweightingWeight['+str(ip)+'] + LHEReweightingWeight['+str(im)+'] - 2*LHEReweightingWeight[0])',
        'samples': mcEFT
    }


for i in range(len(op)):
    for j in range(len(op)):
        if j > i:
            term = op[i]+'_'+op[j]
            ix = mix.index(term)
            
            aliases['rw_MIX_'+term] = {
                'expr' : 'LHEReweightingWeight['+str(ix)+']',
                'samples': mcEFT
            }




