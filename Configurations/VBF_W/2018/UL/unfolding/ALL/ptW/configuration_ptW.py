# Configuration file to produce initial root files 

treeName = 'Events'
fixSuffix = 'ptW'

tagger = 'unfolding_final_v12'
tagger += "_"+fixSuffix


tag = 'vbf_w_2018'+tagger

# used by mkShape to define output directory for root files
# outputDir = '../rootFile/NORWALLSYS'
outputDir = '../../rootFile/'+tagger

# file with TTree aliases
aliasesFile = 'aliases_ptW.py'

# file with list of variables
variablesFile = 'variables_ptW.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples_ptW.py'

# file with list of samples
plotFile = '../plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for ../plots
# different from "outputDir" to do things more tidy
#outputDirPlots = '../plots'
# outputDirPlots = '../plots/NORWALLSYS'
outputDirPlots = '../../plots/'+tagger

# used by mkDatacards to define output directory for ../datacards
outputDirDatacard = '../../datacards/'+tagger

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
