import os
import argparse
import yaml
import json
import logging
import re
import ROOT as R
import numpy as np
import CombineHarvester.CombineTools.plotting as plot

ranges = {
    'k_cW': [-1,1],
    'k_cHB': [-20,20],
    'k_cHQ1': [-100,100],
    'k_cHW': [-5,5],
    'k_cHWB': [-10,10],
    'k_cHbox': [-30,30],
    'k_cHj1': [-2,2],
    'k_cHl1': [-120,120]
}

priors = {
    'k_cW': 50,
    'k_cHB': 50,
    'k_cHQ1': 50,
    'k_cHW': 50,
    'k_cHWB': 50,
    'k_cHbox': 10,
    'k_cHj1': 50,
    'k_cHl1': 50
}

parser = argparse.ArgumentParser()
parser.add_argument("-c","--config", help="Config file" , type=str)
parser.add_argument("-o","--outputdir", help="Output folder", type=str)
parser.add_argument("-pois","--pois", help="POIs you want to fit can be one or list separated by space", type=str, nargs="+", required=True)
parser.add_argument("-fr","--freeze", help="POIs you want to freeze as a space-separated list", type=str, nargs="+", required=False, default = [])
parser.add_argument("-prof", help="Specify --floatOtherPOIs", action="store_true", default=False)
parser.add_argument("-of","--outputfile", help="Output file for plot/graph command", type=str, default="scans_EFT.root")
parser.add_argument("-ofr","--outputfileranges", help="Output file for ranges", type=str, default="ranges.txt")
parser.add_argument("-p","--process", help="Process to run [scan, hadd, graph, interval]", type=str)
parser.add_argument("--mc-asimov", action="store_true", default=False)
parser.add_argument("--data-asimov", action="store_true", default=False)
parser.add_argument("--data-unblind", action="store_true", default=False)
parser.add_argument("--dry", action="store_true", help="Do not run, only create script", default=False)
parser.add_argument("--doLocal", action="store_true", help="Do not run in Batch, run in local", default=False)
parser.add_argument("--doNotSaveFunc", action="store_true", help="Do not specify --saveSpecifiedFunc", default=False)
parser.add_argument("--doNotSaveRateParam",action="store_true",  help="Do not add rateparam to output", default=False)
parser.add_argument("-fo","--fit-options", help="Robust fit options 0,1,2", type=int, default=0)
parser.add_argument("-q","--queue", help="Queue", type=str,default="tomorrow")
parser.add_argument("-v","--verbose", help="Combine verbosity level", type=int, default=0)
parser.add_argument("--points", help="Points", type=int,default=200)
parser.add_argument("--prior", help="Float specifying the prior for profiled operators", type=float,default=None)
parser.add_argument("--split", help="Split", type=int,default=5)
parser.add_argument("--rMin", help="Min for scan", type=float,default=0)
parser.add_argument("--rMax", help="Max for scan", type=float,default=1.5)
parser.add_argument("--skip-initial", action="store_true", help="skip initial fit", default=False)
parser.add_argument("--clean", help="Remove previous scan point root files", action="store_true", default=False)
parser.add_argument("--randomPoints", help="Random start points for MultiDim", type=int,default=0)
parser.add_argument("--rangeFactor", help="Factor to scale current ranges", type=int,default=1)
args = parser.parse_args()


fact = args.rangeFactor
for key in ranges.keys():
   ranges[key][0]*=fact
   ranges[key][1]*=fact

if args.config.endswith(".yaml"):
    config = yaml.load(open(args.config))
elif args.config.endswith(".json"):
    config = json.load(open(args.config))
else: 
    print("Error! No valid input file")
    exi(1)


fitter_options= { 
    0:  "--robustFit=1 --setRobustFitTolerance=0.1 --cminDefaultMinimizerStrategy=0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --stepSize=0.01 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND",
    1:  "--robustFit=1 --setRobustFitTolerance=0.2 --cminDefaultMinimizerStrategy=0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2 --stepSize=0.005 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND",
    2:  "--robustFit=1 --setRobustFitTolerance=0.3 --cminDefaultMinimizerStrategy=0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999 --cminFallbackAlgo Minuit2,Migrad,0:0.3 --stepSize=0.001 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND",
    3:  "--cminDefaultMinimizerStrategy=0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999 --cminFallbackAlgo Minuit2,Migrad,0:0.5 --stepSize=0.005 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND",
    4: "--cminDefaultMinimizerStrategy=0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999 --cminFallbackAlgo Minuit2,Migrad,0:0.8 --stepSize=0.01 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND"

   }


