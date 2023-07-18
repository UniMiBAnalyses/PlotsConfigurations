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

for var in CMS_PS_ISRUp CMS_PS_ISRDown CMS_PS_FSRDown CMS_PS_FSRUp; do python ../scripts/delete_nuisance_shapes.py -i prova.root -s VBF-V_dipole -n ${var}; done

python ../scripts/nuisances_tools/apply_nuisances_effect.py -i prova.root -o prova_PSnuis.root --nuisance-effect PS_effect_fit_v4.5_2018_split_VBF-V_Pythia.root -s VBF-V_dipole -n CMS_PS_FSR CMS_PS_ISR

hadd prova_wPS.root prova.root prova_PSnuis.root  


##################

Then we decorrelate FSR and ISR for all the samples  

#################

for var in CMS_PS_FSR CMS_PS_ISR; do python ../scripts/nuisances_tools/rename_shape_root.py -i prova_wPS.root --shape-name ${var} -sf txtsForScripts/samples_PS_extraction.txt; done
