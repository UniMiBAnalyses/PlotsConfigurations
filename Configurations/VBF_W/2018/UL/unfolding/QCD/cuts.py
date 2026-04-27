# cuts

supercut = '1.'

cuts['ALL'] = '1.'

cuts['SR'] = 'nLepton>=1 && (Alt$(Lepton_pt[0],0) > 25.) \
                && ((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
                && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) > 3.)) \
                && (Alt$(abs(CleanJet_eta[0]), 5) < 4.7) \
                && (Alt$(abs(CleanJet_eta[1]), 5) < 4.7) \
                && (Alt$(CleanJet_pt[1], 0) > 30.) \
                && (Alt$(CleanJet_pt[0],0) > 40.) \
                && (mjj >= 400.) \
                && (detajj > 2.) \
                && (Alt$(Lepton_eta[0],-3) > -2.) \
                && (Alt$(Lepton_eta[0],3) < 2.) \
                && Alt$(Lepton_pt[1],0)<=15. \
                && Alt$(Lepton_isLoose[1],1)> 0.5 \
                && ((abs(Lepton_pdgId[0])==11 && Lepton_pt[0] > 35.) || (abs(Lepton_pdgId[0])==13) ) \
                && bVeto \
                && detajj > 4. \
                && CleanJet_pt[1]>70. \
                && mtw1 > 50. \
                && DNNJoined > 0.5  \
                '

