import argparse
import os
from multiprocessing import Pool

parser = argparse.ArgumentParser()
parser.add_argument("-cfg", help="Configuration file", type=str, required=True )
parser.add_argument("-A", help="File A", type=str, )
parser.add_argument("-B", help="File B", type=str)
parser.add_argument("--ta", help="Title A", type=str)
parser.add_argument("--tb", help="Title B", type=str)
parser.add_argument("-o", "--output", help="Output", type=str)
parser.add_argument("--ns", "--normalise", dest="normalise", help="Normalize shapes", action="store_true", default=False)
args = parser.parse_args()

def submit(cmd):
   os.system(cmd)

try: os.mkdir(args.output)
except: print("--> Directory {} already present".format(args.output))

conf_dir = "/".join(i for i in args.cfg.split("/")[:-1])
cutsFile = ""
samplesFile = ""
variablesFile = ""
execfile(args.cfg)

  
cuts = {}
samples = {}
variables = {}
execfile(conf_dir + "/" + cutsFile)
execfile(conf_dir + "/" + samplesFile)
execfile(conf_dir + "/" + variablesFile)


cmds = []
for cut in cuts.keys():
   print("---> " + cut)
   for sample in samples.keys():
      for var in variables.keys():
         if "cuts" in variables[var].keys() and cut not in variables[var]["cuts"]: continue
         cmds.append("python compare_plots.py -A " + args.A +  " -B " + args.B + " --ta " + args.ta + " --tb " + args.tb + " --cut " + cut + " --var " + var + " --sample " + sample + " -o " + args.output + (" --ns" if args.normalise else ""))
         # os.system("python compare_plots.py -A " + args.A +  " -B " + args.B + " --ta " + args.ta + " --tb " + args.tb + " --cut " + cut + " --var " + var + " --sample " + sample + " -o " + args.output)


pool = Pool(processes=8)
pool.map(submit, cmds)