file_name = "_".join(i for i in args.pois)
if len(args.freeze) > 0:
   file_name += "_freeze_" + "_".join(i for i in args.freeze)

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
#    cmd.append("source /cvmfs/cms.cern.ch/cmsset_default.sh")
#    cmd.append("eval `scramv1 runtime -sh`") 
    cmd.append("cp {0} {1}/combined.root".format(workspace, outdir))
    cmd.append("cd "+ outdir)
    cmd.append("echo '{}' > log.txt".format("Initial dir: "+ outdir))

    range_str = ""
    for p in args.pois:
       print(p)
       range_str += p + "={0},{1}:".format(ranges[p][0], ranges[p][1])
    # delete last :
    if args.prof or len(args.freeze) > 0:
        for key, _ in ranges.items():
            if key not in args.pois and key not in args.freeze:
                range_str += key + "=-{0},{0}:".format(args.prior if args.prior else priors[key])
                
    range_str = range_str[:-1]
    saveFunc = ""
    redefinepoi = ",".join(i for i in args.pois)
    floatpoi = ""

    if not args.doNotSaveFunc:
        # --saveSpecifiedNuis=all
        saveFunc = " --saveSpecifiedFunc=r"

        if args.prof:
           saveFunc += "," + ",".join(key for key in ranges.keys())
           redefinepoi = ",".join(key for key in ranges.keys())
           floatpoi = " --floatOtherPOIs=1 "

        if not args.doNotSaveRateParam:
            rp = []
            # retrieve rate params
            dfile = open(datac["datacard"], "r")
            cont = dfile.readlines()
            
            # search for the rate params:
            for line in cont:
                if "rateParam" not in line: continue
                cleanline = a = [i for i in line.split(" ") if i]
                rp.append(cleanline[0])

            saveFunc += "," + ",".join(rp)

    randomPoints = ""
    if args.randomPoints: randomPoints = " --pointsRandProf=" + str(args.randomPoints) + " "

    print("----> " + randomPoints)
    # Prepare the script to create the impacts
    if not args.skip_initial:
        cmd.append("""combine -M MultiDimFit --saveWorkspace -n .{5}.initialFit \
                    combined.root {0} {1} -v {2} -m 125 --redefineSignalPOI {3} -P {7} --setParameterRanges {4} {6} {8}""".format(toysf,
                        fitter_options[args.fit_options], args.verbose, redefinepoi, range_str, file_name, saveFunc, ",".join(i for i in args.pois), floatpoi))
    if args.clean:
        cmd.append("rm higgsCombine.{0}.scan_all.POINTS*".format("_".join(i for i in args.pois)))

    if not args.doLocal:
        cmd.append("""combineTool.py -M MultiDimFit -m 125  higgsCombine.{0}.initialFit.MultiDimFit.mH125.root -n .{0}.scan_all --redefineSignalPOI {11} -P {13} \
                    --setParameterRanges {1}  --snapshotName MultiDimFit  \
                    {2} --algo grid  {4} \
                    --split-points={9} --job-mode=condor --task-name {8} \
                    --sub-opts='+JobFlavour="{5}"' -v {6} {7} {10} --points={3} {12} {14}""".format(file_name, range_str, toysf, args.points,
                            fitter_options[args.fit_options],args.queue, args.verbose, "--dry-run" if args.dry else "",
                            datac["datacard_name"] + "_" + "_".join(i for i in args.pois), args.split, saveFunc, redefinepoi, randomPoints, ",".join(i for i in args.pois), floatpoi) )

    else:
        cmd.append("""combine -M MultiDimFit -m 125  higgsCombine.{0}.initialFit.MultiDimFit.mH125.root -n .{0}.scan_all.POINTS --redefineSignalPOI {7} -P {9} \
                    --setParameterRanges {1}  --snapshotName MultiDimFit  \
                    {2} --algo grid  {4} -v {5} {6} --points={3} {8} {10}""".format(file_name, range_str, toysf, args.points,
                            fitter_options[args.fit_options], args.verbose, saveFunc, redefinepoi, randomPoints, ",".join(i for i in args.pois), floatpoi))

        # move the file with the expected hadd name so that we can reuse other functions
        cmd.append("""mv higgsCombine.{0}.scan_all.POINTS.MultiDimFit.mH125.root higgsCombine.{0}.scan_all.POINTS.root""".format(file_name))

    with open("{}/script_preparation_{}.sh".format(outdir, file_name), "w") as of:
        of.write("\n\n".join(cmd))

    if not args.dry:
        os.system("sh {}/script_preparation_{}.sh".format(outdir, file_name))
    else:
        f_log = open(outdir + "/commands.txt", "w")
        for c in cmd: 
            f_log.write(c)
            f_log.write("\n\n")
        log.info(cmd)

