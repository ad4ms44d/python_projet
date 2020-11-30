# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:45:14 2020

@author: adam.saade et guilhem.amoros
"""

# =============================================================================
# Bibliothèques :
# =============================================================================

import sys
from math  import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# =============================================================================
# Fonctions :
# =============================================================================

def minimum(L):
    mini =L[0]
    for i in L:
        if mini>= i:
            mini = i
    return  mini

def maximum(L):
    maxi = L[0]
    for i in L:
        if maxi <= i:
            maxi = i
    return maxi

def moyenne(L):
    s = 0
    n = len(L)
    for k in range(n):
        s = s + L[k]
    return s/n

def variance(L):
    moy = moyenne(L)
    var= 0
    n = len(L)
    for k in range(n):
        var = var + (L[k]-moy)**2
    return sqrt(var/n)

def ecart_type(L):
    v = variance(L)
    return  sqrt(v)

def correlation(L1,L2) :
    num = 0
    somme_den1 = 0
    somme_den2 = 0
    xa = moyenne(L1)
    yb = moyenne(L2)
    for k in range(len(L1)):
        num = num + ((L1[k] - xa)*(L2[k] - yb))
        somme_den1 = somme_den1 + ((L1[k] - xa)**2)
        somme_den2 = somme_den2 + ((L2[k] - xa)**2)
    den = (sqrt(somme_den1))*(sqrt(somme_den2))
    if den != 0 : return num / den 
    else : return 'erreur : division par 0, comparez-vous 2 même listes ?'


def fonction_alpha(t,h):
    return ((17.27*t)/(237.7+t)+np.log(h/100))

def trose(t,h):
    return ((237.7*fonction_alpha(t,h))/(17.27-fonction_alpha(t,h)))

def calcul_humidex(t,h):
    hum=t+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15+trose(t,h)))))-10)
    return hum

def list_humidex(temp,humidity):    #temp et humi sont des listes
    humidex=[]
    for k in range(len(temp)):
        humidex.append(calcul_humidex(temp[k],humidity[k]))
    
    return humidex

def delta(L):
    delta = []
    n = len(L)
    for k in range(n-1):
        d = L[k+1]-L[k]
        delta.append(d)
    return delta

def decalage_temps(L) : 
    """ ici L est une liste de datetime """
    erreur = []
    for k in range (len(L)-1) :
        a = L[k]
        b = L[k+1]
        if b - a > datetime.timedelta(minutes=20):
            erreur.append((a,b))
    if erreur == [] :
        return 'Les écarts de temps sont tous inférieurs à 20 minutes'
    else : return " Voici la liste des couples d'horaires où l'écart est >20minutes :",erreur

def ecart(idi, variable, preci,lim):
    """ ici idi = capteur, variable = temp,lum etc.., preci = nombre de fois l'ecart-type 
    et lim = limite de l'écart qu'on tolère"""
    res = []
    L = delta(Id[idi][variable])
    moy_ecart = moyenne(L)
    et = ecart_type(L)
    erreur = preci*et
    for k in range(len(L)-1):
        if L[k] > moy_ecart + erreur and abs(L[k]-L[k+1]) > lim :
            res.append((abs(L[k]-L[k+1]),Id[idi].index[k]))
    if res ==  [] : return ' pas de discontinuité pour :',variable
    else : return 'les grosses discontinuités pour' + ' '+ variable +' sont (écarts et heures indiquées) :', res

def presence(a) :
    """ ici a est le capteur qu'on veut etudier"""
    horaires = []
    L = Id[a]['noise']
    maxi = maximum(L)
    for k in range(len(L)):
        if 40 <= L[k] <= maxi :
            horaires.append(Id[a].index[k])
    return 'Voici la liste des horaires quand le bureau (où il y a le capteur' + str(a) + ') est potentiellement occupé :', horaires


# =============================================================================
# Créattion de dataframe et listes utiles
# =============================================================================

Id = [0]
Id_temp = [0]
Id_humidity = [0]
humidex = [0]
data = [0]
data_corr = []
for k in range(6): # ici on crée différentes listes et dataframe utiles pour créer les courbes et établir les statistiques
    Id.append(df[df['id']== k+1])
    Id_temp.append(Id[k+1]['temp'])
    Id_humidity.append(Id[k+1]['humidity'])
    humidex.append(list_humidex(Id_temp[k+1],Id_humidity[k+1]))
    data.append(pd.DataFrame(humidex[k+1], index = Id[k+1].index, columns = ['humidex']))
    a = np.arange(0,1336)
minutes = []
for k in range(6):
    minutes.append(Id[k+1].index.minute)
test = minutes[1]

# =============================================================================
# Détection des anomalies : 
# =============================================================================
for k in range(6):
    print(' Capteur :' + str(k+1))
    print("\n")
    print(presence(k+1))
    print("\n")
    print(decalage_temps(Id[k+1].index))
    print("\n")
    print(ecart(k+1,'temp',3,10))
    print("\n")
    print(ecart(k+1,'noise',3,10))
    print("\n")
    print(ecart(k+1,'co2',3,5))
    print("\n")
    print(ecart(k+1,'lum',3,50))
    print("\n")
    print(ecart(k+1,'humidity',3,10))




    
