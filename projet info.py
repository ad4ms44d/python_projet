import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('EIVP_KM.csv', sep=';')
data_describe=data.describe()
temp=data['temp']
sent_at=data['sent_at']
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
    
def humi(a,d):
    return ((17.27*data.temp[a])/(237.7+data.temp[a])+np.log(data.humidity[a]))

def trose(a,d):
    return ((237.7*humi(a,d))/(17.27-humi(a,d)))

def humidex(a,d):
    hum=data.temp[a]+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/273+trose(a,d))))-10)
    return hum

def correlation(a,b):
    data.corr()
    