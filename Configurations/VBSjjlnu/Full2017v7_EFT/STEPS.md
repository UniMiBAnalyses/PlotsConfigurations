################

Run shapes for the following configs

################

- conf_fit_EFT_DNNcut_geq0p5_bkg_only
- conf_fit_EFT_DNNcut_geq0p5_eft
- conf_fit_EFT_DNNcut_geq0p5_sm

################

# Join ele and mu data and fakes

python ../scripts/sum_data_flavours.py  -i rootFile_fit_2017_EFT_DNNcut_geq0p5_bkg_only/plots_fit_2017_EFT_DNNcut_geq0p5_bkg_only.root -y 2017


################ 

# Rename PS uncertainties by splitting them by sample

	python ../scripts/nuisances_tools/rename_shape_root.py -i rootfiles/Full2017v7_EFT/plots_fit_2017_EFT_DNNcut_geq0p5_eft.root --shape-name CMS_PS_FSR -sf ../Full2018v7_EFT/txtsForScripts/samples_EFT_datacard.txt 

	python ../scripts/nuisances_tools/rename_shape_root.py -i rootfiles/Full2017v7_EFT/plots_fit_2017_EFT_DNNcut_geq0p5_eft.root --shape-name CMS_PS_ISR -sf ../Full2018v7_EFT/txtsForScripts/samples_EFT_datacard.txt
 
################

# First merge the files 

	hadd plots_fit_2017_EFT_DNNcut_geq0p5_full.root rootFile_fit_2017_EFT_DNNcut_geq0p5_bkg_only/plots_fit_2017_EFT_DNNcut_geq0p5_bkg_only.root rootFile_fit_2017_EFT_DNNcut_geq0p5_sm/plots_fit_2017_EFT_DNNcut_geq0p5_sm.root rootFile_fit_2017_EFT_DNNcut_geq0p5_eft/plots_fit_2017_EFT_DNNcut_geq0p5_eft.root

################

# For 2017 the PS uncertainities are bugged. However the PS config from 2018 to 2017 is exactly the same. Therefore we can import the PS uncertainties for all samples from 2018 to 2017

	python ../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_2017_EFT_DNNcut_geq0p5_full.root -o plots_fit_2017_EFT_DNNcut_geq0p5_full_PSnuis.root --nuisance-effect ../Full2018v7_EFT/PS_effect_fit_2018_EFT_DNNcut_geq0p5_full.root -sf ../Full2018v7_EFT/txtsForScripts/samples_PS_extraction.txt -n CMS_PS_FSR CMS_PS_ISR

# Delete old nuisances

	while read p; do for var in CMS_PS_ISRUp CMS_PS_ISRDown CMS_PS_FSRDown CMS_PS_FSRUp; do python ../scripts/delete_nuisance_shapes.py -i plots_fit_2017_EFT_DNNcut_geq0p5_full.root -s "$p" -n ${var}; done; done <../Full2018v7_EFT/txtsForScripts/samples_PS_extraction.txt

# Merge the files

	hadd plots_fit_2017_EFT_DNNcut_geq0p5_full_wPS.root plots_fit_2017_EFT_DNNcut_geq0p5_full_PSnuis.root plots_fit_2017_EFT_DNNcut_geq0p5_full.root

################

# Rename PS uncertainties by splitting them by sample
	python ../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_2017_EFT_DNNcut_geq0p5_full_wPS.root --shape-name CMS_PS_ISR -sf ../Full2018v7_EFT/txtsForScripts/samples_PS_extraction.txt 

	python ../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_2017_EFT_DNNcut_geq0p5_full_wPS.root --shape-name CMS_PS_FSR -sf ../Full2018v7_EFT/txtsForScripts/samples_PS_extraction.txt 
################
# extract PDF effect for bookeeping

	python ../scripts/nuisances_tools/extract_nuisances_effect.py -i plots_fit_2017_EFT_DNNcut_geq0p5_full.root -o PDF_effect_bkg_fit_2017_EFT_DNNcut_geq0p5_full.root -sf ../Full2018v7_EFT/txtsForScripts/samples_PDF_extraction.txt -cf ../Full2018v7_EFT/txtsForScripts/cuts_PS_extraction.txt -v ALL -n pdf_weight_1718

# extract QCDscale on signal to apply to 2018

	python ../scripts/nuisances_tools/extract_nuisances_effect.py -i plots_fit_2017_EFT_DNNcut_geq0p5_full.root -o QCDscale_effect_sm_bkg_fit_2017_EFT_DNNcut_geq0p5_full.root -s sm -cf ../Full2018v7_EFT/txtsForScripts/cuts_PS_extraction.txt -v ALL -n QCDscale_VBS_envelope


#################

# Make datacards

	mkDatacards.py --pycfg=configuration_fit_Combination_2017_EFT_DNNcut_geq0p5_full_datacards.py   --inputFile rootfiles/plots_fit_2017_EFT_DNNcut_geq0p5_full_wPS.root --skipMissingNuisance
