# 
# Expanded version of cuts.py 
# 
supercut = ' Alt$(Lepton_pt[0],0) > 25.             && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5              && Alt$(CleanJet_pt[1], 0) > 30.             && Alt$(CleanJet_pt[0],0) > 40.             && ((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))             && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) >3.))             && (mjj >= 400.) && (detajj > 2.)              && (Alt$(Lepton_eta[0],-3) > -2.) && (Alt$(Lepton_eta[0],3) < 2.)             && Alt$(Lepton_isTightElectron_mva_90p_Iso2016[1], 0) < 0.5              ' 


cuts['ele_SR'] = ' \
 (abs(Lepton_pdgId[0])==11)                   && bVeto                   && CleanJet_pt[1]>70.                   && detajj >= 4                   && mtw1 > 50.                   \
 ' 
   
 cuts['mu_SR'] = ' \
 (abs(Lepton_pdgId[0])==13)                   && bVeto                   && CleanJet_pt[1]>70.                   && detajj >= 4                   && mtw1 > 50.                   \
 ' 
   
 cuts['ele_HWJ'] = ' \
 (abs(Lepton_pdgId[0])==11)                     && bVeto                     && mjj <= 750.                     && detajj < 4                     && mtw1 > 50.                      \
 ' 
   
 cuts['ele_PUWJ'] = ' \
 (abs(Lepton_pdgId[0])==11)                     && detajj >= 5.                     && CleanJet_pt[1]<=50.                    && bVeto                     && PuppiMET_pt>70.                     && mtw1>50.                      \
 ' 
   
 cuts['mu_HWJ'] = ' \
 (abs(Lepton_pdgId[0])==13)                     && bVeto                     && mjj <= 750.                     && detajj < 4                     && mtw1 > 50.                      \
 ' 
   
 cuts['mu_PUWJ'] = ' \
 (abs(Lepton_pdgId[0])==13)                     && detajj >= 5.                     && CleanJet_pt[1]<=50.                    && bVeto                     && PuppiMET_pt>70.                     && mtw1>50.                      \
 ' 
   
 cuts['topcr'] = ' \
 bReqTight                   \
 ' 
   
 cuts['ele_FakeCR'] = ' \
 (abs(Lepton_pdgId[0])==11)                       && detajj < 5.                       && bVeto                      && mtw1<50.                       && CleanJet_pt[1]<70.                        \
 ' 
   
 cuts['mu_FakeCR'] = ' \
 (abs(Lepton_pdgId[0])==13)                       && detajj < 5.                       && bVeto                      && mtw1<50.                       && CleanJet_pt[1]<70.                        \
 ' 
   
 