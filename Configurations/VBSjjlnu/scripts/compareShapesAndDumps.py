import os 
import sys 
import argparse
from multiprocessing import Pool
import ROOT 
import numpy as np
from array import array
from itertools import combinations

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

def drawIt(item):
   cm = item["canvas"]
   try:
      shapes_file = ROOT.TFile(item["shape"]["file"])
      tree_file = ROOT.TFile(item["tree"]["file"])

      h_sm_1 = shapes_file.Get(item["shape"]["path"])
      h_sm_1.SetDirectory(0)

      t = tree_file.Get(item["tree"]["path"])

      # print("h_sm", "h_sm", len(item["tree"]["binedges"]), array('f', item["tree"]["binedges"]))
      h_sm = ROOT.TH1D("h_sm", "h_sm", len(item["tree"]["binedges"])-1, array('f', item["tree"]["binedges"]))
      n = t.Draw("{} >> h_sm".format(item["tree"]["var"]), "weight")

      h_sm.SetBinContent(1, h_sm.GetBinContent(0) +  h_sm.GetBinContent(1))
      h_sm.SetBinContent(0, 0)

      h_sm.SetBinContent(h_sm.GetNbinsX(), h_sm.GetBinContent(h_sm.GetNbinsX()) + h_sm.GetBinContent(h_sm.GetNbinsX() + 1))
      h_sm.SetBinContent(h_sm.GetNbinsX() + 1, 0.)



      h_sm.SetLineColor(ROOT.kAzure+1)
      h_sm_1.SetLineColor(ROOT.kOrange+1)


      h_sm.SetLineWidth(2)
      h_sm_1.SetLineWidth(2)
      
      #if abs(h_sm.Integral() - h_sm_1.Integral()) > 0.00001 :
      #    print("{} Draw: {:.20f} mkShapes: {:.20f}".format(component, h_sm.Integral(), h_sm_1.Integral()))


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

      h_bench_one.GetYaxis().SetRangeUser(0.99, 1.01)


      leg = ROOT.TLegend(0.89, 0.89, 0.6, 0.6)
      leg.SetBorderSize(0)
      leg.AddEntry(h_sm, "{} Draw".format(item["component"]), "F")
      leg.AddEntry(h_sm_1, "{} Shapes".format(item["component"]), "F")


      c, pad1, pad2 = cm.getCanv()

      pad1.cd()
      h_sm.Draw("hist")
      h_sm_1.Draw("hist same")
      leg.Draw()
      pad1.SetLogy()

      pad2.cd()
      h_bench_one.Draw("E2")
      h_bench_two.Draw("P same")

      c.cd()
      c.Draw()

      c.Print(item["output"] + ".png")
      c.Print(item["output"] + ".pdf")

   except: pass
   

def mkdir(path):
   try:
      os.mkdir(path)
      os.system("cp /afs/cern.ch/user/g/gboldrin/index.php " + path)
   except:
      pass


parser = argparse.ArgumentParser()
parser.add_argument("-o","--output", help="output directory where to store the plots" , type=str, required=True)
parser.add_argument("--tree", help="Path to the file with the trees (from mkShapesMulti)" , type=str, required=True)
parser.add_argument("--shapes", help="Path to the file with the shapes (from mkShapesMulti)" , type=str, required=True)
parser.add_argument("--vshapes", help="The variable to be compared taken from the shapes file." , type=str, required=True)
parser.add_argument("--tshapes", help="The variables to be compared taken from the tree file." , type=str, required=True)
parser.add_argument("--binedges", help="The bin edges for the tree variable" , nargs="+", required=True)
parser.add_argument("--nProc", help="Number of processes for parallel" , type=int, required=False)
args = parser.parse_args()

if __name__ == "__main__":

   # first create output dir
   mkdir(args.output)

   # object to be passed to the multithread function

   plot_dict = []
   # grab the regions
   f = ROOT.TFile(args.tree)
   regions = [i.GetName() for i in f.GetListOfKeys()] 

   # grab the shapes
   f_shapes = ROOT.TFile(args.shapes)


   comb = list(combinations( ["cHB", "cHl1", "cHj1", "cHQ1", "cHWB", "cW", "cHbox", "cHW"] , 2))
   
   components = []
   
   for op in ["cHB", "cHl1", "cHj1", "cHQ1", "cHWB", "cW", "cHbox", "cHW"]:
       components.append("quad_" + op)
       components.append("sm_lin_quad_" + op)
       
   for c in comb:
       components.append("sm_lin_quad_mixed_" + c[0] + "_" + c[1])
       components.append("sm_lin_quad_mixed_" + c[1] + "_" + c[0])
       
       
   components.append("sm")

   plots = []

   cm = canvMaker()

   for reg in regions:

      mkdir(args.output + "/" + reg)

      if "boost" in reg: subt = "dnn_inputs_boosted"
      elif "res" in reg: subt = "dnn_inputs_resolved"

      for component in components:
         
         plots.append(
	 	{
			"shape": {
				"file": args.shapes,
				"path": reg + "/" + args.vshapes + "/histo_" + component,
			},
     			"tree": {
				"file": args.tree,
				"path": reg + "/" + subt + "/" + "tree_" + component,
                                "var": args.tshapes,
                                "binedges": [float(i) for i in args.binedges]
			},
			"output": args.output + "/" + reg + "/" + component + "_" + args.vshapes,
			"component": component,
			"canvas": cm,
                }
	 )


   nproc = len(plots) if len(plots) < 8 else 8
   if args.nProc: nproc = args.nProc
   pool = Pool(processes=nproc)
   pool.map(drawIt, plots)
   drawIt(plots[0])

