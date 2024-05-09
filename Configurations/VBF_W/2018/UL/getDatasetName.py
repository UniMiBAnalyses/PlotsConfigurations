from LatinoAnalysis.Tools.commonTools import *
import os
import ROOT

def getListMC(samples):
    _MClist = {}
    for key in samples.keys():
        if key != 'DATA' and key != 'Fake':
            _MClist[key] = samples[key]['name']
    return _MClist

def GetTree(MClist):
    samples_dict = {}
    for key in MClist:
        samples_dict[key] = {"mini": []}
        for smp in MClist[key]:
            Tree = smp.split("/")[-1].split("__")[0].split("nanoLatino_")[-1]
            if Tree not in samples_dict[key]["mini"]:
                samples_dict[key]["mini"].append(Tree)
    return samples_dict

def latex_safe(word):
    if isinstance(word, str):  # Se word is una stringa
        return word.replace("_", "\\textunderscore ")
    elif isinstance(word, list):  # Se word is una lista
        return [w.replace("_", "\\textunderscore ") for w in word]
    else:
        return word  

def readXS(name, cfg):
    with open(cfg, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.strip().startswith("samples['"):
            parts = line.split(".extend(")
            sample_name = parts[0].split("samples['")[-1].split("']")[0]
            if sample_name == name:
                attributes = parts[1].strip('[] \n').split(',')
                if len(attributes) == 3:
                    xs = str(attributes[0].strip().split("'xsec=")[-1].split("'")[0])
                    kfact = str(attributes[1].strip().split("'kfact=")[-1].split("'")[0])
                    ref = attributes[2].strip().split("'ref=")[-1].split("'")[0]
                    return (xs,kfact,ref)
    return None

def joinLatex(dataset, xs, ref):
    print dataset
    print xs
    print ref
    if len(dataset) == len(xs) == len(ref): 
        output_string = ""
        for i in range(len(dataset)):
            output_string += "& {} & {} & {} \\\\".format(latex_safe(dataset[i]), xs[i], ref[i])
        return output_string
    else:
        print ("dataset: ", len(dataset))
        print ("xs: ", len(xs))
        print ("ref: ", len(ref))
        return None


if __name__ == '__main__':

    

    samplesCfg = "PlotsConfigurations/Configurations/VBF_W/2018/UL/samples.py"
    SamplesCfg = "/eos/user/a/abulla/CMSSW_11_0_4/src/LatinoAnalysis/NanoGardener/python/framework/samples/Summer20UL18_106x_nAODv9.py"
    XsCfg = "/eos/user/a/abulla/CMSSW_11_0_4/src/LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections_UL.py"
    CMSSW=os.environ["CMSSW_BASE"]

    if os.path.exists(CMSSW+'/src/'+samplesCfg) :
        handle = open(CMSSW+'/src/'+samplesCfg)
        exec(handle)
        handle.close()
    else :
        print "!!! ERROR file ", samplesCfg, " does not exist."
        exit()

    if os.path.exists(SamplesCfg) :
        handle = open(SamplesCfg)
        exec(handle)
        handle.close()
    else :
        print "!!! ERROR file ", SamplesCfg, " does not exist."
        exit()

    MClist = getListMC(samples)
    MCTreeslist = GetTree(MClist)
    print(MCTreeslist.items()) ##questi sono i soprannomi dentro a samples 'name', i "nomi" dentro a nanoLatino_"nome"_partx.root
    # print(MClist) ## questi sono i rootfiles che prendo da samples.py
        
    ## prendiamoci le sezioni d'urto
    for process, info in MCTreeslist.items():
        xs_list = []
        kfac_list = []
        ref_list = []
        for mini_process in info['mini']:
            result = readXS(mini_process, XsCfg)
            if result is not None:
                xs, kfact, ref = result
                xs_list.append(xs)
                kfac_list.append(kfact)
                ref_list.append(ref)
        MCTreeslist[process]['xs'] = xs_list
        MCTreeslist[process]['ref'] = ref_list


    # print(MCTreeslist) 
    for i in MCTreeslist:
        print MCTreeslist[i]["mini"]
    # # Creazione della tabella
    # table = r"""
    # \begin{sidewaystable}
    # \setlength\tabcolsep{2.5pt}
    # \begin{tabular}{l|l l l}
    # \hline
    # Sample Name & nanoAOD Path & $\sigma$(pb) & Ref. \\
    # \hline
    # \hline
    # """

    # for key in MCTreeslist:
    #     item = len(MCTreeslist[key]["mini"])
    #     # _process = " \\\ ".join(latex_safe(MCTreeslist[key]["mini"]))
    #     _process = latex_safe(key)
    #     # _ref = MCTreeslist[key]["ref"]
    #     dataset = []
    #     xs = []
    #     ref = []
    #     for mini in MCTreeslist[key]["mini"]:
    #         # print len(mini)
    #         DatasetName = Samples[mini]['nanoAOD'].split("/")[1]
    #         dataset.append(DatasetName) 
    #     for xs_ in MCTreeslist[key]["xs"]:
    #         xs.append(xs_)
    #     for ref_ in MCTreeslist[key]["ref"]:
    #         ref.append(ref_)
    #     string = joinLatex(dataset, xs,ref)
    #     # _xs = " \\\ & ".join(xs)
    #     # _ref = " \\\ & ".join(ref)
    #     # _dataset = " \\\ & ".join(latex_safe(dataset))
    #     if item > 1:
    #         table += "\multirow{{{}}}{{{}}}{{{}}} {} \n\\hline\n".format(item,"*",_process, string)
    #     else:
    #         table += "{} {} \n\\hline\n".format(_process, string)
    #     # else:
    #     #     table += "{} & Sample not found in Samples \\\\ \n\\hline\n".format(key)

    # table += """
    # \end{tabular}
    # \caption{Tabella delle informazioni sui campioni}
    # \label{tab:campioni}

    # \end{sidewaystable}
    # """

    # # Scrivi il contenuto della tabella in un file txt
    # with open('tabella.txt', 'w') as file:
    #     file.write(table)

    # print("Contenuto della tabella scritto nel file 'tabella.txt'")