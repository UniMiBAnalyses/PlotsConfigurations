import ROOT as R
import sys

f = R.TFile(sys.argv[1], "UPDATE")

print("--> Starting")
for k in f.GetListOfKeys():
    print("--> " + k.GetName())
    R.gDirectory.Cd(k.GetName())
    R.gDirectory.Delete(sys.argv[2]+";*")

    R.gDirectory.Cd("../")
    print("-->Done")

f.Write()
f.Close()
