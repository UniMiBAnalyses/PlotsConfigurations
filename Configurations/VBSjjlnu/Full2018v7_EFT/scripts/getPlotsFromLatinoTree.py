import ROOT
import argparse
import os
import numpy as np
import json

def drawLumi(lumi):
   #Fancy stuffs
   tex3 = ROOT.TLatex(0.90,.915,"{:.1f}".format(lumi) + " fb^{-1} (13 TeV)")
   tex3.SetNDC()
   tex3.SetTextAlign(31)
   tex3.SetTextFont(42)
   tex3.SetTextSize(0.04)
   tex3.SetLineWidth(3)
   return tex3


def drawCMS():
   tex4 = ROOT.TLatex(0.27,.915, "CMS")
   tex4.SetNDC()
   tex4.SetTextAlign(31)
   tex4.SetTextFont(62)
   tex4.SetTextSize(0.045)
   tex4.SetLineWidth(3)
   return tex4


def drawSimulation():
   tex5 = ROOT.TLatex(0.45,.917, "Simulation")
   tex5.SetNDC()
   tex5.SetTextAlign(31)
   tex5.SetTextFont(52)
   tex5.SetTextSize(0.04)
   tex5.SetLineWidth(3)
   return tex5


def drawPreliminary():
   tex6 = ROOT.TLatex(0.64,.917, "Preliminary")
   tex6.SetNDC()
   tex6.SetTextAlign(31)
   tex6.SetTextFont(52)
   tex6.SetTextSize(0.04)
   tex6.SetLineWidth(3) 
   return tex6
   

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Command line parser for model testing')
   parser.add_argument('-f', "--file",    dest='file',     help='the root file with distributions of eFT reweighting weights', required = True)
   parser.add_argument('-c', "--cut",     dest='cut',      help='The name of the cut you want to compute quantiles on as expressed in the Latinos framework', required = True)
   parser.add_argument('-v', "--variable",    dest='variable',     help='The name of the variable TDrectory as defined in the variables.py', required = True)
   parser.add_argument('-s', "--sample",    dest='sample',     help='The name of the sample you want to extract the quantiles as defined in the samples.py', required = True)
   parser.add_argument('-o', "--output",    dest='output',     help='name of the outoput folder that will store the plots. Default=tree_plots', required = False, default="tree_plots")
   parser.add_argument('-l', "--lumi",    dest='lumi',     help='Luminosity. Default=60', required = False, default=60., type=float)
   args = parser.parse_args()

   ROOT.gROOT.SetBatch(1)
   ROOT.TH1.SetDefaultSumw2(True)
   ROOT.gStyle.SetOptStat(1111)

   f = ROOT.TFile(args.file)
   t = f.Get(args.cut + "/" + args.variable + "/tree_" + args.sample)

   shapes = [i.GetName() for i in t.GetListOfBranches()]
   
   if not os.path.isdir(args.output):
      os.mkdir(args.output)
   
   os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + args.output)

   for s in shapes:

      h = ROOT.TH1D("h_{}".format(s), "h_{}".format(s), 100, t.GetMinimum(s)-0.1, t.GetMaximum(s)+0.1)
      #h.GetXaxis().SetTitle("Weight")
      h.GetYaxis().SetTitle("Events")
      h.SetLineWidth(2)
      h.SetLineColor(ROOT.kBlack)
      
      h.GetYaxis().SetTitleSize(0.05)
      h.GetYaxis().SetLabelSize(0.04)
      h.GetYaxis().SetTitleOffset(1)
      
      h.GetXaxis().SetTitleSize(0.05)
      h.GetXaxis().SetLabelSize(0.04)
      h.GetXaxis().SetTitleOffset(0.9)
      
      h.GetYaxis().SetMaxDigits(3)
      h.SetTitle("")
      
      n = t.Draw("{} >> h_{}".format(s, s), "1==1")
      w = np.ndarray((n), 'd', t.GetV1())
      
      
      c = ROOT.TCanvas("c_{}".format(s), "c_{}".format(s), 1000, 1000)
      ROOT.gPad.SetFrameLineWidth(2)

      h.Draw("hist")
      c.Update()
      
      # Fancy stuff
      cms = drawCMS()
      simu = drawSimulation()
      prel = drawPreliminary()
      
      cms.Draw() 
      simu.Draw()
      prel.Draw()

      # Draw and save
      c.Draw()

      c.Print( args.output + "/{}.png".format(s) )
      c.Print( args.output + "/{}.pdf".format(s) )

      c.SetLogy()
      c.Print( args.output + "/{}_log.png".format(s) )
      c.Print( args.output + "/{}_log.pdf".format(s) )
         