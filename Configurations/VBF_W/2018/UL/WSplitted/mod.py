import ROOT
import os
import numpy as np
import time

f = ROOT.TFile("/afs/cern.ch/user/a/abulla/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBF_W/2018/rootFile/charge_final_v2/fixed_plots_vbf_w_2018charge_final_v2.root", "UPDATE")

tomodify = {
    "ele_HWJ_minus": ["Wjets_HT_hardJets", "Fake"],
    "ele_SR_minus": ["Fake"]
}

for region in tomodify:
    print("Processing region {}...".format(region))

    if "SR" in region:
        var = "DNN0p5Joined10"
    else:
        var = "highDNN0p5events"

    region_plus = region.replace("minus", "plus")

    histo_data_minus = f.Get("{}/{}/histo_DATA".format(region,var))
    histo_data_plus  = f.Get("{}/{}/histo_DATA".format(region_plus,var))

    dir_minus = f.Get("{}/{}".format(region,var))
    dir_plus  = f.Get("{}/{}".format(region_plus,var))

    print(dir_minus)
    print(region)
    print(var)

    keys = [k.GetName() for k in dir_minus.GetListOfKeys()]

    for sample in tomodify[region]:

        histo_plus_nominal = dir_plus.Get("histo_{}".format(sample))

        SF = []

        for i in range(1, histo_plus_nominal.GetNbinsX()+1):

            data_plus = histo_data_plus.GetBinContent(i)
            mc_plus   = histo_plus_nominal.GetBinContent(i)

            if data_plus > 0:
                sf = mc_plus / data_plus
            else:
                sf = 0.0

            SF.append(sf)

        print("Mean SF for {} {}: {}".format(region, sample, np.mean(SF)))

        for name in keys:

            if not name.startswith("histo_{}".format(sample)):
                continue

            histo_to_modify = dir_minus.Get(name)

            for i in range(1, histo_to_modify.GetNbinsX()+1):

                data_minus = histo_data_minus.GetBinContent(i)
                data_err   = histo_data_minus.GetBinError(i)

                histo_to_modify.SetBinContent(i, data_minus * SF[i-1])
                histo_to_modify.SetBinError(i, data_err * SF[i-1])

            dir_minus.cd()
            histo_to_modify.Write(name, ROOT.TObject.kOverwrite)

f.Close()