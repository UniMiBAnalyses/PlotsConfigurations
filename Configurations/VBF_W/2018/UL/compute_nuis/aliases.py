import os
import copy
import inspect

configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
conf_folder = configurations +"/VBF_W/2018/"
utils_folder = configurations +"/VBF_W/utils/"

signals = [c for c in samples if "WLNuJJ" in c]
#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
# mc = [skey for skey in samples]


aliases['lhesel'] = {
    'class': 'LHE_selection',
    'args': (),
     'linesToAdd' : [
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}macros/lhemjj.cc+'.format(utils_folder)
        ] 
} 
