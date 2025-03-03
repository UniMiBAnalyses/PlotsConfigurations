import os
import copy
import inspect
import json

configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
conf_folder = configurations +"/VBF_W/2016/"
utils_folder = configurations +"/VBF_W/utils/"

# DNN multiclass
models_path = utils_folder + '2018/NN/multiclassCONDOR/'

map_multiclass = {
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


model_best = {}
for v in ["ptW", "leppt", "lepeta", "nJet", "jet1pt", "jet1eta", "jet2pt", "jet2eta", "detajj", "mjj", "ptjj", "dphijj"]:
    candidates_ev = [d for d in os.listdir(models_path) if d.startswith(v) and 'even' in d]
    candidates_ev_sorted = sorted(candidates_ev, key=lambda x: int(x.split('_v')[-1]) if '_v' in x else 0,reverse=True)
    model_best[v] = {}
    model_best[v]["even"] = candidates_ev_sorted[0] + "/"
    candidates_odd = [d for d in os.listdir(models_path) if d.startswith(v) and 'odd' in d]
    candidates_odd_sorted = sorted(candidates_odd, key=lambda x: int(x.split('_v')[-1]) if '_v' in x else 0,reverse=True)
    model_best[v]["odd"] = candidates_odd_sorted[0] + "/"

    model_ev = models_path + '/' + model_best[v]["even"]
    transform_ev = model_ev + 'cumulative_distributions.root'
    model_odd = models_path + '/' + model_best[v]["odd"]
    transform_odd = model_ev + 'cumulative_distributions.root'

    for i in range(1, map_multiclass[v]+1):
        aliases['MultiClass_{}_class{}'.format(v,i)] = {
            'class': 'MVAReaderDNNMultiRatio',
            'args': (model_ev, transform_ev, model_odd, transform_odd, False, i),
            'linesToAdd': [
                'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                'gSystem->Load("libDNNEvaluator.so")',
                '.L {}macros/multiclassmva_reader_DNN_ratio.cc+'.format(utils_folder),
            ]
        }