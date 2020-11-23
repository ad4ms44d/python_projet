# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:37:00 2020

@author: adam.saade
"""
# =============================================================================
# test le power shell
# =============================================================================
import sys
import pandas as pd
from math import *

def minimum(L):
    min=L[0]
    for i in L:
        if min>= i:
            min = i
    return min

def maximum(L):
    max = L[0]
    for i in L:
        if max<= i:
            max = i
    return max

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


def calcul(L):
    if a == 'moyenne':
        print('la moyenne vaut :')
        return  moyenne(L)
    elif a == 'ecart_type' :
        print("l'ecart type vaut :")
        return  ecart_type(L)
    elif a == 'maximum' :
        print('le maximum vaut :')
        return  maximum(L)
    elif a == 'variance':
        print('la variance vaut :')
        return  moyenne(L)
    elif a == 'minimum' :
        print('la minimum vaut :')
        return  moyenne(L)
    else : return 'calcul impossible'
    
def cal(L,c):
    return globals()[c](L)


def main(L):
    df = pd.read_csv("EIVP_KM.csv",sep=";", index_col = 'sent_at', parse_dates = True)
    id_1 = df[df['id']==1]
    id_1_temp = id_1['temp']
    return cal(id_1_temp,L)

print(main(sys.argv[1]))



       
