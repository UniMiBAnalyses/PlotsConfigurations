# cuts

## skim included in this supercut, run on central prod
supercut = '((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
             && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) > 3.))\
             && Alt$(Lepton_pt[0],0) > 27. && Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 \
             && Alt$(CleanJet_pt[1], 0) > 30. && Alt$(CleanJet_pt[0],0) > 40. \
             && (mjj >= 400.) && (detajj > 2.) && (Alt$(Lepton_eta[0],-3) > -2.) && (Alt$(Lepton_eta[0],3) < 2.)\
            '
# # supercut = '1'

# # skim NOT included in this supercut (run on private prod)
# supercut = '((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
#              && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) > 3.))\
#             '

#skim
# '"Alt$(Lepton_pt[0],0) > 27. &&
# Alt$(Lepton_pt[1],0)<=15 && Alt$(Lepton_isLoose[1],1)> 0.5 &&
#  Alt$(CleanJet_pt[1], 0) > 30. && Alt$(CleanJet_pt[0],0) > 40. &&
#  (mjj >= 400.) && (detajj > 2.) && 
# (Alt$(Lepton_eta[0],-3) > -2.) && (Alt$(Lepton_eta[0],3) < 2.)"',
  


# cuts['Z'] = '1'

#SR is ort to:
#top
#PU e Fake
#levo fake e DY + ort to WH
#fake

# 35 a ele e 30 a mu

cuts['ele_SR'] = '(abs(Lepton_pdgId[0])==11) \
                  && Lepton_pt[0]>35. \
                  && bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj >= 4 \
                  && mtw1 > 50. \
                 '

cuts['mu_SR'] = '(abs(Lepton_pdgId[0])==13) \
                  && Lepton_pt[0]>30. \
                  && bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj >= 4 \
                  && mtw1 > 50. \
                 '

#Hard & PU WJets CRs
cuts['ele_HWJ'] = '(abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0]>35. \
                    && bVeto \
                    && mjj <= 750. \
                    && detajj < 4 \
                    && mtw1 > 50. \
                    '


cuts['ele_PUWJ'] = '(abs(Lepton_pdgId[0])==11) \
                    && Lepton_pt[0]>35. \
                    && detajj >= 5. \
                    && CleanJet_pt[1]<=50.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    '

cuts['mu_HWJ'] = '(abs(Lepton_pdgId[0])==13) \
                    && Lepton_pt[0]>30. \
                    && bVeto \
                    && mjj <= 750. \
                    && detajj < 4 \
                    && mtw1 > 50. \
                    '


cuts['mu_PUWJ'] = '(abs(Lepton_pdgId[0])==13) \
                    && Lepton_pt[0]>30. \
                    && detajj >= 5. \
                    && CleanJet_pt[1]<=50.\
                    && bVeto \
                    && PuppiMET_pt>70. \
                    && mtw1>50. \
                    '
                    
# Top control region (common mu & e)
cuts['topcr']  = ' bReqTight \
                 && Lepton_pt[0]>35. \
                 '

# cuts['ele_topcr']  = 'abs(Lepton_pdgId[0])==11 && bReqTight \
                #  '

## Fake CR   
cuts['ele_FakeCR']  = '(abs(Lepton_pdgId[0])==11) \
                      && Lepton_pt[0]>35. \
                      && detajj < 5. \
                      && bVeto\
                      && mtw1<50. \
                      && CleanJet_pt[1]<70.  \
                     '
    
cuts['mu_FakeCR']  = '(abs(Lepton_pdgId[0])==13) \
                      && Lepton_pt[0]>30. \
                      && detajj < 5. \
                      && bVeto\
                      && mtw1<50. \
                      && CleanJet_pt[1]<70.  \
                     '
