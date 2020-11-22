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
id_5 = df[df['id']==5]
id_1_temp = id_1['temp']
id_5_temp = id_5['temp']


id_1_humi = id_1['humidity']
id_5_humi = id_5['humidity']

#print(id_1_humi)

def fonction_alpha(t,h):
    return ((17.27*t)/(237.7+t)+np.log(h/100))

def trose(t,h):
    return ((237.7*fonction_alpha(t,h))/(17.27-fonction_alpha(t,h)))

def calcul_humidex(t,h):
    a = trose(t,h)
    hum = t + 0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15 + a))))-10)
    return hum

def list_humidex(temp,humidity):    #temp et humi sont des listes
    humidex=[]
    for k in range(len(temp)):
        humidex.append(calcul_humidex(temp[k],humidity[k]))
    
    return humidex

humidex = list_humidex(id_1_temp,id_1_humi )

#print(humidex_5)
#date = id_1['2019-08-25':'2019-08-26']

def confortable(humidex):
        if  humidex <= 29:
            return 0 #"aucun inconfort ne sera ressenti"
        elif humidex <= 38:
            return 1 #"un leger inconfort se fera ressentir"
        elif humidex <= 45:
            return 2 #"un fort inconfort sera ressenti"
        elif humidex<= 54:
            return 3 #"l'inconfort devient dangereux"
        elif humidex <= 60:
            return 4 #"Coup de chaleur imminent"


def delta(L):
    delta = []
    n = len(L)
    for k in range(n-1):
        d = L[k+1]-L[k]
        delta.append(d)
    return delta
#print(delta(id_1_temp))

id_1['humidex'] = humidex
id_1['humidex'].plot()

b = id_1['humidex'].map(confortable)
