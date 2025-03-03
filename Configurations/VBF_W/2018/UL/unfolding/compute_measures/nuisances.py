from pprint import pprint
import re
# # # name of samples here must match keys in samples.py 

mc_bkg =["Wjets_HT", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
mc_bkg = mc_bkg + [c for c in samples if "Out" in c]
signals = ["WLNuJJ"]

mc = signals + mc_bkg
mc_selected =["Wjets_HT", "top", "DY_M-50", "DY_else"]

regions = ["ele_SR","mu_SR","ele_HWJ","mu_HWJ","ele_PUWJ", "mu_PUWJ","topcr","ele_FakeCR","mu_FakeCR"]
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

phase_spaces_tot_ele = [ c for c in regions if 'ele' in c]
phase_spaces_tot_mu = [ c for c in regions if 'mu' in c]
phase_spaces_tot_sr = [ c for c in regions if 'SR' in c]
phase_spaces_tot_sr_top = [ c for c in regions if 'SR' in c or "topcr" in c]
wj_region = [ c for c in regions if 'HWJ' in c]

# # # # # ################################ THEORETICAL UNCERTAINTIES  #################################

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
# variations   = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-4],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-2],1)', 'Alt$(LHEScaleWeight[nLHEScaleWeight-1],1)']

# for sample in mc_bkg :
#     nuisances['QCDscale_'+sample] = {
#         'name'  : 'QCDscale_'+sample,
#         'kind'  : 'weight',
#         'type'  : 'shape',
#         'samples'  :  { sample: variations }
#     }

# # # # #Correlate all signal samples
nuisances['QCDscale_WLNuJJ'] = {
    'name'  : 'QCDscale_WLNuJJ',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples': { k: ['Alt$(LHEScaleWeight['+str(i)+'], 1.)' for i in range(0,9)] for k in signals},
}

# nuisances['PS_ISR']  = {
#                 'name'  : 'CMS_PS_ISR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {   sample : ['PSWeight[2]','PSWeight[0]'] for sample in mc if sample not in signals}
#             }

# nuisances['PS_FSR']  = {
#                 'name'  : 'CMS_PS_FSR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {     
#                     sample : ['PSWeight[3]','PSWeight[1]'] for sample in mc if sample not in signals}
#             }

nuisances['PS_dipole']  = {
                'name'  : 'CMS_PS_dipole',
                'kind'  : 'weight_envelope',
                'type'  : 'shape',
                'samples': { k: ['PSWeight['+str(i)+']' for i in range(0,4)] for k in signals},
            }

# # # ##############

# # # ###### uncomment from here 4 datacards
# nuisances['pdf_weight_Wjets_HT'] = {
#     'name'  : 'pdf_weight_Wjets_HT',
#     'kind'  : 'weight',
#     'type'  : 'shape',
#     'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["Wjets_HT"]},
# }

# nuisances['pdf_weight_top'] = {
#     'name'  : 'pdf_weight_top',
#     'kind'  : 'weight',
#     'type'  : 'shape',
#     'samples' :  { s: ['Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in ["top"] },
# }

nuisances['pdf_weight_WLNuJJ'] = {
    'name'  : 'pdf_weight_WLNuJJ',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples': { k : [ 'Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103) ] for k in signals },
}
