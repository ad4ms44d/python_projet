# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:40:08 2020

@author: adam.saade
"""

import matplotlib.pyplot as plt
import pandas as pd
df_1 = pd.read_csv("EIVP_KM.csv",sep=";")
#print(df)
## test 
#print(df.shape)
#print(df.head)
#print(df['id'].value_counts())
#print(df['id'].value_counts().plot.bar())
# test 2
df = pd.read_csv("EIVP_KM.csv",sep=";", index_col = 'sent_at', parse_dates = True)

id_1 = df[df['id']==1]
id_1_temp = id_1['temp']
#print(id_1_temp)

#print(id_1['temp']['2019-08':'2019-10'].plot())

id_1_humi = id_1['humidity']
print(id_1_humi)