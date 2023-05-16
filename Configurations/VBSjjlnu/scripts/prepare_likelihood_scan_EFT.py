import os
import argparse
import yaml
import json
import logging
import re
import ROOT as R
import CombineHarvester.CombineTools.plotting as plot

ranges = {
    'k_cW': [-50,50],
    'k_cHB': [-50,50],
    'k_cHQ1': [-50,50],
    'k_cHW': [-50,50],
    'k_cHWB': [-50,50],
    'k_cHbox': [-50,50],
    'k_cHj1': [-50,50],
    'k_cHl1': [-50,50]
}

parser = argparse.ArgumentParser()
parser.add_argument("-c","--config", help="Config file" , type=str)
parser.add_argument("-o","--outputdir", help="Output folder", type=str)
parser.add_argument("-pois","--pois", help="POIs you want to fit can be one or list separated by space", type=str, nargs="+", required=True)
parser.add_argument("-fr","--freeze", help="POIs you want to freeze as a space-separated list", type=str, nargs="+", required=False)
parser.add_argument("-prof", help="Specify --floatOtherPOIs", action="store_true", default=False)
parser.add_argument("-of","--outputfile", help="Output file for plot/graph command", type=str)
parser.add_argument("-p","--process", help="Process to run [scan, hadd, graph, interval]", type=str)
parser.add_argument("--mc-asimov", action="store_true", default=False)
parser.add_argument("--data-asimov", action="store_true", default=False)
parser.add_argument("--data-unblind", action="store_true", default=False)
parser.add_argument("--dry", action="store_true", help="Do not run, only create script", default=False)
parser.add_argument("-fo","--fit-options", help="Robust fit options 0,1,2", type=int, default=0)
parser.add_argument("-q","--queue", help="Queue", type=str,default="microcentury")
parser.add_argument("-v","--verbose", help="Combine verbosity level", type=int, default=0)
parser.add_argument("--points", help="Points", type=int,default=200)
parser.add_argument("--split", help="Split", type=int,default=5)
parser.add_argument("--rMin", help="Min for scan", type=float,default=0)
parser.add_argument("--rMax", help="Max for scan", type=float,default=1.5)
parser.add_argument("--skip-initial", action="store_true", help="skip initial fit", default=False)
parser.add_argument("--clean", help="Remove previous scan point root files", action="store_true", default=False)
args = parser.parse_args()


if args.config.endswith(".yaml"):
    config = yaml.load(open(args.config))
elif args.config.endswith(".json"):
    config = json.load(open(args.config))
else: 
    print("Error! No valid input file")
    exi(1)


fitter_options= { 
    0:  "--robustFit=1 --setRobustFitTolerance=0.1 --cminDefaultMinimizerStrategy=0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --stepSize=0.01 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND",
    1:  "--robustFit=1 --setRobustFitTolerance=0.2 --cminDefaultMinimizerStrategy=0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2 --stepSize=0.005 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND",
    2:  "--robustFit=1 --setRobustFitTolerance=0.3 --cminDefaultMinimizerStrategy=0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.3 --stepSize=0.001 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND",
   
   }

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s: %(message)s',\
                     datefmt = '%m/%d/%Y %I:%M:%S %p')

def create_logger(name, file):
    l = logging.getLogger(name)
    # Console logger to INFO
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)
    # l.addHandler(ch)
    # File handler Debug
    logfile = logging.FileHandler(file, 'a')
    logfile.setLevel(logging.DEBUG)
    form = logging.Formatter(fmt = '%(asctime)s - %(levelname)s: %(message)s',
                                        datefmt = '%m/%d/%Y %I:%M:%S %p')
    logfile.setFormatter(form)
    l.addHandler(logfile)

########################################
def do_scan(datac):    
    log = logging.getLogger(datac["datacard_name"])
    outdir = datac["outputdir"] 
    workspace = datac['workspace']
    cmd = []  
    print(workspace) 
    cmd.append("cp {0} {1}/combined.root".format(workspace, outdir))
    cmd.append("cd "+ outdir)
    cmd.append("echo '{}' > log.txt".format("Initial dir: "+ outdir))

    range_str = ""
    for p in args.pois:
       print(p)
       range_str += p + "={0},{1}:".format(ranges[p][0], ranges[p][1])
    # delete last :
    range_str = range_str[:-1]

    # Prepare the script to create the impacts
    if not args.skip_initial:
        cmd.append("""combine -M MultiDimFit --saveWorkspace -n .{5}.initialFit \
                    combined.root {0} {1} -v {2} -m 125 --redefineSignalPOIs {3} --setParameterRanges {4} {6} {7}""".format(toysf,
                        fitter_options[args.fit_options], args.verbose, ",".join(i for i in args.pois), range_str, "_".join(i for i in args.pois), 
                        "" if not args.prof else " --floatOtherPOIs=1",  "" if args.freeze is None else ",".join(i for i in args.freeze)))
    if args.clean:
        cmd.append("rm higgsCombine.{0}.scan_all.POINTS*".format("_".join(i for i in args.pois)))
    cmd.append("""combineTool.py -M MultiDimFit higgsCombine.{0}.initialFit.MultiDimFit.mH125.root -n .{0}.scan_all \
                --setParameterRanges {1}  --snapshotName MultiDimFit  \
                {2} --algo grid --point {3} {4} \
                --split-points={9} --job-mode=condor --task-name {8} \
                --sub-opts='+JobFlavour="{5}"' -v {6} {7} {10} {11}""".format("_".join(i for i in args.pois), range_str, toysf, args.points,
                        fitter_options[args.fit_options],args.queue, args.verbose, "--dry-run" if args.dry else "",
                        datac["datacard_name"], args.split, "" if not args.prof else "--floatOtherPOIs=1 ",  "" if args.freeze is None else ",".join(i for i in args.freeze)))

    with open("{}/script_preparation.sh".format(outdir), "w") as of:
        of.write("\n\n".join(cmd))

    if not args.dry:
        os.system("sh {}/script_preparation.sh".format(outdir))
    else:
        log.info(cmd)

