#!/bin/bash

# Array con le directory
dirs=("detajj" "dphijj" "jet1eta" "jet1pt" "jet2eta" "jet2pt" "lepeta" "leppt" "nJet" "ptjj" "ptW" "mjj")
# dirs=("ptW" "jet1eta" "dphijj" "detajj")

# Numero massimo di processi simultanei
max_jobs=6
job_count=0

for dir in "${dirs[@]}"; do
    (
        cd $dir
        # command="mkShapesMulti.py --pycfg=configuration_${dir}.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=nextweek --Silent"
        command="mkShapesMulti.py --pycfg=configuration_${dir}.py --batchSplit=Samples,Files --doNotCleanup --nThreads=10 --doResub --ForceResub"
        # command="mkDatacards.py --pycfg=configuration_${dir}.py --inputFile ../../rootFile/noHIPMunfolding_final_${dir}/plots_vbf_w_2016noHIPMunfolding_final_${dir}_p_bkg.root"
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
#         cd ../rootFile/noHIPMunfolding_final_$dir
#         command="hadd -j -f plots_vbf_w_2016noHIPMunfolding_final_${dir}_p_bkg.root plots_vbf_w_2016noHIPMunfolding_final_$dir.root ../noHIPMunfolding_final_bkgOnly/plots_vbf_w_2016noHIPMunfolding_final_bkgOnly.root"
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
