import ROOT 
ROOT.TH1.SetDefaultSumw2()
import argparse 
import sys
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="input file", type=str)
parser.add_argument("-o","--output", help="output file", type=str)
parser.add_argument("-m","--merge", help="Merge these regions in format new_name:reg1,reg2 new_name:reg3,reg4", type=str, nargs="+")
parser.add_argument("-v","--variables", help="merge only these variables", type=str, nargs="+")
parser.add_argument("--copy", dest="copy", help="Copy unmerged regions.", default="False", action="store_true")
parser.add_argument("--include-old", dest="includeold", help="Also include old regions before merging", default="False", action="store_true")
args = parser.parse_args()

if __name__ == "__main__":

   # --merge new_name:reg1,reg2 new_name:reg3,reg4 ...

   start = datetime.now()

   merge_pattern = {}
   ignore_regions = []
   for entry in args.merge:
      new_name = entry.split(":")[0]
      regions = entry.split(":")[1].split(",")
      ignore_regions += regions
      merge_pattern[new_name] = regions
 

   print(merge_pattern)
   print(ignore_regions)

   to_be_merged = {}
   to_not_merge = {}

   f = ROOT.TFile(args.input, "READ")
   
   regions = [i.GetName() for i in f.GetListOfKeys()]
   not_merged = [i for i in regions if i not in ignore_regions]
   if args.includeold: not_merged += ignore_regions
  
   for new_region in merge_pattern.keys():
      to_be_merged[new_region] = {}
      for r in merge_pattern[new_region]:
         to_be_merged[new_region][r] = {}
         for v in args.variables:
            d_ = f.Get(r)
            vars = [i.GetName() for i in d_.GetListOfKeys()]
            if v not in vars: continue
            d = f.Get(r + "/" + v)
            
            print(v, r)
            to_be_merged[new_region][r][v] = {}
         
            d = f.Get(r + "/" + v)
            for hist in [i.GetName() for i in d.GetListOfKeys()]:
                to_be_merged[new_region][r][v][hist] = d.Get(hist).Clone()

   for region in not_merged:
      to_not_merge[region] = {}
      for v in args.variables:
         d_ = f.Get(region)
         vars = [i.GetName() for i in d_.GetListOfKeys()]
         if v not in vars: continue
         d = f.Get(region + "/" + v)
         to_not_merge[region][v] = {}
         for hist in [i.GetName() for i in d.GetListOfKeys()]:
            to_not_merge[region][v][hist] = d.Get(hist).Clone()


   merged = {}

   for new_region in merge_pattern.keys():
      # print(new_region, merge_pattern[new_region][0], merge_pattern[new_region][1:])
      base = merge_pattern[new_region][0]
      add = merge_pattern[new_region][1:]
      merged[new_region] = {}
 
      for variable in to_be_merged[new_region][base].keys():
         merged[new_region][variable] = {}
         
         
         for hname in to_be_merged[new_region][base][variable].keys():
            orig = []
            h1 = to_be_merged[new_region][base][variable][hname]
            orig.append(h1.Integral())
            for i in add:
               h1.Add(to_be_merged[new_region][i][variable][hname])
               orig.append(to_be_merged[new_region][i][variable][hname].Integral())
           
            # print(hname, orig, sum(orig), h1.Integral())
            merged[new_region][variable][hname] = h1

   end = datetime.now()
   print("Collected merged histo in {} seconds".format((end - start).total_seconds()))
  
   f_out = ROOT.TFile(args.output, "update")

   if args.copy: 
      print ("> Now adding the old regions")      
      for region in to_not_merge.keys():
         print(">Cut: ", region)
         f_out.mkdir(region)
         f_out.cd(region)
         for v in to_not_merge[region].keys():
            print("Variable: " + v)
            f_out.mkdir(region + "/" + v)
            f_out.cd(region + "/" + v)
            for histo in to_not_merge[region][v].keys():
               to_not_merge[region][v][histo].Write()
            f_out.cd("..")
         end = datetime.now()
         print("Done in {} seconds".format((end - start).total_seconds()))
         f_out.cd("..")

   print ("> Now adding the new regions")

   for new_region in merged.keys():
      print(">Cut: ", new_region)
      f_out.mkdir(new_region)
      f_out.cd(new_region)
      for v in merged[new_region].keys():
         print("Variable: " + v)
         f_out.mkdir(new_region + "/" + v)
         f_out.cd(new_region + "/" + v)
         for histo in merged[new_region][v].keys():
            merged[new_region][v][histo].Write()
         f_out.cd("..")
      end = datetime.now()
      print("Done in {} seconds".format((end - start).total_seconds()))
      f_out.cd("..")

   #f_out.Write()

   ROOT.gROOT.GetListOfFiles().Remove(f_out)
   ROOT.gROOT.GetListOfFiles().Remove(f)
   f_out.Close()
   f.Close()
         

   

