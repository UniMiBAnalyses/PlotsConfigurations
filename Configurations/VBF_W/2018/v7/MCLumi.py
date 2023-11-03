from LatinoAnalysis.Tools.commonTools import *
import os
import ROOT

def getLumi(TreeName, iProd, prodCfg='/eos/user/a/abulla/CMSSW_11_0_4/src/LatinoAnalysis/NanoGardener/python/framework/Productions_cfg.py'):
 # Compute #evts
    genEventCount = 0
    genEventSumw  = 0.0
    genEventSumw2 = 0.0

    FileList = getSampleFiles(mcDirectory,TreeName,True,'nanoLatino_')
    print("File(s): ", FileList)

    for iFile in FileList:
        f = ROOT.TFile.Open(iFile.replace('###',''),'READ')
        Runs = f.Get("Runs")
        for iRun in Runs :
            trailer = ""
            if hasattr(iRun, "genEventSumw_"): trailer = "_" 
            genEventCount += getattr(iRun, "genEventCount"+trailer)
            genEventSumw  += getattr(iRun, "genEventSumw" +trailer)
            genEventSumw2 += getattr(iRun, "genEventSumw2"+trailer)
        f.Close()
    

    ### Get XS
# Load Producton Cfg + check
    CMSSW=os.environ["CMSSW_BASE"]
    if os.path.exists(CMSSW+'/src/'+prodCfg) :
      handle = open(CMSSW+'/src/'+prodCfg)
      exec(handle)
      handle.close()
      prodList =  Productions.keys() 
    #   print(prodList)  
    else:
      print 'ERROR: Please specify the input data config'
      exit(1)
    if not iProd in prodList:
      print 'ERROR: iProd not in prodList: ',prodList 

    # Load X-section
    xsDB = xsectionDB()
    xsDB.readPython(CMSSW+'/src/'+Productions[iProd]['xsFile'])
    xsDB.readYR(Productions[iProd]['YRver'][0],Productions[iProd]['YRver'][1])

    # Get x-sections + checks
    xs = []
    if   '_ext' in TreeName : TreeNameXS = TreeName.split('_ext')[0]
    elif '-ext' in TreeName : TreeNameXS = TreeName.split('-ext')[0]
    else:                    TreeNameXS = TreeName
    xs.append( xsDB.get(TreeNameXS) )
    for iEntry in range(len(xs)):
      if not xs[iEntry] == xs[0] :
        print 'ERROR: getBaseW: Trying to mix samples with different x-section'
        exit()
    print(xs)

    ### AND NOW: Compute new baseW
    # print("tree: ", TreeName)

    nEvt = genEventSumw
    # print("nEvt: ", nEvt)
    Xsec  = xsDB.get(TreeNameXS)
    ## if no xs is found, set it to 1
    if Xsec == '':
        Xsec = 1000000.
    baseW = float(Xsec)*1000./nEvt
    lumi = 1./baseW
    # print("lumi: ", lumi)

    return lumi


def getListMC(samples):
    _MClist = []
    for key in samples.keys():
        if key != 'DATA' and key != 'Fake':
            for smp in samples[key]['name']:
                _MClist.append(smp)
    return _MClist

def GetTree(MClist):
    samples_name = []
    for iFile in range(len(MClist)):
        Tree = MClist[iFile].split("/")[-1].split("__")[0].split("nanoLatino_")[-1]
        if Tree not in samples_name:
            samples_name.append(Tree)
    return samples_name


if __name__ == '__main__':
    samplesCfg = "PlotsConfigurations/Configurations/VBF_W/2018/UL/samples.py"
    CMSSW=os.environ["CMSSW_BASE"]

    if os.path.exists(CMSSW+'/src/'+samplesCfg) :
        handle = open(CMSSW+'/src/'+samplesCfg)
        exec(handle)
        handle.close()
    else :
        print "!!! ERROR file ", samplesCfg, " does not exist."
        exit()

    MClist = getListMC(samples)
    MCTreeslist = GetTree(MClist)
    # print(MCTreeslist)
    # print(MClist)
    lumi_dict = {}

    for tree in MCTreeslist:
        # print("tree: ", tree)
        lumi = getLumi(tree, "Summer20UL18_106x_nAODv9_Full2018v9")
        ## fill the dictionary
        lumi_dict[tree] = lumi

    ## print the dictionary in a txt file
    with open("UL/lumi_dict2018.txt", "w") as f:
        f.write(str(lumi_dict))

    # print(getLumi("WLNuJJ_EWK", "Autumn18_102X_nAODv7_Full2018v7"))
    # print(getLumi("EWK_LNuJJ", "Summer16_102X_nAODv7_Full2016v7"))

    # print(getLumi('DYJetsToLL_M-50', "Autumn18_102X_nAODv7_Full2018v7"))
    # print("bellaaaa")
    # print(getLumi('DYJetsToLL_M-50_ext2', "Autumn18_102X_nAODv7_Full2018v7"))
    # print("bellaaaa")
    # print(1./float(getBaseWnAOD(mcPrivateDirectory,'Autumn18_102X_nAODv7_Full2018v7',['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext2'])))







