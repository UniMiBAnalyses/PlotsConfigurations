# cuts

supercut = 'nLepton>=1 && (Alt$(Lepton_pt[0],0) > 25.) \
            && ((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
            && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) > 3.))\
            && (Alt$(CleanJet_pt[1], 0) > 30.) \
            && (Alt$(CleanJet_pt[0],0) > 40.) \
            && (mjj >= 400.) \
            && (detajj > 2.) \
            && (Alt$(Lepton_eta[0],-3) > -2.) \
            && (Alt$(Lepton_eta[0],3) < 2.) \
            && Alt$(Lepton_pt[1],0)<=15. \
            && Alt$(Lepton_isLoose[1],1)> 0.5 \
            '

# supercut = '(Alt$(CleanJet_pt[0],0.)>40. && Alt$(CleanJet_pt[1],0.)>30.)\
#             && Alt$(Lepton_pt[1],0.)<10. \
#             '

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


cuts['ele_SR'] = '(abs(Lepton_pdgId[0])==11) \
                  && Lepton_pt[0] > 35. \
                  && bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj > 4 \
                  && mtw1 > 50. \
                 '

cuts['mu_SR'] = '(abs(Lepton_pdgId[0])==13)\
                  && bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj > 4 \
                  && mtw1 > 50. \
                 '

cuts['ele_SR_cut1p2'] = '(abs(Lepton_pdgId[0])==11) \
                  && Lepton_pt[0] > 35. \
                  && bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj > 4 \
                  && mtw1 > 50. \
                  && RatioJets_pt > 1.2\
                 '

cuts['mu_SR_cut1p2'] = '(abs(Lepton_pdgId[0])==13)\
                  && bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj > 4 \
                  && mtw1 > 50. \
                  && RatioJets_pt > 1.2\
                 '
cuts['ele_SR_cut1p3'] = '(abs(Lepton_pdgId[0])==11) \
                  && Lepton_pt[0] > 35. \
                  && bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj > 4 \
                  && mtw1 > 50. \
                  && RatioJets_pt > 1.3\
                 '

cuts['mu_SR_cut1p3'] = '(abs(Lepton_pdgId[0])==13)\
                  && bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj > 4 \
                  && mtw1 > 50. \
                  && RatioJets_pt > 1.3\
                 '

# cuts['ele_SR_no2PU'] = '(abs(Lepton_pdgId[0])==11) \
#                   && Lepton_pt[0] > 35. \
#                   && bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                   && abs(Dphilep1jet2) < 2.\
#                  '

# cuts['mu_SR_no2PU'] = '(abs(Lepton_pdgId[0])==13)\
#                   && bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                   && abs(Dphilep1jet2) < 2.\
#                  '

# cuts['ele_SR_noPUSTRONG'] = '(abs(Lepton_pdgId[0])==11) \
#                   && Lepton_pt[0] > 35. \
#                   && bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                   && abs(Dphilep1jet2) < 2.\
#                   && RatioJets_pt < 1.5\
#                  '

# cuts['mu_SR_noPUSTRONG'] = '(abs(Lepton_pdgId[0])==13)\
#                   && bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                   && abs(Dphilep1jet2) < 2.\
#                   && RatioJets_pt < 1.5\
#                  '

# cuts['ele_SR_noPUSWEET'] = '(abs(Lepton_pdgId[0])==11) \
#                   && Lepton_pt[0] > 35. \
#                   && bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                   && abs(Dphilep1jet2) < 2.\
#                   && RatioJets_pt < 2.5\
#                  '

# cuts['mu_SR_noPUSWEET'] = '(abs(Lepton_pdgId[0])==13)\
#                   && bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                   && abs(Dphilep1jet2) < 2.\
#                   && RatioJets_pt < 2.5\
#                  '

# cuts['ele_SR_noPUJET'] = '(abs(Lepton_pdgId[0])==11) \
#                   && Lepton_pt[0] > 35. \
#                   && bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                   && abs(Dphilep1jet2) < 2.\
#                   && CleanJet_pt[0] < 340.\
#                  '

# cuts['mu_SR_noPUJET'] = '(abs(Lepton_pdgId[0])==13)\
#                   && bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                   && abs(Dphilep1jet2) < 2.\
#                   && CleanJet_pt[0] < 340.\
#                  '




# # # ##Hard & PU WJets CRs
# cuts['ele_HWJ'] = '(abs(Lepton_pdgId[0])==11) \
#                     && Lepton_pt[0] > 35. \
#                     && bVeto \
#                     && mjj <= 750. \
#                     && detajj <= 4 \
#                     && mtw1 > 50. \
#                     '

# cuts['ele_PUWJ'] = '(abs(Lepton_pdgId[0])==11) \
#                     && Lepton_pt[0] > 35. \
#                     && detajj > 5. \
#                     && CleanJet_pt[1]<=70.\
#                     && bVeto \
#                     && PuppiMET_pt>70. \
#                     && mtw1>50. \
#                     '


# cuts['mu_HWJ'] = '(abs(Lepton_pdgId[0])==13) \
#                     && bVeto \
#                     && mjj <= 750. \
#                     && detajj <= 4 \
#                     && mtw1 > 50. \
#                     '

# cuts['mu_PUWJ'] = '(abs(Lepton_pdgId[0])==13) \
#                     && detajj > 5. \
#                     && CleanJet_pt[1]<=70.\
#                     && bVeto \
#                     && PuppiMET_pt>70. \
#                     && mtw1>50. \
#                     '

                    
# # # # Top control region (common mu & e)
# cuts['topcr']  = '((zeroJet && !bVeto) || bReqTight) \
#                   && Lepton_pt[0] > 35.\
#                   '

# # # ## Fake CR   
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
