import os 
import sys
import CombineHarvester.CombineTools.ch as ch
import argparse
from itertools import combinations 
import ROOT
from copy import deepcopy

parser = argparse.ArgumentParser()
parser.add_argument("--dcs", help="Path to the datacards" , nargs="+", required=True)
parser.add_argument("--output", help="Path to the output folder" , type=str, required=True)
parser.add_argument("--ops", help="List of operators you want to compare the shapes" , nargs="+", required=False, default=[])
parser.add_argument("--add2BaseRegion", dest="append_to_regions", help="Add this string to the base regions definitions to match the files" , nargs="+", required=True)
parser.add_argument("--legend", dest="leglab", help="Legend to be shown for each file" , nargs="+", required=True)

args = parser.parse_args()

ROOT.gStyle.SetOptStat(0)

regexp_regions = [
   "res_wjetcr_ele",
   "res_wjetcr_mu", 
   "boost_wjetcr_ele", 
   "boost_wjetcr_mu",
   "res_topcr_ele",
   "res_topcr_mu",
   "boost_topcr_ele", 
   "boost_topcr_mu", 
   "boost_sig_ele_DNN_leq_0p5", 
   "boost_sig_mu_DNN_leq_0p5",
   "res_sig_ele_DNN_leq_0p5",
   "res_sig_mu_DNN_leq_0p5",
   "boost_sig_ele_DNN_geq_0p5",
   "boost_sig_mu_DNN_geq_0p5",
   "res_sig_ele_DNN_geq_0p5",
   "res_sig_mu_DNN_geq_0p5"
]

class canvMaker():

    count = 0
    def __init__(self):
        print("Initialized canvas handler")

    def getCanv(self):
        c = ROOT.TCanvas("c_{}".format(self.count), "c_{}".format(self.count), 700, 800)
        ROOT.gPad.SetFrameLineWidth(3)

        pad1 = ROOT.TPad("pad", "pad", 0, 0.3, 1, 1)
        pad1.SetFrameLineWidth(2)
        pad1.SetBottomMargin(0.005)
        pad1.Draw()

        pad2 = ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3)
        pad2.SetFrameLineWidth(2)
        pad2.SetTopMargin(0.05)

        pad2.SetFrameBorderMode(0)
        pad2.SetBorderMode(0)
        pad2.SetBottomMargin(0.4)
        pad2.Draw()

        self.count += 1

        return c, pad1, pad2


def getExpectedSigNames(pois):

    l = ["histo_sm"]
    for poi in pois:
        l.append("histo_sm_lin_quad_" + poi)
        l.append("histo_quad_" + poi)

    ppois = list(combinations(pois, 2))
    for ppair in ppois:
        l.append("histo_sm_lin_quad_mixed_" + ppair[0] + "_" + ppair[1])
        l.append("histo_sm_lin_quad_mixed_" + ppair[1] + "_" + ppair[0])

    return l

def mkdir(path):
   try:
      os.mkdir(path)
      os.system("cp /afs/cern.ch/user/g/gboldrin/index.php " + path)
   except:
      pass


##########################

if len(args.dcs) != 2:
    print("[ERROR] can only work with two datacards")
    sys.exit(0)

# if we want to filter EFT then this
if len(args.ops) != 0:
   shapes = getExpectedSigNames(args.ops)

mkdir(args.output)

# retrieve shapes
shapes_files = {}

for idx, dc in enumerate(args.dcs):

    print("----> idx: {} datacrds: {}".format(idx, dc))
    shapes_files[idx] = {}

    datacard_name = dc.split("/")[-1]
    os.system("cp " + dc  + " .")

    dr = ch.CombineHarvester()
    dr.ParseDatacard(datacard_name)


    regions = dr.bin_set()
    processes = dr.process_set()
    if len(args.ops) == 0:
       shapes = ["histo_" + procname for procname in processes]


    shapes_files[idx] = {k: "" for k in regions}
    current_shapes = shapes_files[idx]

    print(shapes_files)

    f = open(datacard_name, "r")
    contents = f.readlines()

    i = 0
    while any(current_shapes[k] == "" for k in regions):
    
        line = contents[i]
        for j in regions:
            if j in line:
                for entry in line.split(" "):
                    if os.path.isfile(entry):
                        current_shapes[j] = entry
                        i+= 1
                        continue
        i += 1

    os.system("rm " + datacard_name)
    f.close()



#print(shapes_files)


#sys.exit(0)
cm = canvMaker()

for reg in regexp_regions:

    f1 = ROOT.TFile(shapes_files[0][reg + args.append_to_regions[0]])
    f2 = ROOT.TFile(shapes_files[1][reg + args.append_to_regions[1]])
    outf = args.output + "/" + reg
    mkdir(outf)
    
    for sh_ in shapes:
        if sh_ not in [j.GetName() for j in f1.GetListOfKeys()]: continue

        h_sm = f1.Get(sh_)
        h_sm_1 = f2.Get(sh_)

        print(h_sm.Integral(), h_sm_1.Integral())

        h_sm.SetLineColor(ROOT.kAzure+1)
        h_sm_1.SetLineColor(ROOT.kOrange+1)


        h_sm.SetLineWidth(2)
        h_sm_1.SetLineWidth(2)
        
        h_bench = h_sm.Clone("bench")

        h_bench_one = h_sm.Clone("bench_1")
        h_bench_two = h_sm_1.Clone("bench_2")


        h_bench_one.Divide(h_bench)
        h_bench_two.Divide(h_bench)


        h_bench_one.SetFillStyle(3004)
        h_bench_one.SetFillColor(ROOT.kBlack)
        h_bench_one.SetLineWidth(2)
        h_bench_one.SetLineColor(ROOT.kBlack)


        h_sm.SetTitle("")
        h_sm_1.SetTitle("")


        h_sm.GetYaxis().SetTitle("Events")


        h_sm.GetYaxis().SetTitleSize(0.05)
        h_sm.GetYaxis().SetLabelSize(0.04)
        h_sm.GetYaxis().SetTitleOffset(1)
        h_sm.GetYaxis().SetMaxDigits(3)

        

        h_bench_one.SetTitle("")

        h_bench_one.GetXaxis().SetTitleSize(0.13)
        h_bench_one.GetYaxis().SetLabelSize(0.08)
        h_bench_one.GetXaxis().SetLabelSize(0.1)

        h_bench_one.GetYaxis().SetTitleSize(0.1)
        h_bench_one.GetYaxis().SetTitleOffset(0.5)
        h_bench_one.GetYaxis().SetNdivisions(4)

        h_bench_one.GetYaxis().SetTitle("Histo/Blue")

        h_bench_one.GetYaxis().SetRangeUser(0.4, 1.6)

        leg = ROOT.TLegend(0.89, 0.89, 0.6, 0.6)
        leg.SetBorderSize(0)
        leg.AddEntry(h_sm, args.leglab[0] + " {:.2f}".format(h_sm.Integral()), "F")
        leg.AddEntry(h_sm_1, args.leglab[1] + " {:.2f}".format(h_sm_1.Integral()), "F")


        c, pad1, pad2 = cm.getCanv()

        pad1.cd()
        h_sm.Draw("hist")
        h_sm_1.Draw("hist same")
        leg.Draw()
        pad1.SetLogy()


        pad2.cd()
        h_bench_one.Draw("E2")
        h_bench_two.Draw("P same")

        # c.cd()
        c.Draw()


        c.Print(outf + "/{}.png".format(sh_))
        c.Print(outf + "/{}.pdf".format(sh_))

    f1.Close()
    f2.Close()
