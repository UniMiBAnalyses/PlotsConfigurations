
##############################################
# now variables to plot
# Include also variables to be plotted


var = [
    'pt1',
    'eta1',
    'phi1',
    'puppimet_phi',
    'mtw1',
    'puppimet',
    'ptW',
    'jetpt1',
    'jetpt2',
    'jeteta1',
    'jeteta1',
    'mjj',
    'detajj',
    'R',
    'Zl1',
    'QGL1',
    'QGL2',
    # 'genWeight',
    # 'Xsec',
    # 'baseW',
    # 'singleW',
    # 'puWeight',
    # 'SingleLepton_trigEff_corrected',
    # 'Lepton_RecoSF',
    # 'Lepton_tightElectron_mvaFall17V1Iso_WP90_IdIsoSF',
    # 'Lepton_tightMuon_cut_Tight_HWWW_IdIsoSF',
    # 'btagSF',
    # 'PUJetIdSF',
    # 'METFilter_MC',
    # 'Lepton_genmatched',
    # 'Lepton_isTightElectron_mvaFall17V1Iso_WP90',
    # 'Lepton_isTightMuon_cut_Tight_HWWW',
    # 'Wjets_photon_filter',
    # 'LepWPCut_1l',
    # 'LepWPWeight_1l',
]


all_var = { v:v for v in var }

## need expressions for this!
all_var['pt1'] = 'Lepton_pt[0]'
all_var['eta1'] = 'Lepton_eta[0]'
all_var['phi1'] = 'Lepton_phi[0]'
all_var['puppimet_phi'] =  'PuppiMET_phi'
all_var['puppimet'] = 'PuppiMET_pt'
all_var['jetpt1'] = 'CleanJet_pt[0]'
all_var['jetpt2'] = 'CleanJet_pt[1]'
all_var['jeteta1'] = 'CleanJet_eta[0]'
all_var['jeteta2'] = 'CleanJet_eta[1]'
all_var['R'] = 'R_AN'
all_var['QGL1'] = 'Jet_qgl[0]'
all_var['QGL2'] = 'Jet_qgl[1]'

# all_var['SingleLepton_trigEff_corrected'] = 'SingleLepton_trigEff_corrected[0]'
# all_var['Lepton_RecoSF'] = 'Lepton_RecoSF[0]'
# all_var['Lepton_tightElectron_mvaFall17V1Iso_WP90_IdIsoSF'] = 'Lepton_tightElectron_mvaFall17V1Iso_WP90_IdIsoSF[0]'
# all_var['Lepton_tightMuon_cut_Tight_HWWW_IdIsoSF'] = 'Lepton_tightMuon_cut_Tight_HWWW_IdIsoSF[0]'
# all_var['Lepton_genmatched'] = 'Lepton_genmatched[0]'
# all_var['Lepton_isTightElectron_mvaFall17V1Iso_WP90'] = 'Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]'
# all_var['Lepton_isTightMuon_cut_Tight_HWWW'] = 'Lepton_isTightMuon_cut_Tight_HWWW[0]'



variables['dnn_inputs_all'] = {
    'tree': all_var,
    'cuts' : ['ele_SR', 'mu_SR', 'ele_HWJ', 'mu_HWJ', 'ele_FakeCR', 'mu_FakeCR']
}

# variables['dnn_inputs_all'] = {
#     'tree': all_var,
#     'cuts' : ['SR2', 'SR4', 'SRAll', 'HWJ2', 'HWJ4', 'HWJAll']
# }

