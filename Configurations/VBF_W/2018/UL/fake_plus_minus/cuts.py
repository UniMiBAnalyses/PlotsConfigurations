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
            && DNNJoined >= 0.5 \
            '



cuts['ele_SR_plus'] = 'Lepton_pdgId[0]==-11 \
                  && Lepton_pt[0] > 35. \
                  && bVeto \
                  && detajj > 4 \
                  && CleanJet_pt[1]>70. \
                  && mtw1 > 50. \
                 '

cuts['mu_SR_plus'] = 'Lepton_pdgId[0]==-13 \
                  && bVeto \
                  && detajj > 4 \
                  && CleanJet_pt[1]>70. \
                  && mtw1 > 50. \
                 '

cuts['ele_SR_minus'] = 'Lepton_pdgId[0]==11 \
                  && Lepton_pt[0] > 35. \
                  && bVeto \
                  && detajj > 4 \
                  && CleanJet_pt[1]>70. \
                  && mtw1 > 50. \
                 '

cuts['mu_SR_minus'] = 'Lepton_pdgId[0]==13 \
                  && bVeto \
                  && detajj > 4 \
                  && CleanJet_pt[1]>70. \
                  && mtw1 > 50. \
                 '


# # ##Hard & PU WJets CRs
cuts['ele_HWJ_plus'] = 'Lepton_pdgId[0]==-11 \
                    && Lepton_pt[0] > 35. \
                    && bVeto \
                    && mjj <= 750. \
                    && detajj <= 4 \
                    && mtw1 > 50. \
                    '

cuts['ele_PUWJ_plus'] = 'Lepton_pdgId[0]==-11 \
                    && Lepton_pt[0] > 35. \
                    && detajj > 5. \
                    && CleanJet_pt[1]<=70.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    '


cuts['mu_HWJ_plus'] = 'Lepton_pdgId[0]==-13 \
                    && bVeto \
                    && mjj <= 750. \
                    && detajj <= 4 \
                    && mtw1 > 50. \
                    '

cuts['mu_PUWJ_plus'] = 'Lepton_pdgId[0]==-13 \
                    && detajj > 5. \
                    && CleanJet_pt[1]<=70.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    '

cuts['ele_HWJ_minus'] = 'Lepton_pdgId[0]==11 \
                    && Lepton_pt[0] > 35. \
                    && bVeto \
                    && mjj <= 750. \
                    && detajj <= 4 \
                    && mtw1 > 50. \
                    '

cuts['ele_PUWJ_minus'] = 'Lepton_pdgId[0]==11 \
                    && Lepton_pt[0] > 35. \
                    && detajj > 5. \
                    && CleanJet_pt[1]<=70.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    '


cuts['mu_HWJ_minus'] = 'Lepton_pdgId[0]==13 \
                    && bVeto \
                    && mjj <= 750. \
                    && detajj <= 4 \
                    && mtw1 > 50. \
                    '

cuts['mu_PUWJ_minus'] = 'Lepton_pdgId[0]==13 \
                    && detajj > 5. \
                    && CleanJet_pt[1]<=70.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    '

                    
# # # # Top control region (common mu & e)
cuts['ele_topcr_plus']  = '(bReq) \
                  && Lepton_pdgId[0]==-11 \
                  && Lepton_pt[0] > 35. \
                '
cuts['mu_topcr_plus']  = '(bReq) \
                  && Lepton_pdgId[0]==-13 \
                '

cuts['ele_topcr_minus']  = '(bReq) \
                  && Lepton_pdgId[0]==11 \
                  && Lepton_pt[0] > 35. \
                '
cuts['mu_topcr_minus']  = '(bReq) \
                  && Lepton_pdgId[0]==13 \
                '



#### Fake CRs
cuts['ele_FakeCR_minus']  = 'Lepton_pdgId[0]==11 \
                      && Lepton_pt[0] > 35. \
                      && detajj <= 5. \
                      && bVeto\
                      && mtw1<=50. \
                      && mtw1 > 20. \
                      && CleanJet_pt[1]<=70.  \
                     '

cuts['ele_FakeCR_plus']  = 'Lepton_pdgId[0]==-11 \
                      && Lepton_pt[0] > 35. \
                      && detajj <= 5. \
                      && bVeto\
                      && mtw1<=50. \
                      && mtw1 > 20. \
                      && CleanJet_pt[1]<=70.  \
                      '

cuts['mu_FakeCR_minus']  = 'Lepton_pdgId[0]==13 \
                      && detajj <= 5. \
                      && bVeto\
                      && mtw1<=50. \
                      && mtw1 > 20. \
                      && CleanJet_pt[1]<=70.  \
                     '

cuts['mu_FakeCR_plus']  = 'Lepton_pdgId[0]==-13 \
                      && detajj <= 5. \
                      && bVeto\
                      && mtw1<=50. \
                      && mtw1 > 20. \
                      && CleanJet_pt[1]<=70.  \
                      '
