# Configuration file to produce initial root files 

treeName = 'Events'

tagger = 'DNNTREE_Fake'
tag = 'vbf_w_2018'+tagger

# used by mkShape to define output directory for root files
outputDir = 'rootFile/'+tagger

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'ttree_var.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples_central.py' 

# file with list of samples
plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plots'
outputDirPlots = 'plots/'+tag


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
