# cuts

supercut = '(Alt$(CleanJet_pt[0],0.)>40. && Alt$(CleanJet_pt[1],0.)>30.)\
            && (Alt$(Lepton_eta[0],-3) > -2.) && (Alt$(Lepton_eta[0],3) < 2.)\
            && (Alt$(Lepton_pt[0],0) > 30.)\
            && mtw1 < 20 && CleanJet_pt[1]<=70.\
            && (MET_pt < 60 || PuppiMET_pt < 60)\
            '

# cuts['Z'] = '1'

#SR is ort to:
#top
#PU e Fake
#levo fake e DY + ort to WH
#fake

cuts['ele_FR_QCDgr1p5'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 38. \
                     && Dphilep1met > 1.5 \
                     '

cuts['mu_FR_QCDgr1p5'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==13) \
                     && Dphilep1met > 1.5 \
                     '

cuts['ele_FR_Zpeakgr1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 38. \
                    && mll>60. && mll<120. \
                    && Dphilep1met > 1.5 \
                    '
cuts['mu_FR_Zpeakgr1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==13) \
                    && (abs(Lepton_pdgId[1])==13) \
                    && mll>60. && mll<120. \
                    && Dphilep1met > 1.5 \
                    '

cuts['ele_FR_QCDless1p5'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 38. \
                     && Dphilep1met < 1.5 \
                     '

cuts['mu_FR_QCDless1p5'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==13) \
                     && Dphilep1met < 1.5 \
                     '

cuts['ele_FR_Zpeakless1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 38. \
                    && mll>60. && mll<120. \
                    && Dphilep1met < 1.5 \
                    '
cuts['mu_FR_Zpeakless1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==13) \
                    && (abs(Lepton_pdgId[1])==13) \
                    && mll>60. && mll<120. \
                    && Dphilep1met < 1.5 \
                    '

cuts['ele_FR_QCD'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 38. \
                     '

cuts['mu_FR_QCD'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==13) \
                     '

cuts['ele_FR_Zpeak'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 38. \
                    && mll>60. && mll<120. \
                    '
cuts['mu_FR_Zpeak'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==13) \
                    && (abs(Lepton_pdgId[1])==13) \
                    && mll>60. && mll<120. \
                    '

                    
# # # # # Top control region (common mu & e)
cuts['ele_topcrgr1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 38.\
                    && Dphilep1met > 1.5 \
                    '
cuts['mu_topcrgr1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    && Dphilep1met > 1.5 \
                    '
cuts['ele_topcrless1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 38.\
                    && Dphilep1met < 1.5 \
                    '
cuts['mu_topcrless1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    && Dphilep1met < 1.5 \
                    '
cuts['ele_topcr']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 38.\
                    '
cuts['mu_topcr']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    '