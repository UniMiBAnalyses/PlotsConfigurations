python DrawNuisancesAll.py --inputFile ../../datacards/HIPM_END/topcr/events/shapes/histos_topcr.root --outputDirPlots ../../plots/HIPMAN_topcr --nuisancesFile nuisances.py --samplesFile samples.py --cutName topCR --onlySample top

python DrawNuisancesAll.py --inputFile ../../datacards/HIPM_END/ele_HWJ/events/shapes/histos_ele_HWJ.root --outputDirPlots ../../plots/HIPMAN_ele_HWJ --nuisancesFile nuisances.py --samplesFile samples.py --cutName ele_HWJ --onlySample Wjets

python DrawNuisancesAll.py --inputFile ../../datacards/HIPM_END/mu_HWJ/events/shapes/histos_mu_HWJ.root --outputDirPlots ../../plots/HIPMAN_mu_HWJ --nuisancesFile nuisances.py --samplesFile samples.py --cutName mu_HWJ --onlySample Wjets

python DrawNuisancesAll.py --inputFile ../../datacards/HIPM_END/mu_FakeCR/events/shapes/histos_mu_FakeCR.root --outputDirPlots ../../plots/HIPMAN_mu_FakeCR --nuisancesFile nuisances.py --samplesFile samples.py --cutName mu_FakeCR --onlySample Fake

python DrawNuisancesAll.py --inputFile ../../datacards/HIPM_END/ele_FakeCR/events/shapes/histos_ele_FakeCR.root --outputDirPlots ../../plots/HIPMAN_ele_FakeCR --nuisancesFile nuisances.py --samplesFile samples.py --cutName ele_FakeCR --onlySample Fake

python DrawNuisancesAll.py --inputFile ../../datacards/HIPM_END/mu_SR/DNNoutput_ALLbin4/shapes/histos_mu_SR.root --outputDirPlots ../../plots/HIPMAN_mu_SR --nuisancesFile nuisances.py --samplesFile samples.py --cutName mu_SR --onlySample WLNuJJ

python DrawNuisancesAll.py --inputFile ../../datacards/HIPM_END/ele_SR/DNNoutput_ALLbin4/shapes/histos_ele_SR.root --outputDirPlots ../../plots/HIPMAN_ele_SR --nuisancesFile nuisances.py --samplesFile samples.py --cutName ele_SR --onlySample WLNuJJ