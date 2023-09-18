# 2017 Boost
for poi in k_cHl1 k_cHQ1 k_cHWB k_cHbox k_cHB k_cW k_cHW k_cHj1; do python scripts/prepare_likelihood_scan_EFT.py -c datacards/datacard_config_2017_EFT_FullOps_BoostAllVars_DNNcut_geq0p5_full_mWW_10.json -o datacards/2017_EFT_FullOps_BoostAllVars_DNNcut_geq0p5_full_mWW_10_cHB_cW_cHW_cHWB_cHj1_cHbox_cHl1_cHQ1 -p scan -pois $poi --data-asimov -fo 1 --points 40 --split 1 -prof --randomPoints 10 -v 0; done

# 2018 

#for poi in k_cHWB k_cHbox k_cHB k_cW k_cHW k_cHj1; do python scripts/prepare_likelihood_scan_EFT.py -c datacards/datacard_config_2018_EFT_FullOps_DNNcut_geq0p5_full_mWW_10.json -o datacards/2018_EFT_FullOps_DNNcut_geq0p5_full_mWW_10_cHB_cW_cHW_cHWB_cHj1_cHbox -p graph -pois $poi --data-asimov -fo 1 --points 30 --split 1 -prof --randomPoints 10 -v 0; done
