import ROOT
import argparse
import os
import numpy as np
import json

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


def getLegend(pos="upperright"):
    if pos == "upperright":
        leg = ROOT.TLegend(0.4, 0.6, 0.89, 0.86)
        leg.SetBorderSize(0)
        leg.SetNColumns(1)
        leg.SetTextSize(0.035)
    elif pos == "lowerright":
        leg = ROOT.TLegend(0.4, 0.14, 0.89, 0.4)
        leg.SetBorderSize(0)
        leg.SetNColumns(1)
        leg.SetTextSize(0.035)
        
    elif pos == "lowerleft":
        leg = ROOT.TLegend(0.4, 0.6, 0.89, 0.86)
        leg.SetBorderSize(0)
        leg.SetNColumns(1)
        leg.SetTextSize(0.035)
    elif pos == "upperleft":
        leg = ROOT.TLegend(0.4, 0.6, 0.89, 0.86)
        leg.SetBorderSize(0)
        leg.SetNColumns(1)
        leg.SetTextSize(0.035)
    
    return leg

def getDefaultRatio(default, ratio_range):
   
   h_bench = default.Clone("clone")
   h_bench.Divide(default)
   h_bench.SetFillStyle(3004)
   h_bench.SetFillColor(ROOT.kBlack)
   h_bench.SetLineWidth(2)
   h_bench.SetLineColor(ROOT.kBlack)
   h_bench.GetXaxis().SetTitleSize(0.13)
   h_bench.GetYaxis().SetLabelSize(0.08)
   h_bench.GetXaxis().SetLabelSize(0.1)

   h_bench.GetYaxis().SetTitleSize(0.1)
   h_bench.GetYaxis().SetTitleOffset(0.5)
   h_bench.GetYaxis().SetNdivisions(4)

   h_bench.GetYaxis().SetRangeUser(ratio_range[0],ratio_range[1])

   h_bench.SetLineColor(ROOT.kBlack)
   
   return h_bench

def getRatio(numerator, denominator):
    
   h_alt = numerator.Clone("clone")
   h_alt.Divide(denominator)
    
   return h_alt

def drawLumi(lumi):
   #Fancy stuffs
   tex3 = ROOT.TLatex(0.90,.915,"{:.1f}".format(lumi) + " fb^{-1} (13 TeV)")
   tex3.SetNDC()
   tex3.SetTextAlign(31)
   tex3.SetTextFont(42)
   tex3.SetTextSize(0.05)
   tex3.SetLineWidth(3)
   return tex3


def drawCMS():
   tex4 = ROOT.TLatex(0.27,.915, "CMS")
   tex4.SetNDC()
   tex4.SetTextAlign(31)
   tex4.SetTextFont(62)
   tex4.SetTextSize(0.06)
   tex4.SetLineWidth(3)
   return tex4


def drawSimulation():
   tex5 = ROOT.TLatex(0.45,.917, "Simulation")
   tex5.SetNDC()
   tex5.SetTextAlign(31)
   tex5.SetTextFont(52)
   tex5.SetTextSize(0.048)
   tex5.SetLineWidth(3)
   return tex5


def drawPreliminary():
   tex6 = ROOT.TLatex(0.64,.917, "Preliminary")
   tex6.SetNDC()
   tex6.SetTextAlign(31)
   tex6.SetTextFont(52)
   tex6.SetTextSize(0.048)
   tex6.SetLineWidth(3) 
   return tex6
   

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Command line parser for model testing')
   parser.add_argument('-f', "--file",    dest='file',     help='the root file with distributions of eFT reweighting weights', required = True)
   parser.add_argument('-s', "--samples",    dest='samples',     help='The name of the sample you want to extract the quantiles as defined in the samples.py', required = True, nargs="+")
   parser.add_argument('-o', "--output",    dest='output',     help='name of the outoput folder that will store the plots. Default=tree_plots', required = False, default="tree_plots")
   parser.add_argument('-l', "--lumi",    dest='lumi',     help='Luminosity. Default=60', required = False, default=60., type=float)
   parser.add_argument('-int', "--show-integral",    dest='integral',     help='Show integral in legend', required = False, default=False, action="store_true")
   args = parser.parse_args()

   ROOT.gROOT.SetBatch(1)
   ROOT.TH1.SetDefaultSumw2(True)
   ROOT.gStyle.SetOptStat(0)

   ratio_range = [0.7,1.3]
   showIntegral = True

   cm = canvMaker()

   f = ROOT.TFile(args.file)
   regions = [i.GetName() for i in f.GetListOfKeys()]

   if not os.path.isdir(args.output):
      os.mkdir(args.output)
   
   os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + args.output)

   for reg in regions:
      print(reg)
      d = f.Get(reg)
      variables = [i.GetName() for i in d.GetListOfKeys()]

      for var in variables:
         print(var)
         d_ = d.Get(var)

         c, pad1, pad2 = cm.getCanv()
         leg = getLegend("upperright") 

         histos = []

         print([i.GetName() for i in d_.GetListOfKeys()])

         for idx, s in enumerate(args.samples):
            h = d_.Get("histo_" + s)

            print s, h.Integral()

            h.SetLineColor(idx+1)
            
            h.GetYaxis().SetTitle("Events")
            h.SetLineWidth(2)
            h.SetMinimum(0)
            
            h.GetYaxis().SetTitleSize(0.05)
            h.GetYaxis().SetLabelSize(0.04)
            h.GetYaxis().SetTitleOffset(1)
            
            h.GetXaxis().SetTitleSize(0.05)
            h.GetXaxis().SetLabelSize(0.04)
            h.GetXaxis().SetTitleOffset(0.9)
            
            h.GetYaxis().SetMaxDigits(3)
            h.SetTitle("")

            histos.append(h)
         
         pad1.cd()
         histos[0].Draw("hist e")

         if len(histos) > 1:
            for h_ in histos[1:]: h_.Draw("hist same")

         for hist, sample in zip(histos, args.samples):
            name = sample + " [{:.2f}]".format(hist.Integral()) if args.integral else sample
            leg.AddEntry(hist, name , "F")

         # Fancy stuff
         cms = drawCMS()
         simu = drawSimulation()
         prel = drawPreliminary()
            
         cms.Draw() 
         simu.Draw()
         prel.Draw()

         leg.Draw()

         pad2.cd()

         bench = getDefaultRatio(histos[0], ratio_range)
         bench.SetMarkerSize(0)
         bench.GetYaxis().SetTitle("Ratio")
         bench.GetXaxis().SetTitle(var)

         bench.Draw("E2")

         ratios = []

         if len(histos) > 1:
            for h_ in histos[1:]:
               ratio = getRatio(h_, histos[0])
               ratios.append(ratio)
               
         for h in ratios:    
            h.Draw("hist same")


         # Draw and save
         c.Draw()

         c.Print( args.output + "/{}_{}.png".format(reg, var) )
         c.Print( args.output + "/{}_{}.pdf".format(reg, var) )

         c.SetLogy()
         c.Print( args.output + "/{}_{}_log.png".format(reg, var) )
         c.Print( args.output + "/{}_{}_log.pdf".format(reg, var) )
         
