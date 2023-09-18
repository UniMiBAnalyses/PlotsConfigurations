import ROOT 
import argparse 
import sys
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="input file", type=str)
parser.add_argument("-o","--output", help="output file", type=str)
parser.add_argument("-m","--merge", help="Merge these regions in format new_name:reg1,reg2 new_name:reg3,reg4", type=str, nargs="+")
parser.add_argument("-v","--variables", help="merge only these variables", type=str, nargs="+")
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

   f = ROOT.TFile(args.input, "READ")
   
   regions = [i.GetName() for i in f.GetListOfKeys()]
  
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
   
   # first copy the original shapes
   f_out = ROOT.TFile(args.output, "RECREATE")
   for r in regions:
      if r in ignore_regions : continue 

      print(">Cut: ", r)
      d = f.Get(r)
      f_out.mkdir(r)
      f.cd(r)
   
      for v in args.variables:
         vars_ = [i.GetName() for i in d.GetListOfKeys()]
         if v not in vars_: continue
         
         var = d.Get(v)
         f_out.mkdir(r + "/" + v)
         f_out.cd(r + "/" + v)
     
         for histo in [h.GetName() for h in var.GetListOfKeys()]:
            h_ = var.Get(histo).Clone()
            h_.Write()
          
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
         f_out.mkdir(new_region + "/" + v)
         f_out.cd(new_region + "/" + v)
         for histo in merged[new_region][v].keys():
            merged[new_region][v][histo].Write()
         f_out.cd("..")
      end = datetime.now()
      print("Done in {} seconds".format((end - start).total_seconds()))
      f_out.cd("..")

   f_out.Write()
   f_out.Close()
   f.Close()
         

   

