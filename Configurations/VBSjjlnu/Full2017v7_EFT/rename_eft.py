import ROOT
import os 


if __name__ == "__main__":

   d = {}
   f_ = "rootfiles_2/plots_fit_2017_EFT_DNNcut_geq0p5_eft.root"
   f = ROOT.TFile(f_)
   reg = [i.GetName() for i in f.GetListOfKeys()]

   for r in reg:
      d_ = f.Get(r)

      d[r] = [i.GetName() for i in d_.GetListOfKeys()]
    
   f.Close()

   nuis = "CMS_PS_FSR"
   new = "CMS_PS_FSR_EFT"

   for idx, r in enumerate(reg):
      
         print("---> {} {}/{}".format(r,idx, len(reg)))
         os.system("python ../scripts/nuisances_tools/rename_shape_root.py -i {} --shape-name {} -sf ../Full2018v7_EFT/txtsForScripts/samples_EFT_datacard.txt --rename {} -dc {}".format(f_, nuis, new, r))    
