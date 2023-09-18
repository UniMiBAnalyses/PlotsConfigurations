import os
import argparse
import ROOT 
import numpy as np
import ast
from glob import glob
from multiprocessing import Pool
import itertools

def convertOpToLatex(op):
    d = {
        "k_cW": "c_{W}",
        "k_cHW": "c_{HW}",
        "k_cHbox": "c_{Hbox}",
        "k_cHB": "c_{HB}",
        "k_cHl1": "c_{H,l}^{(1)}",
        "k_cHj1": "c_{H,j}^{(1)}",
        "k_cHQ1": "c_{H,Q}^{(1)}"
    }

    if op in d.keys(): return d[op]
    else: return op

parser = argparse.ArgumentParser()
parser.add_argument("-d","--directory", help="Direcotry output of prepare_datacards_EFT.py" , type=str, required=True)
parser.add_argument("-o","--output", help="output directory where to store the plots" , type=str, required=True)
parser.add_argument("--mc-asimov", action="store_true", default=False)
parser.add_argument("--data-asimov", action="store_true", default=False)
parser.add_argument("--data-unblind", action="store_true", default=False)
parser.add_argument("--dry", action="store_true", default=False)
parser.add_argument("--lumi", default="60", type=str, required=False)
args = parser.parse_args()

def drawNuis(item):

    fit_ = item["fit"]
    out_ = item["output"]

    cmds = []

    try:
        os.mkdir(out_ + "/" + item["var"])
        os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + out_ + "/" + item["var"])
    except:
        pass

    out = out_ + "/" + item["var"] + "/" + item["op"]
    if not os.path.isdir(out): 
        os.mkdir(out)
        os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + out)

    out += "/" + item["op"] + "_" + item["branch"]


    cmds.append("mkEFTScan.py " +  fit_ + " -p " + item["op"] + " " + item["branch"] + " -isNuis -l " + args.lumi + " -xlabel " + \
                 convertOpToLatex(item["op"]) + " -energy 13 -cms -preliminary -o " + out)

    if not args.dry:
        for command in cmds: os.system(command)
    else:
        print(cmds)


if __name__ == "__main__":

    not_interesting_branches = ['limit', 'limitErr', 'mh', 'syst', 'iToy', 'iSeed', 'iChannel', 't_cpu', 't_real', 'quantileExpected', 'deltaNLL']

    if not os.path.isdir(args.directory):
        print("[ERROR] directory {} does not exist".format(args.output))
        sys.exit(0)

    try:
        os.mkdir(args.output)
    except: 
        pass

    # variables = [i.split("/")[-1] for i in glob(args.directory + "/*")]

    outdir = args.directory + "/*/likelihood_scan"

    if args.data_asimov:
        outdir += "_data_asimov"
    elif args.mc_asimov:
        outdir += "_mc_asimov"
    elif args.data_unblind:
        outdir += "_data"

    
    all_fits = glob(outdir + "/higgsCombine.*.scan_all.POINTS.root")

    infos = []
   
    # build info dict containing datacards, operator name and so on
    for fit_file in all_fits:
        op = fit_file.split(".")[1]
        var = fit_file.split("/")[-3]
        datacard = glob("/".join(fit_file.split("/")[:-2]) + "/combined*.txt")
        
        # retrieve branches
        f = ROOT.TFile(fit_file)
        t = f.Get("limit")
        branches_ = [i.GetName() for i in t.GetListOfBranches() if i.GetName() not in not_interesting_branches]

        for b_ in branches_:

            infos.append(
                {
                    "op": op,
                    "var": var,
                    "fit": fit_file,
                    "output": args.output,
                    "branch": b_
                }
            )
    
    nproc = len(infos) if len(infos) < 8 else 8
    pool = Pool(processes=nproc)
    pool.map(drawNuis, infos)