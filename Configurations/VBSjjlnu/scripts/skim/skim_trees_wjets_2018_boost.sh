#!/bin/bash


if [ $# -lt 1 ]
  then
    echo "Usage: ./skim_trees_wjets_2018_boost.sh <res_bin>"
    exit 0
fi



BASEDIR=`pwd`
cd $CMSSW_BASE/src/LatinoAnalysis/Tools/scripts

#/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/
#/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/

TARGETDIR="/eos/user/g/gboldrin/nanoLatino/Autumn18_102X_nAODv7_Full2018v7_skim"

if [ $1 = 1 ]; then
#bin 1 
SUBDIR="boost_bin_1"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==0)*(w_lep_pt < 50) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi

if [ $1 = 2 ]; then
#bin 2
SUBDIR="boost_bin_2"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==0)*(w_lep_pt >= 50 && w_lep_pt < 100) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 3 ]; then
#bin 3 
SUBDIR="boost_bin_3"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==0)*(w_lep_pt >= 100 && w_lep_pt < 150) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 4 ]; then
#bin 4
SUBDIR="boost_bin_4"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==0)*(w_lep_pt >= 150 && w_lep_pt < 200) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 5 ]; then
#bin 5 
SUBDIR="boost_bin_5"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==0)*(w_lep_pt >= 200 && w_lep_pt < 300) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 6 ]; then
#bin 6
SUBDIR="boost_bin_6"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==0)*(w_lep_pt >= 300 && w_lep_pt < 400) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5

fi 

if [ $1 = 7 ]; then
#bin 7
SUBDIR="boost_bin_7"
mkdir -p $TARGETDIR/$SUBDIR

python submitSkimWithSystematics.py \
        --tag 2018_$SUBDIR \
        --basedir /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7_skim  \
        --targetdir $TARGETDIR/$SUBDIR  \
        --step MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018 \
        --samples-file  $BASEDIR/samples_to_skim_Wjets.cfg \
        --variations ElepT MupT MET JES JER fatjetJES fatjetJER fatjetJMR fatjetJMS   \
        --cut "(VBS_category==0)*(w_lep_pt >= 400) && mjj_vbs >=500 && deltaeta_vbs >= 2.5 && Lepton_pt > 30 && PuppiMET_pt > 30 " \
        --branches-remove "HM*" "me_*" "MH*" \
        --save-entrylists \
        -q microcentury    \
        --files-per-job 5
fi 

