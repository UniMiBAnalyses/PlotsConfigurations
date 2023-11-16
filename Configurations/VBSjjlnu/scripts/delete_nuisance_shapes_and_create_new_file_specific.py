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

samples = ['sm', 'top', 'DY', 'VBF-V_dipole', 'VV_osWW', 'VV_ssWW', 'VV_WZjj', 'VV_WZll', 'VV_ZZ', 'VVV', 'Vg', 'VgS', 'ggWW', 'Wjets_res_1', 'Wjets_res_2', 'Wjets_res_3', 'Wjets_res_4', 'Wjets_res_5', 'Wjets_res_6', 'Wjets_res_7', 'Wjets_res_8', 'Wjets_res_9', 'Wjets_res_10', 'Wjets_res_11', 'Wjets_res_12', 'Wjets_res_13', 'Wjets_res_14', 'Wjets_res_15', 'Wjets_res_16', 'Wjets_res_17', 'Wjets_res_18', 'Wjets_res_19', 'Wjets_res_20', 'Wjets_res_21', 'Wjets_boost_1', 'Wjets_boost_2', 'Wjets_boost_3', 'Wjets_boost_4', 'Wjets_boost_5', 'Wjets_boost_6', 'Wjets_boost_7']


to_ignore = []
for s in samples:
   for nuis in args.nuisances:
      to_ignore.append("histo_" + s + "_" + nuis)


#f.ls()
for idx, k in enumerate(f.GetListOfKeys()):
    print("--> " + k.GetName() + " {}/{}".format(idx, len([i.GetName() for i in f.GetListOfKeys()]))) 
    fO.mkdir(k.GetName())
    d = f.Get(k.GetName())
    for idx2, z in enumerate(d.GetListOfKeys()):
        print("{}/{} {}".format(idx2, len([i.GetName() for i in d.GetListOfKeys()]), z.GetName() ))
        if args.vars and z.GetName() not in args.vars:
            continue
        v = d.Get(z.GetName())
        fO.mkdir(k.GetName() + "/" + z.GetName())
        # print("Faccio cd... in " + k.GetName() + "/" + z.GetName())
        fO.Cd(k.GetName() + "/" + z.GetName())
        #print(z)
        # print ">>> ", k.GetName(), z.GetName()
    
        for s in v.GetListOfKeys():

            if s.GetName() not in to_ignore:
               h = f.Get(k.GetName() + "/" + z.GetName() + "/" + s.GetName())
               h.SetDirectory(0)
               h.Write()


        fO.Cd("../")
        R.gDirectory.Cd("../")
    
    fO.Cd("../")
    R.gDirectory.Cd("../")

fO.Write()
fO.Close()
