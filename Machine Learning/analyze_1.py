import os
import glob
import numpy as np
import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt

DATABASE = "Machine Learning/database/"



def get_directory_hierarchy():
    all_years = glob.glob(f"{DATABASE}*")
    DF_dictionary = {}
    for year in all_years:
        year_doc = year.split("\\")
        all_XPT = glob.glob(year_doc[0]+"/"+year_doc[1]+"/Lab/*")
        print(year_doc[1])
        for xpt in all_XPT:
            xpt_path, xpt_name = xpt.split("\\")
            print(xpt_name, end=" ")
            if year_doc[1] in DF_dictionary.keys():
                DF_dictionary[year_doc[1]].append(xpt_name)
            else:
                DF_dictionary[year_doc[1]] = [xpt_name]
        print("\n")

def get_DF_of_year(year, threshold=5):
    result = {}
    db = glob.glob(f"{DATABASE}{year}/Lab/*")
    for xpt in db:
        df, meta = pyreadstat.read_xport(xpt)
        df_new = df.dropna(thresh=int(len(df.columns)-(threshold/100)*len(df.columns)))
        df_new["year"] = year
        xpt_name = xpt.split("\\")[1]
        result[xpt_name] = df_new
        print(f"{xpt_name} : {len(df_new)/len(df)} : with at most {threshold}% of NAN")
        df_new.head(5).to_csv(f"{DATABASE}{year}/Lab/{xpt_name}.csv")
    return result


year_1999 = get_DF_of_year(year="1999-2000", threshold=2)
year_2001 = get_DF_of_year(year="2001-2002", threshold=2)
year_2003 = get_DF_of_year(year="2003-2004", threshold=2)


