# example of configuration file
treeName= 'Events'


tag = 'fit_2018_EFT_200323'
direc = "conf_fit_EFT_200323"

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases.py'

# file with list of variables
variablesFile = direc+'/variables_EFT.py'

# file with list of cuts
cutsFile = direc +'/cuts.py' 

# UNCOMMENT THS IF YOU WANT TO RUN MKShapes
# samplesFile = direc+'/samples_split.py'

# UNCOMMENT THS IF YOU WANT TO RUN MKPLOT
# samplesFile = direc+'/samples_split_EFT.py' 

# UNCOMMENT THS IF YOU WANT TO RUN MKDatacard
samplesFile = direc+'/samples_split_EFT_datacard.py' 

#t file with list of samples
plotFile = direc+'/plot_EFT_cHj1_cW_cHbox_cHl1.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plot_'+tag +"_rescaled/detajpt_ext"
outputDirPlots = 'plot_'+tag  

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag 
# outputDirDatacard = 'datacards_'+tag +"_Dipole_split_v4"

# structure file for datacard
structureFile = direc+'/structure.py'


# nuisances file for mkDatacards and for mkShape
# nuisancesFile = direc+'/nuisances.py'
# nuisancesFile = direc + '/nuisances_datacard_split.py'
# nuisancesFile = direc + '/nuisances_datacard_split_2pois.py'



# UNCOMMENT THS IF YOU WANT TO RUN MKShapes
# nuisancesFile = direc + '/nuisances_EFT.py'

# UNCOMMENT THS IF YOU WANT TO RUN MKPLOT
nuisancesFile = direc + '/nuisances.py'


customizeScript = direc + '/customize.py'
