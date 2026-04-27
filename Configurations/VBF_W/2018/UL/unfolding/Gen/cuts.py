# cuts

supercut = '1.'


cuts['ALL'] = '(((abs(Alt$(DressedLepton_pdgId[0],0))==11) || (abs(Alt$(DressedLepton_pdgId[0],0))==13))>0) \
            && (Alt$(DressedLepton_isPrompt[0],0)==1) \
            && (Alt$(DressedLepton_pt[0],0)>=20.) \
            && (Alt$(nCleanGenJet20,0)>=2) \
            && Alt$(CleanGenJet_pt[0],0) >= 25. \
            && Alt$(CleanGenJet_pt[1],0) >= 25. \
            && Alt$(CleanGenJet_eta[0],10) < 5. \
            && Alt$(CleanGenJet_eta[0],10) > -5. \
            && Alt$(CleanGenJet_eta[1],10) < 5. \
            && Alt$(CleanGenJet_eta[1],10) > -5. \
            && mjj_gen > 120. \
            && lhe_gensel > 0.5'

# cuts['ele_mu'] = '( (abs(Alt$(DressedLepton_pdgId[0],0)) == 11) || (abs(Alt$(DressedLepton_pdgId[0],0)) == 13) )'

# cuts['ele_mu_notau'] = '( (abs(Alt$(DressedLepton_pdgId[0],0)) == 11) || (abs(Alt$(DressedLepton_pdgId[0],0)) == 13) ) \
#                         && DressedLepton_isPrompt[0] == 1 \
#                         && DressedLepton_isTauDecayProduct[0] == 0 \
#                         && DressedLepton_isDirectPromptTauDecayProduct[0] == 0 '

# cuts['ele_mu_LHE'] = '( ( abs(Alt$(LHEPart_pdgId[2],0))==11 || abs(Alt$(LHEPart_pdgId[2],0))==13 || \
#                          abs(Alt$(LHEPart_pdgId[2],0))==12 || abs(Alt$(LHEPart_pdgId[2],0))==14 ) && \
#                        ( abs(Alt$(LHEPart_pdgId[3],0))==11 || abs(Alt$(LHEPart_pdgId[3],0))==13 || \
#                          abs(Alt$(LHEPart_pdgId[3],0))==12 || abs(Alt$(LHEPart_pdgId[3],0))==14 ) )'


# cuts['tauVetoALL'] = '( tauVetoALL )'

# cuts['tauVeto'] = '( tauVeto )'

