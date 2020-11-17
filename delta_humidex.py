# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:39:43 2020

@author: adam.saade
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("EIVP_KM.csv",sep=";", index_col = 'sent_at', parse_dates = True)
#print(df.head())


id_1 = df[df['id']==1]
id_1_temp = id_1['temp']
print(id_1_temp)

print(id_1['temp']['2019-08'].resample('D').plot())

id_1_humi = id_1['humidity']
#print(id_1_humi)

def fonction_alpha(t,h):
    return ((17.27*t)/(237.7+t)+np.log(h))

def trose(t,h):
    return ((237.7*fonction_alpha(t,h))/(17.27-fonction_alpha(t,h)))

def calcul_humidex(t,h):
    hum=t+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/273+trose(t,h))))-10)
    return hum

def list_humidex(temp,humidity):    #temp et humi sont des listes
    humidex=[]
    for k in range(len(temp)):
        humidex.append(calcul_humidex(temp[k],humidity[k]))
    
    return humidex

humidex = list_humidex(id_1_temp,id_1_humi )
#print(humidex)
date = id_1['2019-08-25':'2019-08-26']
#print(date)

def delta(L):
    delta = []
    n = len(L)
    for k in range(n-1):
        d = L[k]-L[k+1]
        delta.append(d)
    return delta
print(delta(id_1_temp))
