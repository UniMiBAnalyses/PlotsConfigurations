
# How to run the analysis 
### CMSSW_11_1_4 IS NEEDED FOR DNN OUTPUT VARIABLE!!
To run it on CMSSW_10_6_4 pls comment the dnn variable everywhere
Furtheremore (refer to Giorgio for this) it is needed a customization of https://github.com/UniMiBAnalyses/NNEvaluation/blob/master/DNNTensorflow/src/DNNEvaluatorSavedModel.cpp#L74 in CMSSW_11_1_4:


    void NNEvaluation::DNNEvaluatorSavedModel::open_session(){
        if (session_ready_) return;

        // metaGraph_ = tensorflow::loadMetaGraph(graphPath_); // TODO check what happens if file not present
        // // create a new session and add the graphDef
        // session_ = tensorflow::createSession(metaGraph_, graphPath_);
        tensorflow::GraphDef* graphDef = tensorflow::loadGraphDef(graphPath_);
        session_ = tensorflow::createSession(graphDef);
        session_ready_ = true;
        std::cout << "Tensorflow session ready" <<std::endl;
    }  

# SM & EFT sample position:
Private sample are NOT in:

    treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

but are now in:

    treeBaseDirPrivate = 'gwterax2/users/amassiro/EFT_W_EWK/nanoaod/postProc'

A little customization is thus needed is samples.py!

Anyway, one can re apply the skim modifying the https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/Steps_cfg.py file, adding these lines somewhere:

    '2Jets1leptonW': {
                    'isChain': False,
                    'do4MC': True,
                    'do4Data': True,
                    'selection': '"(Alt$(Lepton_pt[0],0) > 25.) && (Alt$(CleanJet_pt[1], 0) > 30.) && (Alt$(CleanJet_pt[0],0) > 40.) && (mjj >= 400.) && (detajj > 2.) && (Alt$(Lepton_eta[0],-3) > -2.) && (Alt$(Lepton_eta[0],3) < 2.) && Alt$(Lepton_pt[1],0)<=15. && Alt$(Lepton_isLoose[1],1)> 0.5 && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )"',
        },  

Similarly for the EFT nanoAOD, in samplesEFT.py, samples are no more in:

    treeBaseDirEFTPrivate = '/eos/user/a/abulla/gridpack/EFT_FullSim/root'

but in 

    treeBaseDirEFTPrivate = 'gwterax2/users/amassiro/EFT_W_EWK/gridpack/EFT_FullSim/root'
    
    
# Produce the shapes:

### N.B. dont know why but the hadd process (with systematics) is rather slow. The last step ofter requires several hours, if kill the process, the final root file is not usable. There is some nuisance probabily which has something. Easy way to solve, try add one by one and see how slow is the hadd process!

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=tomorrow

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_vbf_w_2016.root rootFile/plots_vbf_w_2016_ALL_*.root
    hadd rootFile/plots_vbf_w_2016.root rootFile/plots_vbf_w_2016_do.root rootFile/prov/plots_vbf_w_2016.root 


# Make plots:
For this section, at the time being (nov. 2022), it is needed CMSSW10_6_4 (for example) recreating the same path ~/CMSSW 10../src/Plotconfig/config/VBF_W/2016/ and here it is needed utils folder. This folder is used somewhere in the nuisances, it is easy to solve this problem, didnt have the time!


    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root --onlyPlot=cratio  --showIntegralLegend=1 --plotNormalizedDistributions

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root --showIntegralLegend=1
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root --showIntegralLegend=1  --plotNormalizedDistributionsTHstack
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root --showIntegralLegend=1  --plotNormalizedDistributions

# Make DataCards
    mkDatacards.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root


# Make nuis plot
    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurations/Configurations/VBF_W/2016/datacards/topcr/eta1/shapes/histos_topcr.root  \
     --outputDirPlots ../../../../PlotsConfigurations/Configurations/VBF_W/2016/topcr_nuisance  \
     --nuisancesFile ../../../../PlotsConfigurations/Configurations/VBF_W/2016/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurations/Configurations/VBF_W/2016/samples.py \
     --cutName topcr

