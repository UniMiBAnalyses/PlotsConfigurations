# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

supercut='nLepton>2'

cuts['wz_old_vbs_total'] ='wz_region2 && bVeto && leppt25_wz && twoJetOrMore && mjj>500 && jet_cuts'
cuts['wz_old_vbs_mll_cut'] ='wz_region2 && bVeto && leppt25_wz && twoJetOrMore && mjj>500 && jet_cuts && mll_cut_wz'
cuts['wz_old_vbs_mlll_cut'] ='wz_region2 && bVeto && leppt25_wz && twoJetOrMore && mjj>500 && jet_cuts && WH3l_mlll > 100'
cuts['wz_old_vbs_mll_mlll_cut'] ='wz_region2 && bVeto && leppt25_wz && twoJetOrMore && mjj>500 && jet_cuts && WH3l_mlll > 100 && mll_cut_wz'

cuts['wz_inc_total'] ='wzinc && bVeto && jeteta_exclude2'
cuts['wz_inc_softmuonveto'] ='wzinc && bVeto && softmuon_veto'
cuts['wz_inc_eee'] ='wzinc && bVeto && EEE'
cuts['wz_inc_mee'] ='wzinc && bVeto && MEE'
cuts['wz_inc_mme'] ='wzinc && bVeto && MME'
cuts['wz_inc_mmm'] ='wzinc && bVeto && MMM'

cuts['wz_vbs_total'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && jeteta_exclude2'
cuts['wz_vbs_softmuonveto'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && softmuon_veto && jeteta_exclude2'
cuts['wz_vbs_eee'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && EEE && jeteta_exclude2'
cuts['wz_vbs_mee'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MEE && jeteta_exclude2'
cuts['wz_vbs_mme'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MME && jeteta_exclude2'
cuts['wz_vbs_mmm'] ='wzinc && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MMM && jeteta_exclude2'

cuts['ZZ_inc_total'] ='zz && bVeto && jeteta_exclude2'
cuts['ZZ_inc_softmuonveto'] ='zz && bVeto && softmuon_veto'
cuts['ZZ_inc_eee'] ='zz && bVeto && EEE'
cuts['ZZ_inc_mee'] ='zz && bVeto && MEE'
cuts['ZZ_inc_mme'] ='zz && bVeto && MME'
cuts['ZZ_inc_mmm'] ='zz && bVeto && MMM'

cuts['ZZ_vbs_total'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && jeteta_exclude2'
cuts['ZZ_vbs_softmuonveto'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && softmuon_veto && jeteta_exclude2'
cuts['ZZ_vbs_eee'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && EEE && jeteta_exclude2'
cuts['ZZ_vbs_mee'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MEE && jeteta_exclude2'
cuts['ZZ_vbs_mme'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MME && jeteta_exclude2'
cuts['ZZ_vbs_mmm'] ='zz && bVeto && twoJetOrMore && mjj>500 && jet_cuts && MMM && jeteta_exclude2'