# -*- coding: utf-8 -*-

import subprocess
import os


def leggi_samples(file_path, var):
    lines_to_save = []
    save_next_5_lines = False
    with open(file_path, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if i < 12:
                lines_to_save.append(line)
            if line.startswith("samples['WLNuJJ_{}".format(var)):
                save_next_5_lines = True
                j = i
            if save_next_5_lines and i < j + 7:
                lines_to_save.append(line)
    return lines_to_save


def do_aliases(var, aliases):
    string = 'CMSSW=os.environ["CMSSW_BASE"]\n'
    string += 'aliasesFile = "PlotsConfigurations/Configurations/VBF_W/2017/UL/unfolding/aliases_noDNNs.py"\n'
    string += 'if os.path.exists(CMSSW+"/src/"+aliasesFile):\n'
    string += '  handle = open(CMSSW+"/src/"+aliasesFile)\n'
    string += '  exec(handle)\n'
    string += '  handle.close()\n'
    string += '\n'
    string += '\n'

    for alias in aliases:
        if var in alias:
            string += 'aliases["{}"] = {}\n'.format(alias, aliases[alias])

    return string

def do_variables(var, variables):
    string = ''
    for variable in variables:
        if var in variable or "events" in variable:
            string += 'variables["{}"] = {}\n'.format(variable, variables[variable])

    return string


## execute the cconfig so i get the paths before modifying it
CMSSW=os.environ["CMSSW_BASE"]
configFile = "PlotsConfigurations/Configurations/VBF_W/2017/UL/unfolding/ALL/configuration.py"
if os.path.exists(CMSSW+'/src/'+configFile):
    handle = open(CMSSW+'/src/'+configFile)
    exec(handle)
    handle.close()

aliases={}
aliasesFile = "PlotsConfigurations/Configurations/VBF_W/2017/UL/unfolding/ALL/aliases_onlyDNNS.py"
if os.path.exists(CMSSW+'/src/'+aliasesFile):
    handle = open(CMSSW+'/src/'+aliasesFile)
    exec(handle)
    handle.close()

variables={}
variablesFile = "PlotsConfigurations/Configurations/VBF_W/2017/UL/unfolding/BKG_ONLY/variables.py"
if os.path.exists(CMSSW+'/src/'+variablesFile):
    handle = open(CMSSW+'/src/'+variablesFile)
    exec(handle)
    handle.close()

haddedFile = os.path.join(os.getcwd(),outputDir,"plots_{}.root".format(tag))
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2017/UL/unfolding/ALL/samples_onlysig.py"

var_unfolding = ["ptW", "leppt", "lepeta", "nJet", "jet1pt", "jet1eta", "jet2pt", "jet2eta", "detajj", "mjj", "ptjj", "dphijj"]
# var_unfolding = ["mjj"]

# Lista per memorizzare i processi avviati
processes = []

for var in var_unfolding:
    # Leggi le righe da salvare
    lines_to_save = leggi_samples(CMSSW+'/src/'+samplesFile, var)
    with open('samples_{}.py'.format(var), 'w') as output_file:
        for line in lines_to_save:
            output_file.write(line)
    ## close the file
    output_file.close()

    lines_to_save = do_aliases(var, aliases)
    with open('aliases_{}.py'.format(var), 'w') as output_file:
        for line in lines_to_save:
            output_file.write(line)
    output_file.close()

    lines_to_save = do_variables(var, variables)
    with open('variables_{}.py'.format(var), 'w') as output_file:
        for line in lines_to_save:
            output_file.write(line)
    output_file.close()

    
    # Sostituisci "allsig" con "var" in configuration.py
    command = "sed 's/allsig/{}/g' configuration.py > configuration_{}.py".format(var, var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    # sostituisci variables.py con variables_var.py
    command = "sed -i 's/variables.py/variables_{}.py/g' configuration_{}.py".format(var, var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    # sostituisci aliases.py con aliases_var.py
    command = "sed -i 's/aliases.py/aliases_{}.py/g' configuration_{}.py".format(var, var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    # Sostituisci "samples.py" con "samples_var.py" in configuration.py
    command = "sed -i 's/samples.py/samples_{}.py/g' configuration_{}.py".format(var, var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    command = "sed -i 's|rootFile|../rootFile|g' configuration_{}.py".format(var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    command = "sed -i 's|datacards|../datacards|g' configuration_{}.py".format(var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    command = "sed -i 's|plots|../plots|g' configuration_{}.py".format(var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()

    ## se presente, la rinomino aggiungendo _old alla fine
    if os.path.exists(var):
        command = "rm -rf {}".format(var)
        processes.append(subprocess.Popen(command, shell=True))
        processes[-1].wait()

    ## creo la cartella e la popolo con quello che mi serve!
    command = "mkdir {}".format(var) 
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()

    command = "mv samples_{}.py {}".format(var, var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    command = "mv configuration_{}.py {}".format(var, var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    command = "mv aliases_{}.py {}".format(var, var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()
    command = "mv variables_{}.py {}".format(var, var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()

    command = "ln -s ../../BKG_ONLY/cuts.py ../../BKG_ONLY/structure.py ../../BKG_ONLY/nuisances.py {}".format(var)
    processes.append(subprocess.Popen(command, shell=True))
    processes[-1].wait()


    


