from bs4 import BeautifulSoup 
import requests
from fake_useragent import UserAgent 

user_agent = {"user-agent":UserAgent().chrome}
url = "https://www.turkiye.gov.tr/doviz-kurlari"
r = requests.get(url,headers=user_agent)

if r.ok:
	soup = BeautifulSoup(r.text,"html.parser")
	liste = list()
	for i in soup.find_all("td"):
		liste.append(i.text)

	# Dolar
	print("*"*30);print(liste[0]);print("Alış:",liste[1]);print("Satış:",liste[2]);print("Efektif alış:",liste[3]);print("Efektif satış:",liste[4]);print("*"*30)
	# Euro
	print(liste[15]);print("Alış:",liste[16]);print("Satış:",liste[17]);print("Efektif alış:",liste[18]);print("Efektif satış:",liste[19]);print("*"*30)
	# Sterlin
	print(liste[20]);print("Alış:",liste[21]);print("Satış:",liste[22]);print("Efektif alış:",liste[23]);print("Efektif satış:",liste[24]);print("*"*30)
		
else:
	print("Bağlantı sağlanamadı!")