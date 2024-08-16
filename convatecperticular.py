from bs4 import BeautifulSoup
import requests
source=requests.get('https://www.vitalitymedical.com/convatec-activelife-one-piece-drainable-pouch-cut-to-fit-022771-125330.html').text
soup=BeautifulSoup(source,'lxml')

product=soup.find('h1', class_="h1").text
print(product)

print()

price=soup.find('span', class_="special-price").text
print(price)

