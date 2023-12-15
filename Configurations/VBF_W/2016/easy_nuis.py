# 
# Expanded version of samples.py 
# 
nuisances['lumi_Uncorrelated'] = { 
     'name'  :   'lumi_13TeV_2016' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['lumi_CurrCalib'] = { 
     'name'  :   'lumi_13TeV_CurrCalib' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['lumi_Ghosts'] = { 
     'name'  :   'lumi_13TeV_Ghosts' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['lumi_LScale'] = { 
     'name'  :   'lumi_13TeV_LSCale' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['lumi_XYFact'] = { 
     'name'  :   'lumi_13TeV_XYFact' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['fake_syst_mu'] = { 
     'name'  :   'CMS_fake_syst_mu' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'Fake',
     },  
     'cuts'  :  [ 
            'mu_SR',
            'mu_HWJ',
            'mu_PUWJ',
            'mu_FakeCR',
     ],  
}  
   
 nuisances['fake_syst_ele'] = { 
     'name'  :   'CMS_fake_syst_ele' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'Fake',
     },  
     'cuts'  :  [ 
            'ele_SR',
            'ele_HWJ',
            'ele_PUWJ',
            'ele_FakeCR',
     ],  
}  
   
 nuisances['fake_ele'] = { 
     'name'  :   'CMS_fake_ele_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Fake',
     },  
     'cuts'  :  [ 
            'ele_SR',
            'ele_HWJ',
            'ele_PUWJ',
            'ele_FakeCR',
     ],  
}  
   
 nuisances['fake_ele_stat'] = { 
     'name'  :   'CMS_fake_ele_stat_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Fake',
     },  
     'cuts'  :  [ 
            'ele_SR',
            'ele_HWJ',
            'ele_PUWJ',
            'ele_FakeCR',
     ],  
}  
   
 nuisances['fake_mu'] = { 
     'name'  :   'CMS_fake_mu_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Fake',
     },  
     'cuts'  :  [ 
            'mu_SR',
            'mu_HWJ',
            'mu_PUWJ',
            'mu_FakeCR',
     ],  
}  
   
 nuisances['fake_mu_stat'] = { 
     'name'  :   'CMS_fake_mu_stat_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Fake',
     },  
     'cuts'  :  [ 
            'mu_SR',
            'mu_HWJ',
            'mu_PUWJ',
            'mu_FakeCR',
     ],  
}  
   
 nuisances['btag_shape_jes'] = { 
     'name'  :   'CMS_btag_jes' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['btag_shape_lf'] = { 
     'name'  :   'CMS_btag_lf' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['btag_shape_hf'] = { 
     'name'  :   'CMS_btag_hf' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['btag_shape_hfstats1'] = { 
     'name'  :   'CMS_btag_hfstats1_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['btag_shape_hfstats2'] = { 
     'name'  :   'CMS_btag_hfstats2_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['btag_shape_lfstats1'] = { 
     'name'  :   'CMS_btag_lfstats1_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['btag_shape_lfstats2'] = { 
     'name'  :   'CMS_btag_lfstats2_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['btag_shape_cferr1'] = { 
     'name'  :   'CMS_btag_cferr1' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['btag_shape_cferr2'] = { 
     'name'  :   'CMS_btag_cferr2' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['trigg'] = { 
     'name'  :   'CMS_eff_trigger_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['prefire'] = { 
     'name'  :   'CMS_eff_prefiring_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['eff_e'] = { 
     'name'  :   'CMS_eff_e_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
     'cuts'  :  [ 
            'ele_SR',
            'ele_HWJ',
            'ele_PUWJ',
            'ele_FakeCR',
     ],  
}  
   
 nuisances['eff_m'] = { 
     'name'  :   'CMS_eff_m_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
     'cuts'  :  [ 
            'mu_SR',
            'mu_HWJ',
            'mu_PUWJ',
            'mu_FakeCR',
     ],  
}  
   
 nuisances['JetPUID_sf'] = { 
     'name'  :   'CMS_jetpuid_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['JESAbsolute'] = { 
     'name'  :   'CMS_j_scale_JESAbsolute' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESAbsolute_2016'] = { 
     'name'  :   'CMS_j_scale_JESAbsolute_2016' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESBBEC1'] = { 
     'name'  :   'CMS_j_scale_JESBBEC1' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESBBEC1_2016'] = { 
     'name'  :   'CMS_j_scale_JESBBEC1_2016' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESEC2'] = { 
     'name'  :   'CMS_j_scale_JESEC2' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESEC2_2016'] = { 
     'name'  :   'CMS_j_scale_JESEC2_2016' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESFlavorQCD'] = { 
     'name'  :   'CMS_j_scale_JESFlavorQCD' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESHF'] = { 
     'name'  :   'CMS_j_scale_JESHF' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESHF_2016'] = { 
     'name'  :   'CMS_j_scale_JESHF_2016' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESRelativeBal'] = { 
     'name'  :   'CMS_j_scale_JESRelativeBal' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['JESRelativeSample_2016'] = { 
     'name'  :   'CMS_j_scale_JESRelativeSample_2016' ,
     'kind'  :   'suffix' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
            'DY_else',
            'DY_M-50',
            'Wjets_HT',
     },  
     'folderUp'    :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESup' ,
     'folderDown'  :   '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016_JESdo' ,
}  
   
 nuisances['singleTopToTTbar'] = { 
     'name'  :   'singleTopToTTbar' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'top',
     },  
}  
   
 nuisances['TopPtRew'] = { 
     'name'  :   'CMS_topPtRew' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'top',
     },  
}  
   
 nuisances['QCD_scale_Wjets_HT'] = { 
     'name'  :   'QCDscale_Wjets_HT' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Wjets_HT',
     },  
}  
   
 nuisances['QCD_scale_top'] = { 
     'name'  :   'QCDscale_top' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'top',
     },  
}  
   
 nuisances['QCD_scale_VV'] = { 
     'name'  :   'QCDscale_VV' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VV',
     },  
}  
   
 nuisances['QCD_scale_VBS'] = { 
     'name'  :   'QCDscale_VBS' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
     },  
}  
   
 nuisances['QCD_scale_ggWW'] = { 
     'name'  :   'QCDscale_ggWW' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'ggWW',
     },  
}  
   
 nuisances['QCD_scale_Higgs'] = { 
     'name'  :   'QCDscale_Higgs' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Higgs',
     },  
}  
   
 nuisances['QCD_scale_DY_M-50'] = { 
     'name'  :   'QCDscale_DY_M-50' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DY_M-50',
     },  
}  
   
 nuisances['QCD_scale_DY_else'] = { 
     'name'  :   'QCDscale_DY_else' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'DY_else',
     },  
}  
   
 nuisances['QCD_scale_VBF-Z'] = { 
     'name'  :   'QCDscale_VBF-Z' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBF-Z',
     },  
}  
   
 nuisances['QCD_scale_Vg'] = { 
     'name'  :   'QCDscale_Vg' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Vg',
     },  
}  
   
 nuisances['QCD_scale_VVV'] = { 
     'name'  :   'QCDscale_VVV' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VVV',
     },  
}  
   
 nuisances['QCD_scale_WLNuJJ_accept'] = { 
     'name'  :   'QCDscale_Wjets' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'WLNuJJ',
     },  
}  
   
 nuisances['PU'] = { 
     'name'  :   'CMS_PU_2016' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'DY_M-50',
            'Higgs',
            'VVV',
            'top',
            'ggWW',
            'DY_else',
            'Wjets_HT',
            'WLNuJJ',
            'Vg',
            'VV',
     },  
}  
   
 nuisances['UE'] = { 
     'name'  :   'UE_CUET' ,
     'type'  :   'lnN' ,
     'samples'  :  { 
            'VBS',
            'VBF-Z',
            'VV',
            'Higgs',
            'VVV',
            'ggWW',
            'DY_else',
            'WLNuJJ',
            'Vg',
            'DY_M-50',
     },  
}  
   
 nuisances['WJets_reweight'] = { 
     'name'  :   'WJets_rew' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Wjets_HT',
     },  
}  
   
 nuisances['WJets_reweight_functional'] = { 
     'name'  :   'WJets_rew_func' ,
     'kind'  :   'weight' ,
     'type'  :   'shape' ,
     'samples'  :  { 
            'Wjets_HT',
     },  
}  
   
 nuisances['Top_norm_2016'] = { 
     'name'  :   'CMS_Top_norm_2016' ,
     'type'  :   'rateParam' ,
     'samples'  :  { 
            'top',
     },  
}  
   
 nuisances['WPUJet_norm_ele_2016'] = { 
     'name'  :   'CMS_WPUJet_norm_ele_2016' ,
     'type'  :   'rateParam' ,
     'samples'  :  { 
            'Wjets_HT_PUJets',
     },  
     'cuts'  :  [ 
            'ele_SR',
            'ele_HWJ',
            'ele_PUWJ',
            'topcr',
            'ele_FakeCR',
     ],  
}  
   
 nuisances['WPUJet_norm_mu_2016'] = { 
     'name'  :   'CMS_WPUJet_norm_mu_2016' ,
     'type'  :   'rateParam' ,
     'samples'  :  { 
            'Wjets_HT_PUJets',
     },  
     'cuts'  :  [ 
            'mu_SR',
            'mu_HWJ',
            'mu_PUWJ',
            'topcr',
            'mu_FakeCR',
     ],  
}  
   
 nuisances['WhardJet_norm_ele_2016'] = { 
     'name'  :   'CMS_WhardJet_norm_ele_2016' ,
     'type'  :   'rateParam' ,
     'samples'  :  { 
            'Wjets_HT_hardJets',
     },  
     'cuts'  :  [ 
            'ele_SR',
            'ele_HWJ',
            'ele_PUWJ',
            'topcr',
            'ele_FakeCR',
     ],  
}  
   
 nuisances['WhardJet_norm_mu_2016'] = { 
     'name'  :   'CMS_WhardJet_norm_mu_2016' ,
     'type'  :   'rateParam' ,
     'samples'  :  { 
            'Wjets_HT_hardJets',
     },  
     'cuts'  :  [ 
            'mu_SR',
            'mu_HWJ',
            'mu_PUWJ',
            'topcr',
            'mu_FakeCR',
     ],  
}  
   
 nuisances['stat'] = { 
     'type'  :   'auto' ,
     'samples'  :  { 
     },  
}  
   
 