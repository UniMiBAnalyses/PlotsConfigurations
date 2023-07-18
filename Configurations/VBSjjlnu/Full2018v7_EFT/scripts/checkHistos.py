import os
import argparse
import ROOT 
import numpy as np
import ast
from glob import glob
from multiprocessing import Pool
import sys


# def checkHisto(files):
#     pass


# parser = argparse.ArgumentParser()
# parser.add_argument("-f","--file", help="The root file with Latino Histos" , type=str, required=True)
# parser.add_argument("-v","--variables", help="Only the variables.py file from latinos with variables definitions", required=True)
# parser.add_argument("-c","--cuts", help="Only the cuts.py file from latinos with cuts definitions", required=True)
# parser.add_argument("-o","--output", help="The output root file with the shapes", type=str, default="latinoShapesFromTrees.root")

# args = parser.parse_args()

if __name__ == "__main__":

    # if not os.path.isfile(args.variables):
    #     print("[ERROR] file {} does not exist".format(args.variables))

    # # check for the presence of the variable file
    # if not os.path.isfile(args.file):
    #     print("[ERROR] file {} does not exist".format(args.file))


    # variables = collections.OrderedDict()
    # cuts = collections.OrderedDict()

    # # read the cuts
    # if sys.version_info[0] == 2:
    #     execfile(args.cuts)
    # elif sys.version_info[0] == 3:
    #     exec(open(args.cuts).read())
    # else:
    #     print("[ERROR] Running with a python version different from 2 or 3")
    #     sys.exit(0)

    # # read the variables

    # if sys.version_info[0] == 2:
    #     execfile(args.variables)
    # elif sys.version_info[0] == 3:
    #     exec(open(args.variables).read())
    # else:
    #     print("[ERROR] Running with a python version different from 2 or 3")
    #     sys.exit(0)

    files = sys.argv[1]
    ls = glob(files + "/*.root")

    for idx, file_ in enumerate(ls):
        if idx % 100 == 0:
            print(str(idx) + "/" + str(len(ls)))
        f = ROOT.TFile(file_)
        if len([i.GetName() for i in f.GetListOfKeys()]) == 0:
            print("---> " + file_)
        for region in [i.GetName() for i in f.GetListOfKeys()]:
            d = f.Get(region)
            if len([i.GetName() for i in d.GetListOfKeys()]) == 0:
                print("---> " + file_ + " " + region)
            for variable in [i.GetName() for i in d.GetListOfKeys()]:
                v = d.Get(variable)

                if len([i.GetName() for i in v.GetListOfKeys()]) == 0:
                    print("---> " + file_ + " " + region + " " + variable)

                for shape in [i.GetName() for i in v.GetListOfKeys()]:
                    sh_ = v.Get(shape)

                    if sh_.GetEntries() == 0:
                        print("---> " + file_ + " " + shape)

    
