# example of configuration file

treeName= 'Events'

date = 'apr27'

version = '2018_full_mischarge'

tag = 'VBS_SS' + '_' + version + '_' + date

# used by mkShape to define output directory for root files
outputDir = 'rootFile' + '_' + tag

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py'
# cutsFile = 'cuts_fast.py'

# file with list of samples
samplesFile = 'samples.py'

# file with list of samples
plotFile = 'plot.py'

# luminosity to normalize to (in 1/fb)
lumi = 59.74 

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plots' + '_' + tag


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards' + '_' + tag


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
# nuisancesFile = 'nuisances_fast.py'


