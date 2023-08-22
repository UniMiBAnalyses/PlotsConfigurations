# example of configuration file
treeName= 'Events'

#date='_Nov252018_ptll'
date='_2018_31082022_NuisRun'

tag = 'VBS_WW'+date


# used by mkShape to define output directory for root files
outputDir = 'SSWW_nuisances/rootFile'+date

# file with TTree aliases
aliasesFile = 'aliases_EFTdatacard.py'

# file with list of variables
variablesFile = 'variables_EFTdatacard.py'

# file with list of cuts
cutsFile = 'cuts.py'
#cutsFile = 'cuts_forPlots.py'

# file with list of samples
samplesFile = 'samples_EFTdatacard.py'

# file with list of samples
plotFile = 'plot_EFTdatacard.py'

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '../EFTdatacards/try3/plotVBS'+date


# used by mkDatacards to define output directory for datacards
outputDirDatacard = '../EFTdatacards/try3/datacards'+tag


# structure file for datacard
structureFile = 'structure_EFTdatacard.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances_EFTdatacard.py'
