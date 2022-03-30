#====================================================
# CSV METHOD
#====================================================
"""
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
"""
#====================================================
# DATAFRAME TO CSV METHOD
#====================================================
"""
d = []

d.append({'row1': data1, 'row2': data2})

df = pd.DataFrame(d)

df.to_csv('C:\.csv', ';')
"""
#====================================================
# JSON METHOD
#====================================================
"""
#Dictionary
dict = {}

#Creating the JSON file
import json

with open(r'C:\.json', 'w', encoding='utf-8') as file:
    json.dump(dict, file, ensure_ascii = False, indent=0)
    
lire = open(r'C:\.json', 'r', encoding='utf-8')
fichier = lire.read()
list = json.loads(fichier)
"""
#====================================================
# SOURCES
#====================================================

"""
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
"""

#------------------------------
"""
#Statistiques équipes
page_equipeStats = requests.get("https://fr.whoscored.com/Regions/74/Tournaments/22/Seasons/8671/Stages/19866/TeamStatistics/France-Ligue-1-2021-2022")
#Output: stats équipe

#Statistiques joueurs
page_joeurStats = requests.get("https://fr.whoscored.com/Players/349368/Show/"+str(joueur)) #Attention au format Prénom-Nom
#Output: stats joueur
"""
#====================================================
# Code
#====================================================

import pandas as pd
import requests
from selenium import webdriver
import time

from bs4 import BeautifulSoup

#Statistiques équipes
#page_equipeStats = requests.get("https://fr.whoscored.com/Regions/74/Tournaments/22/Seasons/8671/Stages/19866/TeamStatistics/France-Ligue-1-2021-2022")
#Output: stats équipe

#Statistiques joueurs
#page_joeurStats = requests.get("https://fr.whoscored.com/Players/349368/Show/"+str(joueur)) #Attention au format Prénom-Nom
#Output: stats joueur

driver = webdriver.Firefox()

url= "https://fr.whoscored.com/Regions/74/Tournaments/22/Seasons/8671/Stages/19866/TeamStatistics/France-Ligue-1-2021-2022"
#driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")

stats_table = soup.find('div', id="statistics-team-table-summary")

#d = []

#Team Name
team_link = stats_table.find_all('a', class_ = "team-link")
names = []
for i in team_link:
    name_string = i.contents[0]
    index_of_char = name_string.index('.')
    names.append(name_string[index_of_char+1:])
#d.append({'name': names})
#print(names)

#Team Goals
team_goal = stats_table.find_all('td', class_ = "goal")
goal = []
for i in team_goal:
    goal.append(i.contents[0])
#d.append({'goal': goal])
#print(goal)

#Team shotsPerGame
team_shotsPerGame = stats_table.find_all('td', class_ = "shotsPerGame")
shotsPerGame = []
for i in team_shotsPerGame:
    shotsPerGame.append(i.contents[0])
#d.append({'shotsPerGame': shotsPerGame})
#print(shotsPerGame)

#Team yelloCard
team_yelloCard = stats_table.find_all('span', class_ = "yellow-card-box")
yelloCard = []
for i in team_yelloCard:
    yelloCard.append(i.contents[0])
#d.append({'yelloCard': yelloCard})
#print(yelloCard)

#Team redCard
team_redCard = stats_table.find_all('span', class_ = "red-card-box")
redCard = []
for i in team_redCard:
    redCard.append(i.contents[0])
#d.append({'redCard': redCard})
#print(redCard)

#Team possession
team_possession = stats_table.find_all('td', class_ = "possession")
possession = []
for i in team_possession:
    possession.append(i.contents[0])
#d.append({'possession': possession})
#print(possession)

#Team passSuccess
team_passSuccess = stats_table.find_all('td', class_ = "passSuccess")
passSuccess = []
for i in team_passSuccess:
    passSuccess.append(i.contents[0])
#d.append({'passSuccess': passSuccess})
#print(passSuccess)

#Team aerialWonPerGame
team_aerialWonPerGame = stats_table.find_all('td', class_ = "aerialWonPerGame")
aerialWonPerGame = []
for i in team_aerialWonPerGame:
    aerialWonPerGame.append(i.contents[0])
#d.append({'aerialWonPerGame': aerialWonPerGame})
#print(aerialWonPerGame)

#Team stat-value rating
team_stat_value_rating = stats_table.find_all('span', class_ = "stat-value rating")
stat_value_rating = []
for i in team_stat_value_rating:
    stat_value_rating.append(i.contents[0])
#d.append({'rating': stat_value_rating})
#print(stat_value_rating)

#print(d)

df = pd.DataFrame(list(zip(names,goal,shotsPerGame,yelloCard,redCard,possession,passSuccess,aerialWonPerGame,stat_value_rating)),columns=['names','goal','shotsPerGame','yelloCard','redCard','possession','passSuccess','aerialWonPerGame','rating'])

df.to_csv('Project_Webscraping/team_stats.csv', ';')



liste_joueur = ['Kylian Mbappé','Cristiano Ronaldo','Lionel Messi']

#https://www.google.com/search?client=firefox-b-d&q=kylian+mbapp%C3%A9+whoscored

for i in liste_joueur:
    #Google search for player
    url= "https://www.google.com/search?client=firefox-b-d&q="+str(i.replace(" ","+")+"+fr.whoscored.com+statistics")
    driver.get(url)
    time.sleep(5)

    #Get to player stats page
    if driver.find_elements_by_id('L2AGLb'):
        driver.find_element_by_id('L2AGLb').click()
        time.sleep(5)
    result = driver.find_elements_by_id('rso')
    result[0].find_element_by_class_name("iUh30").click()
    time.sleep(2)

    #Get current URL
    player_url = driver.current_url

    #Get player infos history
    url_history= player_url.replace('Show', 'History')
    driver.get(url_history)
    time.sleep(5)
    
    if driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button[2]"):
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button[2]").click()
        time.sleep(3)
    #qc-cmp2-summary-buttons
    #/html/body/div[1]/div/div/div/div[2]/div/button[2] Accept button xpath
    #//div[contains(@class, 'qc-cmp2-summary-buttons')]/button[contains(text(),'J'ACCEPTE')]

    #For BS4
    #content = driver.page_source.encode('utf-8').strip()
    #soup = BeautifulSoup(content,"html.parser")

    #table = soup.find_all('div', id='statistics-table-summary')
    #print(table)
    all_infos = []
    time.sleep(2)
    for tr in driver.find_elements_by_xpath('//*[@class="ml12-lg-3 ml12-m-4 ml12-s-5 ml12-xs-6 semi-attached-table"]/table//tr'):
        tds = tr.find_elements_by_tag_name('td')
        time.sleep(2)
        infos = []
        for td in tds:
            if td.text != '':
                infos.append(td.text)
        all_infos.append(infos)
    
    all_infos = all_infos[:-1]
    all_infos.pop(0)
    print(all_infos)
        

    """
    print(driver.find_element_by_class_name("col12-lg-1 col12-m-1 col12-s-2 col12-xs-2 grid-abs overflow-text").text)
    print(driver.find_element_by_class_name('team_link').text)
    print(driver.find_element_by_class_name('tournament-link  iconize iconize-icon-left').text)
    driver.find_element_by_class_name(' css-gweyaj').click()
    """

    



