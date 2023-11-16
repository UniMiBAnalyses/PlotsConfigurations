import ROOT as R
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("-s","--sample", help="Sample", type=str, default="*")
parser.add_argument("-n","--nuisances", help="Nuisances", type=str, nargs="+")
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

# print(args.input)

samples = ['top', 'DY', 'VBF-V_dipole', 'VV_osWW', 'VV_ssWW', 'VV_WZjj', 'VV_WZll', 'VV_ZZ', 'VVV', 'Vg', 'VgS', 'ggWW', 'Wjets_res_1', 'Wjets_res_2', 'Wjets_res_3', 'Wjets_res_4', 'Wjets_res_5', 'Wjets_res_6', 'Wjets_res_7', 'Wjets_res_8', 'Wjets_res_9', 'Wjets_res_10', 'Wjets_res_11', 'Wjets_res_12', 'Wjets_res_13', 'Wjets_res_14', 'Wjets_res_15', 'Wjets_res_16', 'Wjets_res_17', 'Wjets_res_18', 'Wjets_res_19', 'Wjets_res_20', 'Wjets_res_21', 'Wjets_boost_1', 'Wjets_boost_2', 'Wjets_boost_3', 'Wjets_boost_4', 'Wjets_boost_5', 'Wjets_boost_6', 'Wjets_boost_7']

#f.ls()
for k in f.GetListOfKeys():
    #print(k)
    fO.mkdir(k.GetName())
    d = f.Get(k.GetName())
    for z in d.GetListOfKeys():
        if args.vars and z.GetName() not in args.vars:
            continue
        v = d.Get(z.GetName())
        fO.mkdir(k.GetName() + "/" + z.GetName())
        # print("Faccio cd... in " + k.GetName() + "/" + z.GetName())
        fO.Cd(k.GetName() + "/" + z.GetName())
        #print(z)
        # print ">>> ", k.GetName(), z.GetName()
    
        for s in v.GetListOfKeys():
            for sample in samples:
               if s.GetName() != "histo_" + sample and "_" + sample + "_" in s.GetName():
                  #print(s.GetName(), sample)
                  nuis = s.GetName().split("histo_" + sample + "_")[1]
                  if nuis in args.nuisances and ( sample in s.GetName() or sample == "*"):
                     # print(s.GetName(), s.GetName() in args.nuisances, args.sample in s.GetName() or args.sample == "*") 
                     continue

                  # check if we have the nuisance already
                  v2 = fO.Get(k.GetName() + "/" + z.GetName())
                  if s.GetName() in [i.GetName() for i in v2.GetListOfKeys()]: 
                     print(s.GetName())
                     continue

               # if args.nuisances in s.GetName() and ( args.sample in s.GetName() or args.sample == "*"): continue
               h = f.Get(k.GetName() + "/" + z.GetName() + "/" + s.GetName())
               h.SetDirectory(0)
               h.Write()

        fO.Cd("../")
        R.gDirectory.Cd("../")
    
    fO.Cd("../")
    R.gDirectory.Cd("../")

fO.Write()
fO.Close()
