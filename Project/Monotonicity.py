from pickle import FALSE
import pandas as pd 
import numpy as np
import scipy.stats
from scipy.stats import norm
import math
from math import sqrt
import matplotlib.pyplot as plt
from pickle import FALSE

#importing pandas as pd
import pandas as pd

# Read and store content
# of an excel file
read_file = pd.read_excel ("/Users/samhitharao/Downloads/clean_ver (1).xlsx")

read_file.to_csv ("Test.csv",index = None,header=True)
df = pd.DataFrame(pd.read_csv("Test.csv"))

data1=df['AQI']
data2=df['PM2.5']
import seaborn as sns; sns.set_theme(color_codes=True)
ax = sns.regplot(x=data1, y=data2, data=df)
plt.show(block=FALSE)


result1 = data1.is_monotonic_increasing

print('Monotonicity of AQI is:',result1) 

print("spearman coefficient\n")
print(df.corr(method='spearman'))





