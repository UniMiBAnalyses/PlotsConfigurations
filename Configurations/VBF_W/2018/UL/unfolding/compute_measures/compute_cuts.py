supercut = '1'
cuts['TOT'] = '1.'

# detajj cuts
cuts['detajj_bin1'] = '(detajj_gen < 4.0) && {}'.format(fiducial)
cuts['detajj_bin2'] = '(detajj_gen >= 4.0) && (detajj_gen < 4.2) && {}'.format(fiducial)
cuts['detajj_bin3'] = '(detajj_gen >= 4.2) && (detajj_gen < 4.4) && {}'.format(fiducial)
cuts['detajj_bin4'] = '(detajj_gen >= 4.4) && (detajj_gen < 4.6) && {}'.format(fiducial)
cuts['detajj_bin5'] = '(detajj_gen >= 4.6) && (detajj_gen < 4.8) && {}'.format(fiducial)
cuts['detajj_bin6'] = '(detajj_gen >= 4.8) && (detajj_gen < 5.0) && {}'.format(fiducial)
cuts['detajj_bin7'] = '(detajj_gen >= 5.0) && (detajj_gen < 5.2) && {}'.format(fiducial)
cuts['detajj_bin8'] = '(detajj_gen >= 5.2) && (detajj_gen < 5.5) && {}'.format(fiducial)
cuts['detajj_bin9'] = '(detajj_gen >= 5.5) && (detajj_gen < 6.0) && {}'.format(fiducial)
cuts['detajj_bin10'] = '(detajj_gen >= 6.0) && {}'.format(fiducial)

# dphijj cuts
cuts['dphijj_bin1'] = '(dphijj_gen < 1.5) && {}'.format(fiducial)
cuts['dphijj_bin2'] = '(dphijj_gen >= 1.5) && (dphijj_gen < 2.0) && {}'.format(fiducial)
cuts['dphijj_bin3'] = '(dphijj_gen >= 2.0) && (dphijj_gen < 2.5) && {}'.format(fiducial)
cuts['dphijj_bin4'] = '(dphijj_gen >= 2.5) && (dphijj_gen < 2.6) && {}'.format(fiducial)
cuts['dphijj_bin5'] = '(dphijj_gen >= 2.6) && (dphijj_gen < 2.7) && {}'.format(fiducial)
cuts['dphijj_bin6'] = '(dphijj_gen >= 2.7) && (dphijj_gen < 2.8) && {}'.format(fiducial)
cuts['dphijj_bin7'] = '(dphijj_gen >= 2.8) && (dphijj_gen < 2.9) && {}'.format(fiducial)
cuts['dphijj_bin8'] = '(dphijj_gen >= 2.9) && (dphijj_gen < 3.0) && {}'.format(fiducial)
cuts['dphijj_bin9'] = '(dphijj_gen >= 3.0) && (dphijj_gen < 3.05) && {}'.format(fiducial)
cuts['dphijj_bin10'] = '(dphijj_gen >= 3.05) && {}'.format(fiducial)

# mjj cuts
cuts['mjj_bin1'] = '(mjj_gen < 850.0) && {}'.format(fiducial)
cuts['mjj_bin2'] = '(mjj_gen >= 850.0) && (mjj_gen < 1000.0) && {}'.format(fiducial)
cuts['mjj_bin3'] = '(mjj_gen >= 1000.0) && (mjj_gen < 1200.0) && {}'.format(fiducial)
cuts['mjj_bin4'] = '(mjj_gen >= 1200.0) && (mjj_gen < 1400.0) && {}'.format(fiducial)
cuts['mjj_bin5'] = '(mjj_gen >= 1400.0) && (mjj_gen < 1600.0) && {}'.format(fiducial)
cuts['mjj_bin6'] = '(mjj_gen >= 1600.0) && (mjj_gen < 2000.0) && {}'.format(fiducial)
cuts['mjj_bin7'] = '(mjj_gen >= 2000.0) && (mjj_gen < 2500.0) && {}'.format(fiducial)
cuts['mjj_bin8'] = '(mjj_gen >= 2500.0) && {}'.format(fiducial)

