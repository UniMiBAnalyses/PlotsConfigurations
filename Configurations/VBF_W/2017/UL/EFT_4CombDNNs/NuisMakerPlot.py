
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
from collections import defaultdict,OrderedDict
ROOT.gROOT.SetBatch(True)

def list_dirs(obj):
    return [k.GetName() for k in obj.GetListOfKeys() if k.IsFolder()]

def find_histograms(rootfile, region, variable, sample, valid_nuisances=None):
    base_path = f"{region}/{variable}"
    nominal_name = f"{base_path}/histo_{sample}"
    nominal = rootfile.Get(nominal_name)
    if not nominal:
        return None, {}

    all_keys = [k.GetName() for k in rootfile.Get(base_path).GetListOfKeys()]
    systs = {}
    for k in all_keys:
        if k.startswith(f"histo_{sample}_") and k.endswith("Up"):
            syst = k[len(f"histo_{sample}_"):-2]  # strip "histo_sample_" and "Up"
            if valid_nuisances and syst not in valid_nuisances:
                print(f"[DEBUG] ❌ '{syst}' ignorata: non è in nuisances.py (name)")
                continue
            up = rootfile.Get(f"{base_path}/histo_{sample}_{syst}Up")
            down = rootfile.Get(f"{base_path}/histo_{sample}_{syst}Down")
            if up and down:
                systs[syst] = (up, down)
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
        print(f"⚠️ Errore durante l'import di {nuisance_file}.\nImporta solo i dati necessari nel file, oppure commenta gli import esterni.\nErrore: {e}")
        sys.exit(1)

    if "nuisances" not in full_context:
        raise ValueError(f"File {nuisance_file} non definisce un dizionario 'nuisances'.")

    nuisance_dict = full_context["nuisances"]
    nuisance_names = {entry["name"] for entry in nuisance_dict.values() if "name" in entry}
    return nuisance_names

def plot_ratio(region, variable, sample, nominal, syst_name, up, down, outdir):
    # Debug: verifica presenza istogrammi
    if not nominal:
        print(f"[DEBUG] ❌ Istogramma nominale mancante per {region}/{variable}/{sample}")
        return
    if not up or not down:
        print(f"[DEBUG] ❌ Istogramma sistematico mancante: {syst_name} per {sample}")
        return

    # Debug: numero di bin
    nbins_nom = nominal.GetNbinsX()
    nbins_up = up.GetNbinsX()
    nbins_down = down.GetNbinsX()

    print(f"[DEBUG] {region}/{variable}/{sample} - {syst_name}")
    print(f"  Nominal bins: {nbins_nom}, Up bins: {nbins_up}, Down bins: {nbins_down}")

    if nbins_nom != nbins_up or nbins_nom != nbins_down:
        print(f"[DEBUG] ⚠️ Numero di bin non corrisponde! Salto il plot.")
        return

    # Debug: contenuto dei bin
    nom_vals = np.array([nominal.GetBinContent(i+1) for i in range(nbins_nom)])
    up_vals = np.array([up.GetBinContent(i+1) for i in range(nbins_up)])
    down_vals = np.array([down.GetBinContent(i+1) for i in range(nbins_down)])

    # print(f"  ➤ Contenuti bin (Nom): {nom_vals}")
    # print(f"  ➤ Contenuti bin (Up):  {up_vals}")
    # print(f"  ➤ Contenuti bin (Down):{down_vals}")

    # Debug: se tutto è zero
    if np.all(nom_vals == 0) and np.all(up_vals == 0) and np.all(down_vals == 0):
        print(f"[DEBUG] ⚠️ Tutti i bin sono zero per {sample}, {syst_name}. Plot non creato.")
        return

    x = np.array([nominal.GetBinCenter(i+1) for i in range(nbins_nom)])

    with np.errstate(divide='ignore', invalid='ignore'):
        ratio_up = np.true_divide(up_vals, nom_vals)
        ratio_down = np.true_divide(down_vals, nom_vals)
        ratio_up[nom_vals == 0] = np.nan
        ratio_down[nom_vals == 0] = np.nan

    # --- Plot con due pannelli (main + ratio)
    fig, (ax_main, ax_ratio) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [2, 1]}, figsize=(8, 6))

    # MAIN PLOT (Nominal, Up, Down)
    ax_main.step(x, nom_vals, where='mid', label='Nominal', color='black')
    ax_main.step(x, up_vals, where='mid', label='Up', color='red')
    ax_main.step(x, down_vals, where='mid', label='Down', color='blue')
    ax_main.set_ylabel('Content')
    ax_main.set_title(f"{region}/{variable} - {sample} - {syst_name}")
    ax_main.legend()

    # RATIO PLOT (Up/Nom, Down/Nom)
    ax_ratio.step(x, ratio_up, where='mid', label='Up/Nom', color='red')
    ax_ratio.step(x, ratio_down, where='mid', label='Down/Nom', color='blue')
    ax_ratio.axhline(1.0, color='gray', linestyle='--')  # Linea di riferimento per 1

    # Calcolo della variazione massima dal valore centrale 1
    ratio_vals = np.concatenate([ratio_up, ratio_down])
    max_diff = max(abs(ratio_vals.min() - 1), abs(ratio_vals.max() - 1))

    # Aggiungiamo un piccolo margine (padding) al range
    padding = 0.1 * max_diff  # 10% di margine
    sym_range = max_diff + padding

    # Limiti simmetrici rispetto a 1, sempre entro [0.7, 1.3]
    lower_limit = max(0.7, 1 - sym_range)
    upper_limit = min(1.3, 1 + sym_range)
    ax_ratio.set_ylim(lower_limit, upper_limit)

    # Aggiungere la griglia al ratio plot
    ax_ratio.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Etichette e legenda
    ax_ratio.set_xlabel('Bin')
    ax_ratio.set_ylabel('Ratio')
    ax_ratio.legend()

    # Salvataggio del plot
    outpath = os.path.join(outdir, region, variable, sample)

    # Percorso al file index.php da copiare
    index_php_src = '/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/plots/index.php'

    # Crea ogni livello della struttura e copia index.php
    ensure_directory_with_index_php(outdir, index_php_src)
    ensure_directory_with_index_php(os.path.join(outdir, region), index_php_src)
    ensure_directory_with_index_php(os.path.join(outdir, region, variable), index_php_src)
    ensure_directory_with_index_php(outpath, index_php_src)

    # Ora puoi salvare il plot
    outfile = os.path.join(outpath, f"{sample}_{syst_name}_ratio.png")

    plt.savefig(outfile)
    plt.close(fig)
    print(f"[DEBUG] ✅ Plot salvato in {outfile}")

