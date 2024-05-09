# cuts

# supercut = '1'
supercut = '(Alt$(CleanJet_pt[0],0.)>40. && Alt$(CleanJet_pt[1],0.)>30.)\
            && (Alt$(Lepton_eta[0],-3) > -2.) && (Alt$(Lepton_eta[0],3) < 2.)\
            && mtw1 < 20 && CleanJet_pt[1]<=70.\
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

cuts['ele_FR_QCDgr1p5'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 30. \
                     && Dphilep1met > 1.5 \
                     '

cuts['mu_FR_QCDgr1p5'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==13) \
                     && Lepton_pt[0] > 25. \
                     && Dphilep1met > 1.5 \
                     '

cuts['ele_FR_Zpeakgr1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 30. \
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

cuts['ele_FR_QCDless1p5'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 30. \
                     && Dphilep1met < 1.5 \
                     '

cuts['mu_FR_QCDless1p5'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==13) \
                     && Lepton_pt[0] > 25. \
                     && Dphilep1met < 1.5 \
                     '

cuts['ele_FR_Zpeakless1p5'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 30. \
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

cuts['ele_FR_QCD'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==11) \
                     && Lepton_pt[0] > 30. \
                     '

cuts['mu_FR_QCD'] = 'nLepton15==1 \
                     && (abs(Lepton_pdgId[0])==13) \
                     && Lepton_pt[0] > 25. \
                     '

cuts['ele_FR_Zpeak'] = 'nLepton15 > 1 \
                    && (abs(Lepton_pdgId[0])==11) \
                    && (abs(Lepton_pdgId[1])==11) \
                    && Lepton_pt[0] > 30. \
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
                    && Lepton_pt[0] > 30.\
                    && Dphilep1met > 1.5 \
                    '
cuts['mu_topcrgr1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    && Lepton_pt[0] > 25.\
                    && Dphilep1met > 1.5 \
                    '
cuts['ele_topcrless1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 30.\
                    && Dphilep1met < 1.5 \
                    '
cuts['mu_topcrless1p5']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    && Lepton_pt[0] > 25.\
                    && Dphilep1met < 1.5 \
                    '
cuts['ele_topcr']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0] > 30.\
                    '
cuts['mu_topcr']  = '((zeroJet && !bVeto) || bReqTight) \
                    && (abs(Lepton_pdgId[0])==13) \
                    && Lepton_pt[0] > 25.\
                    '