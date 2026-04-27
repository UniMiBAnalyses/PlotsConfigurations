# -*- coding: utf-8 -*-
import argparse
import ROOT
import numpy as np
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt
import sys
import os
import inspect
import collections
import shutil
import json
from collections import defaultdict, OrderedDict
ROOT.gROOT.SetBatch(True)

def list_dirs(obj):
    return [k.GetName() for k in obj.GetListOfKeys() if k.IsFolder()]

def find_histograms(rootfile, region, variable, sample, valid_nuisances=None):
    base_path = "{}/{}".format(region, variable)
    
    # Costruisci il nome dell'istogramma nominale
    nominal_name = "{}/histo_{}".format(base_path, sample)

    # Tenta di ottenere l'istogramma nominale
    nominal = rootfile.Get(nominal_name)
    if not nominal:
        print("[DEBUG] ❌ Istogramma nominale '{}' non trovato.".format(nominal_name))
        return None, {}

    # Lista tutte le chiavi per il path specificato
    all_keys = []
    try:
        all_keys = [k.GetName() for k in rootfile.Get(base_path).GetListOfKeys()]
    except AttributeError as e:
        print("[DEBUG] Errore durante l'accesso al TDirectory: {}".format(e))
        return nominal, {}

    systs = {}
    for k in all_keys:
        if k.startswith("histo_{}_".format(sample)) and k.endswith("Up"):
            syst = k[len("histo_{}_".format(sample)):-2]  # Estrae il nome della sistematica

            # Verifica se la sistematica è valida, se è stato fornito un elenco di valid_nuisances
            if valid_nuisances and syst not in valid_nuisances:
                print("[DEBUG] ❌ '{}' ignorata: non è in nuisances.py".format(syst))
                continue

            # Prova a ottenere gli istogrammi 'Up' e 'Down'
            try:
                up = rootfile.Get("{}/histo_{}_{}Up".format(base_path, sample, syst))
                down = rootfile.Get("{}/histo_{}_{}Down".format(base_path, sample, syst))
            except AttributeError as e:
                print("[DEBUG] Errore durante l'accesso agli istogrammi 'Up' e 'Down' per {}: {}".format(syst, e))
                continue

            # Verifica che entrambi gli istogrammi siano validi
            if up and down:
                systs[syst] = (up, down)
            else:
                print("[DEBUG] ❌ Istogrammi 'Up' e/o 'Down' non trovati per '{}'.".format(syst))

    return nominal, systs

def load_nuisances(nuisance_file, sample_names):
    full_context = {
        "__builtins__": __builtins__,
        "samples": {name: None for name in sample_names},
        "eleWP": "mvaFall17V2Iso_WP90_tthmva_70", 
        "muWP": "cut_Tight_HWWW_tthmva_80",  
        "mcDirectoryLat": "/path/to/mc/directory",
        "nuisances": {}, 
        # Mock delle funzioni che causano problemi
        "getSampleFiles": lambda *args, **kwargs: [],
        "getBaseW": lambda *args, **kwargs: "",
        "addSampleWeight": lambda *args, **kwargs: None,
        "os": os,
        "collections": collections,
        "json": json,
        "defaultdict": defaultdict,
        "OrderedDict": OrderedDict,
    }

    try:
        with open(nuisance_file, "r") as f:
            lines = f.readlines()

        # Rimuovi gli import
        clean_lines = []
        for line in lines:
            if line.strip().startswith("import") or line.strip().startswith("from "):
                continue
            clean_lines.append(line)

        code = compile("".join(clean_lines), nuisance_file, 'exec')
        exec(code, full_context)  # tutto in un unico contesto

    except Exception as e:
        print("⚠️ Errore durante l'import di {}.\nImporta solo i dati necessari nel file, oppure commenta gli import esterni.\nErrore: {}".format(nuisance_file, e))
        sys.exit(1)

    if "nuisances" not in full_context:
        raise ValueError("File {} non definisce un dizionario 'nuisances'.".format(nuisance_file))

    nuisance_dict = full_context["nuisances"]
    nuisance_names = {entry["name"] for entry in nuisance_dict.values() if "name" in entry}
    return nuisance_names


