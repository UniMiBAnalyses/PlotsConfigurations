# example of configuration file
treeName= 'Events'


tag = 'fit_2018_EFT_8ops'
direc = "conf_fit_EFT_8ops"

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases.py'

# file with list of variables

# uncomment this to run mkShapes
# variablesFile = direc+'/variables.py'

# Uncomment this to run mkPlot
variablesFile = direc+'/variables_mkPlot.py'

# file with list of cuts
cutsFile = direc +'/cuts.py' 

# file with list of samples 

# Uncomment this for mkShapes
# samplesFile = direc+'/samples_mkShapes.py' 

# Uncomment this for mkPlot
samplesFile = direc+'/samples_mkPlot.py'

#t file with list of samples
plotFile = direc+'/plot_EFT.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plot_'+tag +"_rescaled/detajpt_ext"
outputDirPlots = 'plot_'+tag  

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag 

# structure file for datacard
structureFile = direc+'/structure_split.py'


# Uncomment this to run mkShapes
# nuisancesFile = direc + '/nuisances_empty.py'

# Uncomment this to run mkPlot
nuisancesFile = direc + '/nuisances_mkPlot.py'

customizeScript = direc + '/customize.py'
