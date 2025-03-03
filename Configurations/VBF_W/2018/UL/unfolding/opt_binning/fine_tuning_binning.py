import ROOT
import json
import os
from collections import OrderedDict
from math import sqrt

# Apri il file ROOT
file = ROOT.TFile.Open("/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/rootFile/unfolding_binningOPT_show/plots_vbf_w_2018unfolding_binningOPT_show.root")

# Accedi alla directory "fiducial"
directory = file.Get("SR_fid")
# print(directory.GetListOfKeys())


map = {
    "leppt" : 10,
    "lepeta" : 10,
    "jet1pt" : 7,
    "jet1eta" : 10,
    "jet2pt" : 7,
    "jet2eta" : 10,
    "mjj" : 8,
    "detajj" : 10,
    "ptjj": 8,
    "dphijj": 10,
    "ptW": 7
}
       

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
    if "_ACM" in obj.GetName() or "_Raffa" in obj.GetName() or "nJet" in obj.GetName(): continue
    if "events" in obj.GetName(): continue
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
        print("varibale: ", obj.GetName(), "n_bins: ", n_bins)

        # Inizializza liste per memorizzare i valori di x e la cumulativa
        x_values = []
        cumulative = []
        width = 0

        # Calcola la cumulativa dell'istogramma ( sig / (rad(sig+bkg) ) e normalizzala
        total_entries = 0
        for i in range(1, n_bins + 1):
            # if hist_sig.GetBinContent(i) == 0:
            #     total_entries += 0
            # else:
            #     # total_entries += (hist_sig.GetBinContent(i) / sqrt(hist_sig.GetBinContent(i) + hist_bkg.GetBinContent(i)))
            total_entries += (hist_sig.GetBinContent(i))
            x_values.append(round(hist_sig.GetBinCenter(i)-hist_sig.GetBinWidth(i)/2,5))
            cumulative.append(total_entries)

        # print("x_ranges ", x_values)
        # print("cumulative ", cumulative)
        # Normalizza la cumulativa dividendo ciascun valore per il valore massimo
        max_cumulative = max(cumulative)
        cumulative_normalized = [entry / max_cumulative for entry in cumulative]

        # print("cumulative norm:", cumulative_normalized)
        # print(len(cumulative_normalized))

        ### QUI STO SCEGLIENDO IL NUMERO DI BINNNNNNN
        nGenBin = map[obj.GetName()]
        # Calcola i valori di x corrispondenti a 10 valori equamente spaziati della cumulativa normalizzata
        steps = [1.0 * (i+1) / nGenBin for i in range(nGenBin)]
        # print(steps)
        # print(len(x_values))
        # print(len(cumulative))
        # print(len(cumulative_normalized))



        x_values_at_steps = []
        x_values_at_steps.append(x_values[0])
        for s in steps:
            for x,y in zip(x_values, cumulative_normalized):
                if y >= s:
                    x_values_at_steps.append(x)
                    break

        # x_values_at_steps = [x_values[i] for i, entry in enumerate(cumulative_normalized) if entry >= steps]

        print(obj.GetName())
        print(x_values_at_steps)

        event_counts = []

        # # Itera sui range definiti in x_values_at_steps
        # for i in range(len(x_values_at_steps) - 1):
        #     x_min = x_values_at_steps[i]
        #     x_max = x_values_at_steps[i + 1]
            
        #     # Trova i bin corrispondenti agli estremi del range
        #     bin_min = hist_sig.GetXaxis().FindBin(x_min)
        #     bin_max = hist_sig.GetXaxis().FindBin(x_max) - 1  # Include bin_min, esclude bin_max
            
        #     # Conta gli eventi nei bin
        #     count = 0
        #     for bin in range(bin_min, bin_max + 1):  # Include bin_max
        #         count += hist_sig.GetBinContent(bin)
            
        #     # Salva il conteggio per il range
        #     event_counts.append((x_min, x_max, count))

        # print(event_counts)
        
        if obj.GetName()+"_div" in variables:
            variables[obj.GetName()+"_div"]["range"] = (x_values_at_steps,)
        if obj.GetName()+"_flat" in variables:
            variables[obj.GetName()+"_flat"]["range"] = (x_values_at_steps,)

sorted_variables = OrderedDict(sorted(variables.items()))

# Aprire un nuovo file per la scrittura
# with open("variables_flatS_{}.py".format(nGenBin), "w") as file:
#     # Scrivere il dizionario ordinato nel nuovo file nel formato desiderato
#     for var_name, var_dict in sorted_variables.items():
#         file.write("variables['{}'] = {}\n".format(var_name, var_dict))




# Variable: ptl, Std Dev: 0.030604
# Variable: ptj2, Std Dev: 0.146194
# Variable: detajj, Std Dev: 0.007335
# Variable: ptj1, Std Dev: 0.135636
# Variable: mjj, Std Dev: 0.109640
# Variable: etal, Std Dev: 0.002471
# Variable: ptW, Std Dev: 0.376650
# Variable: etaj2, Std Dev: 0.010192
# Variable: etaj1, Std Dev: 0.009728
# Variable: dphijj, Std Dev: 0.052574
# Variable: ptjj, Std Dev: 0.002257
# Variable: events, Std Dev: 0.000000
# Variable: nJet, Std Dev: 0.545359