# nJet cuts
cuts['nJet_bin1'] = '(nCleanGenJet < 2.5) && {}'.format(fiducial)
cuts['nJet_bin2'] = '(nCleanGenJet >= 2.5) && (nCleanGenJet < 3.5) && {}'.format(fiducial)
cuts['nJet_bin3'] = '(nCleanGenJet >= 3.5) && {}'.format(fiducial)

# ptW cuts
cuts['ptW_bin1'] = '(ptW_gen < 30.0) && {}'.format(fiducial)
cuts['ptW_bin2'] = '(ptW_gen >= 30.0) && (ptW_gen < 45.0) && {}'.format(fiducial)
cuts['ptW_bin3'] = '(ptW_gen >= 45.0) && (ptW_gen < 65.0) && {}'.format(fiducial)
cuts['ptW_bin4'] = '(ptW_gen >= 65.0) && (ptW_gen < 90.0) && {}'.format(fiducial)
cuts['ptW_bin5'] = '(ptW_gen >= 90.0) && (ptW_gen < 120.0) && {}'.format(fiducial)
cuts['ptW_bin6'] = '(ptW_gen >= 120.0) && (ptW_gen < 180.0) && {}'.format(fiducial)
cuts['ptW_bin7'] = '(ptW_gen >= 180.0) && {}'.format(fiducial)

# ptjj cuts
cuts['ptjj_bin1'] = '(ptjj_gen < 30.0) && {}'.format(fiducial)
cuts['ptjj_bin2'] = '(ptjj_gen >= 30.0) && (ptjj_gen < 45.0) && {}'.format(fiducial)
cuts['ptjj_bin3'] = '(ptjj_gen >= 45.0) && (ptjj_gen < 60.0) && {}'.format(fiducial)
cuts['ptjj_bin4'] = '(ptjj_gen >= 60.0) && (ptjj_gen < 75.0) && {}'.format(fiducial)
cuts['ptjj_bin5'] = '(ptjj_gen >= 75.0) && (ptjj_gen < 100.0) && {}'.format(fiducial)
cuts['ptjj_bin6'] = '(ptjj_gen >= 100.0) && (ptjj_gen < 130.0) && {}'.format(fiducial)
cuts['ptjj_bin7'] = '(ptjj_gen >= 130.0) && (ptjj_gen < 180.0) && {}'.format(fiducial)
cuts['ptjj_bin8'] = '(ptjj_gen >= 180.0) && {}'.format(fiducial)

# jet1eta cuts
cuts['jet1eta_bin1'] = '(jeteta1_gen_abs < 0.9) && {}'.format(fiducial)
cuts['jet1eta_bin2'] = '(jeteta1_gen_abs >= 0.9) && (jeteta1_gen_abs < 1.3) && {}'.format(fiducial)
cuts['jet1eta_bin3'] = '(jeteta1_gen_abs >= 1.3) && (jeteta1_gen_abs < 1.7) && {}'.format(fiducial)
cuts['jet1eta_bin4'] = '(jeteta1_gen_abs >= 1.7) && (jeteta1_gen_abs < 2.0) && {}'.format(fiducial)
cuts['jet1eta_bin5'] = '(jeteta1_gen_abs >= 2.0) && (jeteta1_gen_abs < 2.2) && {}'.format(fiducial)
cuts['jet1eta_bin6'] = '(jeteta1_gen_abs >= 2.2) && (jeteta1_gen_abs < 2.4) && {}'.format(fiducial)
cuts['jet1eta_bin7'] = '(jeteta1_gen_abs >= 2.4) && (jeteta1_gen_abs < 3.0) && {}'.format(fiducial)
cuts['jet1eta_bin8'] = '(jeteta1_gen_abs >= 3.0) && (jeteta1_gen_abs < 3.3) && {}'.format(fiducial)
cuts['jet1eta_bin9'] = '(jeteta1_gen_abs >= 3.3) && (jeteta1_gen_abs < 3.6) && {}'.format(fiducial)
cuts['jet1eta_bin10'] = '(jeteta1_gen_abs >= 3.6) && {}'.format(fiducial)