##############################################

def do_hadd(datac):    
    log = logging.getLogger(datac["datacard_name"])
    outdir = datac["outputdir"] 
    workspace = datac['workspace']
    cmd = [ ]
    cmd.append("cd "+ outdir)
    # Prepare the script to create the impacts
    cmd.append("hadd -f higgsCombine.{0}.scan_all.POINTS.root  higgsCombine.{}.scan_all.POINTS.*.MultiDimFit.mH125.root".format("_".join(i for i in args.pois)))
    
    with open("{}/script_preparation_hadd.sh".format(outdir), "w") as of:
        of.write("\n\n".join(cmd))

    if not args.dry:
        os.system("sh {}/script_preparation_hadd.sh".format(outdir))

############################################

def do_graph(datac, outputfile):
    log = logging.getLogger(datac["datacard_name"])
    outdir = datac["outputdir"] 
    workspace = datac['workspace']
    log.info("Getting graph: "+ datac['datacard_name'])
    file = R.TFile.Open(outdir + "/higgsCombine.scan_all.POINTS.root")
    tree = file.Get("limit")
    # gr = plot.TGraphFromTree(tree, "r", "2*deltaNLL","")
    tree.Draw("r:2*deltaNLL","","goff")
    x = tree.GetV1()
    y = tree.GetV2()
    N = tree.GetSelectedRows()
    gr = R.TGraph(N)
    for i in range(N):
        print(i,x[i], y[i])
        gr.SetPoint(i, x[i], y[i])
    if args.data_asimov:
        gr.SetName(datac["datacard_name"] + "_dataasimov")
        gr.SetTitle(datac["datacard_name"] + "_dataasimov")
    if args.mc_asimov:
        gr.SetName(datac["datacard_name"] + "_mcasimov")
        gr.SetTitle(datac["datacard_name"] + "_mcasimov")
    if args.data_unblind:
        gr.SetName(datac["datacard_name"] + "_data")
        gr.SetTitle(datac["datacard_name"] + "_data")
    outputfile.cd()
    gr.Write()

#############################################

def do_getinterval(datac, outputfile):
    outdir = datac["outputdir"] 
    log.info("Getting interval: "+ datac['datacard_name'])

    print(os.getcwd())
    print("python scripts/fit_results_tools/get_likelihood_scan_crossing.py {}/higgsCombine.scan_all.POINTS.root {} >> {}".format(datac["outputdir"], datac["datacard_name"], outputfile))    
    os.system("python scripts/fit_results_tools/get_likelihood_scan_crossing.py {}/higgsCombine.scan_all.POINTS.root {} >> {}".format(datac["outputdir"], datac["datacard_name"], outputfile))

#############################################

if args.process == "graph":
    if args.outputfile:
        outfile_graph = R.TFile(args.outputfile, "UPDATE")
    else:
        print("Please specify --outputfile")
        exit(1)

for datac in config:
    datac['workspace'] = args.outputdir + "/" + datac["datacard_name"] + "/combined_{}.root".format(datac["datacard_name"]) 
    outdir = args.outputdir + "/" + datac["datacard_name"] + "/likelihood_scan"

    if args.data_asimov:
        toysf = "-t -1 --toysFreq --setParameters r=1 --freezeParameters r"
        outdir += "_data_asimov"
    elif args.mc_asimov:
        toysf = "-t -1 --setParameters r=1 --freezeParameters r"
        outdir += "_mc_asimov"
    elif args.data_unblind:
        toysf = ""
        outdir += "_data"
    else:
        toysf = ""

    datac["outputdir"] = outdir 

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    create_logger(datac["datacard_name"], outdir+"/log.txt")
    log = logging.getLogger(datac["datacard_name"])
    if args.dry: log.info("Working in dry mode, no commands executed")
    
    log.info(">>>>>>>>>>>>>>>>>> Starting new run")

    log.info("Preparing datacard: "+ datac["datacard_name"])
    # start scan
    if args.process == "scan":
        do_scan(datac)
    elif args.process == "hadd":
        do_hadd(datac)
    elif args.process == "graph":
        do_graph(datac, outfile_graph)
    elif args.process == "interval":
        do_getinterval(datac, args.outputfile)


if args.process == "graph":
    outfile_graph.Close()
