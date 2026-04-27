from pprint import pprint
import re
# # # name of samples here must match keys in samples.py 

mc_bkg =["Wjets_HT", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
mc_bkg = mc_bkg + [c for c in samples if "Out" in c]
signals = [c for c in samples if "WLNuJJ" in c]

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


# # # # #Correlate all signal samples
for s in signals:
    nuisances['QCDscale_{}'.format(s)] = {
        'name'  : 'QCDscale_{}'.format(s),
        # 'kind'  : 'weight_envelope',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples': { s: ['Alt$(LHEScaleWeight['+str(i)+'], 1.)' for i in range(0,9)]},
    }


    nuisances['PS_dipole_{}'.format(s)]  = {
                    'name'  : 'CMS_PS_dipole_{}'.format(s),
                    # 'kind'  : 'weight_envelope',
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples': { s: ['PSWeight['+str(i)+']' for i in range(0,4)]},
                }

    # # # ##############

    nuisances['pdf_weight_{}'.format(s)] = {
        'name'  : 'pdf_weight_{}'.format(s),
        # 'kind'  : 'weight_envelope',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples': { s : [ 'Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103) ] },
    }
