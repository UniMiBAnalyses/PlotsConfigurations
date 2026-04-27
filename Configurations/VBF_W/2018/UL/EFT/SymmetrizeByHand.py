#!/usr/bin/env python
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

            # Verifica se la sistematica è valida
            if valid_nuisances and syst not in valid_nuisances:
                # print("[DEBUG] ❌ '{}' ignorata: non è in nuisances.py".format(syst))
                continue

            try:
                up = rootfile.Get("{}/histo_{}_{}Up".format(base_path, sample, syst))
                down = rootfile.Get("{}/histo_{}_{}Down".format(base_path, sample, syst))
            except AttributeError as e:
                print("[DEBUG] Errore durante l'accesso agli istogrammi 'Up' e 'Down' per {}: {}".format(syst, e))
                continue

            if up and down:
                systs[syst] = (up, down)

                # # --- DEBUG: stampa contenuto dei bin ---
                # print("[DEBUG] Contenuti per sistematica '{}', sample '{}':".format(syst, sample))
                # for ibin in range(1, up.GetNbinsX() + 1):
                #     up_val = up.GetBinContent(ibin)
                #     down_val = down.GetBinContent(ibin)
                #     print("   Bin {0}: Up = {1}, Down = {2}".format(ibin, up_val, down_val))

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
        "mcDirectoryLatSig": "/path/to/mc/directory",
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
        "re": __import__("re"),  # Aggiungiamo re per le regex
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


def load_variables(variables_path):
    full_context = {
        "variables": {},
        "map_multiclass": {
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
            "ptW": 7,
            "nJet": 3     
        }
    }

    try:
        with open(variables_path, "r") as f:
            lines = f.readlines()

        # Rimuovi gli import
        clean_lines = []
        for line in lines:
            if line.strip().startswith("import") or line.strip().startswith("from "):
                continue
            clean_lines.append(line)

        code = compile("".join(clean_lines), variables_path, 'exec')
        exec(code, full_context)  # tutto in un unico contesto

    except Exception as e:
        print("⚠️ Errore durante l'import di {}.\nImporta solo i dati necessari nel file, oppure commenta gli import esterni.\nErrore: {}".format(variables_path, e))
        sys.exit(1)

    if "variables" not in full_context:
        raise ValueError("File {} non definisce un dizionario 'variables'.".format(variables_path))

    variable_dict = full_context["variables"]
    variable_names = set(variable_dict.keys())

    # print("[INFO] Trovate {} variabili in {}".format(len(variable_names), variables_path))
    # print(variable_names)
    return variable_names

