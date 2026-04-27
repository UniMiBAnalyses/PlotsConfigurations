#!/bin/bash

# Array con le directory
dirs=("detajj" "dphijj" "jet1eta" "jet1pt" "jet2eta" "jet2pt" "lepeta" "leppt" "nJet" "ptjj" "ptW" "mjj")
# dirs=("detajj")

# Numero massimo di processi simultanei
max_jobs=6
job_count=0

TAG="noHIPMunfolding_final_v12"

for dir in "${dirs[@]}"; do
    (
        cd $dir
        sed -i 's|unfolding/BKG_ONLY/samples.py|unfolding/samples_nobkg.py|' samples_${dir}.py
        command="mkShapesMulti.py --pycfg=configuration_${dir}.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=nextweek --Silent"

        # # # # Percorso del file di output haddato che vuoi controllare
        # OUTPUT_FILE="../../rootFile/${TAG}_${dir}/plots_vbf_w_2016${TAG}_${dir}.root"

        # if [ -f "$OUTPUT_FILE" ]; then
        #     echo "✅ Skipping $dir: $OUTPUT_FILE already exists."
        #     exit 0
        # fi
        # command="mkShapesMulti.py --pycfg=configuration_${dir}.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 --doResub --ForceResub"

        # sed -i 's|unfolding/BKG_ONLY/samples.py|unfolding/samples_nobkg.py|' samples_${dir}.py
        # command="python ../../SymmetrizeByHand.py --input  ../../rootFile/${TAG}_${dir}/plots_vbf_w_2016${TAG}_${dir}.root --samples samples_${dir}.py --nuisances nuisances.py --onlyVar variables_${dir}.py --mode fix_empty --submit"
        # sed -i 's|unfolding/samples_nobkg.py|unfolding/BKG_ONLY/samples.py|' samples_${dir}.py
        # command="python ../../truncHistos.py --input ../../rootFile/${TAG}_${dir}/trunc_fixed_plots_vbf_w_2016${TAG}_${dir}_p_bkg.root --samples  samples_${dir}.py --nuisances nuisances.py --onlyVar MultiClass_${dir}_3bin"
        # command="mkPlot.py --pycfg=configuration_${dir}.py --inputFile ../../rootFile/${TAG}_${dir}/fixed_plots_vbf_w_2016${TAG}_${dir}_p_bkg.root --onlyPlot=cratio --showIntegralLegend=1"
        # command="mkDatacards.py --pycfg=configuration_${dir}.py --inputFile ../../rootFile/${TAG}_${dir}/fixed_plots_vbf_w_2016${TAG}_${dir}_p_bkg.root"
        echo "Eseguendo: $command"
        eval $command
    ) &  # Esegui in background
    job_count=$((job_count + 1))

    # Se raggiungiamo il limite massimo di job, aspettiamo che alcuni finiscano
    if [[ $job_count -ge $max_jobs ]]; then
        wait
        job_count=0
    fi
done

# for dir in "${dirs[@]}"; do
#     (
#         cd ../rootFile/${TAG}_$dir
#         command="hadd -j -f fixed_plots_vbf_w_2016${TAG}_${dir}_p_bkg.root fixed_plots_vbf_w_2016${TAG}_$dir.root ../${TAG}_bkgOnly/fixed_plots_vbf_w_2016${TAG}_bkgOnly.root"
#         echo "Eseguendo: $command"
#         eval $command
#         cd -
#     ) &  # Esegui in background
#     job_count=$((job_count + 1))

#     # Se raggiungiamo il limite massimo di job, aspettiamo che alcuni finiscano
#     if [[ $job_count -ge $max_jobs ]]; then
#         wait
#         job_count=0
#     fi
# done
# Aspetta che tutti i processi restanti finiscano
wait
