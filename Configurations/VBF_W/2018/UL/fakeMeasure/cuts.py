# cuts

# supercut = 'nLepton>=1 && (Alt$(Lepton_pt[0],0) > 25.) \
#             && ((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
#             && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) > 3.))\
#             && (Alt$(CleanJet_pt[1], 0) > 30.) \
#             && (Alt$(CleanJet_pt[0],0) > 40.) \
#             && (mjj >= 400.) \
#             && (detajj > 2.) \
#             && (Alt$(Lepton_eta[0],-3) > -2.) \
#             && (Alt$(Lepton_eta[0],3) < 2.) \
#             && Alt$(Lepton_pt[1],0)<=15. \
#             && Alt$(Lepton_isLoose[1],1)> 0.5 \
#             '

supercut = '((Alt$(CleanJet_pt[0], 0.) > 40.) && (Alt$(CleanJet_pt[1], 0.) > 30.))\
            && (abs(Alt$(Lepton_eta[0], 3)) < 2.5)\
            && (Alt$(mtw1, 999) < 20) && (Alt$(CleanJet_pt[1], 999) <= 70.)\
            && ((MET_pt < 60) || (PuppiMET_pt < 60))\
            && (Alt$(Lepton_pt[0], 0) > 25.)'
            

# skim: 
# '"(Alt$(Lepton_pt[0],0) > 25.) && 
# (Alt$(CleanJet_pt[1], 0) > 30.) && 
# (Alt$(CleanJet_pt[0],0) > 40.) && (mjj >= 400.) && 
# (detajj > 2.) && (Alt$(Lepton_eta[0],-3) > -2.) && 
# (Alt$(Lepton_eta[0],3) < 2.) && Alt$(Lepton_pt[1],0)<=15. && 
# Alt$(Lepton_isLoose[1],1)> 0.5 && (
#   Alt$(Lepton_isTightElectron_mvaFall17V2Iso_WP90[1], 0) < 0.5 && 
# Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )"',

# cuts['Z'] = '1'

#SR is ort to:
#top
#PU e Fake
#levo fake e DY + ort to WH
#fake




# ############
# # STANDARD #
# ############

# ### QCD regions
# cuts['ele_FR_QCD'] = 'nLepton15==1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && Lepton_pt[0] > 35. \
#                     '

# cuts['mu_FR_QCD'] = 'nLepton15==1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     '

# ### DY CR
# cuts['ele_FR_Zpeak'] = 'nLepton15 > 1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && (abs(Lepton_pdgId[1])==11) \
#                     && Lepton_pt[0] > 35. \
#                     && mll>60. && mll<120. \
#                     '
# cuts['mu_FR_Zpeak'] = 'nLepton15 > 1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     && (abs(Lepton_pdgId[1])==13) \
#                     && mll>60. && mll<120. \
#                     '

# ### top CR  
# cuts['ele_topcr']  = '(bReq) \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && Lepton_pt[0] > 35.\
#                     '
# cuts['mu_topcr']  = '( bReq ) \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     '




#################
# +/- Splitting #
#################

### QCD regions
cuts['ele_FR_QCD_minus'] = 'nLepton15==1 \
                    && bVeto \
                    && Lepton_pdgId[0]==11 \
                    && Lepton_pt[0] > 35. \
                    '

cuts['ele_FR_QCD_plus'] = 'nLepton15==1 \
                    && bVeto \
                    && Lepton_pdgId[0]==-11 \
                    && Lepton_pt[0] > 35. \
                    '

cuts['mu_FR_QCD_minus'] = 'nLepton15==1 \
                    && bVeto \
                    && Lepton_pdgId[0]==13 \
                    '
cuts['mu_FR_QCD_plus'] = 'nLepton15==1 \
                    && bVeto \
                    && Lepton_pdgId[0]==-13 \
                    '

### DY CR
cuts['ele_FR_Zpeak_minus'] = 'nLepton15 > 1 \
                    && bVeto \
                    && Lepton_pdgId[0]==11 \
                    && Lepton_pdgId[1]==-11 \
                    && Lepton_pt[0] > 35. \
                    && mll>60. && mll<120. \
                    '

cuts['ele_FR_Zpeak_plus'] = 'nLepton15 > 1 \
                    && bVeto \
                    && Lepton_pdgId[0]==-11 \
                    && Lepton_pdgId[1]==11 \
                    && Lepton_pt[0] > 35. \
                    && mll>60. && mll<120. \
                    '

cuts['mu_FR_Zpeak_minus'] = 'nLepton15 > 1 \
                    && bVeto \
                    && Lepton_pdgId[0]==13 \
                    && Lepton_pdgId[1]==-13 \
                    && mll>60. && mll<120. \
                    '
cuts['mu_FR_Zpeak_plus'] = 'nLepton15 > 1 \
                    && bVeto \
                    && Lepton_pdgId[0]==-13 \
                    && Lepton_pdgId[1]==13 \
                    && mll>60. && mll<120. \
                    '

### top CR  
cuts['ele_topcr_minus']  = '(bReq) \
                    && Lepton_pdgId[0]==11 \
                    && Lepton_pt[0] > 35.\
                    '
