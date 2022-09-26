from pickle import FALSE
import pandas as pd 
import numpy as np
import scipy.stats
from scipy.stats import norm
import math
from math import sqrt

read_file = pd.read_excel ("/Users/samhitharao/Downloads/clean_ver.xlsx")

read_file.to_csv ("Test.csv",index = None,header=True)
data = pd.DataFrame(pd.read_csv("Test.csv"))

a_pop_mean = data['AQI'].mean()
pop_mean = 0.65*data['AQI'].mean()
pop_var = data['AQI'].var()
pop_sd=math.sqrt(pop_var)
s_mean = (data['AQI'].mean())
s_var = data['AQI'].var()
s_sd=math.sqrt(s_var)
n=1559
alpha=0.05

print("H0 statement: The AQI has reduced by nearly more than 35% during lockdown")
print("H1 statement: The AQI has not reduced more than 35% during lockdown")
print('65% of population mean: ' ,pop_mean)
print('Alpha: ',alpha)
print('Sample size (total observations in 2020): ',n)
hypo_z=(s_mean-pop_mean)/(s_sd/sqrt(n))
print('hypothetical z value: ',hypo_z,'\n')
if ((scipy.stats.norm.sf(abs(hypo_z)))>0.05):
    print("Reject hypothesis")
else:
    print("Failed to reject hypothesis")
print('H0 : μ >=', pop_mean)
print('H1 : μ <', pop_mean)


print("P value was found to be(in %)",100-scipy.stats.norm.sf(abs(hypo_z))*100)