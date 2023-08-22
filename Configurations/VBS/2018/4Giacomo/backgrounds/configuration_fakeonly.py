# example of configuration file
treeName= 'Events'

#date='_Nov252018_ptll'
date='_2018'

tag = 'fakeonly'+date


# used by mkShape to define output directory for root files
outputDir = 'rootFile'+date+'_fakeonly'

# file with TTree aliases
aliasesFile = 'aliases_310822.py'

# file with list of variables
variablesFile = 'variables_fakeonly.py'

# file with list of cuts
cutsFile = 'cuts.py'
#cutsFile = 'cuts_forPlots.py'

# file with list of samples
samplesFile = 'samples_fakeonly.py'

# file with list of samples
plotFile = 'plot_fakeonly.py'

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot_'+tag


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'+date


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
