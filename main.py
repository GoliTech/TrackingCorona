from bs4 import BeautifulSoup
import requests

url = 'https://www.worldometers.info/coronavirus/'
r = requests.get(url)
x = BeautifulSoup(r.text, "html.parser")
info = x.find_all("div", class_="maincounter-number")

print('Total Cases : ', info[0].text.strip())
print('Total Deaths : ', info[1].text.strip())
print('Total Covered : ', info[2].text.strip())



