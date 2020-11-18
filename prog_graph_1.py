# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:38:05 2020

@author: adam.saade
"""
import pandas as pd
import matplotlib.pyplot as plt

#variables

df = pd.read_csv("EIVP_KM.csv",sep=";", index_col = 'sent_at', parse_dates = True)
id_1 = df[df['id']==1] #donnees du capt 1
id_2 = df[df['id']==2] #donnees du capt 2
id_1_temp = id_1['temp'] #temp du capt 1
id_2_temp = id_2['temp'] #temp du capt 2



#graph

#id_1['temp']['2019-08-15 12:00':'2019-08-16 04:00'].plot()
#id_2['temp']['2019-08-15 12:00':'2019-08-16 04:00'].plot()
L = []
for k in range(6):
    L.append(k+1)
    df[df['id']==k+1]['temp']['2019-08-15 12:00':'2019-08-16 04:00'].plot()
plt.legend(L)
    

#programme pour choisir un graph

def graphique(L):
    a = input()
    
    
