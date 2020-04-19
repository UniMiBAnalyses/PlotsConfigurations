#!/bin/bash

set -e 

DIR=$PWD

for year in Full2017nano_STXS_1p1 Full2018nano_STXS_1p1 #Full2016nano_STXS_1p1 Full2017nano_STXS_1p1 Full2018nano_STXS_1p1
do
    echo " --> $year"
    YEAR=`echo $year | awk -F "Full" '{print $2}' | awk -F "nano" '{print $1}'`
    cd $DIR; cd $year
    echo "mkPlot.py --pycfg configuration.py --inputFile rootFiles_ZH3l_${YEAR}_v6_STXS/plots_ZH3l_${YEAR}_v6_STXS.root --showIntegralLegend 1"
    mkPlot.py --pycfg configuration.py --inputFile rootFiles_ZH3l_${YEAR}_v6_STXS/plots_ZH3l_${YEAR}_v6_STXS.root --showIntegralLegend 1
done