# How to run the analysis 
### CMSSW_11_1_4 IS NEEDED FOR DNN OUTPUT VARIABLE!!
To run it on CMSSW_10_6_4 pls comment the dnn variable everywhere
Furtheremore (refer to Giorgio for this) it is needed a customization of https://github.com/UniMiBAnalyses/NNEvaluation/blob/master/DNNTensorflow/src/DNNEvaluatorSavedModel.cpp#L74 in CMSSW_11_1_4:


    void NNEvaluation::DNNEvaluatorSavedModel::open_session(){
        if (session_ready_) return;

        // metaGraph_ = tensorflow::loadMetaGraph(graphPath_); // TODO check what happens if file not present
        // // create a new session and add the graphDef
        // session_ = tensorflow::createSession(metaGraph_, graphPath_);
        tensorflow::GraphDef* graphDef = tensorflow::loadGraphDef(graphPath_);
        session_ = tensorflow::createSession(graphDef);
        session_ready_ = true;
        std::cout << "Tensorflow session ready" <<std::endl;
    }  

# SM & EFT sample position:
Private sample are NOT in:

    treeBaseDirPrivate = '/eos/user/a/abulla/nanoAOD/postProc/'

but are now in:

    treeBaseDirPrivate = 'gwterax2/users/amassiro/EFT_W_EWK/nanoaod/postProc'

A little customization is thus needed is samples.py!

Anyway, one can re apply the skim modifying the https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/Steps_cfg.py file, adding these lines somewhere:

    '2Jets1leptonW': {
                    'isChain': False,
                    'do4MC': True,
                    'do4Data': True,
                    'selection': '"(Alt$(Lepton_pt[0],0) > 25.) && (Alt$(CleanJet_pt[1], 0) > 30.) && (Alt$(CleanJet_pt[0],0) > 40.) && (mjj >= 400.) && (detajj > 2.) && (Alt$(Lepton_eta[0],-3) > -2.) && (Alt$(Lepton_eta[0],3) < 2.) && Alt$(Lepton_pt[1],0)<=15. && Alt$(Lepton_isLoose[1],1)> 0.5 && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )"',
        },  

Similarly for the EFT nanoAOD, in samplesEFT.py, samples are no more in:

    treeBaseDirEFTPrivate = '/eos/user/a/abulla/gridpack/EFT_FullSim/root'

but in 

    treeBaseDirEFTPrivate = 'gwterax2/users/amassiro/EFT_W_EWK/gridpack/EFT_FullSim/root'
    
    
# Produce the shapes:

### N.B. dont know why but the hadd process (with systematics) is rather slow. The last step ofter requires several hours, if kill the process, the final root file is not usable. There is some nuisance probabily which has something. Easy way to solve, try add one by one and see how slow is the hadd process!

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=tomorrow

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_vbf_w_2016.root rootFile/plots_vbf_w_2016_ALL_*.root
    hadd rootFile/plots_vbf_w_2016.root rootFile/plots_vbf_w_2016_do.root rootFile/prov/plots_vbf_w_2016.root 


# Make plots:
For this section, at the time being (nov. 2022), it is needed CMSSW10_6_4 (for example) recreating the same path ~/CMSSW 10../src/Plotconfig/config/VBF_W/2016/ and here it is needed utils folder. This folder is used somewhere in the nuisances, it is easy to solve this problem, didnt have the time!


    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1 --plotNormalizedDistributions

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root --showIntegralLegend=1
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root --showIntegralLegend=1  --plotNormalizedDistributionsTHstack
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root --showIntegralLegend=1  --plotNormalizedDistributions

# Make DataCards
    mkDatacards.py --pycfg=configuration.py --inputFile rootFile/plots_vbf_w_2016.root


# Make nuis plot
    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurations/Configurations/VBF_W/2016/datacards/topcr/eta1/shapes/histos_topcr.root  \
     --outputDirPlots ../../../../PlotsConfigurations/Configurations/VBF_W/2016/topcr_nuisance  \
     --nuisancesFile ../../../../PlotsConfigurations/Configurations/VBF_W/2016/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurations/Configurations/VBF_W/2016/samples.py \
     --cutName topcr
