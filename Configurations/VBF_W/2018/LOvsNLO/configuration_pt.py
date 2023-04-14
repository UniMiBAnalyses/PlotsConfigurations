# Configuration file to produce initial root files 

treeName = 'Events'

tag = 'vbf_w_2018LOvsPTNLO'

# used by mkShape to define output directory for root files
outputDir = 'rootFile/PTNLO'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples_pt.py' 

# file with list of samples
plotFile = 'plot_pt.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plots'
outputDirPlots = 'plots/PTNLO'


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'

# structure file for datacard
structureFile = 'structure_pt.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
