# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
supercut = '(   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>35)\
             || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
            && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
            && vbs_0_pt > 50 && vbs_1_pt > 30 \
            && PuppiMET_pt > 30 \
            && deltaeta_vbs >= 2.5  \
            && mjj_vbs >= 500 \
            && Mtw_lep < 185 \
            '


############ 
## Signal

cuts["res_sig_ele"] = 'VBS_category==1 \
                      && abs(Lepton_pdgId[0])==11 \
                      && vjet_0_pt > 30 && vjet_1_pt > 30 \
                      && mjj_vjet > 65 && mjj_vjet < 105 \
                      && bVeto \
                      && w_had_pt < 200 \
                      && veto_fatjet_180 \
                      '


cuts["res_sig_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                              '

cuts["boost_sig_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 70 && mjj_vjet < 115 \
                            && bVeto \
                            '


cuts["boost_sig_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 70 && mjj_vjet < 115 \
                            && bVeto \
                            '


###############
#### Wjets

cuts["res_wjetcr_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet> 40 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                '



cuts["res_wjetcr_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet> 40 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                '

cuts["boost_wjetcr_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                             && w_had_pt >= 200 \
                            && mjj_vjet > 40 && (mjj_vjet <= 70 || mjj_vjet >= 115)  \
                            && bVeto \
                            '

cuts["boost_wjetcr_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 40 && (mjj_vjet <= 70 || mjj_vjet >= 115)  \
                            && bVeto \
                            '



###############
##### Top

### Top Tight region

cuts["res_topcr_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bReqTight \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                '

cuts["res_topcr_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bReqTight \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                '


# Tight top
cuts["boost_topcr_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 70 && mjj_vjet < 115 \
                            && bReqTight \
                            '


cuts["boost_topcr_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 70 && mjj_vjet < 115 \
                            && bReqTight \
                            '
                            
                            
# Appending the cut on the weight distributions

cuts["res_sig_ele_EFTweightCut3s"] = 'VBS_category==1 \
                      && abs(Lepton_pdgId[0])==11 \
                      && vjet_0_pt > 30 && vjet_1_pt > 30 \
                      && mjj_vjet > 65 && mjj_vjet < 105 \
                      && bVeto \
                      && w_had_pt < 200 \
                      && veto_fatjet_180 \
                      && EFTweightCut3s \
                      '


cuts["res_sig_mu_EFTweightCut3s"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                && EFTweightCut3s \
                              '

cuts["boost_sig_ele_EFTweightCut3s"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 70 && mjj_vjet < 115 \
                            && bVeto \
                            '


cuts["boost_sig_mu_EFTweightCut3s"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 70 && mjj_vjet < 115 \
                            && bVeto \
                            && EFTweightCut3s \
                            '


###############
#### Wjets

cuts["res_wjetcr_ele_EFTweightCut3s"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet> 40 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                && EFTweightCut3s \
                                '



cuts["res_wjetcr_mu_EFTweightCut3s"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet> 40 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                && EFTweightCut3s \
                                '

cuts["boost_wjetcr_ele_EFTweightCut3s"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                             && w_had_pt >= 200 \
                            && mjj_vjet > 40 && (mjj_vjet <= 70 || mjj_vjet >= 115)  \
                            && bVeto \
                            && EFTweightCut3s \
                            '

cuts["boost_wjetcr_mu_EFTweightCut3s"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 40 && (mjj_vjet <= 70 || mjj_vjet >= 115)  \
                            && bVeto \
                            && EFTweightCut3s \
                            '



###############
##### Top

### Top Tight region

cuts["res_topcr_ele_EFTweightCut3s"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bReqTight \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                && EFTweightCut3s \
                                '

cuts["res_topcr_mu_EFTweightCut3s"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bReqTight \
                                && w_had_pt < 200 \
                                && veto_fatjet_180 \
                                && EFTweightCut3s \
                                '


# Tight top
cuts["boost_topcr_ele_EFTweightCut3s"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 70 && mjj_vjet < 115 \
                            && bReqTight \
                            && EFTweightCut3s \
                            '


cuts["boost_topcr_mu_EFTweightCut3s"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && w_had_pt >= 200 \
                            && mjj_vjet > 70 && mjj_vjet < 115 \
                            && bReqTight \
                            && EFTweightCut3s \
                            '
                            


cuts["all"] = supercut

cuts["all_EFTweightCut3s"] = supercut + " && EFTweightCut3s"
cuts["all_1"] = supercut + " && cut_mixed_weight_cbHIm_cHQ3_EFTweightCut3s"
cuts["all_2"] = supercut + " && cut_quad_weight_cQj31_EFTweightCut3s"
cuts["all_3"] = supercut + " && cut_lin_weight_cHbox_EFTweightCut3s"
cuts["all_4"] = supercut + " && cut_quad_weight_cQQ8_EFTweightCut3s"
cuts["all_5"] = supercut + " && cut_quad_weight_cHbq_EFTweightCut3s"