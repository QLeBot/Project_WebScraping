import pandas as pd
import requests

page = requests.get("")

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.text, 'lxml')

#====================================================
# CSV METHOD
#====================================================

import csv

#Création du CSV
csvFile = open("name.csv", "w", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile,delimiter=';', quotechar='"')

#Création du nom des collones 
csvWriter.writerow(['Row1','Row2'])

#Ecriture dans le fichier CSVcds
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

