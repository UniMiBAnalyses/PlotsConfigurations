# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# import ROOT
# import json

# # Nome del file ROOT
# root_file_name = "/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/rootFile/unfolding_resolution/plots_vbf_w_2018unfolding_resolution.root"

# # Dizionario per memorizzare le deviazioni standard
# std_dev_dict = {}

# # Apri il file ROOT
# file = ROOT.TFile.Open(root_file_name)

# # Itera attraverso le directory principali
# for main_key in file.GetListOfKeys():
#     main_dir = main_key.ReadObj()
#     if not isinstance(main_dir, ROOT.TDirectory):
#         continue

#     # Itera attraverso le subdirectory
#     for sub_key in main_dir.GetListOfKeys():
#         sub_dir = sub_key.ReadObj()
#         if not isinstance(sub_dir, ROOT.TDirectory):
#             continue

#         # Variabile associata a questa subdirectory (dal nome della directory precedente)
#         variable_name = sub_key.GetName().split("ratio_")[-1]


#         # Itera attraverso gli oggetti nella subdirectory
#         for hist_key in sub_dir.GetListOfKeys():
#             hist = hist_key.ReadObj()
#             if not isinstance(hist, ROOT.TH1):
#                 continue

#             # Ottieni i valori dei bin e calcola la deviazione standard
#             std_dev = hist.GetStdDev()

#             # Salva nel dizionario
#             std_dev_dict[variable_name] = std_dev

# # Stampa il risultato
# for var, std in std_dev_dict.items():
#     print("Variable: {}, Std Dev: {:.6f}".format(var, std))

# map = {"ptl" : "leppt", 
#          "etal" : "lepeta", 
#          "ptj1" : "jetpt1", 
#          "etaj1" : "jeteta1", 
#          "ptj2" : "jetpt2", 
#          "etaj2" : "jeteta2", 
#          "mjj" : "mjj", 
#          "detajj" : "detajj"}


# import numpy as np
# import ast

# def calculate_max_bins(y, x, resolution, max_bins=10):
#     bins = [y]  # Lista per i bordi dei bin, partendo da y
#     n = 0       # Contatore del numero di bin
#     while bins[-1] < x and n < max_bins:
#         next_bin_edge = bins[-1] * (1 + resolution)  # Calcola il bordo successivo del bin
#         if next_bin_edge >= x:  # Se il prossimo bordo supera x, termina il ciclo
#             bins.append(x)
#             break
#         bins.append(next_bin_edge)
#         n += 1  # Incrementa il contatore dei bin
#     return n, bins

# # Leggi il file con la definizione delle variabili
# file_path = "/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/opt_binning/variables.py"  # Modifica con il percorso corretto
# ## prendo gia le varibili cosi poi posso sotituire i range
# variables = {}
# handle = open(file_path)
# exec(handle)
# handle.close()

# # Itera su ogni chiave e valore nello std_dev_dict
# for key, value in std_dev_dict.items():
#     if key in map:
#         variable_name = map[key]
#         res = value
#     else:
#         variable_name = key
#         res = value

#     # Cerca la variabile nel dizionario delle variabili
#     for var_key, var_value in variables.items():
#         if "_" in var_key: 
#             continue
#         if "events" in var_key: continue
#         if variable_name == var_key:
#             print("Variable found: {}".format(var_key))
#             print("Variable details: {}".format(var_value))

#             # Ottieni i limiti dai dettagli della variabile
#             y = var_value["range"][1]  # Limite minimo
#             x = var_value["range"][2]  # Limite massimo
            
#             # Calcola i bordi dei bin usando calculate_max_bins
#             n_bins, bin_edges = calculate_max_bins(y, x, res*10)
            
#             print("Number of bins: {}".format(len(bin_edges) - 1))
#             print("Bin edges: {}".format(bin_edges))
#             break  # Esci dal loop dopo aver trovato la variabile




variables = {
    "ptl": 0.030604,
    "ptj2": 0.146194,
    "detajj": 0.007335,
    "ptj1": 0.135636,
    "mjj": 0.109640,
    "etal": 0.002471,
    "ptW": 0.376650,
    "etaj2": 0.010192,
    "etaj1": 0.009728,
    "dphijj": 0.052574,
    "ptjj": 0.002257,
}

import numpy as np

# Dati di input
resolutions = {
    "ptl": 0.030604,
    "ptj2": 0.146194,
    "detajj": 0.007335,
    "ptj1": 0.135636,
    "mjj": 0.109640,  # Fisso a 7 bin
    "etal": 0.002471,
    "ptW": 0.376650,  # Fisso a 5 bin
    "etaj2": 0.010192,
    "etaj1": 0.009728,
    "dphijj": 0.052574,
    "ptjj": 0.002257,
}

# Vincoli
min_bins = 5
max_bins = 15
fixed_bins = {"mjj": 7, "ptW": 5}

# Applica scala logaritmica alle risoluzioni
log_res = {key: -np.log10(val) for key, val in resolutions.items()}

# Normalizza i valori logaritmici per ottenere il range di bin desiderato
min_log = min(log_res.values())
max_log = max(log_res.values())

scaled_bins = {
    key: int(round(min_bins + (max_bins - min_bins) * (val - min_log) / (max_log - min_log)))
    for key, val in log_res.items()
}

# Applica i valori fissi
for key, fixed_value in fixed_bins.items():
    scaled_bins[key] = fixed_value

# Risultati finali
print("Numero di bin per ogni variabile:")
for variable, num_bins in scaled_bins.items():
    print("{}: {} bin".format(variable, num_bins))
