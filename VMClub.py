# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:48:49 2022

@author: djiko
"""

def valuetoint(value_string):
    if value_string[-6:]=='mio. €':
        return int(float(value_string[:-7].replace(',','.'))*1e6)
    if value_string[-3:]=='K €':
        return int(float(value_string[:-4].replace(',','.'))*1e3)
    if value_string == "Transfert libre":
        return 0

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

    
def getInfoclub(url_club,saison):
    page = "https://www.transfermarkt.fr/"+url_club+"saison_id/"+str(saison)
    page = page.replace("startseite", "kader")
    #print(page)
    pageTree = requests.get(page, headers=headers)
    #print (pageTree)
    soup = BeautifulSoup(pageTree.content, 'html.parser')
    #print(soup)
    mydivs = soup.find_all("table")[-1].find_all('td')
    
    Club_update= dict()
    
    Club_update["Age_moyen"] = float(mydivs[-3].text.replace(",","."))
    Club_update["VM_totale"] = valuetoint(mydivs[-2].text)
    Club_update["VM_moyenne"] = valuetoint(mydivs[-1].text)
    
    durée = soup.find(class_ ="dataZusatzDaten").find_all('a')[-1].text
    
    return Club_update, durée

test, durée =getInfoclub("olympique-lyon/startseite/verein/1041/", 2020)
print(test)

print(durée)