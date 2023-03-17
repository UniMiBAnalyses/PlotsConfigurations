from itertools import combinations
import argparse
from src.WVgridpackHelpers import BuildAliasObjects, generateLatinosAlias, generateLatinosAliasSingleChannels


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Command line parser for model testing')
    parser.add_argument('--lhe',     dest='lhe',     help='Prototype lhe file', required = True)
    parser.add_argument('--eo',     dest='excludeop',     help='Exclude these ops', required = False, nargs="+", default = [])
    parser.add_argument('--ch',     dest='channel',     help='Channel on which to compute aliases(em, ep, mum, mup, tam, tap)', required = False,  default = "ep")
    parser.add_argument('--chname',     dest='chname',     help='Append this channel name to alias namme', required = False,  default = None)
    parser.add_argument('--openmode',     dest='open_mode',     help='Open mode for output file (a: append, w: rewrite)', required = False,  default = "w", type=str)
    parser.add_argument('--SMcodegen',     dest='SMcodegen',     help='Flag to specify if the SM weight is computed at reweight or codegen. Second case the weight is 1 else from LHEReweightingWeight', required = False,  default = False, action="store_true")
    args = parser.parse_args()
    
    lhe_dict = {}

    execfile(args.lhe)
    
    ch = lhe_dict[args.channel]
    
    ch = [i.split(":")[1].replace(" ", "") for i in ch.split("\n")]
    ops = [i.split("_m1")[0] for i in ch if "m1" in i and i.split("m1")[0] not in args.excludeop]
        

    chd = {ch[i]:i for i in range(len(ch))}
    
    c_ch  = BuildAliasObjects(chd, ops)
    
    f = open("EFT_aliases.py", args.open_mode)
    
    if args.chname is None:
        # for i in generateLatinosAlias(c_ch).split("\n"):
        #     f.write(i)
        #     f.write("\n")
        #     f.write("\n")
        f.write(generateLatinosAlias(c_ch))
    
    else:
        # for i in generateLatinosAliasSingleChannels(c_ch, args.chname).split("\n"):
        #     f.write(i)
        #     f.write("\n")
        #     f.write("\n")
        f.write(generateLatinosAliasSingleChannels(c_ch, args.chname))
            
    f.close()
    
        
        

        
