# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:38:36 2022

@author: djiko
"""

from selenium import webdriver
import time

#Récupérer note moyenne de chaque équipe année par année

driver = webdriver.Firefox()
driver.get("https://fr.whoscored.com/")

time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button[2]").click()
time.sleep(1)

#/html/body/div[3]/div/div[3]/div[3]/ul/li[1]/a
#/html/body/div[3]/div/div[3]/div[3]/ul/li[18]/a

i=0
print("/html/body/div[3]/div/div[3]/div[3]/ul/li[{}]/a".format(i))

for i in range (1,19):
    if i!=9:
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/ul/li[{}]".format(i)).click()
        print(2)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/div[2]/ul/li[3]/a").click()
        print(3)
        time.sleep(1)
        
        element = driver.find_element_by_id("seasons")
        all_options = element.find_elements_by_tag_name("option")
        
        
        
        print(all_options[0].get_attribute('value'))
        
        """for index_saison in range(5,len(all_options)+1):
            driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/span[5]/select/option[{}]".format(index_saison)).click()
            print(3)
            time.sleep(3)
            try:
                driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[1]/div[2]/ul/li[3]/a").click()
            except:
                print("erreur")
            
            print(4)
            time.sleep(1)
        
        for j in range(1, len(driver.find_element_by_id("seasons"))):
            print("e")"""
            
        #print(len(driver.find_elements_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr")))
        #print(driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[1]/td[8]").text)
        
        Club = dict()
        for line in range(1,len(driver.find_elements_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr"))+1):
            [Club["Classement"],Club["Nom"] ] =  driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[1]".format(line)).text.split(". ")
            Club["But"] = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[2]".format(line)).text
            Club["Tirs pm"] = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[3]".format(line)).text
            Club["CartonJaune"] = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[4]/span[1]".format(line)).text
            Club["CartonRouge"] = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[4]/span[2]".format(line)).text
            Club["Possession"] = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[5]".format(line)).text
            Club["PassesRéussies%"] = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[6]".format(line)).text
            Club["AériensGagnés"] = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[7]".format(line)).text
            Club["Note"] = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[2]/div[3]/div/table/tbody/tr[{}]/td[8]".format(line)).text
            
            print(Club)
        
        
        time.sleep(1)
        