# -*- coding: utf-8 -*-

import sys
# bypass ROOT argv parsing
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import optparse


def compute_var_info(num):
    XS = 39.04 + 32.17

    n = num.GetBinContent(1)
    d = den.GetBinContent(1)
    # d = 4247790.457671976

    err_n = num.GetBinError(1)
    err_d = den.GetBinError(1)
    # err_d = 1429.9466625586956

    ratio = n / d
    err_ratio = ( ( err_n / d )**2 + ( n*err_d / (d**2) )**2 )**(0.5)

    xs_new = ratio * XS
    err_xs_new = XS * err_ratio

    return xs_new,err_xs_new

def compute_ranges(variables,var):
    ## ha più senso prendere il variabile e prendere gli estremi della variabile
    ## ovviamente, sarebe più sicuro coi cuts, ma è più complicato!!

    var_in_var = var.split("_")[0]+"_flat"

    nbin = int(len(variables[var_in_var]['range'][0]) - 1)
    actual_bin = int(var.split("bin")[-1])

    if actual_bin > nbin:
        print("ERROREEEE: actaual bin: ", actual_bin)
        print("TOTAL BINS FROM VARIBALES: ", nbin)

    _min = (variables[var_in_var]['range'][0][actual_bin - 1])
    _max = (variables[var_in_var]['range'][0][actual_bin])

    return float(_min),float(_max)


if __name__ == '__main__':
    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--file',  dest='FileName'     , help='Path to file with source histos')
    parser.add_option('--den' ,  dest='den'          , help='name of the histogram with no gen_bin selection', default="TOT")
    parser.add_option('--variables' , dest='variables'         , help='Path to variables.py for bin definition', default="../opt_binning/opt_variables_10.py")

    (opt, args) = parser.parse_args()

    # Validazione dell'opzione --file
    if opt.FileName is None:
        parser.error("Option --file is required")

    sourceFile = ROOT.TFile(opt.FileName,"r")

    den = sourceFile.Get(opt.den+"/events/histo_WLNuJJ")

    keys = sourceFile.GetListOfKeys()
    selected_keys = []

    for key in keys:
        if key.GetName() != opt.den and key.GetName() not in selected_keys and "out" not in key.GetName() and "fiducial" not in key.GetName(): selected_keys.append(key.GetName())
    selected_keys.sort()

    samples = {}
    handle = open("samples.py")
    exec(handle)
    handle.close()

    variables = {}
    VariablesCfg=opt.variables
    handle = open(VariablesCfg)
    exec(handle)
    handle.close()


    data_dict = {}
    print selected_keys
    for var in selected_keys:
        num = sourceFile.Get(var + "/events/histo_WLNuJJ")
        xs, err = compute_var_info(num)
        _min,_max = compute_ranges(variables,var)
        
        var_parts = var.split("_bin")
        data_dict.setdefault(var_parts[0], {})
        data_dict[var_parts[0]].setdefault("bin" + var_parts[1], {})
        
        data_dict[var_parts[0]]["bin" + var_parts[1]]["XS"] = xs
        data_dict[var_parts[0]]["bin" + var_parts[1]]["XS_err"] = err
        data_dict[var_parts[0]]["bin" + var_parts[1]]["min"] = _min
        data_dict[var_parts[0]]["bin" + var_parts[1]]["max"] = _max


    import json
    # Scrivi il dizionario ordinato in un file JSON
    with open('data.json', 'w') as json_file:
        json.dump(data_dict, json_file, indent=4, sort_keys=True)


