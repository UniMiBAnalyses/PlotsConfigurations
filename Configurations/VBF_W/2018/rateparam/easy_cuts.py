# 
# Expanded version of cuts.py 
# 
supercut = ' ((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))             && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) > 3.))             ' 


cuts['ele_HWJ'] = ' \
 (abs(Lepton_pdgId[0])==11)                     && Lepton_pt[0] > 35.                     && bVeto                     && mjj <= 750.                     && detajj <= 4                     && mtw1 > 50.                      \
 ' 
   
 cuts['mu_HWJ'] = ' \
 (abs(Lepton_pdgId[0])==13)                     && bVeto                     && mjj <= 750.                     && detajj <= 4                     && mtw1 > 50.                      \
 ' 
   
 