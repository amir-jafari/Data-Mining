import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mb = pd.read_csv("microbiome.csv")
print(mb)
print(mb.head())
mb = pd.read_csv("microbiome.csv", header=None)
print(mb.head())
mb = pd.read_table("microbiome.csv", sep=',')
print(mb.head())
mb = pd.read_csv("microbiome.csv", index_col=['Patient','Taxon'])
print(mb.head())
pd.read_csv("microbiome.csv", nrows=4)
print(mb.head())
pd.read_csv("microbiome.csv").head(20)
print(mb.head())
print('#',50*"-")