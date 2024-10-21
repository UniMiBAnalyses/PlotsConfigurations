python DrawNuisancesAll.py --inputFile ../datacards/END/topcr/events/shapes/histos_topcr.root --outputDirPlots ../plots/AN_topcr --nuisancesFile nuisances.py --samplesFile samples.py --cutName topCR --onlySample top
wait $!

python DrawNuisancesAll.py --inputFile ../datacards/END/ele_HWJ/events/shapes/histos_ele_HWJ.root --outputDirPlots ../plots/AN_ele_HWJ --nuisancesFile nuisances.py --samplesFile samples.py --cutName ele_HWJ --onlySample Wjets
wait $!

python DrawNuisancesAll.py --inputFile ../datacards/END/ele_HWJ/events/shapes/histos_mu_HWJ.root --outputDirPlots ../plots/AN_mu_HWJ --nuisancesFile nuisances.py --samplesFile samples.py --cutName mu_HWJ --onlySample Wjets
wait $!

python DrawNuisancesAll.py --inputFile ../datacards/END/mu_FakeCR/events/shapes/histos_mu_FakeCR.root --outputDirPlots ../plots/AN_mu_FakeCR --nuisancesFile nuisances.py --samplesFile samples.py --cutName mu_FakeCR --onlySample Fake
wait $!

python DrawNuisancesAll.py --inputFile ../datacards/END/ele_FakeCR/events/shapes/histos_ele_FakeCR.root --outputDirPlots ../plots/AN_ele_FakeCR --nuisancesFile nuisances.py --samplesFile samples.py --cutName ele_FakeCR --onlySample Fake
wait $!

python DrawNuisancesAll.py --inputFile ../datacards/END/mu_SR/DNNoutput_ALLbin4/shapes/histos_mu_SR.root --outputDirPlots ../plots/AN_mu_SR --nuisancesFile nuisances.py --samplesFile samples.py --cutName mu_SR --onlySample WLNuJJ
wait $!

python DrawNuisancesAll.py --inputFile ../datacards/END/ele_SR/DNNoutput_ALLbin4/shapes/histos_ele_SR.root --outputDirPlots ../plots/AN_ele_SR --nuisancesFile nuisances.py --samplesFile samples.py --cutName ele_SR --onlySample WLNuJJ
wait $!