# structure configuration for datacard
from itertools import product, chain
#structure = {}

signals = [c for c in samples if "WLNuJJ" in c]
for i in signals:
    structure['{}'.format(i)] = {
                    'isSignal' : 1,
                    'isData'   : 0 
             }