# jet2eta cuts
cuts['jet2eta_bin1'] = '(jeteta2_gen_abs < 1.3) && {}'.format(fiducial)
cuts['jet2eta_bin2'] = '(jeteta2_gen_abs >= 1.3) && (jeteta2_gen_abs < 1.8) && {}'.format(fiducial)
cuts['jet2eta_bin3'] = '(jeteta2_gen_abs >= 1.8) && (jeteta2_gen_abs < 2.1) && {}'.format(fiducial)
cuts['jet2eta_bin4'] = '(jeteta2_gen_abs >= 2.1) && (jeteta2_gen_abs < 2.3) && {}'.format(fiducial)
cuts['jet2eta_bin5'] = '(jeteta2_gen_abs >= 2.3) && (jeteta2_gen_abs < 3.0) && {}'.format(fiducial)
cuts['jet2eta_bin6'] = '(jeteta2_gen_abs >= 3.0) && (jeteta2_gen_abs < 3.2) && {}'.format(fiducial)
cuts['jet2eta_bin7'] = '(jeteta2_gen_abs >= 3.2) && (jeteta2_gen_abs < 3.4) && {}'.format(fiducial)
cuts['jet2eta_bin8'] = '(jeteta2_gen_abs >= 3.4) && (jeteta2_gen_abs < 3.6) && {}'.format(fiducial)
cuts['jet2eta_bin9'] = '(jeteta2_gen_abs >= 3.6) && (jeteta2_gen_abs < 3.85) && {}'.format(fiducial)
cuts['jet2eta_bin10'] = '(jeteta2_gen_abs >= 3.85) && {}'.format(fiducial)

# jet1pt cuts
cuts['jet1pt_bin1'] = '(CleanGenJet_pt[0] < 95.0) && {}'.format(fiducial)
cuts['jet1pt_bin2'] = '(CleanGenJet_pt[0] >= 95.0) && (CleanGenJet_pt[0] < 110.0) && {}'.format(fiducial)
cuts['jet1pt_bin3'] = '(CleanGenJet_pt[0] >= 110.0) && (CleanGenJet_pt[0] < 130.0) && {}'.format(fiducial)
cuts['jet1pt_bin4'] = '(CleanGenJet_pt[0] >= 130.0) && (CleanGenJet_pt[0] < 150.0) && {}'.format(fiducial)
cuts['jet1pt_bin5'] = '(CleanGenJet_pt[0] >= 150.0) && (CleanGenJet_pt[0] < 175.0) && {}'.format(fiducial)
cuts['jet1pt_bin6'] = '(CleanGenJet_pt[0] >= 175.0) && (CleanGenJet_pt[0] < 225.0) && {}'.format(fiducial)
cuts['jet1pt_bin7'] = '(CleanGenJet_pt[0] >= 225.0) && {}'.format(fiducial)

# jet2pt cuts
cuts['jet2pt_bin1'] = '(CleanGenJet_pt[1] < 70.0) && {}'.format(fiducial)
cuts['jet2pt_bin2'] = '(CleanGenJet_pt[1] >= 70.0) && (CleanGenJet_pt[1] < 80.0) && {}'.format(fiducial)
cuts['jet2pt_bin3'] = '(CleanGenJet_pt[1] >= 80.0) && (CleanGenJet_pt[1] < 90.0) && {}'.format(fiducial)
cuts['jet2pt_bin4'] = '(CleanGenJet_pt[1] >= 90.0) && (CleanGenJet_pt[1] < 100.0) && {}'.format(fiducial)
cuts['jet2pt_bin5'] = '(CleanGenJet_pt[1] >= 100.0) && (CleanGenJet_pt[1] < 115.0) && {}'.format(fiducial)
cuts['jet2pt_bin6'] = '(CleanGenJet_pt[1] >= 115.0) && (CleanGenJet_pt[1] < 140.0) && {}'.format(fiducial)
cuts['jet2pt_bin7'] = '(CleanGenJet_pt[1] >= 140.0) && {}'.format(fiducial)