cuts['ele_topcr_plus']  = '(bReq) \
                    && Lepton_pdgId[0]==-11 \
                    && Lepton_pt[0] > 35.\
                    '

cuts['mu_topcr_minus']  = '( bReq ) \
                    && Lepton_pdgId[0]==13 \
                    '
cuts['mu_topcr_plus']  = '( bReq ) \
                    && Lepton_pdgId[0]==-13 \
                    '



# #########################
# #  Dphi(l1,met) >< 0.2  #
# #########################

# ### QCD regions
# cuts['ele_FR_QCDgr1p5'] = 'nLepton15==1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && Lepton_pt[0] > 35. \
#                     && Dphilep1met > 0.2 \
#                     '  

# cuts['mu_FR_QCDgr1p5'] = 'nLepton15==1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     && Dphilep1met > 0.2 \
#                     '

# cuts['ele_FR_QCDless1p5'] = 'nLepton15==1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && Lepton_pt[0] > 35. \
#                     && Dphilep1met < 0.2 \
#                     '

# cuts['mu_FR_QCDless1p5'] = 'nLepton15==1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     && Dphilep1met < 0.2 \
#                     '


# ### DY CR 
# cuts['ele_FR_Zpeakgr1p5'] = 'nLepton15 > 1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && (abs(Lepton_pdgId[1])==11) \
#                     && Lepton_pt[0] > 35. \
#                     && mll>60. && mll<120. \
#                     && Dphilep1met > 0.2 \
#                     '
# cuts['mu_FR_Zpeakgr1p5'] = 'nLepton15 > 1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     && (abs(Lepton_pdgId[1])==13) \
#                     && mll>60. && mll<120. \
#                     && Dphilep1met > 0.2 \
#                     '

# cuts['ele_FR_Zpeakless1p5'] = 'nLepton15 > 1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && (abs(Lepton_pdgId[1])==11) \
#                     && Lepton_pt[0] > 35. \
#                     && mll>60. && mll<120. \
#                     && Dphilep1met < 0.2 \
#                     '
# cuts['mu_FR_Zpeakless1p5'] = 'nLepton15 > 1 \
#                     && bVeto \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     && (abs(Lepton_pdgId[1])==13) \
#                     && mll>60. && mll<120. \
#                     && Dphilep1met < 0.2 \
#                     '


# ### top CR
# cuts['ele_topcrgr1p5']  = '(bReq) \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && Lepton_pt[0] > 35.\
#                     && Dphilep1met > 0.2 \
#                     '
# cuts['mu_topcrgr1p5']  = '(bReq) \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     && Dphilep1met > 0.2 \
#                     '
# cuts['ele_topcrless1p5']  = '(bReq) \
#                     && (abs(Lepton_pdgId[0])==11) \
#                     && Lepton_pt[0] > 35.\
#                     && Dphilep1met < 0.2 \
#                     '
# cuts['mu_topcrless1p5']  = '( bReq ) \
#                     && (abs(Lepton_pdgId[0])==13) \
#                     && Dphilep1met < 0.2 \
#                     '












####### Other to check agreement / HEM correction
# # ## Fake CR   
# cuts['ele_FakeCR']  = '(abs(Lepton_pdgId[0])==11) \
#                       && Lepton_pt[0] > 35. \
#                       && detajj <= 5. \
#                       && bVeto\
#                       && mtw1<=50. \
#                       && mtw1 > 20. \
#                       && CleanJet_pt[1]<=70.  \
#                      '

# cuts['mu_FakeCR']  = '(abs(Lepton_pdgId[0])==13) \
#                       && detajj <= 5. \
#                       && bVeto\
#                       && mtw1<=50. \
#                       && mtw1 > 20. \
#                       && CleanJet_pt[1]<=70.  \
#                      '
# ## Fake CR   
# cuts['ele_FakeCRHEM']  = '(abs(Lepton_pdgId[0])==11) \
#                       && Lepton_pt[0] > 35. \
#                       && detajj <= 5. \
#                       && bVeto\
#                       && mtw1<=50. \
#                       && mtw1 > 20. \
#                       && CleanJet_pt[1]<=70.  \
#                       && Lepton_eta[0]<-1.3 \
#                      '

# cuts['mu_FakeCRHEM']  = '(abs(Lepton_pdgId[0])==13) \
#                       && detajj <= 5. \
#                       && bVeto\
#                       && mtw1<=50. \
#                       && mtw1 > 20. \
#                       && CleanJet_pt[1]<=70.  \
#                       && Lepton_eta[0]<-1.3 \
#                      '

# cuts['ele_2FakeCR']  = '(abs(Lepton_pdgId[0])==11) \
#                       && Lepton_pt[0] > 35. \
#                       && detajj <= 5. \
#                       && bVeto\
#                       && (MET_pt <60. || PuppiMET_pt<60.) \
#                       && CleanJet_pt[1]<=70.  \
#                      '

# cuts['mu_2FakeCR']  = '(abs(Lepton_pdgId[0])==13) \
#                       && detajj <= 5. \
#                       && bVeto\
#                       && (MET_pt <60. || PuppiMET_pt<60.) \
#                       && CleanJet_pt[1]<=70.  \
#                      '
