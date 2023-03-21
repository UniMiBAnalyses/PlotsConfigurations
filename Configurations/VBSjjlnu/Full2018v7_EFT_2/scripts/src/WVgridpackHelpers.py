from itertools import combinations


def readReweightCard(file_):
    rew = []
    f = open(file_, "r")
    contents = f.readlines()
    for line in contents:
        if "--rwgt_name" in line:
            op = line.split("--rwgt_name=")[-1].split("\n")[0]
            rew.append(op)
    
    return rew
    

def getListOfSamplesSingleChannels(dict_, sample):
    l = []
    for key in dict_.keys():
        l.append('{}_{}'.format(key, sample))
    return l

def generateLatinosSamplesSingleChannels(dict_, sample):
    l = ""
    for key in dict_.keys():
        l += "samples['{}_{}'] = ".format(key, sample) + "{\n"
        l += "   'name': nanoGetSampleFiles(directory_EFT,'{}'),\n".format(sample)
        l += "   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '{}',\n".format(dict_[key])
        l += "   'FilesPerJob': 50,\n"
        l += "}\n"
        l += "\n"
        
    return l

def generateLatinosSamples(dict_, samples):

    s = ""
    for sam in samples:
        s += "nanoGetSampleFiles(directory_EFT,'{}') + ".format(sam)

    s = s[:-2] + ",\n"

    l = ""
    for key in dict_.keys():
        l += "samples['{}'] = ".format(key) + "{\n"
        l += "   'name': {}".format(s)
        l += "   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil' + '*' + '{}',\n".format(dict_[key])
        l += "   'FilesPerJob': 1,\n"
        l += "}\n"
        l += "\n"
        
    return l

def generateLatinosAliasSingleChannels(dict_, sample):
    l = ""
    for key in dict_.keys():
        l += "aliases['{}_{}'] =".format(key, sample) + " {\n"
        l += "   'expr': '({})',\n".format(dict_[key])
        l += "   'samples': EFT_samples,\n"
        l += "}\n"
        l += "\n"
        
    return l

def generateLatinosAlias(dict_):
    l = ""
    for key in dict_.keys():
        l += "aliases['{}'] =".format(key) + " {\n"
        l += "   'expr': '({})',\n".format(dict_[key])
        l += "   'samples': EFT_samples,\n"
        l += "}\n"
        l += "\n"
        
    return l

def getSM(dict_):
    default = "1"
    if "SM" in dict_.keys():
        default = "LHEReweightingWeight[{}]".format(dict_["SM"])
    return default

def getQuad(dict_, op):
    default = "1"
    if "SM" in dict_.keys():
        default = "LHEReweightingWeight[{}]".format(dict_["SM"])
    return "0.5*(LHEReweightingWeight[{}] + LHEReweightingWeight[{}] - 2*{})".format(dict_[op], dict_[op+"_m1"], default)
        
    
def getLin(dict_, op):
    default = "1"
    if "SM" in dict_.keys():
        default = "LHEReweightingWeight[{}]".format(dict_["SM"])
    return "0.5*(LHEReweightingWeight[{}] - LHEReweightingWeight[{}])".format(dict_[op], dict_[op+"_m1"])

def getSMLiQu(dict_, op):
    return "LHEReweightingWeight[{}]".format(dict_[op])

def getMix(dict_, op1, op2):
    default = "1"
    if "SM" in dict_.keys():
        default = "LHEReweightingWeight[{}]".format(dict_["SM"])
    mix_key = op1 + "_" + op2
    if mix_key not in dict_.keys():
        mix_key = op2 + "_" + op1
        #if mix_key not in dict_.keys(): raise ValueError
        if mix_key not in dict_.keys():
            print(op1 + "_" + op2 + " is missing from weights. putting -999")
            return "-999"
    
    return "LHEReweightingWeight[{}] + {} - LHEReweightingWeight[{}] - LHEReweightingWeight[{}]".format(dict_[mix_key], default, dict_[op1], dict_[op2])

def getSMLinQuadMix(dict_, op1, op2):
    mix_key = op1 + "_" + op2
    if mix_key not in dict_.keys():
        mix_key = op2 + "_" + op1
        #if mix_key not in dict_.keys(): raise ValueError(op1 + "_" + op2)
        if mix_key not in dict_.keys():
            print(op1 + "_" + op2 + " is missing from weights. putting -999")
            return "-999"
    
    return "LHEReweightingWeight[{}]".format(dict_[mix_key])

# for plotting purposes we want to plot the sm as a sample and the EFT (lin + quad) on top of it
def getLiQu(dict_, op):
    default = "1"
    if "SM" in dict_.keys():
        default = "LHEReweightingWeight[{}]".format(dict_["SM"])
    return "(LHEReweightingWeight[{}] - {})".format(dict_[op], default)
    
def getLinQuadMix(dict_, op1, op2):
    default = "1"
    if "SM" in dict_.keys():
        default = "LHEReweightingWeight[{}]".format(dict_["SM"])
    mix_key = op1 + "_" + op2
    if mix_key not in dict_.keys():
        mix_key = op2 + "_" + op1
        #if mix_key not in dict_.keys(): raise ValueError(op1 + "_" + op2)
        if mix_key not in dict_.keys(): 
            print(op1 + "_" + op2 + " is missing from weights. putting -999")
            return "-999"
            
    return "(LHEReweightingWeight[{}] - {})".format(dict_[mix_key], default)


def BuildReweightObjects(dict_, ops):
    c = {}
    for op in ops:
        c["sm"] = getSM(dict_)
        c["quad_" + op] = getQuad(dict_, op)
        c["lin_" + op] = getLin(dict_, op)
        c["sm_lin_quad_" + op] = getSMLiQu(dict_, op)
        c["lin_quad_" + op] = getLiQu(dict_, op)
        
    if len(ops) >= 2:
        combos = list(combinations(ops, 2))
        for op1, op2 in combos:
            c["sm_lin_quad_mixed_" + op1 + "_" + op2] = getSMLinQuadMix(dict_, op1, op2)
            c["lin_quad_mixed_" + op1 + "_" + op2] = getLinQuadMix(dict_, op1, op2)
            
    return c


def BuildAliasObjects(dict_, ops):
    c = {}
    for op in ops:
        c["sm_weight"] = getSM(dict_)
        c["quad_weight_" + op] = getQuad(dict_, op)
        c["lin_weight_" + op] = getLin(dict_, op)
        c["sm_lin_quad_weight_" + op] = getSMLiQu(dict_, op)
        c["lin_quad_weight_" + op] = getLiQu(dict_, op)
        
    if len(ops) >= 2:
        combos = list(combinations(ops, 2))
        for op1, op2 in combos:
            c["sm_lin_quad_mixed_weight_" + op1 + "_" + op2] = getSMLinQuadMix(dict_, op1, op2)
            c["lin_quad_mixed_weight_" + op1 + "_" + op2] = getLinQuadMix(dict_, op1, op2)
            c["mixed_weight_" + op1 + "_" + op2] = getMix(dict_, op1, op2)
            
    return c