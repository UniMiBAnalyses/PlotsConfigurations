import ROOT 
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Command line parser for model testing')
parser.add_argument('-f', '--file', dest='file',     help='Files with shapes', required = True)
parser.add_argument('-v', '--variables',     dest='variables',     help='Clip these variables', required = True, nargs='+')
parser.add_argument('-b', '--bincut',     dest='bincut',     help='Clip EFT prediction from this point', required = True, type=int)
args = parser.parse_args()

ops = ["cW", "cHW", "cHWB", "cHbox", "cHB", "cHl1", "cHQ1", "cHj1"]

os.system("cp " + args.file + " tmp.root")
f = ROOT.TFile("tmp.root", "UPDATE")

for region in [i.GetName() for i in f.GetListOfKeys()]:

    print(region)

    d = f.Get(region)
    f.cd(region)

    for var in [j.GetName() for j in d.GetListOfKeys()]:
        if var not in args.variables: continue

        d_ = d.Get(var)
        f.cd(region + "/" + var)

        shapes = [i.GetName() for i in d_.GetListOfKeys()]
        for shape in shapes:
            # check if this is an EFT shape

            if any(i in shape for i in ops):

                #get the histo
                h = d_.Get(shape)
                bins = h.GetNbinsX()

                # cycle over all bins above threshold
                for j in range(args.bincut+1, bins+1):
                    #clip EFT prediction 
                    h.SetBinContent(j, 0)
                    h.SetBinError(j, 0)

                h.Write(shape)


f.Close()