def load_samples_keys(samples_path):
    samples = {}

    fake_globals = {
        "__builtins__": __builtins__,
        "samples": samples,
        "nanoGetSampleFiles": lambda *args, **kwargs: [],
        "mcDirectoryLat": "",
        "XSWeight": "",
        "SFweight": "",
        "METFilter_MC": "",
        "GenLepMatch": "",
        "CommonWeight": "",
        "os": os,  # Aggiungiamo os
        "inspect": inspect,  # Aggiungiamo inspect
        "collections": collections,  # Aggiungiamo collections
        "getSampleFiles": lambda *args, **kwargs: [],
        "addSampleWeight": lambda *args, **kwargs: [],
        "CMSSW_BASE": os.environ.get("CMSSW_BASE", ""),
    }

    try:
        with open(samples_path, "r") as f:
            lines = f.readlines()

        clean_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("import") or stripped.startswith("from "):
                continue
            clean_lines.append(line)

        code = "".join(clean_lines)
        exec(code, fake_globals)

    except Exception as e:
        print("⚠️ Errore durante l'import di {}.\nImporta solo i dati necessari nel file, oppure commenta gli import esterni.\nErrore: {}".format(samples_path, e))
        sys.exit(1)

    return list(fake_globals["samples"].keys())

import numpy as np
import ROOT
import random

