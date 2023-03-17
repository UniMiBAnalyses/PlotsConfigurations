import argparse
import json 
import numpy as np

def generateLatinosAlias(dict_):
    l = ""
    for key in dict_.keys():
        l += "aliases['{}'] =".format(key) + " {\n"
        l += "   'expr': '({})',\n".format(dict_[key])
        l += "   'samples': EFT_samples,\n"
        l += "}\n"
        l += "\n"
        
    return l

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Command line parser for model testing')
    parser.add_argument('-j', '--json',    dest='json',     help='The json file with structure \{"component": \{"sx": float, "dx": float\}\}', required = True)
    parser.add_argument('-cn', '--cutname',     dest='cutname',     help='Name of the cut', required = False, default="EFTweightCut")
    parser.add_argument('-o', '--output',     dest='output',     help='Name of the output file to store the alias definition', required = False, default="EFTweightCut.py")
    parser.add_argument('-v', '--verbose',     dest='verbose',     help='Print names of created aliases', required = False, default=False, action='store_true')
    args = parser.parse_args()
    
    file_ = open(args.json, "r")
    qdict = json.load(file_)
    file_.close()
    
    f = open(args.output,  "w")
    
    cut_names = []
    l = ""
    for key in qdict.keys():
        if qdict[key]["dx"] == qdict[key]["sx"]:
            print("[ERROR] for " + key + " left and right quantile are identical, skipping")
            continue
        l += "aliases['{}'] =".format("cut_{}_{}".format(key, args.cutname)) + " {\n"
        l += "   'expr': '(({} < {}) * ({} > {}))',\n".format(key, qdict[key]["dx"], key, qdict[key]["sx"])
        l += "   'samples': EFT_samples,\n"
        l += "}\n"
        l += "\n"
        
        cut_names.append("cut_{}_{}".format(key, args.cutname))
        
        
    print("---> INFO: Defined {} new aliases".format(len(cut_names)))
    
    f.write(l)
    
    intermediate = np.array_split(cut_names, 50)
    inter_names = []
    
    l = ""
    for idx, key in enumerate(intermediate):
        l += "aliases['{}'] =".format("cut_{}_{}".format(args.cutname, idx)) + " {\n"
        l += "   'expr': '({})',\n".format(" * ".join(i for i in key))
        l += "   'samples': EFT_samples,\n"
        l += "}\n"
        l += "\n"
        
        inter_names.append("cut_{}_{}".format(args.cutname, idx))
        
        
    print("---> INFO: Defined {} new intermediate aliases".format(len(inter_names)))
    
    f.write(l)
    
    l = ""
    l += "aliases['{}'] =".format(args.cutname) + " {\n"
    l += "   'expr': '({})',\n".format(" * ".join(i for i in inter_names))
    l += "   'samples': EFT_samples,\n"
    l += "}\n"
    l += "\n"
    
    f.write(l) 
    
    if args.verbose:
        print(inter_names + cut_names)
    
    print("---> INFO: Defined overall cut {}".format(args.cutname))
    print("---> DONE")