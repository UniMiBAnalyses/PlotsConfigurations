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

supercut = '(Alt$(Lepton_eta[0],-3) > -2.) && (Alt$(Lepton_eta[0],3) < 2.)\
            && (Alt$(Lepton_eta[1],-3) > -2.) && (Alt$(Lepton_eta[1],3) < 2.)\
            && mtw1 < 20 \
            && (MET_pt < 60 || PuppiMET_pt < 60)\
            '

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

cuts['ele_FR_QCDgr1p5'] = 'nLepton15==2 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 35. \
                     && Dphilep1met > 1.5 \
                     '

cuts['mu_FR_QCDgr1p5'] = 'nLepton15==2 \
                     && (abs(Lepton_pdgId[0])==13) \
                     && Lepton_pt[0] > 25. \
                     && Dphilep1met > 1.5 \
                     '

cuts['ele_FR_Zpeakgr1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 35. \
                    && mll>60. && mll<120. \
                    && Dphilep1met > 1.5 \
                    '
cuts['mu_FR_Zpeakgr1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==13) \
                    && (abs(Lepton_pdgId[1])==13) \
                    && Lepton_pt[0] > 25. \
                    && mll>60. && mll<120. \
                    && Dphilep1met > 1.5 \
                    '

cuts['ele_FR_QCDless1p5'] = 'nLepton15==2 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 35. \
                     && Dphilep1met < 1.5 \
                     '

cuts['mu_FR_QCDless1p5'] = 'nLepton15==2 \
                     && (abs(Lepton_pdgId[0])==13) \
                     && Lepton_pt[0] > 25. \
                     && Dphilep1met < 1.5 \
                     '

cuts['ele_FR_Zpeakless1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 35. \
                    && mll>60. && mll<120. \
                    && Dphilep1met < 1.5 \
                    '
cuts['mu_FR_Zpeakless1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==13) \
                    && (abs(Lepton_pdgId[1])==13) \
                    && Lepton_pt[0] > 25. \
                    && mll>60. && mll<120. \
                    && Dphilep1met < 1.5 \
                    '

cuts['ele_FR_QCD'] = 'nLepton15==2 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 35. \
                     '

cuts['mu_FR_QCD'] = 'nLepton15==2 \
                     && (abs(Lepton_pdgId[0])==13) \
                     && Lepton_pt[0] > 25. \
                     '

cuts['ele_FR_Zpeak'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 35. \
                    && mll>60. && mll<120. \
                    '
cuts['mu_FR_Zpeak'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==13) \
                    && (abs(Lepton_pdgId[1])==13) \
                    && Lepton_pt[0] > 25. \
                    && mll>60. && mll<120. \
                    '

                    
# # # # # Top control region (common mu & e)
cuts['ele_topcrgr1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 35.\
                    && Dphilep1met > 1.5 \
                    '
cuts['mu_topcrgr1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    && Lepton_pt[0] > 25.\
                    && Dphilep1met > 1.5 \
                    '
cuts['ele_topcrless1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 35.\
                    && Dphilep1met < 1.5 \
                    '
cuts['mu_topcrless1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    && Lepton_pt[0] > 25.\
                    && Dphilep1met < 1.5 \
                    '
cuts['ele_topcr']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 35.\
                    '
cuts['mu_topcr']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    && Lepton_pt[0] > 25.\
                    '

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