##############################################

def do_hadd(datac):    
    log = logging.getLogger(datac["datacard_name"])
    outdir = datac["outputdir"] 
    workspace = datac['workspace']
    cmd = [ ]
    cmd.append("cd "+ outdir)
    # Prepare the script to create the impacts
    cmd.append("hadd -f higgsCombine.{0}.scan_all.POINTS.root  higgsCombine.{0}.scan_all.POINTS.*.MultiDimFit.mH125.root".format(file_name))
    
    with open("{}/script_preparation_hadd_{}.sh".format(outdir, file_name), "w") as of:
        of.write("\n\n".join(cmd))

    if not args.dry:
        os.system("sh {}/script_preparation_hadd_{}.sh".format(outdir, file_name))

############################################

def do_graph(datac, outputfile):
    log = logging.getLogger(datac["datacard_name"])
    outdir = datac["outputdir"] 
    workspace = datac['workspace']
    log.info("Getting graph: "+ datac['datacard_name'])
    file = R.TFile.Open(outdir + "/higgsCombine.{0}.scan_all.POINTS.root".format(file_name))
    tree = file.Get("limit")
    # gr = plot.TGraphFromTree(tree, "r", "2*deltaNLL","")
    tree.Draw("{}:2*deltaNLL".format(":".join(args.pois)),"","goff")
    
    N = tree.GetSelectedRows()
    x = np.ndarray((N), 'd', tree.GetV1())[1:]
    y = np.ndarray((N), 'd', tree.GetV2())[1:]

    gr = R.TGraph(x.size, x, y)
    gr.SetMarkerStyle(8)
    gr.SetMarkerColor(R.kBlack)
    gr.SetLineWidth(2)
    gr.SetLineColor(R.kBlack)

    if args.data_asimov:
        gr.SetName(datac["datacard_name"] + "_dataasimov")
        gr.SetTitle(datac["datacard_name"] + "_dataasimov")
    if args.mc_asimov:
        gr.SetName(datac["datacard_name"] + "_mcasimov")
        gr.SetTitle(datac["datacard_name"] + "_mcasimov")
    if args.data_unblind:
        gr.SetName(datac["datacard_name"] + "_data")
        gr.SetTitle(datac["datacard_name"] + "_data")

    if file_name not in [i.GetName() for i in outputfile.GetListOfKeys()]:
        outputfile.mkdir(file_name)

    outputfile.cd(file_name)
    gr.Write( datac['datacard_name'] )

    outputfile.Write()
    #gr.Write(file_name + "/" + datac['datacard_name'])

    # Save scans in pdf and png
    os.system("mkEFTScan.py {0} -ff png pdf -p {1} -maxNLL 5 -o {2}/{3}_{4} ".format(
        outdir + "/higgsCombine.{0}.scan_all.POINTS.root -cms -preliminary -energy 13 -lumi 59.74".format(file_name), 
        " ".join(args.pois),
        outdir,
        datac['datacard_name'],
        file_name
    ))

#############################################

