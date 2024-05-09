import ROOT
import json
import os
from collections import OrderedDict

# Apri il file ROOT
file = ROOT.TFile.Open("/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/rootFile/unfolding_binningOPT/plots_vbf_w_2018unfolding_binningOPT.root")

# Accedi alla directory "fiducial"
directory = file.Get("SR_fid")

## prendo gia le varibili cosi poi posso sotituire i range
variables = {}
handle = open("variables.py")
exec(handle)
handle.close()

# Ciclo su tutti gli istogrammi nella directory
for key in directory.GetListOfKeys():
    obj = key.ReadObj()
    if "flat" in obj.GetName() or "div" in obj.GetName() or "nJet" in obj.GetName(): continue
    if isinstance(obj, ROOT.TDirectoryFile):
        for k in obj.GetListOfKeys():
            hist = k.ReadObj()

            # Ottieni il numero totale di bin dell'istogramma
            n_bins = hist.GetNbinsX()

            # Inizializza liste per memorizzare i valori di x e la cumulativa
            x_values = []
            cumulative = []
            width = 0

           # Calcola la cumulativa dell'istogramma e normalizzala
            total_entries = 0
            for i in range(1, n_bins + 1):
                total_entries += hist.GetBinContent(i)
                x_values.append(round(hist.GetBinCenter(i)-hist.GetBinWidth(i)/2,2))
                cumulative.append(total_entries)

            # Normalizza la cumulativa dividendo ciascun valore per il valore massimo
            max_cumulative = max(cumulative)
            cumulative_normalized = [entry / max_cumulative for entry in cumulative]

            # print(cumulative_normalized)
            # print(len(cumulative_normalized))

            # Calcola i valori di x corrispondenti a 10 valori equamente spaziati della cumulativa normalizzata
            nGenBin = 20
            steps = [1.0 * (i+1) / nGenBin for i in range(nGenBin)]
            
            x_values_at_steps = []
            x_values_at_steps.append(x_values[0])
            for s in steps:
                for i, entry in enumerate(cumulative_normalized):
                    if entry >= s:
                        x_values_at_steps.append(x_values[i])
                        break

            # x_values_at_steps = [x_values[i] for i, entry in enumerate(cumulative_normalized) if entry >= steps]

            print(obj.GetName())
            print(x_values_at_steps)

            if obj.GetName()+"_div" in variables:
                variables[obj.GetName()+"_div"]["range"] = (x_values_at_steps,)
            if obj.GetName()+"_flat" in variables:
                variables[obj.GetName()+"_flat"]["range"] = (x_values_at_steps,)

sorted_variables = OrderedDict(sorted(variables.items()))

# Aprire un nuovo file per la scrittura
with open("opt_variables.py", "w") as file:
    # Scrivere il dizionario ordinato nel nuovo file nel formato desiderato
    for var_name, var_dict in sorted_variables.items():
        file.write("variables['{}'] = {}\n".format(var_name, var_dict))




