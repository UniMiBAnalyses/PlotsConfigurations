import ROOT
import json
import os
from collections import OrderedDict
from math import sqrt

# Apri il file ROOT
file = ROOT.TFile.Open("/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/rootFile/unfolding_binningOPT/plots_vbf_w_2018unfolding_binningOPT.root")

# Accedi alla directory "fiducial"
directory = file.Get("SR_fid")
# print(directory.GetListOfKeys())

## prendo gia le varibili cosi poi posso sotituire i range
variables = {}
handle = open("variables.py")
exec(handle)
handle.close()

# Ciclo su tutti gli istogrammi nella directory
for key in directory.GetListOfKeys():
    # print(key.GetName())
    obj = key.ReadObj()
    # print(obj.GetName())
    if "_flat" in obj.GetName() or "_div" in obj.GetName() or "nJet" in obj.GetName(): continue
    if isinstance(obj, ROOT.TDirectoryFile):
        for k in obj.GetListOfKeys():
            if "WLNuJJ" in k.GetName():
                hist_sig = k.ReadObj()
            elif "HT_hardJets" in k.GetName():
                hist_bkg1 = k.ReadObj()
            elif "HT_PUJets" in k.GetName():
                hist_bkg2 = k.ReadObj()

        # hist_bkg = hist_bkg1.Clone()
        # hist_bkg.Add(hist_bkg2)

        # Ottieni il numero totale di bin dell'istogramma
        n_bins = hist_sig.GetNbinsX()

        # Inizializza liste per memorizzare i valori di x e la cumulativa
        x_values = []
        cumulative = []
        width = 0

        # Calcola la cumulativa dell'istogramma ( sig / (rad(sig+bkg) ) e normalizzala
        total_entries = 0
        for i in range(1, n_bins + 1):
            if hist_sig.GetBinContent(i) == 0:
                total_entries += 0
            else:
                # total_entries += (hist_sig.GetBinContent(i) / sqrt(hist_sig.GetBinContent(i) + hist_bkg.GetBinContent(i)))
                total_entries += (hist_sig.GetBinContent(i))
            x_values.append(round(hist_sig.GetBinCenter(i)-hist_sig.GetBinWidth(i)/2,2))
            cumulative.append(total_entries)

        # Normalizza la cumulativa dividendo ciascun valore per il valore massimo
        max_cumulative = max(cumulative)
        cumulative_normalized = [entry / max_cumulative for entry in cumulative]

        # print(cumulative_normalized)
        # print(len(cumulative_normalized))

        ### QUI STO SCEGLIENDO IL NUMERO DI BINNNNNNN
        nGenBin = 20
        # Calcola i valori di x corrispondenti a 10 valori equamente spaziati della cumulativa normalizzata
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
with open("opt_variables_{}.py".format(nGenBin), "w") as file:
    # Scrivere il dizionario ordinato nel nuovo file nel formato desiderato
    for var_name, var_dict in sorted_variables.items():
        file.write("variables['{}'] = {}\n".format(var_name, var_dict))