def getLSintersections (graphScan, val):

    xings = []
    n = graphScan.GetN ()
    x = list(graphScan.GetX ())
    y = list(graphScan.GetY ())
    x, y = zip(*sorted(zip(x, y)))
    found = False

    for i in range(n):
        if (y[i] == val):
            xings.append(x[i])
            continue
        if i > 0:
            if ((y[i] - val) * (y[i-1] - val) < 0):
                xings.append(x[i-1] +  abs ((y[i-1] - val) * (x[i] - x[i-1]) / (y[i] - y[i-1])) )

    if len(xings) == 0:
        print("@ @ @ WARNING @ @ @: returning graph x-axis range limits")
        xings.append(graphScan.GetXaxis ().GetXmin ()) 
        xings.append(graphScan.GetXaxis ().GetXmax ())
    
    elif len(xings) == 1:
        if (xings[0] < 0):
            print("@ @ @ WARNING @ @ @: returning graph x-axis higher limit")
            xings.append(graphScan.GetXaxis().GetXmax ()) 
        else :
            print("@ @ @ WARNING @ @ @: returning graph x-axis lower limit")
            xings.append (xings[0])
            xings[0] = graphScan.GetXaxis ().GetXmin ()
            
    if len(xings) > 2:
        print("@ @ @ WARNING @ @ @: more than two intersections found, returning the first two")
        xings = xings[:2]

    return xings


def do_getinterval(datac, outfile_graph, outputfile):

    outdir = datac["outputdir"] 
    log.info("Getting interval: "+ datac['datacard_name'])

    ranges = {}

    f_out = open(outputfile, "a")

    d = outfile_graph.Get(file_name)

    for graphname in [i.GetName() for i in d.GetListOfKeys()]:
        
        ranges[graphname] = {}

        graphScan = d.Get(graphname)
        ranges[graphname]["ones"] = getLSintersections(graphScan, 1.0)
        ranges[graphname]["twos"] = getLSintersections(graphScan, 3.84)

        #print(graphname, ranges[graphname]["ones"], ranges[graphname]["twos"])

    f_out.write("[{}]\n".format(file_name))
    for key, items in ranges.items():
        f_out.write("{} \t [{:.3f},{:.3f}] \t [{:.3f},{:.3f}]\n".format(
            key,
            items["ones"][0],
            items["ones"][1],
            items["twos"][0],
            items["twos"][1]
        ))

#############################################

if args.process == "graph" or args.process == "interval":
    if args.outputfile:
        outfile_graph = R.TFile(args.outputfile, "UPDATE")
    else:
        print("Please specify --outputfile")
        exit(1)

for datac in config:
    datac['workspace'] = args.outputdir + "/" + datac["datacard_name"] + "/combined_{}.root".format(datac["datacard_name"])
    datac['datacard'] = args.outputdir + "/" + datac["datacard_name"] + "/combined_{}.txt".format(datac["datacard_name"]) 
    outdir = args.outputdir + "/" + datac["datacard_name"] + "/likelihood_scan"

    print(datac['workspace'])
    print(datac['datacard'])

    if args.data_asimov:
        toysf = "-t -1 --toysFreq --setParameters r=1" 
        toysf += ","
        for op in args.pois:
            toysf += op + "=0,"
        if args.prof or len(args.freeze) > 0:
           for op in ranges.keys(): 
              if op not in args.pois: toysf += op + "=0,"

        toysf = toysf[:-1] + " "

        toysf += " --freezeParameters r"
        if len(args.freeze) > 0: 
           toysf += "," + ",".join(i for i in args.freeze)

        outdir += "_data_asimov"
    elif args.mc_asimov:
        toysf = "-t -1 --setParameters r=1"
        toysf += ","
        for op in args.pois:
            toysf += op + "=0,"
        if args.prof or len(args.freeze) > 0:
           for op in ranges.keys(): 
              if op not in args.pois: toysf += op + "=0,"

        toysf = toysf[:-1] + " "

        toysf += " --freezeParameters r"
        if len(args.freeze) > 0: 
           toysf += "," + ",".join(i for i in args.freeze)
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



if args.process == "interval":
    do_getinterval(datac, outfile_graph, args.outputfileranges)

if args.process == "graph":
    outfile_graph.Close()