def load_samples_keys(samples_path):
    samples = {}

    fake_globals = {
        "__builtins__": __builtins__,
        "samples": samples,
        "nanoGetSampleFiles": lambda *args, **kwargs: [],
        "mcDirectoryLat": "",
        "mcDirectoryLatSig": "/path/to/mc/directory",
        "XSWeight": "",
        "SFweight": "",
        "METFilter_MC": "",
        "GenLepMatch": "",
        "CommonWeight": "",
        "os": os,
        "inspect": inspect,
        "collections": collections,
        "getSampleFiles": lambda *args, **kwargs: [],
        "addSampleWeight": lambda *args, **kwargs: [],
        "CMSSW_BASE": '/afs/cern.ch/user/a/abulla/CMSSW_11_1_4'
    }

    def custom_exec_from_path(path):
        with open(path, "r") as f:
            lines = f.readlines()

        clean_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("import") or stripped.startswith("from "):
                continue
            clean_lines.append(line)

        code = "".join(clean_lines)
        exec(code, fake_globals)

    try:
        # Esegui il primo file
        custom_exec_from_path(samples_path)

        # Controlla se il primo file ha settato una variabile con il path di un secondo file
        if "samplesFile" in fake_globals:
            print("🔁 Eseguo samples secondario: {}".format(fake_globals['samplesFile']))
            cmssw = fake_globals.get("CMSSW_BASE", "")
            samples_file_path = os.path.join(cmssw, "src", fake_globals["samplesFile"])
            print("🔁 Controllo samples secondario: {}".format(samples_file_path))
            if os.path.exists(samples_file_path):
                print("🔁 Eseguo anche samples secondario: {}".format(samples_file_path))
                custom_exec_from_path(samples_file_path)

    except Exception as e:
        print("⚠️ Errore durante l'import di {}.\nErrore: {}".format(samples_path, e))
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
    # print("[INFO] ➕ Simmetrizzando '{}' (mode={}) per '{}' in '{}/{}'".format(syst, mode, sample, region, variable))

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

        # Evita valori negativi
        new_up_arr = np.where(new_up_arr < 0, 1e-6, new_up_arr)
        new_down_arr = np.where(new_down_arr < 0, 1e-6, new_down_arr)

    elif mode == "up":
        new_up_arr = up_arr
        new_down_arr = 2 * nom_arr - up_arr

    elif mode == "down":
        new_down_arr = down_arr
        new_up_arr = 2 * nom_arr - down_arr
    
    elif mode == "fix_empty":
        changed = False

        # Fallback per nominale vuoto
        if "sm" in sample or "quad" in sample:
            if np.any(nom_arr == 0):
                print("[WARNING] ❌ Il nominale contiene valori == 0, lo sostituisco con 1e-6")
                nom_arr = np.where(nom_arr == 0, 1e-6, nom_arr)
                changed = True
            elif np.any(nom_arr < 0):
                print("[WARNING] ❌ Il nominale contiene valori < 0, lo sostituisco con 1e-6")
                return
        else:
            if np.any(nom_arr <= 0):
                print("[WARNING] ❌ Il nominale contiene valori <= 0, lo sostituisco con 1e-6")
                nom_arr = np.where(nom_arr <= 0, 1e-6, nom_arr)
                changed = True


        # --- Step 1: fix preliminare ---
        nom_arr  = np.where(nom_arr  > 0, nom_arr,  1e-6)
        up_arr   = np.where(up_arr   > 0, up_arr,   1e-6)
        down_arr = np.where(down_arr > 0, down_arr, 1e-6)

        # --- Step 2: maschere ---
        only_up   = (up_arr > 0) & (down_arr <= 1e-6)
        only_down = (down_arr > 0) & (up_arr <= 1e-6)
        both_bad  = (up_arr <= 1e-6) & (down_arr <= 1e-6)

        # --- Step 3: copia iniziale ---
        new_up_arr   = np.copy(up_arr)
        new_down_arr = np.copy(down_arr)

        # Simmetrizza rispetto a down
        if np.any(only_up):
            changed = True
            new_down_arr[only_up] = 2 * nom_arr[only_up] - up_arr[only_up]

        # Simmetrizza rispetto a up
        if np.any(only_down):
            changed = True
            new_up_arr[only_down] = 2 * nom_arr[only_down] - down_arr[only_down]

        # Fallback: entrambe vuote → assegna il nominale
        if np.any(both_bad):
            changed = True
            new_up_arr[both_bad]   = nom_arr[both_bad]
            new_down_arr[both_bad] = nom_arr[both_bad]

        # --- Step 4: fix finale ---
        new_up_arr   = np.where(new_up_arr   > 0, new_up_arr,   1e-6)
        new_down_arr = np.where(new_down_arr > 0, new_down_arr, 1e-6)

        # Se nessuna modifica necessaria, restituisci gli originali
        if not changed:
            new_up_arr = up_arr
            new_down_arr = down_arr
        else:
            print("[INFO] 🔧 Simmetrizzazione applicata per sample {} e syst '{}' in '{}'".format(sample, syst, region))

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

        print("[INFO] 📊 up ratio: mean={}, std={} (calcolati su {} bin centrali)".format(up_mean,up_std, np.count_nonzero(central_mask_up)))
        print("[INFO] 📊 down ratio: mean={}, std={} (calcolati su {} bin centrali)".format(down_mean, down_std, np.count_nonzero(central_mask_down)))

        def clip_outliers(ratio, mean, std, mask, direction):
            corrected_ratio = np.copy(ratio)
            n_changed = 0
            for i in range(len(ratio)):
                delta = abs(ratio[i] - mean)
                threshold = 2 * std
                is_outlier = delta > threshold
                print("[DEBUG] bin {}: ratio = {:.3f}, mask = {}, |ratio - mean| = {:.3f}, 2*std = {:.3f}, outlier_mask = {}".format(
                    i, ratio[i], mask[i], delta, threshold, is_outlier))
                
                if mask[i] and is_outlier:
                    new_ratio = random.uniform(mean - 1. * std, mean + 1. * std)
                    corrected_ratio[i] = new_ratio
                    new_val = new_ratio * nom_arr[i]
                    print("[VERBOSE] ⚠️  {}: bin {}, ratio originale = {} → nuova ratio = {}, nuovo valore = {}".format(direction, i=i+1, ratio=ratio[i], new_ratio=new_ratio, new_val=new_val))
                    n_changed += 1
            print("[INFO] 🔧 {}: {} bin corretti su {} validi".format(direction, n_changed, np.count_nonzero(mask)))
            return corrected_ratio

        new_ratio_up = clip_outliers(ratio_up, up_mean, up_std, valid_mask, "up")
        new_ratio_down = clip_outliers(ratio_down, down_mean, down_std, valid_mask, "down")

        new_up_arr = nom_arr * new_ratio_up
        new_down_arr = nom_arr * new_ratio_down

    else:
        print("[ERROR] ❌ Modalità di simmetrizzazione '{}' non riconosciuta. Usa 'max', 'up', 'down' o 'smooth'.".format(mode))
        return

    if changed:
        print("[DEBUG] ✔️ Nuovi contenuti calcolati. Scrittura nuovi istogrammi...")

    new_up = up.Clone("histo_{}_{}Up".format(sample, syst))
    new_down = down.Clone("histo_{}_{}Down".format(sample, syst))
    new_nom = nominal.Clone("histo_{}".format(sample))

    for ibin in range(1, new_up.GetNbinsX() + 1):
        new_up.SetBinContent(ibin, new_up_arr[ibin - 1])
        new_down.SetBinContent(ibin, new_down_arr[ibin - 1])
        new_nom.SetBinContent(ibin, nom_arr[ibin - 1])

    if not args.dryrun:

        base_dir = "{}/{}".format(region, variable)
        rootfile.cd(base_dir + "/")
        new_up.Write(new_up.GetName(), ROOT.TObject.kOverwrite)
        new_down.Write(new_down.GetName(), ROOT.TObject.kOverwrite)
        new_nom.Write(new_nom.GetName(), ROOT.TObject.kOverwrite)

        # print("[INFO] ✅ Scritti: {} e {} in {}".format(new_up.GetName(), new_down.GetName(), base_dir))

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
    parser.add_argument("--nuisances", required=True, help="Path to nuisances.py file (must define a 'nuisances' dict)")
    parser.add_argument("--onlyCut", nargs='+', help="Restrict to specific regions", default=[])
    parser.add_argument("--onlyVar", nargs='+', help="Restrict to specific variables", default=[])
    parser.add_argument("--onlySample", nargs='+', help="Restrict to specific samples", default=[])
    parser.add_argument("--onlySyst", nargs='+', help="Restrict to specific systematics", default=[])
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--mode", choices=["max", "up", "down","smooth", "fix_empty"], default="fix_empty", help="Symmetrization mode")
    parser.add_argument("--update", default=False, help="overwrite existing file", action="store_true")
    parser.add_argument("--submit", default=False, help="job is executed on a condor node to make it faster", action="store_true")
    parser.add_argument("--dry-run", dest="dryrun", action="store_true", help="Only print the tasks without executing them")
    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    input_dir = os.path.dirname(input_path)
    input_file = os.path.basename(input_path)

    if args.update:
        print("[INFO] Scriverò direttamente nel file: {}".format(input_path))
        file_to_use = input_path
        rootfile = ROOT.TFile.Open(file_to_use, "UPDATE")
    elif args.dryrun:
        print("[INFO] Eseguo in modalità dry-run, non verranno apportate modifiche al file: {}".format(input_path))
        file_to_use = input_path
        rootfile = ROOT.TFile.Open(file_to_use, "READ")
    else:
        fixed_file_name = os.path.join(input_dir, "fixed_{}".format(input_file))
        file_to_use = fixed_file_name
        if os.path.exists(file_to_use):
            print("[WARNING] Il file {} esiste già. Faccio update di questo!!.".format(file_to_use))
            rootfile = ROOT.TFile.Open(file_to_use, "UPDATE")
        else:
            shutil.copy2(input_path, file_to_use)
            print("[INFO] ✨ Lavorerò su una copia del file: {}".format(file_to_use))
            rootfile = ROOT.TFile.Open(file_to_use, "UPDATE")

    if not rootfile or not rootfile.IsOpen():
        print("[ERROR] ❌ Impossibile aprire il file ROOT: {}".format(input_path))
        sys.exit(1)

    if args.submit:
        subfile = "run_symmetrize.jds"

        # prendo la working dir corrente (da dove lanci lo script python)
        current_dir = os.getcwd()
        executable_path = os.path.join(current_dir, "run_symmetrize.sh")
        output_path = os.path.join(current_dir, "run_symmetrize.out")

        # genera il .jds per condor
        with open(subfile, "w") as f:
            f.write("executable = {0}\n".format(executable_path))
            f.write("universe = vanilla\n")
            f.write("output = {0}\n".format(output_path))
            f.write("error = /dev/null\n")
            f.write("log = /dev/null\n")
            f.write('MY.WantOS = "el7"\n')
            f.write("request_cpus = 1\n")
            f.write('+JobFlavour = "workday"\n')
            f.write("queue\n")

        python_script = os.path.abspath(__file__)  # path assoluto dello script corrente
        samples_file = os.path.abspath(args.samples)
        variables_file = None
        variables_list = None
        if args.onlyVar:
            # caso 1: lista di un elemento che finisce con .py → è un file di variabili
            if len(args.onlyVar) == 1 and args.onlyVar[0].endswith(".py"):
                variables_file = os.path.abspath(args.onlyVar[0])
            elif len(args.onlyVar) > 1:
                # caso 2: lista di variabili da passare come --onlyCut
                variables_list = " ".join(args.onlyVar)
        nuisances_file = os.path.abspath(args.nuisances)
        output_file = os.path.dirname(file_to_use) + "/{0}".format(os.path.basename(file_to_use))

        # output_file = "/eos/user/a/abulla/www/public/VBF_W/2018/sys/rootFile/unfolding_final_v8_bkgOnly/fixed_{0}".format(os.path.basename(input_file))

        ## write sh
        shfile = "run_symmetrize.sh"
        with open(shfile, "w") as f:
            f.write("#!/bin/bash\n\n")
            f.write("# Configura l'ambiente\n")
            f.write("export X509_USER_PROXY=/afs/cern.ch/user/a/abulla/.proxy\n")
            f.write("export EOS_MGM_URL=root://eoscms.cern.ch\n")
            f.write("voms-proxy-info\n")
            f.write("export SCRAM_ARCH=slc7_amd64_gcc820\n")
            f.write("export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n")
            f.write("source $VO_CMS_SW_DIR/cmsset_default.sh\n")
            f.write("cd /afs/cern.ch/user/a/abulla/CMSSW_11_1_4\n")
            f.write("eval `scramv1 ru -sh`\n")
            f.write("ulimit -c 0 -s unlimited\n\n")

            f.write("# Passaggio alla directory temporanea\n")
            f.write("cd $TMPDIR\n")
            f.write("echo \"Current directory: $(pwd)\"\n")
            f.write("echo \"Contents of $TMPDIR:\"\n")
            f.write("ls -l\n\n")

            f.write("# Copia dei file necessari nella directory temporanea\n")
            f.write("cp {0} .\n".format(python_script))
            f.write("cp {0} .\n".format(samples_file))
            if variables_file:
                f.write("cp {0} .\n".format(variables_file))
            f.write("cp {0} .\n".format(nuisances_file))
            f.write("xrdcp {0} .\n".format(os.path.realpath(file_to_use).replace("home-a","user/a")))
            f.write("ls -l\n\n")

            f.write("# Controllo input\n")
            f.write("if [ ! -f \"{0}\" ]; then\n".format(os.path.basename(file_to_use)))
            f.write("  echo \"[ERROR] File di input non trovato in TMPDIR!\"\n")
            f.write("  exit 1\n")
            f.write("fi\n\n")

            f.write("# Esecuzione dello script Python\n")
            f.write("python {0} \\\n".format(os.path.basename(python_script)))
            f.write("  --input {0} \\\n".format(os.path.basename(file_to_use)))
            f.write("  --samples {0} \\\n".format(os.path.basename(samples_file)))
            f.write("  --nuisances {0} \\\n".format(os.path.basename(nuisances_file)))
            if variables_file:
                f.write("  --onlyVar {0} \\\n".format(os.path.basename(variables_file)))
            elif args.onlyVar:
                f.write("  --onlyVar {0} \\\n".format(variables_list))
            if args.onlyCut:
                f.write("  --onlyCut {0} \\\n".format(" ".join(args.onlyCut)))
            if args.onlySample:
                f.write("  --onlySample {0} \\\n".format(" ".join(args.onlySample)))
            if args.onlySyst:
                f.write("  --onlySyst {0} \\\n".format(" ".join(args.onlySyst)))
            f.write("  --mode {0} \\\n".format(args.mode))
            f.write("  --update\n\n")

            f.write("# Controllo se lo script Python ha avuto successo\n")
            f.write("if [ -f \"{}\" ]; then\n".format(os.path.basename(file_to_use)))
            f.write("  echo \"[INFO] Output ROOT file creato.\"\n")
            f.write("else\n")
            f.write("  echo \"[ERROR] Nessun file di output creato!\"\n")
            f.write("  exit 1\n")
            f.write("fi\n\n")

            f.write("# Copia finale su EOS se tutto è andato a buon fine\n")
            f.write("if [ $? -eq 0 ]; then\n")
            f.write("  echo \"[INFO] Script completato con successo, copio l'output su EOS...\"\n")
            f.write("  xrdcp -f {0} {1}\n".format(os.path.basename(file_to_use), os.path.realpath(file_to_use).replace("home-a","user/a")))
            f.write("echo \"[INFO] Copia completata.\"\n")
            f.write("else\n")
            f.write("  echo \"[ERROR] Script Python fallito, nessun file copiato!\"\n")
            f.write("  exit 1\n")
            f.write("fi\n")

        os.chmod(shfile, 0o755)
        os.system("condor_submit {}".format(subfile))
        sys.exit(0)
 


    regions = list_dirs(rootfile)
    if args.onlyCut:
        regions = [r for r in regions if any(cut in r for cut in args.onlyCut)]

    ## consider EFT just in case
    sample_names = load_samples_keys(args.samples)
    ops = ["cW", "cHDD", "cHWB", "cHj1", "cHQ1", "cHj3", "cHQ3", "cHl3", "cll1", "cWtil", "cHWtil"]
    # ops = []
    for op1 in ops:
        sample_names.append("sm_lin_quad_{}".format(op1))
        sample_names.append("quad_{}".format(op1))
        for op2 in ops:
            if op1 != op2:
                sample_names.append("sm_lin_quad_mixed_{}_{}".format(op1, op2))
    if args.onlySample:
        sample_names = [s for s in sample_names if any(sample in s for sample in args.onlySample)]

    seen = set()
    sample_names = [x for x in sample_names if not (x in seen or seen.add(x))]

    valid_nuisances = None
    if args.nuisances:
        valid_nuisances = load_nuisances(args.nuisances, sample_names)

        if args.onlySyst:
            # Filtro solo le systematics richieste
            filtered_nuisances = []
            for n in valid_nuisances:
                if "norm" in n:
                    # le tengo solo se esplicitamente richieste
                    if n in args.onlySyst:
                        filtered_nuisances.append(n)
                else:
                    if any(syst in n for syst in args.onlySyst):
                        filtered_nuisances.append(n)
            valid_nuisances = filtered_nuisances

    print("DEBUG sample_names =", sample_names)
    tasks = []
    for region in regions:
        region_dir = rootfile.Get(region)
        variables = list_dirs(region_dir)
        # print(variables)
        if args.onlyVar:
            # print("[INFO] Filtrando le variabili in base a: {}".format(args.onlyVar))
            if len(args.onlyVar) == 1 and args.onlyVar[0].endswith(".py"):
                var = load_variables(args.onlyVar[0])
                args.onlyVar = var
            variables = [v for v in variables if any(v == var for var in args.onlyVar)]
            # print(variables)
        for variable in variables:
            for sample in sample_names:
                if args.onlySample and sample not in args.onlySample:
                    continue
                # tasks.append((region, variable, sample, valid_nuisances, rootfile))
                ## filtro direttamwnte i task in base alla strategia di analisi.. 
                control_regions = ("topcr", "PUWJ", "HWJ")
                if (
                    (any(region.endswith(r) for r in control_regions) and ("events" in variable or "class0" in variable))
                    or
                    (region.endswith("SR") and variable != "events")
                ):
                    tasks.append((region, variable, sample, valid_nuisances, rootfile))

    print("[INFO] Trovati {} task da eseguire.".format(len(tasks)))
    
    for task in tasks:
        region, variable, sample, valid_nuisances, rootfile = task
        
        # Trova gli istogrammi nominali e le sistematiche
        nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
        print("[DEBUG] Trovati {} sistematiche per '{}' in '{}/{}'".format(len(systs), sample, region, variable))
        
        if nominal and systs:
            for syst, (up, down) in systs.items():
                print("[DEBUG] Simmetrizzando per la sistematica '{}'".format(syst))
                symmetrize(region, variable, sample, nominal, syst, up, down, rootfile, args.mode)

    # Dopo aver terminato, chiudi il file ROOT
    rootfile.Close()

    print("All done. Changes saved to: {}".format(args.input))