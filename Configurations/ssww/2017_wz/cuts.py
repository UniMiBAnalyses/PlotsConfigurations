# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

# supercut='\
# nLepton>1 && nCleanJet > 1 &&\
# Alt$(Lepton_pt[0],0.)>30 && Alt$(Lepton_pt[1],0.)>30 && Alt$(Lepton_pt[2],0.)<10 && mjj >500 && detajj > 2.5\
# && abs(Alt$(CleanJet_eta[1],-9999.))<5 && abs(Alt$(CleanJet_eta[0],-9999.))<5\
# && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5 && Alt$(CleanJet_pt[0],-9999.) >30 && Alt$(CleanJet_pt[1],-9999.) >30'

supercut='\
mjj > 150 && EleWPTight'
'''
## Signal regions
cuts['lowmjj'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : ' jetpt30 && leppt30 && mjj < 500 && bVeto && tauVeto_ww',
    }
}
cuts['top'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : ' (!bVeto) && tauVeto_ww && jetpt30 && leppt30 && mjj > 500',
    }
}
cuts['ssww'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'tauVeto_ww && bVeto && jetpt30 && leppt30 && mjj > 500',
    }
}
'''

cuts['wz_pt30_twoJetOrMore'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt30_wz && twoJetOrMore&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['wz_inc'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt25_wz',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}

cuts['wz_twoJetOrMore'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt25_wz && twoJetOrMore&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['wz_zeroJet'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt25_wz && zeroJet && mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['wz_oneJet'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt25_wz && oneJet&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['eee'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'twoJetOrMore && bVeto && leppt25_wz && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==11*11*11&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mee'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'twoJetOrMore && bVeto && leppt25_wz && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*11*11&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mme'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'twoJetOrMore && bVeto && leppt25_wz && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*13*11&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mmm'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'twoJetOrMore && bVeto && leppt25_wz && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*13*13&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}

cuts['wz_pt30_twoJetOrMore_jeteta_exclude'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt30_wz && twoJetOrMore && jeteta_exclude&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['wz_twoJetOrMore_jeteta_exclude'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt25_wz && twoJetOrMore && jeteta_exclude&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['wz_zeroJet_jeteta_exclude'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt25_wz && zeroJet && jeteta_exclude&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['wz_oneJet_jeteta_exclude'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'bVeto && leppt25_wz && oneJet && jeteta_exclude&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['eee_jeteta_exclude'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'twoJetOrMore && bVeto && leppt25_wz && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==11*11*11 && jeteta_exclude&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mee_jeteta_exclude'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'twoJetOrMore && bVeto && leppt25_wz && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*11*11 && jeteta_exclude&& mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mme_jeteta_exclude'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'twoJetOrMore && bVeto && leppt25_wz && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*13*11 && jeteta_exclude',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
cuts['mmm_jeteta_exclude'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'region' : 'twoJetOrMore && bVeto && leppt25_wz && abs(Alt$(Lepton_pdgId[0],0)*Alt$(Lepton_pdgId[1],0)*Alt$(Lepton_pdgId[2],0))==13*13*13 && jeteta_exclude',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
'''
cuts['zz'] = {
    'expr': 'zz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'jetpt50_leppt0' : 'jetpt50 && leppt0',
        'jetpt30_leppt0' : 'jetpt30 && leppt0',
        'jetpt30_leppt1' : 'jetpt30 && leppt30',
    }
}
'''
