from collections import OrderedDict

variables = {}
handle = open("../opt_binning/variables_semiflat.py")
exec(handle)
handle.close()

_map={
    "ptW" : "ptW_gen",
    "leppt" : "DressedLepton_pt[0]",
    "lepeta" : "lepeta_gen_abs",
    "nJet" : "nCleanGenJet",
    "jet1pt" : "CleanGenJet_pt[0]",
    "jet2pt" : "CleanGenJet_pt[1]",
    "jet1eta" : "jeteta1_gen_abs",
    "jet2eta" : "jeteta2_gen_abs",
    "detajj" : "detajj_gen",
    "mjj" : "mjj_gen",
    "ptjj" : "ptjj_gen",
    "dphijj" : "dphijj_gen"
}

cuts = {}
cuts['TOT'] = "'1.'"
cuts['fiducial'] = "'{}'.format(fiducial)"

for var in variables:
    if "_ACM" in var:
        nBins = len(variables[var]["range"][0]) - 1
        var_to_use = var.split("_")[0]

        print("var: ", var_to_use)
        print("nBin: ", nBins)
        for i in range(1,nBins+1):
            if i == 1:
                cuts["{}_bin{}".format(var_to_use, i)] = "'({} < {}) && {{}}'.format(fiducial)".format(_map.get(var_to_use), variables[var]["range"][0][i])
            elif i == nBins:
                cuts["{}_bin{}".format(var_to_use,i)] = "'({} >= {}) && {{}}'.format(fiducial)".format(_map.get(var_to_use),variables[var]["range"][0][i-1])
            else:
                cuts["{}_bin{}".format(var_to_use,i)] = "'({} >= {}) && ({} < {}) && {{}}'.format(fiducial)".format(_map.get(var_to_use),variables[var]["range"][0][i-1],_map.get(var_to_use),variables[var]["range"][0][i])

        cuts["{}_out".format(var_to_use)] = "'!({})'.format(fiducial)"

sorted_cuts = OrderedDict(sorted(cuts.items()))

# Aprire un nuovo file per la scrittura
with open("compute_cuts.py", "w") as file:
    file.write("supercut = '1'\n")
    # Scrivere il dizionario ordinato nel nuovo file nel formato desiderato
    for var_name, var_dict in sorted_cuts.items():
        file.write("cuts['{}'] = {}\n".format(var_name,var_dict))