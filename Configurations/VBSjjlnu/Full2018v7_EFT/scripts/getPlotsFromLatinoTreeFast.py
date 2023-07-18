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
   parser.add_argument('-f', "--file",    dest='file',     help='the root file', required = True)
   parser.add_argument('-r', "--regions",    dest='regions',     help='Plot only these regions', required = False, nargs="+")
   parser.add_argument('-s', "--samples",    dest='samples',     help='Plot only these samples', required = False, nargs="+")
   parser.add_argument('-v', "--variables",    dest='variables',     help='Plot only these variables', required = False, nargs="+")
   parser.add_argument('-o', "--output",    dest='output',     help='name of the outoput folder that will store the plots. Default=tree_plots', required = False, default="tree_plots")
   parser.add_argument('-l', "--lumi",    dest='lumi',     help='Luminosity. Default=60', required = False, default=60., type=float)
   parser.add_argument('-ln', "--logy",    dest='logy',     help='Also plot logy', required = False, action="store_true")
   args = parser.parse_args()

   ROOT.gROOT.SetBatch(1)
   ROOT.TH1.SetDefaultSumw2(True)
   ROOT.gStyle.SetOptStat(0)

   f = ROOT.TFile(args.file)

   regions = [i.GetName() for i in f.GetListOfKeys()]

   try:
      os.mkdir(args.output)
      os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + args.output)
   except:
      print("Cannot create output")

   for reg in regions:
      
      if args.regions is not None and reg not in args.regions: continue

      d = f.Get(reg)

      try:
         os.mkdir(args.output + "/" + reg)
         os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + args.output + "/" + reg)
      except: pass
 
      var = [i.GetName() for i in d.GetListOfKeys()]
      for v in var:
         
         if args.variables is not None and v not in args.variables: continue
         # try:
         #    os.mkdir(args.output + "/" + reg + "/" + v)
         #    os.system("cp /afs/cern.ch/user/g/gboldrin/public/index.php " + args.output + "/" + reg + "/" + v)
         # except: pass

         hists = d.Get(v)
         shapes = [i.GetName() for i in hists.GetListOfKeys() if "Up" not in i.GetName() and "Down" not in i.GetName()]

         for sh in shapes:

            if args.samples is not None and sh.split("histo_")[1] not in args.samples: continue

            h = hists.Get(sh)
            h.SetDirectory(0)
             
            h.GetYaxis().SetTitle("Events")
            h.GetXaxis().SetTitle(v)
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
            
            
            c = ROOT.TCanvas("c_{}".format(sh), "c_{}".format(sh), 1000, 1000)
     
            leg = ROOT.TLegend(0.89, 0.89, 0.6, 0.6)
            leg.SetBorderSize(0)
           
            leg.AddEntry(h, sh.split("histo_")[1], "F")

            ROOT.gPad.SetFrameLineWidth(3)
            h.Draw("hist e")
            c.Update()
            leg.Draw()
            
            # Fancy stuff
            cms = drawCMS()
            simu = drawSimulation()
            prel = drawPreliminary()
            
            cms.Draw() 
            simu.Draw()
            prel.Draw()

            # Draw and save
            c.Draw()

            #c.Print( args.output + "/{}.png".format(s) )
            #c.Print( args.output + "/{}.pdf".format(s) )

            #c.SetLogy()
            c.Print( args.output + "/" + reg + "/{}_{}.png".format(v, sh) )
            c.Print( args.output + "/" + reg + "/{}_{}.pdf".format(v, sh) )

            if args.logy:
               c.SetLogy()
               c.Update()
               c.Draw()
               c.Print( args.output + "/" + reg + "/{}_{}_log.png".format(v, sh) )
               c.Print( args.output + "/" + reg + "/{}_{}_log.pdf".format(v, sh) )
