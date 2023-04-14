import numpy as np
import uproot

def normalize_weights(weights, nEvt):
    """
    Normalizes the input array of weights to the specified number of events.
    
    Parameters:
        weights (array-like): An array of weights.
        nEvt (int): The number of events to normalize the weights to.
    
    Returns:
        An array of normalized weights.
    """
    weights = np.array(weights)
    sumw = np.sum(weights)
    if sumw != 0:
        normalized_weights = (weights / sumw) * nEvt
    else:
        normalized_weights = np.zeros(len(weights))
    return normalized_weights

# Carica il file root contenente il tree "Events"
file1 = uproot.open("rootFile/plots_vbf_wNLO_2018.root")
tree1 = file1["HWJAll/dnn_inputs_all/tree_Wjets_HT_hardJets"]
tree2 = file1["HWJAll/dnn_inputs_all/tree_Wjets_NLO_hardJets"]

# Estrae il numero di eventi con i rispettivi pesi
# nevents1 = tree1.numentries
weights1 = tree1["genWeight"].array()
# xsec1 = tree1["Xsec"].array()[0]
xsec1 = 61526.7


# nevents2 = tree2.numentries
weights2 = tree2["genWeight"].array()
# xsec2 = tree2["Xsec"].array()[0]
xsec2 = 61526.7


weights1_norm = normalize_weights(weights1, len(weights1))
weights2_norm = normalize_weights(weights2, len(weights2))

weights1 = weights1_norm
weights2 = weights2_norm

# Calcola la somma dei pesi e la somma dei quadrati dei pesi per ogni sample
sum_weights1 = np.sum(weights1)
sum_weights2 = np.sum(weights2)

sum_weights2_squared = np.sum(weights2**2)
sum_weights1_squared = np.sum(weights1**2)

# Calcola la potenza statistica per ogni sample
# stat_power1 = sum_weights1**2 / sum_weights1_squared * xsec1
# stat_power2 = sum_weights2**2 / sum_weights2_squared * xsec2

# stat_power1 = sum_weights1**0.5
# stat_power2 = sum_weights2**0.5

stat_power1 = sum_weights1_squared**0.5
stat_power2 = sum_weights2_squared**0.5

# Stampa la potenza statistica di ogni sample
print("Sample 1 statistical power: ", stat_power1)
print("Sample 2 statistical power: ", stat_power2)