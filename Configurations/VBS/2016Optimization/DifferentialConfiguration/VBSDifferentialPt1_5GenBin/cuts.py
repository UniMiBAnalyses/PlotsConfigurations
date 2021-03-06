# cuts
cuts = {}
#Different supercut used

#supercut for test on succesive selections
supercut='\
std_vector_jet_pt[0]>30 && std_vector_jet_pt[1]>30 \
&& veto_EMTFBug \
&& abs(std_vector_jet_eta[1])<5 && abs(std_vector_jet_eta[0])<5 '


#supercut='1'#for test on raw samples

#complete supercut
# supercut='\
# abs(std_vector_jet_eta[1])<5 && abs(std_vector_jet_eta[0])<5 \
# && metPfType1 > 30 \
# && std_vector_jet_pt[0]>30 && std_vector_jet_pt[1]>30 \
# && (abs((std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
# && (abs((std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
# && veto_EMTFBug '


#&& (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) > 0 '


#signal cuts are used as preselections           

#cuts['VBS_13TeV_SS']='(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) > 0'
#cuts['VBS_13TeV_PreSelOnly']='1'


tauVeto = '\
( std_vector_tau_pt[0] < 18 || std_vector_tau_looseIso_dbeta[0] < 1. || (sqrt( pow(std_vector_tau_eta[0] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[0] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[0] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[0] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[1] < 18 || std_vector_tau_looseIso_dbeta[1] < 1. || (sqrt( pow(std_vector_tau_eta[1] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[1] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[1] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[1] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[2] < 18 || std_vector_tau_looseIso_dbeta[2] < 1. || (sqrt( pow(std_vector_tau_eta[2] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[2] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[2] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[2] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[3] < 18 || std_vector_tau_looseIso_dbeta[3] < 1. || (sqrt( pow(std_vector_tau_eta[3] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[3] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[3] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[3] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[4] < 18 || std_vector_tau_looseIso_dbeta[4] < 1. || (sqrt( pow(std_vector_tau_eta[4] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[4] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[4] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[4] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[5] < 18 || std_vector_tau_looseIso_dbeta[5] < 1. || (sqrt( pow(std_vector_tau_eta[5] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[5] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[5] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[5] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) '
            

BVeto = '\
( std_vector_jet_pt[0] < 20 || (std_vector_jet_csvv2ivf[0] < 0.8484 )  ) \
&& ( std_vector_jet_pt[1] < 20 || (std_vector_jet_csvv2ivf[1] < 0.8484 )  ) \
&& ( std_vector_jet_pt[2] < 20 || (std_vector_jet_csvv2ivf[2] < 0.8484 )  ) \
&& ( std_vector_jet_pt[3] < 20 || (std_vector_jet_csvv2ivf[3] < 0.8484 )  ) \
&& ( std_vector_jet_pt[4] < 20 || (std_vector_jet_csvv2ivf[4] < 0.8484 )  ) \
&& ( std_vector_jet_pt[5] < 20 || (std_vector_jet_csvv2ivf[5] < 0.8484 )  ) '

#csvv2ivf combined secondary vertex alghortim. Higher values means a better probability of tagging a b-jet

softMuVeto='\
( std_vector_softMuPt[0] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[0] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[0] - std_vector_lepton_phi[0])-pi)-pi, 2) )< 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[0] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[0] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[1] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[1] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[1] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[1] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[1] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[2] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[2] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[2] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[2] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[2] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[3] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[3] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[3] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[3] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[3] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[4] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[4] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[4] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[4] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[4] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[5] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[5] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[5] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[5] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[5] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) '


bJetVeto = BVeto +'&&'+ softMuVeto
bJetTag  = '(!(' + bJetVeto + '))>=1'  

zveto ='(abs(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) != 11*11 ||(mll>20 && abs(mll - 91) > 15))'

#cuts['VBS_13TeV_AllVetoes5']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto 
#cuts['VBS_13TeV_AllVetoesNoMu5']  =zveto + '&&' + tauVeto +'&&'+ BVeto 


##############################################################################################
## Comparison with table page 90 of Jasper thesis ###########################################


