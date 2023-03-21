from itertools import combinations
import argparse
from src.WVgridpackHelpers import *
import sys

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Command line parser for model testing')
    parser.add_argument('--rew',     dest='rew',     help='Reweight card for the order of Reweighting weights', required = True)
    parser.add_argument('--eo',     dest='excludeop',     help='Exclude these ops', required = False, nargs="+", default = [])
    parser.add_argument('--ko',     dest='keepop',     help='Keep these ops', required = False, nargs="+", default = ["*"])
    parser.add_argument('--ch',     dest='channels',     help='Channels on which to compute aliases(em, ep, mum, mup, tam, tap)', required = False,  default = [], nargs="+")
    parser.add_argument('--chname',     dest='chname',     help='Append this channel name to alias name', required = False,  default = None)
    parser.add_argument('--openmode',     dest='open_mode',     help='Open mode for output file (a: append, w: rewrite)', required = False,  default = "w", type=str)
    parser.add_argument('--SMcodegen',     dest='SMcodegen',     help='Flag to specify if the SM weight is computed at reweight or codegen. Second case the weight is 1 else from LHEReweightingWeight', required = False,  default = False, action="store_true")
    args = parser.parse_args()
    
    lhe_dict = {}

    ch = readReweightCard(args.rew)

    ops = [i.split("_m1")[0] for i in ch if "m1" in i and i.split("_m1")[0] not in args.excludeop and (i.split("_m1")[0] in args.keepop or args.keepop[0] == "*")]

    print(ops)

    chd = {ch[i]:i for i in range(len(ch))}
    c_ch  = BuildAliasObjects(chd, ops)
    sam_ch = BuildReweightObjects(chd, ops)

    print(sam_ch.keys())
    
    f = open("EFT_aliases.py", args.open_mode)
    
    
    if args.chname is None:
        f.write(generateLatinosAlias(c_ch))
    
    else:
        f.write(generateLatinosAliasSingleChannels(c_ch, args.chname))

    if len(args.channels) > 0:
        f2 = open("EFT_samples.py", args.open_mode)
        f2.write(generateLatinosSamples(sam_ch, args.channels))
            
    f.close()
    
        
        

        
