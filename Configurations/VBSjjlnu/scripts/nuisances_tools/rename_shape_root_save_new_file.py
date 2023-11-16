from __future__ import print_function
import ROOT as R
import sys
import argparse

'''
This script can be used to rename a systematic shape including the name
of the samples or a custom name. 

The original shape is not removed
'''

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("-o","--output", help="Output file", type=str)
parser.add_argument("--shape-name", help="Shape name",type=str)
parser.add_argument("--rename", help="Rename",type=str)
parser.add_argument("--samples","-s", help="Samples", nargs="+", type=str)
parser.add_argument("-sf","--samples-file", help="Samples", type=str)
parser.add_argument("-ev","--exclude-vars", help="Exclude vars", type=str, nargs="+")
parser.add_argument("-ec","--exclude-cuts", help="Exclude cuts", type=str, nargs="+")
parser.add_argument("-dc","--do-cuts", help="Do cuts", type=str, nargs="+")
parser.add_argument("-dv","--do-vars", help="Do vars", type=str, nargs="+")
args = parser.parse_args()


if args.samples and len(args.samples) > 0:
    samples = args.samples 
elif args.samples_file:
    samples = [f.strip() for f in open(args.samples_file).readlines()]
else:
    print("Please provide samples of file with a list of samples")
    exit(1)

f = R.TFile(args.input, "READ")
fO = R.TFile(args.output, "RECREATE")

shape_name = args.shape_name
rename_shape = args.rename


rename_dict = {}
for s in samples:

   if rename_shape == None:  new_shape_name = shape_name +"_"+ s
   else:  new_shape_name = rename_shape

   old_name = "histo_"+sample+"_"+shape_name+"Down"
   new_name = "histo_"+sample+"_"+new_shape_name+"Down"
   rename_dict[old_name] = new_name

   old_name = "histo_"+sample+"_"+shape_name+"Up"
   new_name = "histo_"+sample+"_"+new_shape_name+"Up"
   rename_dict[old_name] = new_name

for k in f.GetListOfKeys():
    if args.exclude_cuts and k.GetName() in args.exclude_cuts: continue
    if args.do_cuts and k.GetName() not in args.do_cuts: continue
    d = f.Get(k.GetName())
    fO.mkdir(k.GetName())
    for z in d.GetListOfKeys():
        if args.exclude_vars and z.GetName() in args.exclude_vars: continue
        if args.do_vars and z.GetName() not in args.do_vars: continue
        R.gDirectory.Cd(z.GetName())
        v = d.Get(z.GetName())
        fO.mkdir(k.GetName() + "/" + z.GetName())
        for l in v.GetListOfKeys():

            h = f.Get(k.GetName() + "/" + z.GetName() + "/" + l.GetName())
            h.SetDirectory(0)

            if l.GetName() in rename_dict.keys():
               h.SetName(rename_dict[l.GetName()])
           
            h.Write()

        fO.Cd("../")
        R.gDirectory.Cd("../")


    fO.Cd("../")
    R.gDirectory.Cd("../")
         
print("-> Closing")
      

fO.Write()
fO.Close()
f.Close()
