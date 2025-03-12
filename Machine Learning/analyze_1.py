import os
import glob
import numpy as np
import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt

def find_most_filled_dataframes(db):
    Y = []
    X = []
    Y2 = []
    Y3 = []

    for i in db:
        df, meta = pyreadstat.read_xport(i)
        df_new = df.dropna(thresh=len(df.iloc[0, ])-15)
        i = i.split("\\")[1]
        X.append(i)
        Y.append(len(df_new))
        Y2.append(len(df))
        Y3.append(len(df.iloc[1, ]))
    return X, Y, Y2, Y3

def plot_data_distribution(X, Y, Y2):
    fig, ax = plt.subplots(figsize=(15, 5))

    width = 0.4  # Bar width
    X_indices = np.arange(len(X))  # Numeric indices for x-axis
    
    ax.bar(X_indices - width/2, Y, width=width, label="Data with at most 15 NaN Column")
    ax.bar(X_indices + width/2, Y2, width=width, label="Total amount of data")
    
    ax.set_xticks(X_indices)  # Set x-axis positions
    ax.set_xticklabels(X, rotation=90)  # Apply labels
    ax.set_title("Data including values with at most 15 NaN")
    ax.legend()  # Show legend
    
    fig.tight_layout()
    plt.show()

all_data_files = glob.glob("Machine Learning/database/*.xpt")
X, Y, Y2, Y3 = find_most_filled_dataframes(all_data_files)
plot_data_distribution(X, Y, Y2)
quality_table = pd.DataFrame({"Data Name":X, 
                              "Total length":Y2, 
                              "Data excessed thresh":Y, 
                              "Feature number":Y3})
quality_table["QualityNumber"] = (quality_table["Data excessed thresh"]/
                                  quality_table["Total length"])*quality_table["Feature number"]
max_quality = quality_table["QualityNumber"].max()
quality_table["QualityNumber"] = quality_table["QualityNumber"]/max_quality
print(quality_table)
