# example of configuration file
treeName= 'Events'


# tag = 'fit_2018_EFT_8ops'

# Uncomment this to use with samples_mkDatacard_SMonly
# just saves sm reweighted sample to compare with analysis one
# tag = 'fit_2018_EFT_8ops_SMonly_rew'

tag = 'fit_2018_EFT_8ops_SMonly_VBS'

direc = "conf_fit_EFT_8ops"

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases.py'

# file with list of variables

# uncomment this to run mkShapes
# uncomment this to run mkDatacard
variablesFile = direc+'/variables.py'

# Uncomment this to run mkPlot
# variablesFile = direc+'/variables_mkPlot.py'

# file with list of cuts
cutsFile = direc +'/cuts.py' 

# file with list of samples 

# Uncomment this for mkShapes
# samplesFile = direc+'/samples_mkShapes.py' 

# Uncomment this for mkPlot
# samplesFile = direc+'/samples_mkPlot.py'

# Uncomment this for mkDatacard
# samplesFile = direc+'/samples_mkDatacard.py'

# Uncomment this for mkDatacard only reweighted sm
# samplesFile = direc+'/samples_mkDatacard_onlySM_rew.py'

# Uncomment this for mkDatacard only VBS reference
samplesFile = direc+'/samples_mkDatacard_onlySM_VBS.py'

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

# structure file for datacard EFT
# structureFile = direc+'/structure.py'

# structure file for datacard REFERENCE
structureFile = direc+'/structure_SMVBS.py'


# Uncomment this to run mkShapes
# nuisancesFile = direc + '/nuisances_empty.py'

# Uncomment this to run mkPlot
nuisancesFile = direc + '/nuisances_mkPlot.py'


customizeScript = direc + '/customize.py'
