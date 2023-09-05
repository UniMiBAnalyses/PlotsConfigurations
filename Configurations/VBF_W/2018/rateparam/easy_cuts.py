# 
# Expanded version of cuts.py 
# 
supercut = ' ((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))             && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) > 3.))             ' 


cuts['ele_SR'] = ' \
 (abs(Lepton_pdgId[0])==11)                   && Lepton_pt[0] > 35.                   && bVeto                   && CleanJet_pt[1]>70.                   && detajj > 4                   && mtw1 > 50.                   \
 ' 
   
 cuts['mu_SR'] = ' \
 (abs(Lepton_pdgId[0])==13)                  && bVeto                   && CleanJet_pt[1]>70.                   && detajj > 4                   && mtw1 > 50.                   \
 ' 
   
 cuts['ele_HWJ'] = ' \
 (abs(Lepton_pdgId[0])==11)                     && Lepton_pt[0] > 35.                     && bVeto                     && mjj <= 750.                     && detajj <= 4                     && mtw1 > 50.                      \
 ' 
   
 cuts['ele_HWJ-SR'] = ' \
 (abs(Lepton_pdgId[0])==11)                     && Lepton_pt[0] > 35.                     && bVeto                     && mjj <= 750.                     && detajj <= 4                     && mtw1 > 50.                     && detajj > 3                     && CleanJet_pt[1]>70.                      \
 ' 
   
 cuts['ele_PUWJ'] = ' \
 (abs(Lepton_pdgId[0])==11)                     && Lepton_pt[0] > 35.                     && detajj > 5.                     && CleanJet_pt[1]<=70.                    && bVeto                     && PuppiMET_pt>70.                     && mtw1>50.                      \
 ' 
   
 cuts['mu_HWJ'] = ' \
 (abs(Lepton_pdgId[0])==13)                     && bVeto                     && mjj <= 750.                     && detajj <= 4                     && mtw1 > 50.                      \
 ' 
   
 cuts['mu_HWJ-SR'] = ' \
 (abs(Lepton_pdgId[0])==13)                     && bVeto                     && mjj <= 750.                     && detajj <= 4                     && mtw1 > 50.                     && detajj > 3                     && CleanJet_pt[1]>70.                      \
 ' 
   
 cuts['mu_PUWJ'] = ' \
 (abs(Lepton_pdgId[0])==13)                     && detajj > 5.                     && CleanJet_pt[1]<=70.                    && bVeto                     && PuppiMET_pt>70.                     && mtw1>50.                      \
 ' 
   
 cuts['topcr'] = ' \
 ((zeroJet && !bVeto) || bReqTight)                      \
 ' 
   
 cuts['ele_FakeCR'] = ' \
 (abs(Lepton_pdgId[0])==11)                       && Lepton_pt[0] > 35.                       && detajj <= 5.                       && bVeto                      && mtw1<=50.                       && CleanJet_pt[1]<=70.                        \
 ' 
   
 cuts['mu_FakeCR'] = ' \
 (abs(Lepton_pdgId[0])==13)                       && detajj <= 5.                       && bVeto                      && mtw1<=50.                       && CleanJet_pt[1]<=70.                        \
 ' 
   
 