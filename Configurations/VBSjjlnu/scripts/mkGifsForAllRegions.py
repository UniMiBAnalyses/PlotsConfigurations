import os
import argparse
import ROOT 
import numpy as np
import ast
from glob import glob
from multiprocessing import Pool
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("-d","--directory", help="Direcotry output of prepare_datacards_EFT.py" , type=str, required=True)
parser.add_argument("-o","--output", help="output directory where to store the plots" , type=str, required=True)
parser.add_argument("--mc-asimov", action="store_true", default=False)
parser.add_argument("--data-asimov", action="store_true", default=False)
parser.add_argument("--data-unblind", action="store_true", default=False)
parser.add_argument("--dry", action="store_true", default=False)
parser.add_argument("--lumi", default="60", type=str, required=False)
parser.add_argument("--maxNLL", default="5", type=str, required=False)
parser.add_argument("--frequency", default="2", type=str, required=False)
parser.add_argument("--blind", default=[], required=False, nargs="+")
parser.add_argument("--noRateParam", default=False, required=False, action="store_true")
parser.add_argument("--doInitialFit", default=False, required=False, action="store_true")
args = parser.parse_args()

def drawGif(item):

    out_ = item["output"]
    dname = item["datacard"].split("/")[-1]

    cmds = []
    if not os.path.isfile(dname):
        cmds.append("cp {} . ".format(item["datacard"]))

    try:
        os.mkdir(out_ + "/" + item["var"])
        os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + out_ + "/" + item["var"])
    except:
        pass

    addrp = ""
    if not args.noRateParam:
        addrp = " -rp "

    blind = ""
    if args.blind:
        blind = " -blind "+  " ".join(i for i in args.blind) + " "

    out = out_ + "/" + item["var"] + "/" + item["op"]
    if not os.path.isdir(out): 
        os.mkdir(out)
        os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + out)


    cmds.append("mkEFTGifsRegions.py -d " + dname + " " + addrp + blind + " -s " + item["fit"] + " -op " + item["op"] + " -lumi " + args.lumi + " -maxNLL " + args.maxNLL + " -cms -preliminary -energy 13 -drawSigma -logy -frequency " + args.frequency + " -o " + out )

    if not args.dry:
        for command in cmds: os.system(command)
    else:
        print(cmds)


if __name__ == "__main__":

    if not os.path.isdir(args.directory):
        print("[ERROR] directory {} does not exist".format(args.output))
        sys.exit(0)

    try:
        os.mkdir(args.output)
    except: pass

    # variables = [i.split("/")[-1] for i in glob(args.directory + "/*")]

    outdir = args.directory + "/*/likelihood_scan"

    if args.data_asimov:
        outdir += "_data_asimov"
    elif args.mc_asimov:
        outdir += "_mc_asimov"
    elif args.data_unblind:
        outdir += "_data"

    
    if not args.doInitialFit: all_fits = glob(outdir + "/higgsCombine.*.scan_all.POINTS.root")
    else: all_fits = glob(outdir + "/higgsCombine.*.initialFit.MultiDimFit.mH125.root")

    infos = []
   
    # build info dict containing datacards, operator name and so on
    for fit_file in all_fits:
        op = fit_file.split(".")[1]
        # op = fit_file.split("higgsCombine.")[1].split(".scan_all.POINTS.root")[0]
        var = fit_file.split("/")[-3]
        datacard = glob("/".join(fit_file.split("/")[:-2]) + "/combined*.txt")
        if len(datacard) > 1: 
            print("[ERROR] Directory {} contains more than one datacard. clean".format("/".join(fit_file.split("/")[:-2])))
        datacard = datacard[0]

        infos.append(
            {
                "op": op,
                "var": var,
                "datacard": datacard,
                "fit": fit_file,
                "output": args.output
            }
        )
    
    nproc = len(infos) if len(infos) < 8 else 8
    pool = Pool(processes=nproc)
    pool.map(drawGif, infos)

    if not args.dry:
        for item in infos:
            dn = item["datacard"].split("/")[-1]
            os.system("rm " + dn )

