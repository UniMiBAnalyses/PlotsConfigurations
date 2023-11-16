# PS unc are bugged in 2016 take them from 2018 as was done in 2017

python ../../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_2016_EFT_DNNcut_geq0p5_bkg_only.root -o plots_fit_2016_EFT_DNNcut_geq0p5_bkg_only_PSnuis.root --nuisance-effect ../../Full2018v7_EFT/rootfiles_2/PS_effect_plots_fit_2018_EFT_DNNcut_geq0p5_bkg_only.root -sf ../../Full2018v7_EFT/txtsForScripts/samples_PS_extraction.txt -n CMS_PS_FSR CMS_PS_ISR

# also for EFT


# Apply QCD scales from 2017 to 2018 as in 2018 they were not saved in the root files

python ../scripts/nuisances_tools/apply_nuisances_effect.py -i rootfiles_2/plots_fit_2016_EFT_DNNcut_geq0p5_sm.root -o rootfiles_2/plots_fit_2016_EFT_DNNcut_geq0p5_QCDscales_sm.root --nuisance-effect ../Full2017v7_EFT/rootfiles_2/QCDscale_effect_sm_bkg_fit_2017_EFT_DNNcut_geq0p5_full.root -s sm -n QCDscale_VBS_envelope

# rename correctly the nuisances 

for var in CMS_PS_FSR CMS_PS_ISR; do python ../scripts/nuisances_tools/rename_shape_root.py -i rootfiles_2/plots_fit_2016_EFT_DNNcut_geq0p5_sm.root --shape-name ${var} --rename "$var"_VBS -sf ../Full2018v7_EFT/txtsForScripts/samples_PS_merging_VBS_sm.txt; done

#

#Delete old PS from bkg

while read p; do   for var in CMS_PS_ISRUp CMS_PS_ISRDown CMS_PS_FSRDown CMS_PS_FSRUp; do python ../../scripts/delete_nuisance_shapes.py -i plots_fit_2017_EFT_DNNcut_geq0p5_bkg_only_noPSnuis.root -s "$p" -n ${var};done ; done<../../Full2018v7_EFT/txtsForScripts/samples_PS_extraction.txt

# Merge CMS PS unc on EFT
for var in CMS_PS_FSR CMS_PS_ISR; do python ../../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_2016_EFT_DNNcut_geq0p5_eft.root --shape-name ${var} --rename "$var"_EFT -sf ../../Full2018v7_EFT/txtsForScripts/samples_EFT_datacard.txt; done

# apply PDF effect to bkgs

python ../scripts/nuisances_tools/apply_nuisances_effect.py -i rootfiles_2/plots_fit_2016_EFT_DNNcut_geq0p5_full.root -o rootfiles_2/plots_fit_2016_EFT_DNNcut_geq0p5_full_PDFnuis.root --nuisance-effect ../Full2018v7_EFT/rootfiles_2/PDF_effect_plots_fit_2018_EFT_DNNcut_geq0p5_full.root -sf ../Full2018v7_EFT/txtsForScripts/samples_PDF_extraction.txt -n pdf_weight_1718 -nr pdf_weight_16

# delete PDF for sm as in 2016 it is better 

python ../scripts/delete_sample_root.py rootfiles_2/plots_fit_2016_EFT_DNNcut_geq0p5_full_PDFnuis.root sm

# hadd PDF 

hadd plots_fit_2016_EFT_DNNcut_geq0p5_full.root plots_fit_2016_EFT_DNNcut_geq0p5_full_orig.root plots_fit_2016_EFT_DNNcut_geq0p5_full_PDFnuis.root

# Correlate properly PS unc

for var in CMS_PS_FSR CMS_PS_ISR; do python ../scripts/nuisances_tools/rename_shape_root.py -i rootfiles_2/plots_fit_2018_EFT_DNNcut_geq0p5_sm.root --shape-name ${var} --rename "$var"_VBS -sf txtsForScripts/samples_PS_merging_VBS_sm.txt; done
for var in CMS_PS_FSR CMS_PS_ISR; do python ../scripts/nuisances_tools/rename_shape_root.py -i rootfiles_2/plots_fit_2018_EFT_DNNcut_geq0p5_bkg_only.root --shape-name ${var} --rename "$var"_QCD_VV -sf txtsForScripts/samples_PS_merging_VV.txt; done

# to reproduce 2016 

python ../scripts/merge_cuts.py -i rootfiles_2/plots_fit_2016_EFT_DNNcut_geq0p5_full.root -o rootFiles_regions/merged_signal.root -m boost_sig_ele:boost_sig_ele_DNN_geq_0p5,boost_sig_ele_DNN_leq_0p5 boost_sig_mu:boost_sig_mu_DNN_geq_0p5,boost_sig_mu_DNN_leq_0p5 res_sig_ele:res_sig_ele_DNN_geq_0p5,res_sig_ele_DNN_leq_0p5 res_sig_mu:res_sig_mu_DNN_geq_0p5,res_sig_mu_DNN_leq_0p5 -v events fit_bins_boost fit_bins_res DNNoutput_boost DNNoutput_res_v1 Mww_10 Mww  
