# -*- coding: utf-8 -*-

import sys
# bypass ROOT argv parsing
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import optparse


def compute_var_info(dir, key, sample):
    sf = []
    den = dir.Get("histo_{}".format(sample)).GetBinContent(1)

    for histo in dir.GetListOfKeys():
        name = histo.GetName()
        if sample not in name: continue
        # Caso generale
        if key in name and name.endswith("Var"):
            h = dir.Get(name)
            print(name)
            (val, bin) = (h.GetBinContent(1)/den, name.split("V")[1])
            sf.append((val, bin))

        # --- FSR ---
        elif "FSR_dipole" in key and "FSR_dipole" in name and \
             (name.endswith("Down") or name.endswith("Up")):
            h = dir.Get(name)
            print(name)
            bin = 0 if name.endswith("Up") else 1
            sf.append((h.GetBinContent(1)/den, bin))

        # --- ISR ---
        elif "ISR_dipole" in key and "ISR_dipole" in name and \
             (name.endswith("Down") or name.endswith("Up")):
            h = dir.Get(name)
            print(name)
            bin = 0 if name.endswith("Up") else 1
            sf.append((h.GetBinContent(1)/den, bin))

    sf.sort(key=lambda x: int(x[1]))
    return [v for (v,z) in sf]
        

    ##resort the list such that the bins are in order
    sf.sort(key=lambda x: int(x[1]))

    return [v for (v,z) in sf]


if __name__ == '__main__':
    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--file',  dest='FileName'     , help='Path to file with source histos')
    parser.add_option('--den' ,  dest='den'          , help='name of the histogram with no gen_bin selection', default="TOT")
    parser.add_option('--variables' , dest='variables'         , help='Path to variables.py for bin definition', default="../opt_binning/variables_flatS_8.py")

    (opt, args) = parser.parse_args()

    # Validazione dell'opzione --file
    if opt.FileName is None:
        parser.error("Option --file is required")

    sourceFile = ROOT.TFile(opt.FileName,"r")

    # den = sourceFile.Get(opt.den+"/events/histo_WLNuJJ")

    keys = sourceFile.GetListOfKeys()
    selected_keys = []

    for key in keys:
        if key.GetName() != opt.den and key.GetName() not in selected_keys and "out" not in key.GetName(): selected_keys.append(key.GetName())
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

    map = {
        "pdf_weight": "PDFSF",
        "QCDscale": "QCDSF",
        # "PS_ISR_dipole": "PSSF_ISR",
        # "PS_FSR_dipole": "PSSF_FSR",
        "PS_dipole": "PSSF",
    }

    for s in samples.keys():
        for var in selected_keys:
            if "fiducial" not in var:
                var_parts = var.split("_bin")
                data_dict.setdefault(var_parts[0], {})
                data_dict[var_parts[0]].setdefault("bin" + var_parts[1], {})

                dir = sourceFile.Get(var + "/events")

                for nuis in ["pdf_weight", "QCDscale", "PS_dipole"]:
                    norm_fact = compute_var_info(dir,nuis, s)
                    data_dict[var_parts[0]]["bin" + var_parts[1]][map[nuis]] = norm_fact
            else:
                data_dict.setdefault(var+"_"+s, {})
                data_dict[var+"_"+s].setdefault("all", {})

                dir = sourceFile.Get(var + "/events")
                for nuis in ["pdf_weight", "QCDscale", "PS_dipole"]:
                    norm_fact = compute_var_info(dir,nuis, s)
                    data_dict[var+"_"+s]["all"][map[nuis]] = norm_fact

    
    # for var in ["fiducial"]:
    # # for var in ["LHESEL", "LHESEL_PLUS", "LHESEL_MINUS"]:
    #     data_dict.setdefault(var, {})
    #     data_dict[var].setdefault("all", {})

    #     dir = sourceFile.Get(var + "/events")
    #     for nuis in ["pdf_weight", "QCDscale", "PS_dipole"]:
    #         norm_fact = compute_var_info(dir,nuis)
    #         data_dict[var]["all"][map[nuis]] = norm_fact

    import json
    # Scrivi il dizionario ordinato in un file JSON
    with open('diffNuis_fiduciale.json', 'w') as json_file:
        json.dump(data_dict, json_file, indent=4, sort_keys=True)
