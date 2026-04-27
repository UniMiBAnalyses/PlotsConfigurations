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

def truncHisto(region, variable, sample, nominal, syst, up, down, rootfile, savebins=[], written_nominals=None):
    """
    Troncatura di istogrammi: mantiene solo i bin specificati in `savebins`, senza vuoti.
    Salva i nuovi istogrammi nella cartella {region}/{variable}_cut dello stesso ROOT file.
    Il nominale viene salvato una sola volta per (region, variable, sample).
    """
    if written_nominals is None:
        written_nominals = set()

    savebins = list(savebins)
    savebins.sort()  # Ordine crescente, per sicurezza

    def make_truncated_hist(histo, name):
        newtitle = histo.GetTitle()
        nbins_new = len(savebins)

        newhisto = ROOT.TH1F(name, newtitle, nbins_new, 0, nbins_new)
        for i, ibin in enumerate(savebins):
            content = histo.GetBinContent(ibin + 1)
            error = histo.GetBinError(ibin + 1)
            newhisto.SetBinContent(i + 1, content)
            newhisto.SetBinError(i + 1, error)

        newhisto.SetDirectory(0)
        return newhisto

    # Nuova directory
    outdir = "{}/{}_cut3".format(region, variable)
    if not rootfile.GetDirectory(outdir):
        rootfile.mkdir(outdir)
    rootfile.cd(outdir)

    key = (region, variable, sample)
    if key not in written_nominals:
        nominal_cut = make_truncated_hist(nominal, "histo_{}".format(sample))
        nominal_cut.Write()
        written_nominals.add(key)

    if up:
        up_cut = make_truncated_hist(up, "histo_{}_{}Up".format(sample, syst))
        up_cut.Write()

    if down:
        down_cut = make_truncated_hist(down, "histo_{}_{}Down".format(sample, syst))
        down_cut.Write()

# def worker(args):
#     region, variable, sample, valid_nuisances, rootfile = args
#     print("[DEBUG] Worker avviato per '{}/{}' con sample '{}'".format(region, variable, sample))

#     # Trova gli istogrammi nominali e le sistematiche
#     nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
#     if not nominal:
#         print("[DEBUG] Nessun istogramma nominale trovato per '{}' in '{}/{}'".format(sample, region, variable))
#     if not systs:
#         print("[DEBUG] Nessuna sistematica trovata per '{}' in '{}/{}'".format(sample, region, variable))

#     print("[DEBUG] Trovati {} sistematiche per '{}' in '{}/{}'".format(len(systs), sample, region, variable))
#     if nominal and systs:
#         for syst, (up, down) in systs.items():
#             print("[DEBUG] Simmetrizzando per la sistematica '{}'".format(syst))
#             symmetrize(region, variable, sample, nominal, syst, up, down, rootfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input ROOT file")
    parser.add_argument("--samples", required=True, help="Path to a Python file that defines the 'samples' dict")
    parser.add_argument("--nuisances", help="Path to nuisances.py file (must define a 'nuisances' dict)")
    parser.add_argument("--onlyCut", nargs='+', help="Restrict to specific regions", default=[])
    parser.add_argument("--onlyVar", nargs='+', help="Restrict to specific variables", default=["DNNJoinedDphijet1jet2PU2"])
    parser.add_argument("--onlySample", nargs='+', help="Restrict to specific samples", default=[])
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--savebins", type=int, nargs="+", help="Indici di bin da mantenere (0-based)", default=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
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
        written_nominals = set()

        # Trova gli istogrammi nominali e le sistematiche
        nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
        print("[DEBUG] Trovati {} sistematiche per '{}' in '{}/{}'".format(len(systs), sample, region, variable))

        if nominal:
            if not systs and sample in ["DATA", "data", "data_obs"]:  # Nominale solo per i dati
                truncHisto(region, variable, sample, nominal, None, None, None, rootfile, args.savebins, written_nominals)
            else:
                for syst, (up, down) in systs.items():
                    truncHisto(region, variable, sample, nominal, syst, up, down, rootfile, args.savebins, written_nominals)

    # Dopo aver terminato, chiudi il file ROOT
    rootfile.Close()

    print("All done. Changes saved to: {}".format(args.input))