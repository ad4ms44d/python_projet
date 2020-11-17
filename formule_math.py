# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:17:36 2020

@author: adam.saade
"""

# "formule_math"

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
    
    