def symmetrize(region, variable, sample, nominal, syst, up, down, rootfile, mode="max"):
    """
    Simmetrizza o smootha le variazioni sistematiche rispetto al nominale.

    Parameters:
    - mode: "max", "up", "down", "smooth"
    """
    print("[INFO] ➕ Simmetrizzando '{}' (mode={}) per '{}' in '{}/{}'".format(syst, mode, sample, region, variable))

    nom_arr = np.array([nominal.GetBinContent(i+1) for i in range(nominal.GetNbinsX())])
    up_arr = np.array([up.GetBinContent(i+1) for i in range(up.GetNbinsX())])
    down_arr = np.array([down.GetBinContent(i+1) for i in range(down.GetNbinsX())])

    if nom_arr.shape != up_arr.shape or nom_arr.shape != down_arr.shape:
        print("[WARNING] ❌ Shape mismatch tra nominale e variazioni per '{}' in '{}'".format(syst, sample))
        return

    if mode == "max":
        delta = np.maximum(np.abs(up_arr - nom_arr), np.abs(down_arr - nom_arr))
        new_up_arr = nom_arr + delta
        new_down_arr = nom_arr - delta

    elif mode == "up":
        new_up_arr = up_arr
        new_down_arr = 2 * nom_arr - up_arr

    elif mode == "down":
        new_down_arr = down_arr
        new_up_arr = 2 * nom_arr - down_arr

    elif mode == "smooth":
        epsilon = 1e-6  # per evitare divisioni per 0
        valid_mask = nom_arr >= 0

        ratio_up = np.ones_like(up_arr)
        ratio_down = np.ones_like(down_arr)

        ratio_up[valid_mask] = up_arr[valid_mask] / nom_arr[valid_mask]
        ratio_down[valid_mask] = down_arr[valid_mask] / nom_arr[valid_mask]

        # Applichiamo un filtro per evitare outlier evidenti nel calcolo della media/std
        def central_mask(ratio):
            return (ratio > 0.7) & (ratio < 1.3)

        central_mask_up = valid_mask & central_mask(ratio_up)
        central_mask_down = valid_mask & central_mask(ratio_down)

        up_mean, up_std = np.mean(ratio_up[central_mask_up]), np.std(ratio_up[central_mask_up])
        down_mean, down_std = np.mean(ratio_down[central_mask_down]), np.std(ratio_down[central_mask_down])

        print(f"[INFO] 📊 up ratio: mean={up_mean:.3f}, std={up_std:.3f} (calcolati su {np.count_nonzero(central_mask_up)} bin centrali)")
        print(f"[INFO] 📊 down ratio: mean={down_mean:.3f}, std={down_std:.3f} (calcolati su {np.count_nonzero(central_mask_down)} bin centrali)")

        def clip_outliers(ratio, mean, std, mask, direction):
            outlier_mask = np.abs(ratio - mean) > 2 * std
            corrected_ratio = np.copy(ratio)
            n_changed = 0
            for i in range(len(ratio)):
                print("[DEBUG] bin {}: ratio = {:.3f}, mask = {}, outlier_mask = {}".format(i, ratio[i], mask[i], outlier_mask[i]))
                if mask[i] and outlier_mask[i]:
                    new_ratio = random.uniform(mean - 1. * std, mean + 1. * std)
                    corrected_ratio[i] = new_ratio
                    new_val = new_ratio * nom_arr[i]
                    print(f"[VERBOSE] ⚠️  {direction}: bin {i+1}, ratio originale = {ratio[i]:.3f} → nuova ratio = {new_ratio:.3f}, nuovo valore = {new_val:.3f}")
                    n_changed += 1
            print(f"[INFO] 🔧 {direction}: {n_changed} bin corretti su {np.count_nonzero(mask)} validi")
            return corrected_ratio

        new_ratio_up = clip_outliers(ratio_up, up_mean, up_std, valid_mask, "up")
        new_ratio_down = clip_outliers(ratio_down, down_mean, down_std, valid_mask, "down")

        new_up_arr = nom_arr * new_ratio_up
        new_down_arr = nom_arr * new_ratio_down

    else:
        print("[ERROR] ❌ Modalità di simmetrizzazione '{}' non riconosciuta. Usa 'max', 'up', 'down' o 'smooth'.".format(mode))
        return

    print("[DEBUG] ✔️ Nuovi contenuti calcolati. Scrittura nuovi istogrammi...")

    new_up = up.Clone("histo_{}_{}Up".format(sample, syst))
    new_down = down.Clone("histo_{}_{}Down".format(sample, syst))

    for ibin in range(1, new_up.GetNbinsX() + 1):
        new_up.SetBinContent(ibin, new_up_arr[ibin - 1])
        new_down.SetBinContent(ibin, new_down_arr[ibin - 1])

    if not args.dryrun:

        base_dir = "{}/{}".format(region, variable)
        rootfile.cd(base_dir + "/")
        new_up.Write(new_up.GetName(), ROOT.TObject.kOverwrite)
        new_down.Write(new_down.GetName(), ROOT.TObject.kOverwrite)

        print("[INFO] ✅ Scritti: {} e {} in {}".format(new_up.GetName(), new_down.GetName(), base_dir))

