# cuts

supercut = 'nLepton>=1 && (Alt$(Lepton_pt[0],0) > 30.) \
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
            && (Sum$( Alt$(CleanFatJet_mass,0) > 70 && Alt$(CleanFatJet_mass,0) < 115 ) == 0) \
            && ( nJet30 <= 3 || (mjj23 < 65 || mjj23 > 105) ) \
            '


# cuts['Z'] = '1'

#SR is ort to:
#top
#PU e Fake
#levo fake e DY + ort to WH
#fake


# cuts['test'] = ' Lepton_pt[0] > 38. \
#                   && bVeto \
#                  '

cuts['ele_SR'] = '(abs(Lepton_pdgId[0])==11) \
                  && Lepton_pt[0] > 38. \
                  && bVeto \
                  && detajj > 4. \
                  && CleanJet_pt[1]>70. \
                  && mtw1 > 50. \
                 '

cuts['mu_SR'] = '(abs(Lepton_pdgId[0])==13)\
                  && bVeto \
                  && detajj > 4. \
                  && CleanJet_pt[1]>70. \
                  && mtw1 > 50. \
                 '


# # ##Hard & PU WJets CRs
cuts['ele_HWJ'] = '(abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 38. \
                    && bVeto \
                    && mjj <= 750. \
                    && detajj <= 4 \
                    && mtw1 > 50. \
                    '

cuts['ele_PUWJ'] = '(abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 38. \
                    && detajj > 5. \
                    && CleanJet_pt[1]<=70.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    '


cuts['mu_HWJ'] = '(abs(Lepton_pdgId[0])==13) \
                    && bVeto \
                    && mjj <= 750. \
                    && detajj <= 4 \
                    && mtw1 > 50. \
                    '

cuts['mu_PUWJ'] = '(abs(Lepton_pdgId[0])==13) \
                    && detajj > 5. \
                    && CleanJet_pt[1]<=70.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    '

                    
# # # Top control region (common mu & e)
cuts['ele_topcr']  = '(bReq) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 38.\
                    '
cuts['mu_topcr']  = '(bReq) \
                    && (abs(Lepton_pdgId[0])==13) \
                    '
# cuts['topcr']  = '(bReq) \
#                     &&  Lepton_pt[0] > 38.\
#                     '

# # # # ## Fake CR   
# # cuts['ele_FakeCR']  = '(abs(Lepton_pdgId[0])==11) \
# #                       && Lepton_pt[0] > 38. \
# #                       && detajj <= 5. \
# #                       && bVeto\
# #                       && mtw1<=50. \
# #                       && mtw1 > 20. \
# #                       && CleanJet_pt[1]<=70.  \
# #                      '

# # cuts['mu_FakeCR']  = '(abs(Lepton_pdgId[0])==13) \
# #                       && detajj <= 5. \
# #                       && bVeto\
# #                       && mtw1<=50. \
# #                       && mtw1 > 20. \
# #                       && CleanJet_pt[1]<=70.  \
# #                      '
