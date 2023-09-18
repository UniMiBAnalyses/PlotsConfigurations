import os
import argparse
from itertools import combinations
import numpy as np
from copy import copy
import CombineHarvester.CombineTools.plotting as plot


parser = argparse.ArgumentParser()
parser.add_argument("-c","--config", help="Config file" , type=str)
parser.add_argument("-o","--outputdir", help="Output folder", type=str)
parser.add_argument("-pois","--pois", help="All POIs you want to 2d fit", type=str, nargs="+", required=True)
parser.add_argument("--mc-asimov", action="store_true", default=False)
parser.add_argument("--data-asimov", action="store_true", default=False)
parser.add_argument("--data-unblind", action="store_true", default=False)
parser.add_argument("-p","--process", help="Process to run [scan, hadd, graph, interval]", type=str)
parser.add_argument("--doLocal", action="store_true", help="Do not run in Batch, run in local", default=False)
parser.add_argument("--dry", action="store_true", help="do dry run", default=False)
parser.add_argument("--split", help="Split", type=int,default=5)
args = parser.parse_args()

if __name__ == "__main__":

    if len(args.pois) < 2: 
        print("[ERROR] Provide more than 2 ops")
        sys.exit(0)

    commands = []

    cmd = "python scripts/prepare_likelihood_scan_EFT.py -v 1 -fo 1 --points 2000  -c " + \
            args.config + " -o " + args.outputdir +  " -p " + args.process + \
            " --split {}".format(args.split) + " "

    if args.doLocal: cmd += " --doLocal "
    if args.mc_asimov: cmd += " --mc-asimov "
    if args.data_asimov: cmd += " --data-asimov "
    if args.data_unblind: cmd += " --data-unblind "
    if args.dry: cmd += " --dry "



    # now add the pois
    combo = list(combinations(args.pois, 2))

    for poi_pair in combo:

        c = copy(cmd)
        c += " -pois " + " ".join(i for i in poi_pair)
        if len(args.pois) > 2:
            c += " -fr " + " ".join(i for i in args.pois if i not in poi_pair)

        commands.append(c)

    for c in commands:
        os.system(c)
