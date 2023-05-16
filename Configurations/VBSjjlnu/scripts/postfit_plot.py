from __future__ import print_function
import yaml
import json
import argparse
import sys
import os
import subprocess
import condor_prep
import random
from glob import glob

def convertAbs(path):
   if path.startswith("/"): return path
   else: return os.getcwd() + "/" + path 

parser = argparse.ArgumentParser()
parser.add_argument("-c","--config", help="configuration file as json and yaml with configuration of dc combiantions", type=str)
parser.add_argument("-d","--datacards", help="Datacard names, only process these", type=str, nargs="+")
parser.add_argument("-b","--basedir", help="Baseline folder to start from", type=str)
parser.add_argument("-o","--outputdir", help="Output folder, create if not present", type=str)
parser.add_argument("-i","--inputfile", help="Input root file with prefit shapes from output of mkShapesMulti", type=str)
parser.add_argument("--signal-from-prefit", action="store_true", default=False)
parser.add_argument("--plot-config", help="Path of plot configuration.py", required=True, type=str)
parser.add_argument("--region-name", help="Combine region in the datacard to plot", required=False, type=str)
parser.add_argument("--year", help="Year", required=True, type=str)
parser.add_argument("--debug", help="Debug", required=False, action="store_true")
parser.add_argument("--dry", help="Do not run, only print commands", required=False, action="store_true")
parser.add_argument("--skipmkPostFit", help="Skip running of mkPostFitPlot and just runs mkPlot", required=False, action="store_true")
args = parser.parse_args()

#Loading plot configuration
exec(open(args.plot_config))

if args.config.endswith(".yaml"):
    config = yaml.load(open(args.config))
elif args.config.endswith(".json"):
    config = json.load(open(args.config))
else: 
    print("Error! No valid input file")
    exi(1)

################################################################################## 
def post_fit_plots(datac):
    print(">Running post fit plots")
    if args.plot_config == None: 
        print("> ERROR: Missing --plot-config!")
        return

    plotbasedir = os.path.dirname(args.plot_config)
    basedircomb = os.getcwd() +"/"+ args.basedir + "/" + datac["datacard_name"]

    print(basedircomb)    
    fit_file = glob(basedircomb + "/" + "fitDiag*.root")[0]
    cmds = []

    prefit_file =  convertAbs(args.inputfile)
    fit_file    =  convertAbs(fit_file)
    plotbasedir =  convertAbs(plotbasedir)

    if args.outputdir and not os.path.isdir(args.outputdir):
       try:
          os.mkdir(args.outputdir)
       except:
          pass


    plot_path = "/".join(i for i in args.plot_config.split("/")[1:-1])
    plot_path = basedircomb
    if len(plot_path) == 0: plot_path = "."
    plot_path = plot_path + "/" + outputDir if args.outputdir == None else plot_path + "/" + args.outputdir

    if not os.path.isdir(plot_path): os.mkdir(plot_path)

    combconf = None
    for combconf in datac["phase_spaces"]:
        # The baseline is to plot all regions and variables
        # If not specified
        if args.region_name != None and combconf["name"] != args.region_name: continue 

        print("Post fit of variable {}, cut {}".format(combconf["var"], combconf["cut"]))

        cmdpost1 = "cd " + plotbasedir

        if not args.skipmkPostFit:        
           # With kind=b the shapes of post-fit bkg-only fit are saved
           cmdpost1 = """cd {8};\\
               mkPostFitPlot.py --inputFileCombine={0} \\
               --outputFile={1}/postfit_latino_{2}.root --variable {3} \\
               --cutNameInOriginal={4} --cut={5} \\
               --inputFile={6} --kind=s --pycfg={7}  \\
               --getSignalFromPrefit={9} ;""".format(
                   fit_file,
                   plot_path,
                   datac["datacard_name"],
                   combconf["var"],
                   combconf["cut"],
                   combconf["name"] + "_"+args.year, #cut name in the datacard
                   prefit_file,
                   args.plot_config.split("/")[-1],
                   plotbasedir,
                   int(args.signal_from_prefit)
               )

        print(plotbasedir, outputDirPlots, combconf["name"])
        if not os.path.exists(plotbasedir+ "/"+ outputDirPlots+"/"+combconf["name"]):
            os.makedirs(plotbasedir+ "/"+ outputDirPlots+"/"+combconf["name"])
        
        # The samples are plotted with postfit shapes, the pre-fit ratio is added
        # --plotFile={6}
        cmdpost2 = """mkPlot.py  --pycfg={0} \\
            --inputFile={1}/postfit_latino_{2}.root \\
            --showIntegralLegend=1 --showRelativeRatio --plotNormalizedDistributions --minLogC 0.3 --maxLogC 1e2 \\
            --minLogCratio 0.3 --maxLogCratio 1e2 --postFit=p --outputDirPlots={3} \\
            --onlyVariable={4} --onlyCut={5}""".format(
                args.plot_config.split("/")[-1],
                plot_path, 
                datac["datacard_name"],
                outputDirPlots+"/"+combconf["name"],
                combconf["var"], combconf["cut"],
                plotFile+"_res_postfit.py" if "res" in combconf["cut"] else plotFile+"_boost_postfit.py", #####HACK!
            )
        cmds.append(cmdpost1)
        cmds.append(cmdpost2)
        if args.debug or args.dry: 
            print("----------------")
            print(cmdpost1)
            print(cmdpost2)
        if not args.dry: os.system("\n".join([cmdpost1, cmdpost2]))

    with open("{}/log_postfit_plots.txt".format(basedircomb), "w") as wf:
        wf.write("\n".join(cmds))
    print("DONE!")


print(len(config))

for datac in config:
    if args.datacards and datac["datacard_name"] not in args.datacards: continue
    # outdir = args.outputdir + "/" + datac["datacard_name"]
    # datac["outputdir"] = outdir
    # datac["fit_file"] = args.fitfile
    print("Preparing datacard: "+ datac["datacard_name"])
    
    post_fit_plots(datac)
