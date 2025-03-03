#!/usr/bin/env python3

import os
import subprocess
from pprint import pformat

import os
import shutil
import subprocess
from pprint import pformat

def write_pyrunner(sample, variables, cuts, file_path, tag="Shapes"):
    mkShapesMiniDir = os.path.join("/afs/cern.ch/user/a/abulla/CMSSW_14_0_0/src/mkShapesRDFMini", tag)
    cwd = os.getcwd()

    # Rimuove e ricrea la directory `mkShapesMiniDir` in modo sicuro
    if not os.path.exists(mkShapesMiniDir):
        os.makedirs(mkShapesMiniDir)  # Ricrea la directory vuota

    # Copia la directory `python` all'interno di `mkShapesMiniDir` se non c'è
    if not os.path.exists(os.path.join(mkShapesMiniDir, "python")):
        shutil.copytree(os.path.join("/afs/cern.ch/user/a/abulla/CMSSW_14_0_0/src/mkShapesRDFMini/python"), 
                    os.path.join(mkShapesMiniDir, "python"))
    
    # Crea il percorso per il nuovo file
    DestFile = os.path.join(os.path.dirname(file_path), f"{sample}_shapes.root")
    tempFile = os.path.join("/tmp/abulla", f"{sample}_shapes.root")

    with open(f"{mkShapesMiniDir}/{sample}_runner.py", "w") as f:
        f.write("#!/usr/bin/env python3\n\n")
        f.write("from python.mkShapesRDFMini import shapeRDFMaker\n")
        f.write("import ROOT\n")
        f.write("ROOT.EnableImplicitMT()\n")
        f.write("import numpy as np\n")
        f.write("import uproot\n")
        f.write("import time\n")
        f.write("import subprocess\n\n")
        f.write("start_time = time.time()\n\n")
        f.write(f"cuts = {cuts}\n\n")
        f.write(f"variables = {pformat(variables)}\n\n")
        f.write(r'full = {k: "dnn_inputs_all" for k in cuts}')
        f.write("\n")
        f.write(f"sample = shapeRDFMaker(\"{file_path}\")\n")
        f.write(f"sample.defineSample(\"{sample}\")\n")
        f.write("sample.defineVariables(variables)\n")
        f.write("sample.defineStructure(full)\n")
        if sample in ["top", "sm", "Wjets_HT_hardJets", "Wjets_HT_PUJets"]:
            if sample in ["Wjets_HT_hardJets", "Wjets_HT_PUJets"]:
                sample_now = "Wjets_HT"
            elif sample == "sm":
                sample_now = "VBFW"
            else:
                sample_now = sample
            f.write("sample.defineEnvelopes(\n")
            f.write("{\n")
            f.write(f"\"QCDscale_{sample_now}\": {{\n")
            f.write(f"\"samples\": [\"{sample}\"],\n")
            f.write(f"\"variation\": [\"QCDscale_{sample_now}V{{}}Var\".format(i) for i in range(6)]\n")
            f.write("},\n")
            f.write(f"\"pdf\": {{\n")
            f.write(f"\"samples\": [\"{sample}\"],\n")
            f.write(f"\"variation\": [\"pdfV{{}}Var\".format(i) for i in range(103)]\n")
            f.write("}\n")
            f.write("}\n")
            f.write(")\n")
        f.write("sample.buildRDFs()\n")
        f.write("sample.buildHistogramsRDF()\n")
        f.write("sample.convertHistoToNumpy()\n")
        f.write("sample.computeEnvelopes()\n")
        f.write("print(\"--- %s seconds ---\" % (time.time() - start_time))\n\n")
        f.write(f"sample.writeToFile(\"{tempFile}\")\n\n")
        f.write(f"result = subprocess.run([\"xrdcp\", \"{tempFile}\", \"root://eosuser.cern.ch//{DestFile}\"])\n\n")
        f.write("while result.returncode != 0:\n")
        f.write("    print(\"Error in copying file, retying\")\n")
        f.write(f"    subprocess.run([\"xrdcp\", \"{tempFile}\", \"root://eosuser.cern.ch//{DestFile}\"])\n")
        f.write("else:\n")
        f.write("    print(\"File copied successfully\")\n")
        f.write(f"    subprocess.run([\"rm\", \"{tempFile}\"])\n")      
        f.write("print(\"--- %s seconds ---\" % (time.time() - start_time))\n\n")

    subprocess.run(["chmod", "+x", f"{mkShapesMiniDir}/{sample}_runner.py"])


import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--config', dest='config' , type=str, help='config file', required=True)
parser.add_argument('--var', dest='var' , type=str, help='variables file', required=False)

args = parser.parse_args()

config = args.config
## read the config file, it's a .py file, if exists
if config:
    exec(open(config).read())
else:
    print("config file not found")
    exit()

## now read the variablesFile, cutsFile and samplesFile and nuisancesFile
## inizialize the dictionaries if needed (or the lists)

variables = {}
if args.var:
    variablesFile = args.var
    ## altrimenti prendo il file in config

exec(open(variablesFile).read())
cuts = {}
exec(open(cutsFile).read())
cuts = list(cuts.keys())

samples = ["sm", "Wjets_HT", "top", "VV", "VBS" , "Higgs", "DY_M-50", "DY_else", "VBF-Z", "Vg", "VgS", "VVV"]
eft = ["quad_cW", "quad_cHDD", "quad_cHWB", "sm_lin_quad_cW", "sm_lin_quad_cHDD", "sm_lin_quad_cHWB", "sm_lin_quad_mixed_cW_cHDD", "sm_lin_quad_mixed_cW_cHWB", "sm_lin_quad_mixed_cHDD_cHWB"]
eft_debug = ["lin_cW", "lin_cHDD", "lin_cHWB", "mixed_cW_cHDD", "mixed_cW_cHWB", "mixed_cHDD_cHWB"]
samples = samples + eft + eft_debug

for sample in samples:
    filepath = os.path.realpath(os.path.join(outputDir, f"{sample}.root")).replace("home-a", "user/a")
    if not os.path.exists(filepath):
        print(f"File {filepath} not found")
        continue
    if sample == "Wjets_HT":
        write_pyrunner("Wjets_HT_hardJets", variables, cuts, filepath,  tag = tagger)
        write_pyrunner("Wjets_HT_PUJets", variables, cuts, filepath,  tag = tagger)
    else:
        write_pyrunner(sample, variables, cuts, filepath, tag = tagger)
