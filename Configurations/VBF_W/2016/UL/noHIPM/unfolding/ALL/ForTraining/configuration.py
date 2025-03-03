# Configuration file to produce initial root files 

treeName = 'Events'

pretag = "2016noHIPM"
tagger = pretag+'TrainingMC'

tag = 'vbf_w_'+tagger

# used by mkShape to define output directory for root files
# outputDir = 'rootFile/NORWALLSYS'
outputDir = '../../rootFile/'+tagger

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'ttree_var.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py'

# file with list of samples
plotFile = 'plot5.py' 

# luminosity to normalize to (in 1/fb)
lumi = 16.81

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plots'
# outputDirPlots = 'plots/NORWALLSYS'
outputDirPlots = '../../plots/'+tagger

# used by mkDatacards to define output directory for datacards
outputDirDatacard = '../../datacards/'+tagger

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
