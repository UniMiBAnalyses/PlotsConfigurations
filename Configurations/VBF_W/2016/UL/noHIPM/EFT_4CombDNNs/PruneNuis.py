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
                # print("[DEBUG] ❌ '{}' ignorata: non è in nuisances.py".format(syst))
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

def GetPoissError(numberEvents, down, up):
    alpha = 1 - 0.6827
    L = 0
    if numberEvents != 0:
        L = ROOT.Math.gamma_quantile(alpha / 2., numberEvents, 1.)
    U = 0
    if numberEvents == 0:
        U = ROOT.Math.gamma_quantile_c(alpha, numberEvents + 1, 1.)
    else:
        U = ROOT.Math.gamma_quantile_c(alpha / 2., numberEvents + 1, 1.)

    L = numberEvents - L
    if numberEvents > 0:
        U = U - numberEvents

    if up and not down:
        return U
    if down and not up:
        return L
    if up and down:
        return (L, U)


def PruneNuisances(region, variable, sample, nominal, syst_name, up, down, rootfile, threshold=0.10, suppressFluctuationError=True, suppressNegative=True):
    nbins = nominal.GetNbinsX()
    max_var_up = 0.0
    max_var_down = 0.0
    fluctuation_problem = False

    for ibin in range(1, nbins + 1):
        y_nom = nominal.GetBinContent(ibin)
        if y_nom <= 0:
            if suppressNegative:
                continue
            else:
                y_nom = 1e-6

        poisson_err = GetPoissError(y_nom, 0, 1)
        y_up = up.GetBinContent(ibin)
        y_down = down.GetBinContent(ibin)

        if poisson_err > 0:
            max_var_up = max(max_var_up, abs(y_up - y_nom) / poisson_err)
            max_var_down = max(max_var_down, abs(y_down - y_nom) / poisson_err)

        if suppressFluctuationError and (y_up <= 0 or y_down <= 0):
            fluctuation_problem = True
            print(" [!] Fluctuation or negative bin in '{} / {} / {}' for nuisance '{}': up = {:.3f}, down = {:.3f}".format(region, variable, sample, syst_name, y_up, y_down))

    max_variation = max(max_var_up, max_var_down)

    if fluctuation_problem or max_variation < threshold:
        print(" [-] PRUNED '{}' for sample '{}' in {}/{} (max variation: {:.3f})".format(syst_name, sample, region, variable, max_variation))

        # # Sovrascrive le variazioni con il nominale
        # region_dir = rootfile.Get(region)
        # variable_dir = region_dir.Get(variable)

        # up_name = "histo_{}_{}Up".format(sample, syst_name)
        # down_name = "histo_{}_{}Down".format(sample, syst_name)

        # nominal_copy_up = nominal.Clone(up_name)
        # nominal_copy_down = nominal.Clone(down_name)

        # nominal_copy_up.SetDirectory(0)
        # nominal_copy_down.SetDirectory(0)

        # variable_dir.cd()
        # nominal_copy_up.Write(up_name, ROOT.TObject.kOverwrite)
        # nominal_copy_down.Write(down_name, ROOT.TObject.kOverwrite)

        # print(" [=] Replaced '{}' up/down with nominal in {}/{} for sample '{}'".format(syst_name, region, variable, sample))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input ROOT file")
    parser.add_argument("--samples", required=True, help="Path to a Python file that defines the 'samples' dict")
    parser.add_argument("--nuisances", help="Path to nuisances.py file (must define a 'nuisances' dict)")
    parser.add_argument("--onlyCut", nargs='+', help="Restrict to specific regions", default=[])
    parser.add_argument("--onlyVar", nargs='+', help="Restrict to specific variables", default=[])
    parser.add_argument("--onlySample", nargs='+', help="Restrict to specific samples", default=[])
    parser.add_argument("--onlySyst", nargs='+', help="Restrict to specific systematics", default=["CMS_scale_JESAbsolute", "CMS_scale_JESBBEC1", "CMS_scale_JESEC2", "CMS_scale_JESHF", "CMS_scale_e", "CMS_scale_met", "CMS_res_j", "CMS_btag_jes", "CMS_PS_FSR_dipole"])
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    args = parser.parse_args()

    # Apri il file ROOT di input in modalità READ
    rootfile = ROOT.TFile.Open(args.input, "READ")
    
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

        # Trova istogrammi
        nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
        print("[DEBUG] Trovati {} sistematiche per '{}' in '{}/{}'".format(len(systs), sample, region, variable))

        if nominal and systs:
            for syst, (up, down) in systs.items():
                PruneNuisances(region, variable, sample, nominal, syst, up, down, rootfile)

    # Dopo aver terminato, chiudi il file ROOT
    rootfile.Close()

    print("All done. Changes saved to: {}".format(args.input))