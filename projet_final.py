# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:25:22 2020

@author: adam.saade
"""

# =============================================================================
# programme pour affichier les moyennes etc
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
# fonctions :
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


def main(L):
    print('Les dates et choix du capteur seront demandés')
    if L[0] == 'display' :
        if L[1] == 'humidex' :
            a = input('Choisir un capteur :')
            start = input('date de début (format : Y-M-D h:m:s) :')
            end = input('date de fin (format : Y-M-D h:m:s) :')
            data[int(a)]['humidex'][start:end].plot()
            plt.axhline(y=30, color = 'r',label = '< confort')
            plt.axhline(y=39, color = 'b',label = '< léger confort')
            plt.xlabel('dates')
            plt.ylabel('humidex')
            plt.legend()
        elif L[1] in {'noise', 'temp','co2', 'lum', 'humidity'} :
            print('temp en °C, noise en dBA, humidity en % (relative), lum en lux, co2 en ppm')
            a = input('Choisir un capteur :')
            start = input('date de début (format : Y-M-D h:m:s) :')
            end = input('date de fin (format : Y-M-D h:m:s) :')
            Id[int(a)][L[1]][start:end].plot()
            plt.xlabel('dates')
            plt.ylabel('humidex')
            plt.legend()
        else : print('attention les variables sont : noise, temp, co2, lum, humidity ou humidex')
    elif L[0] == 'displayStat' :
        if L[1] in {'noise', 'temp','co2', 'lum', 'humidity'} :
            print('temp en °C, noise en dBA, humidity en % (relative), lum en lux, co2 en ppm')
            a = input('Choisir un capteur :')
            start = input('date de début (format : Y-M-D h:m:s) :')
            end = input('date de fin (format : Y-M-D h:m:s) :')
            serie = Id[int(a)][L[1]]
            moy = moyenne(serie)
            maxi = maximum(serie)
            mini = minimum(serie)
            var = variance(serie)
            et = ecart_type(serie)
            serie[start:end].plot()
            plt.xlabel('dates')
            plt.ylabel(L[1])
            plt.axhline(y= moy, color = "r",linestyle = ":", label = 'moyenne')
            plt.axhline(y= mini, color = "r",linestyle = "--", label = 'minimum')
            plt.axhline(y= maxi, color = "r",linestyle = "--", label = 'maximum')
            plt.suptitle(L[1] + ' ' + 'en fonction du temps' "\n", fontsize = 'large', ha= 'right')
            plt.title( 'variance :' + str(moy) + "\n" 'ecart type :' + str(et), fontsize = 'small',loc = 'right')
            plt.legend([L[1], 'moyenne :' + ' ' + str(moy), 'maximum :' + ' ' + str(maxi), 'minimum :' + ' ' + str(mini)])
        else : print('attention les variables sont : noise, temp, co2, lum, humidity ou humidex')
    elif  L[0] == 'correlation' :
        print('temp en °C, noise en dBA, humidity en % (relative), lum en lux, co2 en ppm')
        a = input('Choisir un capteur :')
        start = input('date de début (format : Y-M-D h:m:s) :')
        end = input('date de fin (format : Y-M-D h:m:s) :')
        Id[int(a)][L[1]][start:end].plot()
        Id[int(a)][L[2]][start:end].plot()
        cor = correlation(Id[int(a)][L[1]], Id[int(a)][L[2]])
        plt.xlabel('dates')
        plt.suptitle(L[1] + ' ' + 'et' + ' ' + L[2] + ' ' + 'en fonction du temps' "\n", fontsize = 'large')
        plt.title('indice de correlation :' + str(cor) , fontsize = 'small',loc = 'right')
        plt.legend()
    else : print ('erreur, utiliser display,displayStat, humidex ou correlation en action ! La date vous sera demandé automatiquement, pas besoin de la mettre ')
    
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
    res = []
    L = delta(Id[idi][variable])
    moy_ecart = moyenne(L)
    et = ecart_type(L)
    erreur = preci*et
    for k in range(len(L)-1):
        if L[k] > moy_ecart + erreur and abs(L[k]-L[k+1]) > lim :
            res.append((abs(L[k]-L[k+1]),Id[idi].index[k]))
    if res ==  [] : return ' RAS'
    else : return 'les grosses discontinuités sont (heures indiquées) :', res

def presence(a) :
    horaires = []
    L = Id[a]['noise']
    maxi = maximum(L)
    for k in range(len(L)):
        if 40 <= L[k] <= maxi :
            horaires.append(Id[a].index[k])
    return 'Voici la liste des horaires quand le bureau (où il y a le capteur' + str(a) + ') est potentiellement occupé :', horaires
            

# =============================================================================
# création des dataframe par id et toutes variables utiles
# =============================================================================
df = pd.read_csv("EIVP_KM.csv",sep=";", index_col = 'sent_at', parse_dates = True)

Id = [0]
Id_temp = [0]
Id_humidity = [0]
humidex = [0]
data = [0]
data_corr = []
for k in range(6):
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
# action pour lire depuis le shell
# =============================================================================
main(sys.argv[1:])
plt.show()



    
            