# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:32:10 2020

@author: user-tp


Scrapping web python 
"""
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup
import re #RegEx
import csv, json
import os
import pandas as pd
import pyodbc


# path01 = os.path.basename('E:/Projet/HACKATHON/Scrappingweb.py')
# print(path01)
# dossierJson="\\scriptDATA\\Json\\"
# dossierCSV="\\scriptDATA\\CSV\"
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
print(dt_string)	

regex01 = r"★\((\d*\s\d*)\)\d" #ID produit bien noté
regex02 = r"★\(\d*\s\d*\)(.*)\s\€" #prix
regex03 = r"[chez]\s(\w*\D\w*)\+" #siteMarchand
regex04 = r"(\(\w*\s\w+\D\d+\))" #nb article en stock
regex05 = r"\w(\s-\s)\w" # tiret 
regex06 = r"\(\d\)"
regex07 = r"\s\d*,"
regex08 = r"[Filtrer].*\w*\sconsommateurs"
regex09 = r"\s\s"
regex10 = r"\d*\d\s\€ de frais de port"
regex11 = r"★(\(\d*\s\d*\).*\s\€\w*\s\w*\s.*)"



lien = 'https://www.google.com/search?tbm=shop&q='



objRecherche = 'samsung+s9'




fichierCSV ='data.csv'
fichierJSON ='data.json'






obj01 = lien + objRecherche
response = get(obj01)

#print(response.text[:99999])

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

#print(html_soup.text)

varAffi01 = "\n" +"###########################################" +"\n" +"########## "
varAffi02 =  "  ###########"+"\n"+"###########################################"+"\n"
elt01 = 'ⓘ' # Carractère ou mot rechercher
elt02 = '★★★★★'

fraisSupp = 'frais de port'
str01 = "COMPARER LES PRIX "
str02 = "COMPARER LES PRIX"
str03 = "\+"
str04 = "frais de port"
str05 = "Livraison gratuite"
str06 = "-"
str07 = 'Filtrer'
str08 = 'chez'
str09 = 'PLUS D\'OPTIONS'


chaine01 = html_soup.text # Chaine de départ

if elt01 in chaine01:
    print(varAffi01 + "Requete réussi" + varAffi02)
    pos01 = chaine01.find(elt01)
    
else:
    print(varAffi01 + "Erreur" + varAffi02)
    
chaine02 = chaine01[pos01:]   #Chaine des articles trouvés
#print(chaine02)
chaine03 = re.sub(elt01, "", chaine02) #remplace ⓘ
#chaine03 = re.sub(elt02, "", chaine03) #remplace ★★★★★
chaine03 = re.sub(str01, "", chaine03) #remplace pb
chaine03 = re.sub(str02, "", chaine03)
chaine04 = re.sub(str03, "\n", chaine03) #### Caractérisitque saut de ligne
chaine04 = re.sub(str04, str04+"\n", chaine04) #
chaine04 = re.sub(str05, " "+str05+"\n", chaine04)
chaine04 = re.sub(str06, "", chaine04)


chaine04 = re.sub(regex04, "", chaine04)
chaine04 = re.sub(regex06, "", chaine04)
chaine04= re.sub(regex07, "", chaine04)
chaine04 = re.sub(str08, "", chaine04)
chaine04= re.sub(regex08, "", chaine04)
chaine04 = re.sub(regex09, "", chaine04)
chaine04 = re.sub(str09, "", chaine04)

tabElem = []
tab02 = []

# print(varAffi01 + "Identifiant Produit" + varAffi02)
# for match in re.finditer(regex01, chaine04):
#     print(*match.groups(), sep='\n')

# print(varAffi01 + "Prix du produit" + varAffi02)
# for match in re.finditer(regex02, chaine04):
#     print(*match.groups(), sep='\n')
 
#print(varAffi01 + "DATAFINAL" + varAffi02)
for match in re.finditer(regex11, chaine04):
    #print(*match.groups(), sep='\n')
    tabElem.append(*match.groups())

tab02.append("Nom,Date,ID,Prix,SiteMarchand,FraisDePort")
for elt in tabElem:
    temp = elt
    temp = temp.replace(",", ".")
    
    temp =  dt_string+','+ temp
    temp = objRecherche +','+ temp
    temp = temp.replace("(", "")
    temp = temp.replace(")", ",")
    temp = temp.replace("\u202f", "")
    #temp = temp.replace("")
    temp = temp.replace("\xa0€", ",")
    temp = temp.replace("\n", ",")
    temp = temp.replace(" de frais de port", "")
    temp = temp.replace(" Livraison gratuite", ",0")
    temp = temp + "$"
    temp = temp.replace(",$", "")
    temp = temp.replace("$", "")
    temp = temp.replace("+", " ")
    
    print(temp)
    tab02.append(temp)
    
for elt in tab02:
    f = open(fichierCSV,'a')
    f.write(elt+"\n")
    f.close()

data = {}

with open(fichierCSV) as csvFile:
    csvReader = csv.DictReader(csvFile)
    id = 0
    for rows in csvReader: 
        print(rows)
        id=id+1              
        data[id] = rows

#Nom,Date,ID,Prix de l'article,Site-marchand,Frais de port

with open(fichierJSON, 'w') as jsonFile:
    jsonFile.write(json.dumps(data,indent=1))

# # Import CSV
# dataCSV = pd.read_csv(r'data.csv')   
# df = pd.DataFrame(dataCSV, columns= ['Nom','Date','ID','Prix','SiteMarchand','FraisDePort'])

# # Connect to SQL Server
# server = '127.0.0.1'
# port = '3306'
# database = 'dbscrap' 
# username = 'root' 
# password = '' 
# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = conn.cursor()

# # Create Table
# cursor.execute('CREATE TABLE article_info (Nom nvarchar(50), Date nvarchar(50), ID int, Prix int, Sitemarchand nvarchar(50),FraisDePort int')

# # Insert DataFrame to Table
# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO article_info (Nom, Date, ID, Prix, siteMarchand, FraisDePort')
#                 VALUES (?,?,?,?,?,?)
#                 ''',
#                 row.Nom, 
#                 row.Date,
#                 row.ID,
#                 row.Prix, 
#                 row.SiteMarchand,
#                 row.FraisDePort,
#                 )
# conn.commit()