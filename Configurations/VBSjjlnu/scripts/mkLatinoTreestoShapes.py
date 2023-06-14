import json
import os
import argparse
import sys
import logging
from glob import glob
import collections
import ROOT
import numpy as np
from array import array


parser = argparse.ArgumentParser()
parser.add_argument("-f","--file", help="The root file with Latino Trees" , type=str, required=True)
parser.add_argument("-v","--variables", help="Only the variables.py file from latinos with variables definitions", required=True)
parser.add_argument("-c","--cuts", help="Only the cuts.py file from latinos with cuts definitions", required=True)
parser.add_argument("-o","--output", help="The output root file with the shapes", type=str, default="latinoShapesFromTrees.root")

args = parser.parse_args()

if __name__ == "__main__":

    # ROOT.EnableImplicitMT()

    # check for the presence of the variable file
    if not os.path.isfile(args.variables):
        print("[ERROR] file {} does not exist".format(args.variables))

    # check for the presence of the variable file
    if not os.path.isfile(args.file):
        print("[ERROR] file {} does not exist".format(args.file))


    variables = collections.OrderedDict()
    cuts = collections.OrderedDict()

    # read the cuts
    if sys.version_info[0] == 2:
        execfile(args.cuts)
    elif sys.version_info[0] == 3:
        exec(open(args.cuts).read())
    else:
        print("[ERROR] Running with a python version different from 2 or 3")
        sys.exit(0)

    # read the variables

    if sys.version_info[0] == 2:
        execfile(args.variables)
    elif sys.version_info[0] == 3:
        exec(open(args.variables).read())
    else:
        print("[ERROR] Running with a python version different from 2 or 3")
        sys.exit(0)

    # get tree names the dumb way

    trees = {}
    fIn = ROOT.TFile(args.file)
    for reg in cuts.keys():
        print(reg)
        d = fIn.Get(reg)
        trees[reg] = []
        v_names = [i.GetName() for i in d.GetListOfKeys()]
        for vn in v_names:
            d_t = d.Get(vn)
            for tn in [j.GetName() for j in d_t.GetListOfKeys()]:
                trees[reg].append(reg + "/" + vn + "/" + tn)
    

    # now process everything with root dataframes

    histos = {}

    # cycle on the cuts
    for cut in trees.keys():
        print(cut)

        histos[cut] = {}

        # cycle on the trees 
        for tree in trees[cut]:
            f = ROOT.RDataFrame(tree, args.file)
            sample = tree.split("/")[-1].split("tree_")[1]

            # cycle on the variables
            for var_name, definition in variables.items():

                range_ = definition["range"]
                tree_var_name = definition["name"]

                # end the cycle if this variable should not be built in this region
                if "cuts" in definition.keys() and cut not in  definition["cuts"]: continue 
                if tree_var_name not in f.GetColumnNames(): 
                    # check if this is an idexed list
                    if "[" in definition["name"] and "]" in definition["name"]:
                        tree_var_name =  definition["name"][:definition["name"].index("[")]
                        if tree_var_name not in f.GetColumnNames(): 
                            print("Excluding variable " + definition["name"])
                            continue
                    else:
                        print("Excluding variable " + definition["name"])
                        continue
                if var_name not in histos[cut].keys() : histos[cut][var_name] = {}

                # build the bins 
                # if range_ is 1 then it is a list with bin edges
                if len(range_) == 1:
                    bins_ = array("f", range_[0])
                # if it is 3 then it is a tuple
                elif len(range_) == 3:
                    bins_ = array("f", np.linspace(range_[1], range_[2], range_[0]))

                nbins_ = len(bins_)-1

                if var_name == "events": 
                    h = f.Histo1D(("histo_" + sample, "histo_" + sample, nbins_, bins_), "1", "weight")
                else:
                    h = f.Histo1D(("histo_" + sample, "histo_" + sample, nbins_, bins_), tree_var_name, "weight")

                histos[cut][var_name]["histo_" + sample] = h
    
    
    #write everything to output file
    fOut = ROOT.TFile("prova_shapes.root", "RECREATE")
    for cut in histos.keys():

        fOut.mkdir(cut)
        fOut.cd(cut)

        for var in histos[cut].keys():

            fOut.mkdir(cut + "/" + var)
            fOut.cd(cut + "/" + var)

            for histo_name, histo in  histos[cut][var].items():
                histo.Write(histo_name)

    fOut.Write()
    fOut.Close()

                