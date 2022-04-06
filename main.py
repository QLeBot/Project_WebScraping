# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:58:56 2022

@author: djiko
"""

import pandas as pd
from Liste_Transfert import *
import time
df = pd.read_csv("C:/Users/djiko/Documents/ESME/Ingé2/Web Scraping/Projet/test.csv",sep=",")
            
df_player = pd.DataFrame()

print(df.dtypes)
print(df.head())
i=0
for index, row in df.iterrows():
    print(row["Lien_URL_Club"])
    dict_players=getListTransfert(row["Lien_URL_Club"], row["Saison"])
    for key, value in dict_players.items():
        try:
          df_player = df_player.append(value, ignore_index=True)
        except:
          print("An exception occurred")
          print(key)

        
df_player.to_csv('liste_transfert.csv')    