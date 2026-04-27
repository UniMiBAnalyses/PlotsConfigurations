CMSSW=os.environ["CMSSW_BASE"]
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/noHIPM/unfolding/ALL/ForTraining/samples_DNN.py"
if os.path.exists(CMSSW+"/src/"+samplesFile):
  handle = open(CMSSW+"/src/"+samplesFile)
  exec(handle)
  handle.close()



fiducial = '(((abs(Alt$(DressedLepton_pdgId[0],0))==11) + (abs(Alt$(DressedLepton_pdgId[0],0))==13))>0) \
            && (Alt$(DressedLepton_isPrompt[0],0)==1) \
            && (Alt$(DressedLepton_pt[0],0)>=20.) \
            && (Alt$(CleanGenJet_pt[0],0)>=60.) \
            && (Alt$(CleanGenJet_pt[1],0)>=60.) \
            && (Alt$(mjj_gen,0)>=300.) \
            && (Alt$(detajj_gen,0)>=4.) \
            && (Alt$(abs(DressedLepton_eta[0]),999.)<2.) \
            && (Alt$(abs(CleanGenJet_eta[0]),999.)<4.7) \
            && (Alt$(abs(CleanGenJet_eta[1]),999.)<4.7) \
            && (Alt$(nCleanGenJet20,0)>=2)'
            
fiducialw = fiducial.replace("&&","*")