def ensure_directory_with_index_php(path, index_php_src):
    os.makedirs(path, exist_ok=True)
    index_php_dst = os.path.join(path, 'index.php')
    if os.path.exists(index_php_src):
        shutil.copy(index_php_src, index_php_dst)


def worker(args):
    inputfile, region, variable, sample, outdir, valid_nuisances = args
    rootfile = ROOT.TFile.Open(inputfile, "READ")
    nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
    if nominal and systs:
        for syst, (up, down) in systs.items():
            plot_ratio(region, variable, sample, nominal, syst, up, down, outdir)
    rootfile.Close()


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
        print(f"⚠️ Errore durante l'import di {samples_path}.\nImporta solo i dati necessari nel file, oppure commenta gli import esterni.\nErrore: {e}")
        sys.exit(1)

    return list(fake_globals["samples"].keys())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input ROOT file")
    parser.add_argument("--samples", required=True, help="Path to a Python file that defines the 'samples' dict")
    parser.add_argument("--nuisances", help="Path to nuisances.py file (must define a 'nuisances' dict)")
    parser.add_argument("--outdir", default="ratio_plots", help="Output directory")
    parser.add_argument("--onlyCut", nargs='+', help="Restrict to specific regions", default=[])
    parser.add_argument("--onlyVar", nargs='+', help="Restrict to specific variables", default=[])
    parser.add_argument("--onlySample", nargs='+', help="Restrict to specific samples", default=[])
    parser.add_argument("--onlySyst", nargs='+', help="Restrict to specific systematics", default=[])
    parser.add_argument("--workers", type=int, default=cpu_count(), help="Number of parallel workers")
    args = parser.parse_args()

    rootfile = ROOT.TFile.Open(args.input, "READ")

    regions = list_dirs(rootfile)
    if args.onlyCut:
        regions = [r for r in regions if any(cut in r for cut in args.onlyCut)]

    sample_names = load_samples_keys(args.samples)
    ops=["cW","cHDD","cHWB"]
    for op1 in ops:
        sample_names.append(f"sm_lin_quad_{op1}")
        sample_names.append(f"quad_{op1}")
        for op2 in ops:
            if op1 != op2:
                sample_names.append(f"sm_lin_quad_mixed_{op1}_{op2}")
    if args.onlySample:
        sample_names = [s for s in sample_names if any(sample in s for sample in args.onlySample)]

    valid_nuisances = None
    if args.nuisances:
        valid_nuisances = load_nuisances(args.nuisances, sample_names)
        if args.onlySyst:
            valid_nuisances = [n for n in valid_nuisances if any(syst in n for syst in args.onlySyst)]


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
                tasks.append((args.input, region, variable, sample, args.outdir, valid_nuisances))

    print(f"Launching {len(tasks)} tasks with {args.workers} workers...")
    with Pool(args.workers) as pool:
        pool.map(worker, tasks)

    print(f"All done. Plots saved to: {args.outdir}")