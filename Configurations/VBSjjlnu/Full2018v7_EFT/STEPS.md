################

Run shapes for the following configs

################

- conf_fit_EFT_DNNcut_geq0p5_bkg_only
- conf_fit_EFT_DNNcut_geq0p5_eft
- conf_fit_EFT_DNNcut_geq0p5_sm

################

For nuisance tratement of VBF-V_dipole run

################

conf_fit_EFT_DNNcut_geq0p5_VBF-V_Pythia


################

on the output file we need to extract the VBF-V ISR and FSR effect into a file, rename on that file VBF-V -> VBF-V_dipole, 
delete from original file the shapes of interest, apply the nuisance effect of VBF-V on the nominal VBF-V_dipole

################

python ../scripts/nuisances_tools/extract_nuisances_effect.py -i rootFile_fit_2018_EFT_DNNcut_geq0p5_VBF-V_Pythia/plots_fit_2018_EFT_DNNcut_geq0p5_VBF-V_Pythia_ALL_VBF-V.root -o PS_effect_fit_v4.5_2018_split_VBF-V_Pythia.root -s VBF-V -cf txtsForScripts/cuts_PS_extraction.txt -v ALL -n CMS_PS_ISR CMS_PS_FSR

for i in CMS_PS_ISRUp CMS_PS_ISRDown CMS_PS_FSRUp CMS_PS_FSRDown; do python ../scripts/rename_sample_root.py -i PS_effect_fit_v4.5_2018_split_VBF-V_Pythia.root --sample VBF-V_${i} --rename VBF-V_dipole_${i}; done


################

hadd plots_fit_2018_EFT_DNNcut_geq0p5_full.root plots_fit_2018_EFT_DNNcut_geq0p5_bkg_only.root rootFile_fit_2018_EFT_DNNcut_geq0p5_sm/plots_fit_2018_EFT_DNNcut_geq0p5_sm.root rootFile_fit_2018_EFT_DNNcut_geq0p5_eft/plots_fit_2018_EFT_DNNcut_geq0p5_eft.root 


################



for var in CMS_PS_ISRUp CMS_PS_ISRDown CMS_PS_FSRDown CMS_PS_FSRUp; do python ../scripts/delete_nuisance_shapes.py -i plots_fit_2018_EFT_DNNcut_geq0p5_full.root -s VBF-V_dipole -n ${var}; done

python ../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_2018_EFT_DNNcut_geq0p5_full.root -o plots_fit_2018_EFT_DNNcut_geq0p5_full_PSnuis.root --nuisance-effect PS_effect_fit_v4.5_2018_split_VBF-V_Pythia.root -s VBF-V_dipole -n CMS_PS_FSR CMS_PS_ISR

hadd plots_fit_2018_EFT_DNNcut_geq0p5_full_wPS.root plots_fit_2018_EFT_DNNcut_geq0p5_full_PSnuis.root plots_fit_2018_EFT_DNNcut_geq0p5_full.root  


##################

Then we decorrelate FSR and ISR for all the samples  

#################

# for var in CMS_PS_FSR CMS_PS_ISR; do python ../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_2018_EFT_DNNcut_geq0p5_full_wPS.root --shape-name ${var} -sf txtsForScripts/samples_PS_extraction.txt; done
for var in CMS_PS_FSR CMS_PS_ISR; do python ../scripts/nuisances_tools/rename_shape_root.py -i rootfiles_2/plots_fit_2018_EFT_DNNcut_geq0p5_bkg_only.root --shape-name ${var} -sf txtsForScripts/samples_PS_extraction.txt; done
for var in CMS_PS_FSR CMS_PS_ISR; do python ../scripts/nuisances_tools/rename_shape_root.py -i rootfiles_2/plots_fit_2018_EFT_DNNcut_geq0p5_sm.root --shape-name ${var} --rename "$var"_VBS -sf txtsForScripts/samples_PS_merging_VBS_sm.txt; done
for var in CMS_PS_FSR CMS_PS_ISR; do python ../scripts/nuisances_tools/rename_shape_root.py -i rootfiles_2/plots_fit_2018_EFT_DNNcut_geq0p5_bkg_only.root --shape-name ${var} --rename "$var"_QCD_VV -sf txtsForScripts/samples_PS_merging_VV.txt; done
for var in CMS_PS_FSR CMS_PS_ISR; do python ../../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_2018_EFT_DNNcut_geq0p5_eft.root --shape-name ${var} --rename "$var"_EFT -sf ../txtsForScripts/samples_EFT_datacard.txt; done

################

# Apply QCD scales from 2017 to 2018 as in 2018 they were not saved in the root files

python ../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_2018_EFT_DNNcut_geq0p5_full_wPS.root -o plots_fit_2018_EFT_DNNcut_geq0p5_full_QCDscales_sm.root --nuisance-effect /eos/user/g/gboldrin/Full2017v7_EFT/QCDscale_effect_sm_bkg_fit_2017_EFT_DNNcut_geq0p5_full.root -s sm -n QCDscale_VBS_envelope

################

# Extract PS for EFT to apply to 2016

python ../scripts/nuisances_tools/extract_nuisances_effect.py -i rootfiles_2/plots_fit_2018_EFT_DNNcut_geq0p5_eft.root -o rootfiles_2/PS_effect_plots_fit_2018_EFT_DNNcut_geq0p5_eft.root -sf txtsForScripts/samples_EFT_datacard.txt -cf txtsForScripts/cuts_PS_extraction.txt -v ALL -n CMS_PS_ISR CMS_PS_FSR

################

# Extract PDF to apply to 2016 

python ../../scripts/nuisances_tools/extract_nuisances_effect.py -i plots_fit_v4.5_2018_split.root -o PDF_effect_bkg_fit_v4.5_2018.root -sf ../samples_PDF_extraction.txt -cf ../cuts_PS_extraction.txt -v ALL -n pdf_weight_1718


################

# Make datacards

mkDatacards.py --pycfg=configuration_fit_Combination_2018_EFT_DNNcut_geq0p5_full_datacards.py   --inputFile rootfiles/plots_fit_2017_EFT_DNNcut_geq0p5_full_wPS_wQCD.root --skipMissingNuisance