# samples['WLNuJJ'] = { 
#     'FilesPerJob': 1,
#     'name': nanoGetSampleFiles(mcDirectoryLatSig, 'Wm_LNuJJ_EWK')
#             + nanoGetSampleFiles(mcDirectoryLatSig, 'Wp_LNuJJ_EWK'),
#     'weight': CommonWeight,
#     'subsamples': {
#         'detajj1': '(detajj_gen < 4.) * {}'.format(fiducialw),
#         'detajj2': '(detajj_gen >= 4.) * (detajj_gen < 4.2) * {}'.format(fiducialw),
#         'detajj3': '(detajj_gen >= 4.2) * (detajj_gen < 4.4) * {}'.format(fiducialw),
#         'detajj4': '(detajj_gen >= 4.4) * (detajj_gen < 4.6) * {}'.format(fiducialw),
#         'detajj5': '(detajj_gen >= 4.6) * (detajj_gen < 4.8) * {}'.format(fiducialw),
#         'detajj6': '(detajj_gen >= 4.8) * (detajj_gen < 5.) * {}'.format(fiducialw),
#         'detajj7': '(detajj_gen >= 5.) * (detajj_gen < 5.2) * {}'.format(fiducialw),
#         'detajj8': '(detajj_gen >= 5.2) * (detajj_gen < 5.5) * {}'.format(fiducialw),
#         'detajj9': '(detajj_gen >= 5.5) * (detajj_gen < 6.) * {}'.format(fiducialw),
#         'detajj10': '(detajj_gen >= 6.) * {}'.format(fiducialw),
#         'detajjOut': '!('+fiducialw+')',
#         'dphijj1': '(dphijj_gen < 1.5) * {}'.format(fiducialw),
#         'dphijj2': '(dphijj_gen >= 1.5) * (dphijj_gen < 2.) * {}'.format(fiducialw),
#         'dphijj3': '(dphijj_gen >= 2.) * (dphijj_gen < 2.5) * {}'.format(fiducialw),
#         'dphijj4': '(dphijj_gen >= 2.5) * (dphijj_gen < 2.6) * {}'.format(fiducialw),
#         'dphijj5': '(dphijj_gen >= 2.6) * (dphijj_gen < 2.7) * {}'.format(fiducialw),
#         'dphijj6': '(dphijj_gen >= 2.7) * (dphijj_gen < 2.8) * {}'.format(fiducialw),
#         'dphijj7': '(dphijj_gen >= 2.8) * (dphijj_gen < 2.9) * {}'.format(fiducialw),
#         'dphijj8': '(dphijj_gen >= 2.9) * (dphijj_gen < 3.) * {}'.format(fiducialw),
#         'dphijj9': '(dphijj_gen >= 3.) * (dphijj_gen < 3.05) * {}'.format(fiducialw),
#         'dphijj10': '(dphijj_gen >= 3.05) * {}'.format(fiducialw),
#         'dphijjOut': '!('+fiducialw+')',
#         'jet1eta1': '(jeteta1_gen_abs < 0.9) * {}'.format(fiducialw),
#         'jet1eta2': '(jeteta1_gen_abs >= 0.9) * (jeteta1_gen_abs < 1.3) * {}'.format(fiducialw),
#         'jet1eta3': '(jeteta1_gen_abs >= 1.3) * (jeteta1_gen_abs < 1.7) * {}'.format(fiducialw),
#         'jet1eta4': '(jeteta1_gen_abs >= 1.7) * (jeteta1_gen_abs < 2.) * {}'.format(fiducialw),
#         'jet1eta5': '(jeteta1_gen_abs >= 2.) * (jeteta1_gen_abs < 2.2) * {}'.format(fiducialw),
#         'jet1eta6': '(jeteta1_gen_abs >= 2.2) * (jeteta1_gen_abs < 2.4) * {}'.format(fiducialw),
#         'jet1eta7': '(jeteta1_gen_abs >= 2.4) * (jeteta1_gen_abs < 3.0) * {}'.format(fiducialw),
#         'jet1eta8': '(jeteta1_gen_abs >= 3.0) * (jeteta1_gen_abs < 3.3) * {}'.format(fiducialw),
#         'jet1eta9': '(jeteta1_gen_abs >= 3.3) * (jeteta1_gen_abs < 3.6) * {}'.format(fiducialw),
#         'jet1eta10': '(jeteta1_gen_abs >= 3.6) * {}'.format(fiducialw),
#         'jet1etaOut': '!('+fiducialw+')',
#         'jet1pt1': '(CleanGenJet_pt[0] < 95.0) * {}'.format(fiducialw),
#         'jet1pt2': '(CleanGenJet_pt[0] >= 95.0) * (CleanGenJet_pt[0] < 110.0) * {}'.format(fiducialw),
#         'jet1pt3': '(CleanGenJet_pt[0] >= 110.0) * (CleanGenJet_pt[0] < 130.0) * {}'.format(fiducialw),
#         'jet1pt4': '(CleanGenJet_pt[0] >= 130.0) * (CleanGenJet_pt[0] < 150.0) * {}'.format(fiducialw),
#         'jet1pt5': '(CleanGenJet_pt[0] >= 150.0) * (CleanGenJet_pt[0] < 175.0) * {}'.format(fiducialw),
#         'jet1pt6': '(CleanGenJet_pt[0] >= 175.0) * (CleanGenJet_pt[0] < 225.0) * {}'.format(fiducialw),
#         'jet1pt7': '(CleanGenJet_pt[0] >= 225.0) * {}'.format(fiducialw),
#         'jet1ptOut': '!('+fiducialw+')',
#         'jet2eta1': '(jeteta2_gen_abs < 1.3) * {}'.format(fiducialw),
#         'jet2eta2': '(jeteta2_gen_abs >= 1.3) * (jeteta2_gen_abs < 1.8) * {}'.format(fiducialw),
#         'jet2eta3': '(jeteta2_gen_abs >= 1.8) * (jeteta2_gen_abs < 2.1) * {}'.format(fiducialw),
#         'jet2eta4': '(jeteta2_gen_abs >= 2.1) * (jeteta2_gen_abs < 2.3) * {}'.format(fiducialw),
#         'jet2eta5': '(jeteta2_gen_abs >= 2.3) * (jeteta2_gen_abs < 3.0) * {}'.format(fiducialw),
#         'jet2eta6': '(jeteta2_gen_abs >= 3.0) * (jeteta2_gen_abs < 3.2) * {}'.format(fiducialw),
#         'jet2eta7': '(jeteta2_gen_abs >= 3.2) * (jeteta2_gen_abs < 3.4) * {}'.format(fiducialw),
#         'jet2eta8': '(jeteta2_gen_abs >= 3.4) * (jeteta2_gen_abs < 3.6) * {}'.format(fiducialw),
#         'jet2eta9': '(jeteta2_gen_abs >= 3.6) * (jeteta2_gen_abs < 3.85) * {}'.format(fiducialw),
#         'jet2eta10': '(jeteta2_gen_abs >= 3.85) * {}'.format(fiducialw),
#         'jet2etaOut': '!('+fiducialw+')',
#         'jet2pt1': '(CleanGenJet_pt[1] < 70.0) * {}'.format(fiducialw),
#         'jet2pt2': '(CleanGenJet_pt[1] >= 70.0) * (CleanGenJet_pt[1] < 80.0) * {}'.format(fiducialw),
#         'jet2pt3': '(CleanGenJet_pt[1] >= 80.0) * (CleanGenJet_pt[1] < 90.0) * {}'.format(fiducialw),
#         'jet2pt4': '(CleanGenJet_pt[1] >= 90.0) * (CleanGenJet_pt[1] < 100.0) * {}'.format(fiducialw),
#         'jet2pt5': '(CleanGenJet_pt[1] >= 100.0) * (CleanGenJet_pt[1] < 115.0) * {}'.format(fiducialw),
#         'jet2pt6': '(CleanGenJet_pt[1] >= 115.0) * (CleanGenJet_pt[1] < 140.0) * {}'.format(fiducialw),
#         'jet2pt7': '(CleanGenJet_pt[1] >= 140.0) * {}'.format(fiducialw),
#         'jet2ptOut': '!('+fiducialw+')',
#         'lepeta1': '(lepeta_gen_abs < 0.15) * {}'.format(fiducialw),
#         'lepeta2': '(lepeta_gen_abs >= 0.15) * (lepeta_gen_abs < 0.3) * {}'.format(fiducialw),
#         'lepeta3': '(lepeta_gen_abs >= 0.3) * (lepeta_gen_abs < 0.5) * {}'.format(fiducialw),
#         'lepeta4': '(lepeta_gen_abs >= 0.5) * (lepeta_gen_abs < 0.65) * {}'.format(fiducialw),
#         'lepeta5': '(lepeta_gen_abs >= 0.65) * (lepeta_gen_abs < 0.8) * {}'.format(fiducialw),
#         'lepeta6': '(lepeta_gen_abs >= 0.8) * (lepeta_gen_abs < 1.) * {}'.format(fiducialw),
#         'lepeta7': '(lepeta_gen_abs >= 1.) * (lepeta_gen_abs < 1.2) * {}'.format(fiducialw),
#         'lepeta8': '(lepeta_gen_abs >= 1.2) * (lepeta_gen_abs < 1.4) * {}'.format(fiducialw),
#         'lepeta9': '(lepeta_gen_abs >= 1.4) * (lepeta_gen_abs < 1.7) * {}'.format(fiducialw),
#         'lepeta10': '(lepeta_gen_abs >= 1.7) * {}'.format(fiducialw),
#         'lepetaOut': '!('+fiducialw+')',
#         'leppt1': '(DressedLepton_pt[0] < 30.0) * {}'.format(fiducialw),
#         'leppt2': '(DressedLepton_pt[0] >= 30.0) * (DressedLepton_pt[0] < 35.0) * {}'.format(fiducialw),
#         'leppt3': '(DressedLepton_pt[0] >= 35.0) * (DressedLepton_pt[0] < 40.0) * {}'.format(fiducialw),
#         'leppt4': '(DressedLepton_pt[0] >= 40.0) * (DressedLepton_pt[0] < 50.0) * {}'.format(fiducialw),
#         'leppt5': '(DressedLepton_pt[0] >= 50.0) * (DressedLepton_pt[0] < 60.0) * {}'.format(fiducialw),
#         'leppt6': '(DressedLepton_pt[0] >= 60.0) * (DressedLepton_pt[0] < 65.0) * {}'.format(fiducialw),
#         'leppt7': '(DressedLepton_pt[0] >= 65.0) * (DressedLepton_pt[0] < 80.0) * {}'.format(fiducialw),
#         'leppt8': '(DressedLepton_pt[0] >= 80.0) * (DressedLepton_pt[0] < 100.0) * {}'.format(fiducialw),
#         'leppt9': '(DressedLepton_pt[0] >= 100.0) * (DressedLepton_pt[0] < 150.0) * {}'.format(fiducialw),
#         'leppt10': '(DressedLepton_pt[0] >= 150.0) * {}'.format(fiducialw),
#         'lepptOut': '!('+fiducialw+')',
#         'mjj1': '(mjj_gen < 850.0) * {}'.format(fiducialw),
#         'mjj2': '(mjj_gen >= 850.0) * (mjj_gen < 1000.0) * {}'.format(fiducialw),
#         'mjj3': '(mjj_gen >= 1000.0) * (mjj_gen < 1200.0) * {}'.format(fiducialw),
#         'mjj4': '(mjj_gen >= 1200.0) * (mjj_gen < 1400.0) * {}'.format(fiducialw),
#         'mjj5': '(mjj_gen >= 1400.0) * (mjj_gen < 1600.0) * {}'.format(fiducialw),
#         'mjj6': '(mjj_gen >= 1600.0) * (mjj_gen < 2000.0) * {}'.format(fiducialw),
#         'mjj7': '(mjj_gen >= 2000.0) * (mjj_gen < 2500.0) * {}'.format(fiducialw),
#         'mjj8': '(mjj_gen >= 2500.0) * {}'.format(fiducialw),
#         'mjjOut': '!('+fiducialw+')',
#         'nJet1': '(nCleanGenJet < 2.5) * {}'.format(fiducialw),
#         'nJet2': '(nCleanGenJet >= 2.5) * (nCleanGenJet < 3.5) * {}'.format(fiducialw),
#         'nJet3': '(nCleanGenJet >= 3.5) * {}'.format(fiducialw),
#         'nJetOut': '!('+fiducialw+')',
#         'ptW1': '(ptW_gen < 30.0) * {}'.format(fiducialw),
#         'ptW2': '(ptW_gen >= 30.0) * (ptW_gen < 45.0) * {}'.format(fiducialw),
#         'ptW3': '(ptW_gen >= 45.0) * (ptW_gen < 65.0) * {}'.format(fiducialw),
#         'ptW4': '(ptW_gen >= 65.0) * (ptW_gen < 90.0) * {}'.format(fiducialw),
#         'ptW5': '(ptW_gen >= 90.0) * (ptW_gen < 120.0) * {}'.format(fiducialw),
#         'ptW6': '(ptW_gen >= 120.0) * (ptW_gen < 180.0) * {}'.format(fiducialw),
#         'ptW7': '(ptW_gen >= 180.0) * {}'.format(fiducialw),
#         'ptWOut': '!('+fiducialw+')',
#         'ptjj1': '(ptjj_gen < 30.0) * {}'.format(fiducialw),
#         'ptjj2': '(ptjj_gen >= 30.0) * (ptjj_gen < 45.0) * {}'.format(fiducialw),
#         'ptjj3': '(ptjj_gen >= 45.0) * (ptjj_gen < 60.0) * {}'.format(fiducialw),
#         'ptjj4': '(ptjj_gen >= 60.0) * (ptjj_gen < 75.0) * {}'.format(fiducialw),
#         'ptjj5': '(ptjj_gen >= 75.0) * (ptjj_gen < 100.0) * {}'.format(fiducialw),
#         'ptjj6': '(ptjj_gen >= 100.0) * (ptjj_gen < 130.0) * {}'.format(fiducialw),
#         'ptjj7': '(ptjj_gen >= 130.0) * (ptjj_gen < 180.0) * {}'.format(fiducialw),
#         'ptjj8': '(ptjj_gen >= 180.0) * {}'.format(fiducialw),
#         'ptjjOut': '!('+fiducialw+')',
#     },
# }


samples['WLNuJJ'] = { 
    'FilesPerJob': 1,
    'name': nanoGetSampleFiles(mcDirectoryLatSig, 'Wm_LNuJJ_EWK')
            + nanoGetSampleFiles(mcDirectoryLatSig, 'Wp_LNuJJ_EWK'),
    'weight': CommonWeight
}