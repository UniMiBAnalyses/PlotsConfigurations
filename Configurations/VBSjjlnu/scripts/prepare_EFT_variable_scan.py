import json
import os
import argparse
import sys
import logging
from glob import glob

def builder(dict_, target, name):
    object_ = {}
    object_["datacard_name"] = name
    object_["folders"] = []

    dir_ = {}
    dir_["basedir"] = target
    dir_["name"] = ""

    object_["folders"].append(dir_)

    object_["phase_spaces"] = []

    for ps, var in dict_.items():
        psdict = {}
        psdict["name"] = ps 
        psdict["var"] = var
        psdict["cut"] = ps

        object_["phase_spaces"].append(psdict)

    return object_



parser = argparse.ArgumentParser()
parser.add_argument("-t","--target", help="Target datacards directory output of mkDatacards" , type=str, required=True)
parser.add_argument("-c","--config", help="A configuration .py file. It should have the signal regions where all variables will be scanned and a list of CR with the observables you want to fit (will be kept fixed)", required=True)
parser.add_argument("-o","--output", help="The json file output compatible with prepare_datacard*.py, default=datacards_all_variables.json", type=str, default="datacards_all_variables.json")

args = parser.parse_args()

if __name__ == "__main__":

    # check for the presence of the datacards folder
    if not os.path.isdir(args.target):
        print("[ERROR] directory {} does not exist".format(args.target))

    # load the config depending on the python version
    conf = {}
    assume_equal = True

    if sys.version_info[0] == 2:
        execfile(args.config)
    elif sys.version_info[0] == 3:
        exec(open(path).read())
    else:
        print("[ERROR] Running with a python version different from 2 or 3")
        sys.exit(1)

    signal_regions = conf["SR"]
    region_dict = conf["CR"]

    # save for each SR the variables
    variables_dict = {k: [i.split("/")[-1] for i in glob(os.path.join(args.target, k, "*"))] for k in signal_regions}

    # if assume equal flag is specified then we assume for each k the list of variables is equal
    # otherwise we make combinations
    if assume_equal:
        variables = [i for i in variables_dict[variables_dict.keys()[0]]]
    else:
        pass

    cards = []
    for v in variables:
        for sr in signal_regions:
            region_dict[sr] = v

        cards.append(builder(region_dict, args.target, v))

    json_string = json.dumps(cards, indent=4)
    
    with open(args.output, 'w') as outfile:
        outfile.write(json_string)