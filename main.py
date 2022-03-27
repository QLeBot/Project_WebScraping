#====================================================
# CSV METHOD
#====================================================

import csv

#Création du CSV
csvFile = open("name.csv", "w", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile,delimiter=';', quotechar='"')

#Création du nom des collones 
csvWriter.writerow(['Row1','Row2'])

#Ecriture dans le fichier CSV
#In for loop
csvWriter.writerow((row_data))

#Fermeture et enregistrement du CSV
csvFile.close()

#====================================================
# DATAFRAME TO CSV METHOD
#====================================================

d = []

d.append({'row1': data1, 'row2': data2})

df = pd.DataFrame(d)

df.to_csv('C:\.csv', 'w')

#====================================================
# JSON METHOD
#====================================================

#Dictionary
dict = {}

#Creating the JSON file
import json

with open(r'C:\.json', 'w', encoding='utf-8') as file:
    json.dump(dict, file, ensure_ascii = False, indent=0)
    
lire = open(r'C:\.json', 'r', encoding='utf-8')
fichier = lire.read()
list = json.loads(fichier)

#====================================================
# SOURCES
#====================================================

#Club Ligue 1
page_ligue1 = requests.get("https://www.transfermarkt.fr/ligue-1/startseite/wettbewerb/FR1")
#Output : liste des clubs 
# clubs

#Liste joueurs
page_joeurs = requests.get("https://www.transfermarkt.fr/"+str(club)+"/startseite/verein/162/saison_id/2021")
#Output: liste des joueurs
# joueurs

#Infos détaillées joueur
page_joeurDetails = requests.get("https://www.transfermarkt.fr/"+str(club)+"/transferrekorde/verein/3524/saison_id/2021/pos//detailpos/0/w_s//altersklasse//plus/1")
#Output: détails joueurs

#Info Joueur
page_joeurInfos = requests.get("https://www.transfermarkt.fr/"+str(joueur)+"/profil/spieler/495667")
#Output: info des joueur

#Statistiques équipes
page_equipeStats = requests.get("https://fr.whoscored.com/Regions/74/Tournaments/22/Seasons/8671/Stages/19866/TeamStatistics/France-Ligue-1-2021-2022")
#Output: stats équipe

#Statistiques joueurs
page_joeurStats = requests.get("https://fr.whoscored.com/Players/349368/Show/"+str(joueur)) #Attention au format Prénom-Nom
#Output: stats joueur

#====================================================
# Code
#====================================================

import pandas as pd
import requests

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_ligue1.text, 'lxml')