def worker(args):
    region, variable, sample, valid_nuisances, rootfile = args
    print("[DEBUG] Worker avviato per '{}/{}' con sample '{}'".format(region, variable, sample))

    # Trova gli istogrammi nominali e le sistematiche
    nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
    if not nominal:
        print("[DEBUG] Nessun istogramma nominale trovato per '{}' in '{}/{}'".format(sample, region, variable))
    if not systs:
        print("[DEBUG] Nessuna sistematica trovata per '{}' in '{}/{}'".format(sample, region, variable))

    print("[DEBUG] Trovati {} sistematiche per '{}' in '{}/{}'".format(len(systs), sample, region, variable))
    if nominal and systs:
        for syst, (up, down) in systs.items():
            print("[DEBUG] Simmetrizzando per la sistematica '{}'".format(syst))
            symmetrize(region, variable, sample, nominal, syst, up, down, rootfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input ROOT file")
    parser.add_argument("--samples", required=True, help="Path to a Python file that defines the 'samples' dict")
    parser.add_argument("--nuisances", help="Path to nuisances.py file (must define a 'nuisances' dict)")
    parser.add_argument("--onlyCut", nargs='+', help="Restrict to specific regions", default=[])
    parser.add_argument("--onlyVar", nargs='+', help="Restrict to specific variables", default=[])
    parser.add_argument("--onlySample", nargs='+', help="Restrict to specific samples", default=[])
    parser.add_argument("--onlySyst", nargs='+', help="Restrict to specific systematics", default=["CMS_scale_JESAbsolute", "CMS_scale_JESAbsolute_2017", "CMS_scale_JESBBEC1", "CMS_scale_JESBBEC1_2017", "CMS_scale_JESBBEC1", "CMS_scale_JESEC2", "CMS_scale_JESEC2_2017", "CMS_scale_JESFlavorQCD", "CMS_scale_JESHF", "CMS_scale_JESHF_2017", "CMS_scale_JESRelativeBal",  "CMS_scale_JESRelativeSample_2017"])
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--mode", choices=["max", "up", "down","smooth"], default="max", help="Symmetrization mode")
    parser.add_argument("--dry-run", dest="dryrun", action="store_true", help="Only print the tasks without executing them")
    args = parser.parse_args()

    # Apri il file ROOT di input in modalità UPDATE
    rootfile = ROOT.TFile.Open(args.input, "UPDATE")
    
    regions = list_dirs(rootfile)
    if args.onlyCut:
        regions = [r for r in regions if any(cut in r for cut in args.onlyCut)]

    sample_names = load_samples_keys(args.samples)
    ops = ["cW", "cHDD", "cHWB"]
    for op1 in ops:
        sample_names.append("sm_lin_quad_{}".format(op1))
        sample_names.append("quad_{}".format(op1))
        for op2 in ops:
            if op1 != op2:
                sample_names.append("sm_lin_quad_mixed_{}_{}".format(op1, op2))
    if args.onlySample:
        sample_names = [s for s in sample_names if any(sample in s for sample in args.onlySample)]

    valid_nuisances = None
    if args.nuisances:
        valid_nuisances = load_nuisances(args.nuisances, sample_names)
        if args.onlySyst:
            valid_nuisances = [n for n in valid_nuisances if any(syst in n for syst in args.onlySyst)]

    #filtro per evitare di normalizzare le nuisance di accettanza sui bkg se non specificamente richiesto in onlySyst
    filtered_nuisances = []
    for n in valid_nuisances:
        if "accept" in n or "norm" in n:
            if n in args.onlySyst:
                filtered_nuisances.append(n)
        else:
            if any(syst in n for syst in args.onlySyst):
                filtered_nuisances.append(n)

    valid_nuisances = filtered_nuisances

    print(valid_nuisances)

    tasks = []
    for region in regions:
        region_dir = rootfile.Get(region)
        variables = list_dirs(region_dir)
        if args.onlyVar:
            variables = [v for v in variables if any(v == var for var in args.onlyVar)]
        for variable in variables:
            for sample in sample_names:
                if args.onlySample and sample not in args.onlySample:
                    continue
                tasks.append((region, variable, sample, valid_nuisances, rootfile))

    for task in tasks:
        region, variable, sample, valid_nuisances, rootfile = task
        
        # Trova gli istogrammi nominali e le sistematiche
        nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
        print("[DEBUG] Trovati {} sistematiche per '{}' in '{}/{}'".format(len(systs), sample, region, variable))
        
        if nominal and systs:
            for syst, (up, down) in systs.items():
                symmetrize(region, variable, sample, nominal, syst, up, down, rootfile, args.mode)

    # Dopo aver terminato, chiudi il file ROOT
    rootfile.Close()

    print("All done. Changes saved to: {}".format(args.input))