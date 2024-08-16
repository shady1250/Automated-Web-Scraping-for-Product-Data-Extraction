from bs4 import BeautifulSoup
import requests
source=requests.get('https://www.vitalitymedical.com/andover-coflex.html').text
soup=BeautifulSoup(source,'lxml')

table=soup.find('div', class_="grouped-items-table-wrapper desktop-items")
itemno=table.find('td', class_="manu-sku")
print(itemno.text)
pricepp=table.find('div', class_="price-box")
pricep=pricepp.find('p', class_="special-price")
lab=pricep.find('span', class_="price-label").text
if lab=="Sale Price:":
     price=pricep.find('span',class_="price").text
else:
    price=table.find('span', class_="special-price")
print(price)

    
        
