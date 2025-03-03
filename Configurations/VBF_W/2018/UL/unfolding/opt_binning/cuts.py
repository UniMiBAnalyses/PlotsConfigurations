# cuts

supercut = 'nLepton>=1 && (Alt$(Lepton_pt[0],0) > 25.) \
            && ((Alt$(abs(CleanJet_eta[0]), 3) <2.5) || (Alt$(abs(CleanJet_eta[0]), 0) > 3.))\
            && ((Alt$(abs(CleanJet_eta[1]), 3) <2.5) || (Alt$(abs(CleanJet_eta[1]), 0) > 3.))\
            && (Alt$(CleanJet_pt[1], 0) > 30.) \
            && (Alt$(CleanJet_pt[0],0) > 40.) \
            && (mjj >= 400.) \
            && (detajj > 2.) \
            && (Alt$(Lepton_eta[0],-3) > -2.) \
            && (Alt$(Lepton_eta[0],3) < 2.) \
            && Alt$(Lepton_pt[1],0)<=15. \
            && Alt$(Lepton_isLoose[1],1)> 0.5 \
            '

cuts['SR_fid'] = 'bVeto \
                  && CleanJet_pt[1]>70. \
                  && detajj > 4 \
                  && mtw1 > 50. \
                  && {} \
                 '.format(fiducial)

# cuts['SR_only'] = 'bVeto \
#                   && CleanJet_pt[1]>70. \
#                   && detajj > 4 \
#                   && mtw1 > 50. \
#                  '

# # cuts['TOT'] = '1.'
# cuts['fiducial'] = '{}'.format(fiducial)