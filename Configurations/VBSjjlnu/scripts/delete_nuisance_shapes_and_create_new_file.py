import ROOT as R
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("-s","--sample", help="Sample", type=str, default="*")
parser.add_argument("-n","--nuisances", help="Nuisances", type=str)
parser.add_argument("-vars","--vars", help="Vars", type=str, nargs="+")
parser.add_argument("-o","--output", help="Output file", type=str)
args = parser.parse_args()


f = R.TFile(args.input, "READ")
fO = R.TFile(args.output, "RECREATE")

# samples = ['VBS','top','DATA','Fake','Wjets_HT','VVV','VV','VgS','Vg','DY','VBF-V','ggWW']
# samples = []
# for ir in range(1,22):
#     samples.append("Wjets_res_"+str(ir))
# for ir in range(1,8):
#     samples.append("Wjets_boost_"+str(ir))


    #f.ls()
for k in f.GetListOfKeys():
    #print(k)
    fO.mkdir(k.GetName())
    d = f.Get(k.GetName())
    print(d)
    for z in d.GetListOfKeys():
        if args.vars and z.GetName() not in args.vars:
            continue
        v = d.Get(z.GetName())
        fO.mkdir(k.GetName() + "/" + z.GetName())
        print("Faccio cd... in " + k.GetName() + "/" + z.GetName())
        fO.Cd(k.GetName() + "/" + z.GetName())
        #print(z)
        print ">>> ", k.GetName(), z.GetName()
    
        for s in v.GetListOfKeys():
            #if "CMS_PS_FSR_VBS_ZV" in s.GetName() : print("Ciao")
            if "CMS_PS_ISR_VBS_ZV" in s.GetName(): print("Ciao")
            if args.nuisances in s.GetName() and ( args.sample in s.GetName() or args.sample == "*"): continue
            h = f.Get(k.GetName() + "/" + z.GetName() + "/" + s.GetName())
            h.SetDirectory(0)
            h.Write()

        fO.Cd("../")
        R.gDirectory.Cd("../")
    
    fO.Cd("../")
    R.gDirectory.Cd("../")

fO.Write()
fO.Close()
