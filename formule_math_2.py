# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:26:22 2020

@author: adam.saade
"""
from math  import *
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
        var = var + (L[k]-m)**2
    return sqrt(var/n)

def ecart_type(L):
    v = variance(L)
    return sqrt(v)

liste =  [1,2,3,4,5,6]

def calcul(L):
    a = input()
    if a == 'moyenne':
        print('la moyenne vaut :')
        return  moyenne(L)
    elif a == 'ecart_type' :
        print("l'ecart type vaut :")
        return  ecart_type(L)
    elif a == 'maximum' :
        print('le maximum vaut :')
        return  maiximum(L)
    elif a == 'variance':
        print('la variance vaut :')
        return  moyenne(L)
    elif a == 'minimum' :
        print('la minimum vaut :')
        return  moyenne(L)
    else : return 'calcul impossible'
    
def cal(L):
    c = input('Quelle valeur statistique voulez-vous ?  ')
    print ('la valeur est :')
    return globals()[c](L)


    