# lepeta cuts
cuts['lepeta_bin1'] = '(lepeta_gen_abs < 0.15) && {}'.format(fiducial)
cuts['lepeta_bin2'] = '(lepeta_gen_abs >= 0.15) && (lepeta_gen_abs < 0.3) && {}'.format(fiducial)
cuts['lepeta_bin3'] = '(lepeta_gen_abs >= 0.3) && (lepeta_gen_abs < 0.5) && {}'.format(fiducial)
cuts['lepeta_bin4'] = '(lepeta_gen_abs >= 0.5) && (lepeta_gen_abs < 0.65) && {}'.format(fiducial)
cuts['lepeta_bin5'] = '(lepeta_gen_abs >= 0.65) && (lepeta_gen_abs < 0.8) && {}'.format(fiducial)
cuts['lepeta_bin6'] = '(lepeta_gen_abs >= 0.8) && (lepeta_gen_abs < 1.0) && {}'.format(fiducial)
cuts['lepeta_bin7'] = '(lepeta_gen_abs >= 1.0) && (lepeta_gen_abs < 1.2) && {}'.format(fiducial)
cuts['lepeta_bin8'] = '(lepeta_gen_abs >= 1.2) && (lepeta_gen_abs < 1.4) && {}'.format(fiducial)
cuts['lepeta_bin9'] = '(lepeta_gen_abs >= 1.4) && (lepeta_gen_abs < 1.7) && {}'.format(fiducial)
cuts['lepeta_bin10'] = '(lepeta_gen_abs >= 1.7) && {}'.format(fiducial)

# leppt cuts
cuts['leppt_bin1'] = '(DressedLepton_pt[0] < 30.0) && {}'.format(fiducial)
cuts['leppt_bin2'] = '(DressedLepton_pt[0] >= 30.0) && (DressedLepton_pt[0] < 35.0) && {}'.format(fiducial)
cuts['leppt_bin3'] = '(DressedLepton_pt[0] >= 35.0) && (DressedLepton_pt[0] < 40.0) && {}'.format(fiducial)
cuts['leppt_bin4'] = '(DressedLepton_pt[0] >= 40.0) && (DressedLepton_pt[0] < 50.0) && {}'.format(fiducial)
cuts['leppt_bin5'] = '(DressedLepton_pt[0] >= 50.0) && (DressedLepton_pt[0] < 60.0) && {}'.format(fiducial)
cuts['leppt_bin6'] = '(DressedLepton_pt[0] >= 60.0) && (DressedLepton_pt[0] < 65.0) && {}'.format(fiducial)
cuts['leppt_bin7'] = '(DressedLepton_pt[0] >= 65.0) && (DressedLepton_pt[0] < 80.0) && {}'.format(fiducial)
cuts['leppt_bin8'] = '(DressedLepton_pt[0] >= 80.0) && (DressedLepton_pt[0] < 100.0) && {}'.format(fiducial)
cuts['leppt_bin9'] = '(DressedLepton_pt[0] >= 100.0) && (DressedLepton_pt[0] < 150.0) && {}'.format(fiducial)
cuts['leppt_bin10'] = '(DressedLepton_pt[0] >= 150.0) && {}'.format(fiducial)

# Out of fiducial region
cuts['detajj_out'] = '!({})'.format(fiducial)
cuts['dphijj_out'] = '!({})'.format(fiducial)
cuts['mjj_out'] = '!({})'.format(fiducial)
cuts['nJet_out'] = '!({})'.format(fiducial)
cuts['ptW_out'] = '!({})'.format(fiducial)
cuts['ptjj_out'] = '!({})'.format(fiducial)
cuts['jet1eta_out'] = '!({})'.format(fiducial)
cuts['jet2eta_out'] = '!({})'.format(fiducial)
cuts['jet1pt_out'] = '!({})'.format(fiducial)
cuts['jet2pt_out'] = '!({})'.format(fiducial)
cuts['lepeta_out'] = '!({})'.format(fiducial)
cuts['leppt_out'] = '!({})'.format(fiducial)