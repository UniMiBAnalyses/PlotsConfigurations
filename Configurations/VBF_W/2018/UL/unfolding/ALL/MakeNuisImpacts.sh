for i in 1 2 3 4 5; do 
    python DrawNuisancesAll.py --inputFile ../datacards/unfolding_DNNMulti_mjj/mu_SR/DNNoutputSR_class${i}_ratio/shapes/histos_mu_SR.root --outputDirPlots ../plots/MCNuis_mu --nuisancesFile nuisances.py --samplesFile samples.py --cutName mu_SR --onlySample WLNuJJ_mjj${i}
    wait $!
done

for i in 1 2 3 4 5; do 
    python DrawNuisancesAll.py --inputFile ../datacards/unfolding_DNNMulti_mjj/ele_SR/DNNoutputSR_class${i}_ratio/shapes/histos_ele_SR.root --outputDirPlots ../plots/MCNuis_ele --nuisancesFile nuisances.py --samplesFile samples.py --cutName mu_SR --onlySample WLNuJJ_mjj${i} --DrawSummary
    wait $!
done