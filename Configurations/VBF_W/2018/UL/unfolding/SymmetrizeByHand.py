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

import re
_charge_re = re.compile(r'(^|[_-])(plus|minus)($|[_-])', re.IGNORECASE)

def get_charge_tag(s):
    m = _charge_re.search(s)
    return m.group(2).lower() if m else None

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
    changed = False

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
        eps = 1e-6

        # --------------------------------------------------
        # 1) identifica bin patologici (nominale non fisico)
        # --------------------------------------------------
        nom_bad  = (nom_arr <= 0)
        up_bad   = (up_arr   <= 0)
        down_bad = (down_arr <= 0)

        new_up_arr   = np.array(up_arr,   copy=True)
        new_down_arr = np.array(down_arr, copy=True)

        # --------------------------------------------------
        # 2) NEUTRALIZZA COMPLETAMENTE i bin patologici
        # --------------------------------------------------
        if np.any(nom_bad):
            print("[WARNING] nominal <= 0 → neutralizing bins (no shape info)")

            nom_arr[nom_bad]      = eps
            new_nom = nom_arr.copy()
            new_up_arr[nom_bad]   = eps
            new_down_arr[nom_bad] = eps

            changed = True

        # --------------------------------------------------
        # 3) logica originale SOLO sui bin sani
        # --------------------------------------------------
        healthy_mask = ~nom_bad

        only_up = healthy_mask & (~up_bad)   & (down_bad)
        only_down = healthy_mask & (~down_bad) & (up_bad)
        both_bad = healthy_mask & (up_bad) & (down_bad)

        # simmetrizzazione usando NOM
        if np.any(only_up):
            changed = True
            new_down_arr[only_up] = 2.0 * nom_arr[only_up] - new_up_arr[only_up]

        if np.any(only_down):
            changed = True
            new_up_arr[only_down] = 2.0 * nom_arr[only_down] - new_down_arr[only_down]

        if np.any(both_bad):
            changed = True
            new_up_arr[both_bad]   = nom_arr[both_bad]
            new_down_arr[both_bad] = nom_arr[both_bad]

        # --------------------------------------------------
        # 4) clamp finale (solo sicurezza numerica)
        # --------------------------------------------------
        new_up_arr   = np.where(new_up_arr   > 0, new_up_arr,   eps)
        new_down_arr = np.where(new_down_arr > 0, new_down_arr, eps)

        if changed:
            print("[INFO] fix_empty: symmetrized/clamped for {} {} in {}"
                .format(syst, sample, region + "/" + variable))
            
    elif mode == "smooth":

        # ===============================
        # Stabilizzazione shape systematics
        # ===============================

        MAX_EFFECT = 0.3      # massimo effetto consentito (±60%)
        epsilon = 1e-6        # evita ratio non fisici

        # consideriamo validi solo bin con nominal significativo
        valid_mask = nom_arr > epsilon

        ratio_up = np.ones_like(up_arr)
        ratio_down = np.ones_like(down_arr)

        ratio_up[valid_mask] = up_arr[valid_mask] / nom_arr[valid_mask]
        ratio_down[valid_mask] = down_arr[valid_mask] / nom_arr[valid_mask]

        print("[INFO] 📊 Stabilizzazione ratio con tanh compression (max effect = ±{:.0f}%)"
            .format(MAX_EFFECT * 100))


        # -------------------------------------------------
        # compressione smooth degli outlier (NO random!)
        # -------------------------------------------------
        def compress_ratio(ratio, mask, direction):

            corrected_ratio = np.copy(ratio)
            n_changed = 0

            for i in range(len(ratio)):

                if not mask[i]:
                    continue

                delta = ratio[i] - 1.0

                # tanh compression
                new_ratio = 1.0 + MAX_EFFECT * np.tanh(delta / MAX_EFFECT)

                # logging solo se davvero modificato
                if abs(delta) > MAX_EFFECT:
                    print(
                        "[INFO] ⚠️  {}: bin {} ratio {:.3f} → {:.3f}".format(
                            direction, i + 1, ratio[i], new_ratio
                        )
                    )
                    n_changed += 1

                corrected_ratio[i] = new_ratio

            print("[INFO] 🔧 {}: {} bin stabilizzati su {} validi"
                .format(direction, n_changed, np.count_nonzero(mask)))

            return corrected_ratio


        # applica compressione
        new_ratio_up = compress_ratio(ratio_up, valid_mask, "up")
        new_ratio_down = compress_ratio(ratio_down, valid_mask, "down")


        # ricostruzione istogrammi
        new_up_arr = np.copy(up_arr)
        new_down_arr = np.copy(down_arr)

        new_up_arr[valid_mask] = nom_arr[valid_mask] * new_ratio_up[valid_mask]
        new_down_arr[valid_mask] = nom_arr[valid_mask] * new_ratio_down[valid_mask]

        if not np.allclose(new_up_arr, up_arr) or not np.allclose(new_down_arr, down_arr):
            changed = True

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
    # ops = ["cW", "cHDD", "cHWB"]
    ops = []
    for op1 in ops:
        sample_names.append("sm_lin_quad_{}".format(op1))
        sample_names.append("quad_{}".format(op1))
        for op2 in ops:
            if op1 != op2:
                sample_names.append("sm_lin_quad_mixed_{}_{}".format(op1, op2))
    if args.onlySample:
        sample_names = [s for s in sample_names if any(sample in s for sample in args.onlySample)]

    # breakpoint() 

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

    tasks = []
    # valid_nuisances = ["CMS_scale_met_2016"]
    # sample_names = ["WLNuJJ_mjj8"]
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

                is_cr = any(r in region for r in control_regions)
                is_sr = "SR" in region

                has_events = ("events" in variable)
                has_class0 = ("class0" in variable)
                has_dnn = ("DNN" in variable) or ("dnn" in variable)

                keep = False

                if is_cr:
                    keep = has_events or has_class0

                elif is_sr:
                    keep = not has_events

                if keep:
                    tasks.append((region, variable, sample, valid_nuisances, rootfile))

    print("[INFO] Trovati {} task da eseguire.".format(len(tasks)))
    
    for task in tasks:
        region, variable, sample, valid_nuisances, rootfile = task
        
        # Trova gli istogrammi nominali e le sistematiche
        nominal, systs = find_histograms(rootfile, region, variable, sample, valid_nuisances)
        print("[DEBUG] {}/{}/{}: nominal={}, systs={}".format(region, variable, sample, nominal is not None, len(systs)))
        print("[DEBUG] Trovati {} sistematiche per '{}' in '{}/{}'".format(len(systs), sample, region, variable))
        
        if nominal and systs:
            for syst, (up, down) in systs.items():
                symmetrize(region, variable, sample, nominal, syst, up, down, rootfile, args.mode)

    # Dopo aver terminato, chiudi il file ROOT
    rootfile.Close()

    print("All done. Changes saved to: {}".format(args.input))