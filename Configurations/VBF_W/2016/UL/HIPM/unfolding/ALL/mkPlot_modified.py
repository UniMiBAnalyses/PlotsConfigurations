import subprocess
import os

def leggi(file_path, var):
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

## execute the cconfig so i get the paths before modifying it
CMSSW=os.environ["CMSSW_BASE"]
configFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/HIPM/unfolding/ALL/configuration.py"
if os.path.exists(CMSSW+'/src/'+configFile):
    handle = open(CMSSW+'/src/'+configFile)
    exec(handle)
    handle.close()

haddedFile = os.path.join(os.getcwd(),outputDir,"plots_{}.root".format(tag))
samplesFile = "PlotsConfigurations/Configurations/VBF_W/2016/UL/HIPM/unfolding/ALL/samples.py"

variables = ["ptW", "leppt", "lepeta", "nJet", "jet1pt", "jet1eta", "jet2pt", "jet2eta", "detajj", "mjj"]
# variables = ["mjj"]

# Lista per memorizzare i processi avviati
processes = []

for var in variables:
    # # Leggi le righe da salvare
    # lines_to_save = leggi(CMSSW+'/src/'+samplesFile, var)

    # # Scrivi le righe in un file
    # with open('samples_{}.py'.format(var), 'w') as output_file:
    #     for line in lines_to_save:
    #         output_file.write(line)

    # Sostituisci "allsig" con "var" in configuration.py
    command = "sed -i 's/plot.py/plot5.py/g' configuration_{}.py".format(var)
    processes.append(subprocess.Popen(command, shell=True))

    # # Attendere il completamento del processo prima di procedere
    # processes[-1].wait()

    # # Sostituisci "samples.py" con "samples_var.py" in configuration.py
    # command = "sed -i 's/samples.py/samples_{}.py/g' configuration_{}.py".format(var, var)
    # processes.append(subprocess.Popen(command, shell=True))

    # # Attendere il completamento del processo prima di procedere
    # processes[-1].wait()

    # # Esegui datacard per tutti, decommenta se le voglio fare
    command = "mkPlot.py --pycfg=configuration_{}.py --inputFile {} --showIntegralLegend=1 --onlyPlot=cratio".format(var, outputDir+"/plots_"+tag+".root")
    processes.append(subprocess.Popen(command, shell=True))
    print(command)

# Attendere il completamento di tutti i processi
for p in processes:
    p.wait()


    


