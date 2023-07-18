from pprint import pprint
# # # name of samples here must match keys in samples.py 

# VBS_samples = ["ewk_WpZ", "ewk_WmZ", "ewk_ZZ", "ewk_WpWm", "ewk_WpWp", "ewk_WmWm"]
VBS_samples = ["sm"]
VBS_WV_samples = ["ewk_WpZ", "ewk_WmZ","ewk_WpWm", "ewk_WpWp", "ewk_WmWm"]
VBS_ZV_samples = ["ewk_WpZ", "ewk_WmZ", "ewk_ZZ"]
VV_WV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj"]
VV_ZV_samples = ["VV_WZll", "VV_ZZ"]

mc =["DY", "top", "VV", "VVV",  "VBF-V_dipole", "Vg", "VgS",  "ggWW","VBS_dipoleRecoil"] + wjets_all_bins + VBS_samples + VV_samples
#"VBF-V","VBS",

phasespaces = ["res_wjetcr_ele",
               "res_wjetcr_mu" ,
               "boost_wjetcr_ele" ,
               "boost_wjetcr_mu",
               "res_topcr_ele",
               "res_topcr_mu" ,
               "boost_topcr_ele" ,
               "boost_topcr_mu",
               "res_sig_ele_DNN_geq_0p5",
               "res_sig_mu_DNN_geq_0p5",
               "res_sig_ele_DNN_leq_0p5" ,
               "res_sig_mu_DNN_leq_0p5",
               "boost_sig_ele_DNN_geq_0p5" ,
               "boost_sig_mu_DNN_geq_0p5",
               "boost_sig_ele_DNN_leq_0p5" ,
               "boost_sig_mu_DNN_leq_0p5",
               ]

def getSamplesWithout(samples, samples_to_remove):
    return [m for m in samples if m not in samples_to_remove]


phase_spaces_boost = [ c for c in phasespaces if 'boost' in c]
phase_spaces_res = [ c for c in phasespaces if 'res' in c]

phase_spaces_res_ele = [ c for c in phase_spaces_res if 'ele' in c]
phase_spaces_res_mu = [ c for c in phase_spaces_res if 'mu' in c]
phase_spaces_boost_ele = [ c for c in phase_spaces_boost if 'ele' in c]
phase_spaces_boost_mu =  [ c for c in phase_spaces_boost if 'mu' in c]

phase_spaces_tot_ele = phase_spaces_res_ele + phase_spaces_boost_ele
phase_spaces_tot_mu = phase_spaces_res_mu + phase_spaces_boost_mu
phase_spaces_tot_res = phase_spaces_res_ele + phase_spaces_res_mu
phase_spaces_tot_boost = phase_spaces_boost_ele + phase_spaces_boost_mu

phase_spaces_dict = {"boost": phase_spaces_boost, "res": phase_spaces_res}
phase_spaces_tot = phase_spaces_tot_ele + phase_spaces_tot_mu

# Function to split a nuisance on different folders for different group of samples
# keeping the same nuisance name
# groups = [ (list of samples, folder), ...  ]
# def split_nuisance_samples_dir(nuisance_name, nuisance_options, variation, groups):
#     for ig, (samples_list, folder) in enumerate(groups):
#         n = {}
#         n.update(nuisance_options)
#         n["samples"] = dict((skey, ['1.','1.']) for skey in samples_list)
#         n["folderUp"] = folder +'_'+variation + 'up'
#         n["folderDown"] = folder +'_'+variation + 'do'
#         nuisances['{}_{}'.format(nuisance_name, ig)] = n

# # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# # #### Luminosity

nuisances = {}