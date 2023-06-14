import ROOT 
import sys


if len(sys.argv) < 2:
   print("Usage python scripts/addNegativeLinQuad.py <root file>")
   sys.exit(0)

ops = ["cW", "cHW", "cHWB", "cHbox", "cHB", "cHl1", "cHQ1", "cHj1"]
f = ROOT.TFile(sys.argv[1], "UPDATE")

for region in [i.GetName() for i in f.GetListOfKeys()]:
    print("-->Region: ", region)
    d = f.Get(region)
    f.cd(region)

    for var in [j.GetName() for j in d.GetListOfKeys()]:
        print("--> Var: " + var)
        d_ = d.Get(var)
        f.cd(region + "/" + var)

        for shape in ["lin", "quad"]:
            for op in ops:

                s_ = "histo_" + shape + "_" + op 
                new_s_ = "histo_" + shape + "m1_" + op 

                h = d_.Get(s_)
                h2 = h.Clone(new_s_)
                h2.Scale(-1)
                h2.SetName(new_s_)

                h2.Write(new_s_)

f.Close()
