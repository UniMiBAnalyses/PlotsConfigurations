import ROOT
import json
import numpy as np
import sys


# ---------------------------------
# Measure scale factor
# ---------------------------------
def measure_sf(file, region_measure, var, sample, mode):

    histo_data = file.Get("{}/{}/histo_DATA".format(region_measure, var))
    histo_mc   = file.Get("{}/{}/histo_{}".format(region_measure, var, sample))

    if not histo_data or not histo_mc:
        raise RuntimeError(
            "Missing histogram for measurement: {}/{}/{}".format(
                region_measure, var, sample
            )
        )

    if mode == "integral":

        data = histo_data.Integral()
        mc   = histo_mc.Integral()

        if data > 0:
            sf = mc / data
        else:
            sf = 0.0

        print "Integral SF ({}, {}) = {}".format(region_measure, sample, sf)

        return sf

    elif mode == "differential":

        SF = []

        for i in range(1, histo_mc.GetNbinsX()+1):

            data = histo_data.GetBinContent(i)
            mc   = histo_mc.GetBinContent(i)

            if data > 0:
                SF.append(mc/data)
            else:
                SF.append(0.0)

        print "Differential SF mean ({}, {}) = {}".format(
            region_measure, sample, np.mean(SF)
        )

        return SF

    else:
        raise RuntimeError("mode must be 'integral' or 'differential'")


# ---------------------------------
# Apply differential SF
# ---------------------------------
def apply_sf(file, region, var, sample, SF):

    dir_ = file.Get("{}/{}".format(region, var))
    histo_data = file.Get("{}/{}/histo_DATA".format(region, var))

    if not dir_:
        raise RuntimeError("Directory not found: {}/{}".format(region, var))

    # ------------------------------
    # find nominal
    # ------------------------------
    histo_nominal = dir_.Get("histo_{}".format(sample))

    if not histo_nominal:
        raise RuntimeError("Nominal histogram not found for sample {}".format(sample))

    # ------------------------------
    # compute SF2 to apply to nominal + systs
    # ------------------------------
    SF2 = []

    for i in range(1, histo_nominal.GetNbinsX()+1):

        nom_old = histo_nominal.GetBinContent(i)
        data    = histo_data.GetBinContent(i)

        nom_new = data * SF[i-1]

        if nom_old > 0:
            sf2 = nom_new / nom_old
        else:
            sf2 = 0.0

        SF2.append(sf2)

    # ------------------------------
    # apply to nominal + systs
    # ------------------------------
    keys = [k.GetName() for k in dir_.GetListOfKeys()]

    for name in keys:

        if not name.startswith("histo_{}".format(sample)):
            continue

        hist = dir_.Get(name)

        for i in range(1, hist.GetNbinsX()+1):

            content = hist.GetBinContent(i)
            error   = hist.GetBinError(i)

            hist.SetBinContent(i, content * SF2[i-1])
            hist.SetBinError(i, error * SF2[i-1])

        dir_.cd()
        hist.Write(name, ROOT.TObject.kOverwrite)


# ---------------------------------
# Apply fixed SF
# ---------------------------------
def apply_fixed_sf(file, region, var, sample, sf):

    dir_ = file.Get("{}/{}".format(region, var))

    if not dir_:
        raise RuntimeError("Directory not found: {}/{}".format(region, var))

    keys = [k.GetName() for k in dir_.GetListOfKeys()]

    for name in keys:

        if not name.startswith("histo_{}".format(sample)):
            continue

        hist = dir_.Get(name)

        for i in range(1, hist.GetNbinsX()+1):

            hist.SetBinContent(i, hist.GetBinContent(i) * sf)
            hist.SetBinError(i, hist.GetBinError(i) * sf)

        dir_.cd()
        hist.Write(name, ROOT.TObject.kOverwrite)


# ---------------------------------
# Main
# ---------------------------------
def run(config_file):

    with open(config_file) as f:
        cfg = json.load(f)

    rootfile = ROOT.TFile(cfg["file"], "UPDATE")
    
    if not rootfile or rootfile.IsZombie():
        raise RuntimeError("Could not open ROOT file: {}".format(cfg["file"]))
        exit(1)


    for op in cfg["operations"]:

        regions = op["regions"]
        samples = op["samples"]
        vars_   = op["vars"]
        action  = op["action"]["applySF"]

        for region in regions:

            for var in vars_:

                for sample in samples:

                    print "\nProcessing:", region, var, sample

                    # -------------------------
                    # Fixed SF
                    # -------------------------
                    if isinstance(action, (int, float)):

                        print "Applying fixed SF =", action

                        apply_fixed_sf(
                            rootfile,
                            region,
                            var,
                            sample,
                            action
                        )

                    # -------------------------
                    # Measured SF
                    # -------------------------
                    elif isinstance(action, dict):

                        if "measureFrom" not in action:
                            raise RuntimeError(
                                "applySF measure mode requires 'measureFrom'"
                            )

                        measure_region = action["measureFrom"]
                        mode = action.get("mode", "differential")

                        sf = measure_sf(
                            rootfile,
                            measure_region,
                            var,
                            sample,
                            mode
                        )

                        if mode == "integral":

                            apply_fixed_sf(
                                rootfile,
                                region,
                                var,
                                sample,
                                sf
                            )

                        else:

                            apply_sf(
                                rootfile,
                                region,
                                var,
                                sample,
                                sf
                            )

                    else:
                        raise RuntimeError(
                            "applySF must be a number or {measureFrom, mode}"
                        )

    rootfile.Close()


# ---------------------------------
# Entry
# ---------------------------------code 
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Usage: python applySF.py config.json"
        sys.exit(1)

    run(sys.argv[1])