import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-A", help="File A", type=str, )
parser.add_argument("-B", help="File B", type=str)
parser.add_argument("--ta", help="Title A", type=str)
parser.add_argument("--tb", help="Title B", type=str)
parser.add_argument("--cut", help="Cut", type=str)
parser.add_argument("--var", help="Var", type=str)
parser.add_argument("--sample", help="Var", type=str)
parser.add_argument("-o", "--output", help="Output", type=str)
parser.add_argument("--ns", "--normalise", dest = "normalise", help="Normalize shapes", action="store_true", default=False)
args = parser.parse_args()


import ROOT as R 

R.gROOT.SetBatch(1)
R.gStyle.SetOptStat(0)
fA = R.TFile(args.A)
fB = R.TFile(args.B)
hA = fA.Get(args.cut +"/"+ args.var +"/histo_"+ args.sample)


hB = fB.Get(args.cut +"/"+ args.var +"/histo_"+ args.sample)
hA.SetLineColor(R.kBlue)
hB.SetLineColor(R.kRed)


if args.normalise:
   hA.Scale(1./hA.Integral())
   hB.Scale(1./hB.Integral())

c = R.TCanvas("c1")
leg = R.TLegend(0.4,0.7,0.6,0.9)
leg.AddEntry(hA, args.ta, "l")
leg.AddEntry(hB, args.tb, "l")
hR1 = R.TRatioPlot(hA, hB, "divsym")
hA.GetXaxis().SetTitle(args.var)
hR1.Draw()
leg.Draw()
c.Draw()
c.SaveAs(args.output+"/{}_{}_{}.png".format(args.cut, args.var, args.sample))