met = 'metPfType1 > 30'
zlep='\
(abs((std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
&&(abs((std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) '
zvetoTest ='((abs(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) != 11*11) || (abs(mll - 91) > 15))'
#cuts['NoCut']='1'
#cuts['Met']=met
#cuts['Met_Z']=met + '&&' +zlep
#cuts['Met_Z_bJet']=met + '&&' +zlep+'&&' +BVeto
#cuts['Met_Z_bJet_MuV']=met + '&&' +zlep+'&&' +BVeto+'&&'+softMuVeto
#cuts['Met_Z_bJet_MuV_TauV']=met + '&&' +zlep+'&&' +BVeto+'&&'+softMuVeto+'&&'+tauVeto
#cuts['Met_Z_bJet_MuV_TauV_Zv']=met + '&&' +zlep+'&&' +BVeto+'&&'+softMuVeto+'&&'+tauVeto+'&&'+zvetoTest
cuts['Test_Algo_5Gen_v7']=met + '&&' +zlep+'&&' +BVeto+'&&'+softMuVeto+'&&'+tauVeto+'&&'+zveto



#cuts['MuonVeto5']=met + '&&' +zlep+'&&'+softMuVeto+'&&'+zveto
#cuts['tauVeto5']=met+'&&' +zlep+'&&'+tauVeto+'&&'+zveto
#cuts['bVeto5']=met + '&&' +zlep+'&&' +BVeto+'&&'+zveto


#if all the 3 veto are used together: error Too many operator in TFormula->elements of the vetor reduced from 10 to 6.
#These Veto<name>_All are used for testing the effect on the number of events

tauVetoAll = '\
( std_vector_tau_pt[0] < 18 || std_vector_tau_looseIso_dbeta[0] < 1. || (sqrt( pow(std_vector_tau_eta[0] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[0] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[0] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[0] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[1] < 18 || std_vector_tau_looseIso_dbeta[1] < 1. || (sqrt( pow(std_vector_tau_eta[1] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[1] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[1] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[1] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[2] < 18 || std_vector_tau_looseIso_dbeta[2] < 1. || (sqrt( pow(std_vector_tau_eta[2] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[2] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[2] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[2] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[3] < 18 || std_vector_tau_looseIso_dbeta[3] < 1. || (sqrt( pow(std_vector_tau_eta[3] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[3] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[3] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[3] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[4] < 18 || std_vector_tau_looseIso_dbeta[4] < 1. || (sqrt( pow(std_vector_tau_eta[4] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[4] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[4] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[4] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[5] < 18 || std_vector_tau_looseIso_dbeta[5] < 1. || (sqrt( pow(std_vector_tau_eta[5] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[5] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[5] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[5] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[6] < 18 || std_vector_tau_looseIso_dbeta[6] < 1. || (sqrt( pow(std_vector_tau_eta[6] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[6] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[6] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[6] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[7] < 18 || std_vector_tau_looseIso_dbeta[7] < 1. || (sqrt( pow(std_vector_tau_eta[7] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[7] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[7] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[7] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[8] < 18 || std_vector_tau_looseIso_dbeta[8] < 1. || (sqrt( pow(std_vector_tau_eta[8] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[8] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[8] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[8] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[9] < 18 || std_vector_tau_looseIso_dbeta[9] < 1. || (sqrt( pow(std_vector_tau_eta[9] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[9] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[9] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[9] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) )\
'
            

BVetoAll = '\
( std_vector_jet_pt[0] < 20 || (std_vector_jet_csvv2ivf[0] < 0.8484 )  ) \
&& ( std_vector_jet_pt[1] < 20 || (std_vector_jet_csvv2ivf[1] < 0.8484 )  ) \
&& ( std_vector_jet_pt[2] < 20 || (std_vector_jet_csvv2ivf[2] < 0.8484 )  ) \
&& ( std_vector_jet_pt[3] < 20 || (std_vector_jet_csvv2ivf[3] < 0.8484 )  ) \
&& ( std_vector_jet_pt[4] < 20 || (std_vector_jet_csvv2ivf[4] < 0.8484 )  ) \
&& ( std_vector_jet_pt[5] < 20 || (std_vector_jet_csvv2ivf[5] < 0.8484 )  ) \
&& ( std_vector_jet_pt[6] < 20 || (std_vector_jet_csvv2ivf[6] < 0.8484 )  ) \
&& ( std_vector_jet_pt[7] < 20 || (std_vector_jet_csvv2ivf[7] < 0.8484 )  ) \
&& ( std_vector_jet_pt[8] < 20 || (std_vector_jet_csvv2ivf[8] < 0.8484 )  ) \
&& ( std_vector_jet_pt[9] < 20 || (std_vector_jet_csvv2ivf[9] < 0.8484 )  ) \
'
#csvv2ivf combined secondary vertex alghortim. Higher values means a better probability of tagging a b-jet

BTagAll = '\
(((std_vector_jet_pt[0]>20)*(std_vector_jet_csvv2ivf[0]>0.8484))+ \
(( std_vector_jet_pt[1]>20)*(std_vector_jet_csvv2ivf[1]>0.8484))+ \
(( std_vector_jet_pt[2]>20)*(std_vector_jet_csvv2ivf[2]>0.8484))+ \
(( std_vector_jet_pt[3]>20)*(std_vector_jet_csvv2ivf[3]>0.8484))+ \
(( std_vector_jet_pt[4]>20)*(std_vector_jet_csvv2ivf[4]>0.8484))+ \
(( std_vector_jet_pt[5]>20)*(std_vector_jet_csvv2ivf[5]>0.8484))+\
(( std_vector_jet_pt[6]>20)*(std_vector_jet_csvv2ivf[6]>0.8484))+ \
(( std_vector_jet_pt[7]>20)*(std_vector_jet_csvv2ivf[7]>0.8484))+ \
(( std_vector_jet_pt[8]>20)*(std_vector_jet_csvv2ivf[8]>0.8484))+ \
(( std_vector_jet_pt[9]>20)*(std_vector_jet_csvv2ivf[9]>0.8484)))>=1 '
BTag5='\
(((std_vector_jet_pt[0]>20)*(std_vector_jet_csvv2ivf[0]>0.8484))+ \
(( std_vector_jet_pt[1]>20)*(std_vector_jet_csvv2ivf[1]>0.8484))+ \
(( std_vector_jet_pt[2]>20)*(std_vector_jet_csvv2ivf[2]>0.8484))+ \
(( std_vector_jet_pt[3]>20)*(std_vector_jet_csvv2ivf[3]>0.8484))+ \
(( std_vector_jet_pt[4]>20)*(std_vector_jet_csvv2ivf[4]>0.8484))+ \
(( std_vector_jet_pt[5]>20)*(std_vector_jet_csvv2ivf[5]>0.8484)))>=1 '



softMuVetoAll='\
( std_vector_softMuPt[0] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[0] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[0] - std_vector_lepton_phi[0])-pi)-pi, 2) )< 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[0] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[0] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[1] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[1] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[1] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[1] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[1] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[2] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[2] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[2] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[2] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[2] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[3] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[3] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[3] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[3] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[3] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[4] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[4] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[4] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[4] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[4] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[5] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[5] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[5] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[5] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[5] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[6] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[6] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[6] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[6] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[6] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[7] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[7] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[7] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[7] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[7] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[8] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[8] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[8] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[8] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[8] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[9] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[9] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[9] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[9] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[9] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
'
#
#cuts['MuonVetoAll']=met + '&&' +zlep+'&&'+softMuVetoAll+'&&'+zveto
#cuts['MuonVeto5']=met + '&&' +zlep+'&&'+softMuVeto+'&&'+zveto
#cuts['tauVetoAll']=met+'&&' +zlep+'&&'+tauVetoAll+'&&'+zveto
#cuts['bVeto_TauV']=met + '&&' +zlep+'&&' +BVetoAll+'&&'+zveto+'&&'+tauVetoAll
#cuts['bVeto_TauV5']=met + '&&' +zlep+'&&' +BVeto+'&&'+zveto+'&&'+tauVeto
#cuts['bVetoAll']=met + '&&' +zlep+'&&' +BVetoAll+'&&'+zveto
#cuts['TauVAll']=met + '&&' +zlep+'&&'+zveto+'&&'+tauVetoAll
#cuts['bVeto5']=met + '&&' +zlep+'&&' +BVeto+'&&'+zveto
#cuts['TauV5']=met + '&&' +zlep+'&&'+zveto+'&&'+tauVeto
#cuts['All']=BVetoAll+'&&'+tauVetoAll+'&&'+softMuVetoAll
#.cuts['5']=BVeto+'&&'+tauVeto+'&&'+softMuVeto

#cuts['bJetTag']=met + '&&' +zlep+'&&' +bJetTag+'&&'+softMuVeto+'&&'+tauVeto+'&&'+zveto
#cuts['Met_Z_bJet_NoMV_TauV_Zv_mll']=met + '&&' +zlep+'&&' +BVetoAll+'&&'+tauVetoAll+'&&'+zvetoTest+'&& mll>20'




##############################################################################################


## Pay attention to ChMisId background: it contains OS leptons that can enter the signal region due to charge misrecostruction. This estimation is made using a probability
## -> OS can pass the selections if either the first or the second has a mis recostructed charge. So we don't know if they will be recostructed as 2 leptons or antileptons. 
## Fort this reason the charge splitting doesn't treat correctly this background--->it should be used for qualitative study only

#cuts['VBS_13TeV_AllVetoes_Positive']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto + '&& std_vector_lepton_flavour[0]>0 && std_vector_lepton_flavour[1]*std_vector_lepton_flavour[0]>0'
#cuts['VBS_13TeV_AllVetoes_Negative']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto + '&& std_vector_lepton_flavour[0]<0 && std_vector_lepton_flavour[1]*std_vector_lepton_flavour[0]>0'
#cuts['VBS_13TeV_AllVetoes_Mu']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto + '&& std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 11*11'
#cuts['VBS_13TeV_AllVetoes_Ele']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto + '&& std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 13*13'

#cuts['VBS_13TeV_AllVetoes_SameFlavour']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto + '&& std_vector_lepton_flavour[0] == std_vector_lepton_flavour[1]'
#cuts['VBS_13TeV_AllVetoes_OppositeFlavour']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto + '&& std_vector_lepton_flavour[0] != std_vector_lepton_flavour[1]'


# 11 = e
# 13 = mu
# 15 = tau
