#!/bin/bash


if [ $# -lt 1 ]
  then
    echo "Usage: ./skim_trees_wjets_2018_res.sh <res_bin>"
    exit 0
fi


BASEDIR=`pwd`
cd $CMSSW_BASE/src/LatinoAnalysis/Tools/scripts

#/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/
#/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/

TARGETDIR="/eos/user/g/gboldrin/nanoLatino/Autumn18_102X_nAODv7_Full2018v7_skim"

if [ $1 = 1 ]; then
#bin 1 
SUBDIR="res_bin_1"
mkdir -p $TARGETDIR/$SUBDIR


python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt < 100) && (vbs_1_pt < 55)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 2 ]; then
# bin 2
SUBDIR="res_bin_2"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt < 100) && vbs_1_pt >= 55 && vbs_1_pt < 75) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 3 ]; then
# bin 3
SUBDIR="res_bin_3"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt < 100) && (vbs_1_pt >= 75 && vbs_1_pt < 100)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 4 ]; then
# bin 4
SUBDIR="res_bin_4"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt < 100) && (vbs_1_pt >= 100 && vbs_1_pt < 135)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5
fi 

if [ $1 = 5 ]; then
# bin 5
SUBDIR="res_bin_5"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt < 100) && (vbs_1_pt >= 135 && vbs_1_pt < 170)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5


fi

if [ $1 = 6 ]; then
# bin 6
SUBDIR="res_bin_6"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt < 100) && (vbs_1_pt >= 170)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 7 ]; then
# bin 7
SUBDIR="res_bin_7"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt < 55)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 8 ]; then
# bin 8
SUBDIR="res_bin_8"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 55 && vbs_1_pt < 75)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 9 ]; then
# bin 9
SUBDIR="res_bin_9"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 75 && vbs_1_pt < 100)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 10 ]; then
# bin 10
SUBDIR="res_bin_10"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 100 && vbs_1_pt < 135)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 11 ]; then

# bin 11
SUBDIR="res_bin_11"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 135 && vbs_1_pt < 170)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 12 ]; then
# bin 12
SUBDIR="res_bin_12"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 170)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 13 ]; then
# bin 13
SUBDIR="res_bin_13"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 200 && w_lep_pt < 300) && (vbs_1_pt < 90)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5
fi 

if [ $1 = 14 ]; then
# bin 14
SUBDIR="res_bin_14"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 200 && w_lep_pt < 300) && (vbs_1_pt >= 90 && vbs_1_pt < 125)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5
fi

if [ $1 = 15 ]; then
# bin 15
SUBDIR="res_bin_15"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 200 && w_lep_pt < 300) && (vbs_1_pt >= 125 && vbs_1_pt < 160)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 16 ]; then
# bin 16
SUBDIR="res_bin_16"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 200 && w_lep_pt < 300) && (vbs_1_pt >= 160)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 17 ]; then
# bin 17
SUBDIR="res_bin_17"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 300 && w_lep_pt < 400) && (vbs_1_pt < 90)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 18 ]; then
# bin 18
SUBDIR="res_bin_18"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 300 && w_lep_pt < 400) && (vbs_1_pt >= 90)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 19 ]; then
# bin 19
SUBDIR="res_bin_19"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 400 && w_lep_pt < 500) && (vbs_1_pt < 85)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 20 ]; then
# bin 20
SUBDIR="res_bin_20"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 400 && w_lep_pt < 500) && (vbs_1_pt >= 85)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 21 ]; then
# bin 21
SUBDIR="res_bin_21"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==1)*((w_lep_pt >= 500)) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5
fi

