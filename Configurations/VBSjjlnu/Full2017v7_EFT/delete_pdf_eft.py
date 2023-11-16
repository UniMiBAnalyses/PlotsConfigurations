import os
from glob import glob
from multiprocessing import Pool
import tqdm 

pdf_vars = ["pdf_weight_1718V{}Var".format(i) for i in range(33)]

def delete(d_):

   file_ = d_["file"]
   out_ = d_["out"]
   
   sample = file_.split("plots_fit_2017_EFT_DNNcut_geq0p5_eft_ALL_")[1].split(".")[0] 
   file_name = file_.split("/")[-1]

   os.system("python ../scripts/delete_nuisance_shapes_and_create_new_file.py -i {} -s {} -n {} -o {}".format(file_, sample, " ".join(i for i in pdf_vars), out_ + "/" + file_name))


if __name__ == "__main__":
   
   in_ = "prova"
   out_ = "prova2"
   ls = glob(in_ + "/*.root")

   tsb = []
   for f in ls:
      d = {}
      d["file"] = f
      d["out"] = out_
      tsb.append(d)

   with Pool(8) as p:
      r = list(tqdm.tqdm(p.imap(delete, tsb), total=len(tsb)))
   #pool = Pool(processes=8)
   #pool.map(delete, tsb)    


   

   
