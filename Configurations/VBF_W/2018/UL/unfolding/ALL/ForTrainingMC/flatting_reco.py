import uproot
import numpy as np


genbinmap = {
    "mjj": {
        "bins": [300, 850, 1000, 1200, 1400, 1600, 2000, 2500, 1000000],
        "gen": "mjj_gen"
    },
    "pt1": {
        "bins": [20, 30, 40, 50, 60, 70, 80, 100, 150, 1000000],
        "gen": "DressedLepton_pt1"
    },
    "detajj": {
        "bins": [4.0, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.5, 6, 10],
        "gen" : "detajj_gen"
    },
    "ptW": {
        "bins": [0,30,60,90,120,180,10000],
        "gen": "ptW_gen",
    },
    "ptjj": {
        "bins": [0,30,50,75,100,130,180,10000],
        "gen" : "ptjj_gen",
    },
    "jetpt1": {
        "bins": [60,110,140,180,230,300,10000],
        "gen" : "CleanGenJet_pt1",
    },
    "jetpt2": {
        "bins": [60, 80, 100, 130, 170, 230, 10000],
        "gen" : "CleanGenJet_pt2",
    },
    "nCleanJet30": {
        "bins": [1.5, 2.5, 3.5, 10.5],
        "gen" : "nCleanGenJet20",
    },
    "Dphijet1jet2": {
        "bins": [0, 2.0, 2.4, 2.6, 2.8, 3.0, 3.2],
        "gen" : "Dphijet1jet2_gen",
    },
    "eta1": {
        "bins": [0.0, 0.15, 0.3, 0.5, 0.65, 0.8, 1.0, 1.2, 1.4, 1.7, 2.0],
        "gen" : "lepeta_gen_abs",
    },
    "jeteta1": {
        "bins": [0.0, 0.9, 1.3, 1.7, 2.0, 2.2, 2.4, 3.0, 3.3, 3.6, 5.0],
        "gen" : "jeteta1_gen_abs",
    },
    "jeteta2": {
        "bins": [0.0, 1.3, 1.8, 2.1, 2.3, 3.0, 3.2, 3.4, 3.6, 3.85, 5.0],
        "gen" : "jeteta2_gen_abs",
    },
}

import numpy as np

def weighted_quantile(values, weights, quantiles):
    """
    Compute weighted quantiles
    quantiles: array in [0,1]
    """
    sorter = np.argsort(values)
    values = values[sorter]
    weights = weights[sorter]

    cdf = np.cumsum(weights)
    cdf = cdf / cdf[-1]

    return np.interp(quantiles, cdf, values)

def compute_quantile_bins(values, weights, nbins=3):

    if len(values) < 10:
        return None

    # rimuovi roba non valida
    mask = np.isfinite(values) & np.isfinite(weights) & (weights > 0)
    values = values[mask]
    weights = weights[mask]

    if len(values) < 10:
        return None

    qs = np.linspace(0, 1, nbins + 1)
    edges = weighted_quantile(values, weights, qs)

    edges = np.unique(edges)

    if len(edges) < nbins + 1:
        return None

    return edges


def process_file(rootfile, genbinmap):

    f = uproot.open(rootfile)

    tree = f["SR/dnn_inputs_all/tree_WLNuJJ"]

    results = {}

    for var, cfg in genbinmap.items():

        print(f"\n=== {var} ===")

        gen_var  = cfg["gen"]
        reco_var = var
        bins     = cfg["bins"]

        if gen_var not in tree.keys() or reco_var not in tree.keys():
            print(f"  -> missing {gen_var} or {reco_var}")
            continue

        arr = tree.arrays([gen_var, reco_var, "weight"], library="np")

        gen    = arr[gen_var]
        reco   = arr[reco_var]
        weight = arr["weight"]

        results[var] = {}

        for i in range(len(bins) - 1):

            gmin = bins[i]
            gmax = bins[i+1]

            mask = (gen >= gmin) & (gen < gmax)

            mask_reco = (reco >= gmin) & (reco < gmax)
            mask_tot = mask & mask_reco

            reco_sel = reco[mask_tot]
            weight_sel = weight[mask_tot]

            if len(reco_sel) < 50:
                continue

            ### qui ne scelgo 3!!!!
            edges = compute_quantile_bins(reco_sel, weight_sel, nbins=3)

            if edges is None:
                continue

            key = f"{gmin}_{gmax}"

            results[var][key] = {
                "edges": edges.tolist(),
                "nevents": int(len(reco_sel)),
                "sumw": float(np.sum(weight_sel))
            }

            print(f"  gen [{gmin}, {gmax}] -> {edges}")

    return results


results = process_file("/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/rootFile/TrainingMC_newWP_geninfo_v10/file.root", genbinmap)