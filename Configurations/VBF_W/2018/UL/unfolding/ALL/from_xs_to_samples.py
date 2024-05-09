from collections import OrderedDict

## i need this for fiducal variable
samples = {}
handle = open("../compute_measures/samples.py")
exec(handle)
handle.close()

cuts = {}
handle = open("../compute_measures/compute_cuts.py")
exec(handle)
handle.close()


samples = {}
example_dict = {  'name'   : "nanoGetSampleFiles(mcDirectoryLatSig,'Wm_LNuJJ_EWK')\n" +
            "               + nanoGetSampleFiles(mcDirectoryLatSig,'Wp_LNuJJ_EWK')",
                        'FilesPerJob' : 5,
                        'EventsPerJob' : 7000,
                    }

for cut in cuts:
    if "TOT" in cut: continue
    var = cut.split("_")[0]
    if "_out" in cut:
        samples["WLNuJJ_{}Out".format(var,number)] = example_dict.copy() 
        samples["WLNuJJ_{}Out".format(var,number)]['weight'] = "CommonWeight+'* !('+fiducial+')'"
    else:
        number = cut.split("_bin")[-1]
        samples["WLNuJJ_{}{}".format(var,number)] = example_dict.copy()
        intresting_string = cuts[cut].replace(fiducial, "").split(" && ")
        if len(intresting_string) > 2:
            samples["WLNuJJ_{}{}".format(var,number)]['weight'] = "CommonWeight+'*'+fiducial+'*'+'{} * {}'".format(intresting_string[0], intresting_string[1])
        else:
            samples["WLNuJJ_{}{}".format(var,number)]['weight'] = "CommonWeight+'*'+fiducial+'*'+'{}'".format(intresting_string[0])

string = 'CMSSW=os.environ["CMSSW_BASE"]\n'
string += 'samplesFile = "PlotsConfigurations/Configurations/VBF_W/2018/UL/unfolding/samples.py"\n'
string += 'if os.path.exists(CMSSW+"/src/"+samplesFile):\n'
string += '  handle = open(CMSSW+"/src/"+samplesFile)\n'
string += '  exec(handle)\n'
string += '  handle.close()\n'
string += '\n'
string += '\n'

string += 'fiducial = "{}"'.format(fiducial)
string += '\n'
string += '\n'

sorted_samples = OrderedDict(sorted(samples.items()))

# Aprire un nuovo file per la scrittura
with open("samples.py", "w") as file:
    file.write(string)
    # Scrivere il dizionario ordinato nel nuovo file nel formato desiderato
    for var_name in sorted_samples:
        file.write("samples['{}'] = {{ \n".format(var_name))
        for field in sorted_samples[var_name]:
            file.write("        '{}' : {},\n".format(field,sorted_samples[var_name][field]))
        file.write("}")
        file.write("\n")
        file.write("\n")
