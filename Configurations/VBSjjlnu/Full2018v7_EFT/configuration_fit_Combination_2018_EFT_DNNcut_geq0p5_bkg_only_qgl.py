# example of configuration file
treeName= 'Events'


tag = 'fit_2018_EFT_DNNcut_geq0p5_bkg_only_qglnuis'
direc = "conf_fit_EFT_DNNcut_geq0p5_bkg_only"

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases_qglnuis.py'

# file with list of variables
variablesFile = direc+'/variables_qglnuis.py'

# file with list of cuts
cutsFile = direc +'/cuts.py' 

# file with list of samples
samplesFile = direc+'/samples.py' 

#t file with list of samples
plotFile = direc+'/plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot_'+tag  

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag 

# structure file for datacard
structureFile = direc+'/structure_split.py'


# nuisances file for mkDatacards and for mkShape
# nuisancesFile = direc+'/nuisances.py'
nuisancesFile = direc+'/nuisances_qglnuis.py'
# nuisancesFile = direc + '/nuisances_datacard_split.py'
# nuisancesFile = direc + '/nuisances_datacard_split_2pois.py'



customizeScript = direc + '/customize.py'
