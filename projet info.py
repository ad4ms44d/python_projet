import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('EIVP_KM.csv', sep=';')
data=pd.read_csv('EIVP_KM.csv', sep=';', index_col = 'sent_at', parse_dates = True)
data_describe=data.describe()
temp=data['temp']
c=str
def evolution_var(c,a,b):
    if c==display:
        x=data.sent_at.iloc[a:b]
        y=data.temp.iloc[a:b]
        plt.title("Température en fonction du temps")
        plt.xlabel('date')
        plt.ylabel('temperature')
        plt.plot(x, y)
        plt.xticks(data.sent_at[a:b])
        plt.show() 
    if c==displayStat:
        x=data.sent_at.iloc[a:b]
        y=data.temp.iloc[a:b]
        plt.title("Valeurs statistique de la température en fonction du temps")
        plt.xlabel('date')
        plt.ylabel('temperature')
        plt.plot(x, y)
        plt.plot(x,data_describe[a:b])
        plt.xticks(data.sent_at[a:b])
        plt.show()

def evolution_var_avec_stats(a,b):
    x=data.sent_at.iloc[a:b]
    y=data.temp.iloc[a:b]
    plt.title("Valeurs statistique de la température en fonction du temps")
    plt.xlabel('date')
    plt.ylabel('temperature')
    plt.plot(x, y)
    plt.plot(x,data_describe[a:b])
    plt.xticks(data.sent_at[a:b])
    plt.show()        


def evolution_var2(a,b,c):
    x=data["a"]
    y=data["b":"c"]
    plt.xlabel('date')
    plt.ylabel('temperature')
    plt.plot(x, y)
    plt.show() 
    
def fonction_alpha(t,h):
    return ((17.27*t)/(237.7+t)+np.log(h))

def trose(t,h):
    return ((237.7*fonction_alpha(t,h))/(17.27-fonction_alpha(t,h)))

def calcul_humidex(t,h):
    hum=t+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/273+trose(t,h))))-10)
    return hum

def list_humidex(temp,humi):    #temp et humi sont des listes
    humidex=[]
    for k in range(len(temp)):
        humidex.append(calcul_humidex(temp[k],humi[k]))
    return humidex
    
def confortable(humidex):
    n=len(temp)
    for k in range(n):
        if  list_humidex(temp,humi) <= 29:
            return "aucun inconfort ne sera ressenti"
        elif 30<=list_humidex(temp,humi) <= 38:
            return "un leger inconfort se fera ressentir"
        elif 39<=list_humidex(temp,humi) <= 45:
            return "un fort inconfort sera ressenti"
        elif 46<=list_humidex(temp,humi) <= 54:
            return "l'inconfort devient dangereux"
        elif 55<=list_humidex(temp,humi) <= 60:
            return "Coup de chaleur imminent"


def correlation(a,b):
    data.corr()
    