from bs4 import BeautifulSoup
import requests
source=requests.get('https://www.vitalitymedical.com/andover-coflex.html').text
soup=BeautifulSoup(source,'lxml')

x=soup.find('table', id="super-product-table")
table_rows=x.find_all('tr')

for tr in table_rows:
    pid=tr.find_all('td', class_="manu-sku")
    for i in pid:
        print(i.text)
        
    des=tr.find_all('td', class_="name")
    for i in des:
        print(i.text)

    size=tr.find_all('td', class_="uom")
    for i in size:
        print(i.text)

 
    
    td=tr.find_all('td', class_="price-col")
    for i in td:
        price=i.find('p', class_="special-price")
        if price is not None:
            pricex=price.find('span',class_="price")
            print(pricex.text)
        if price is None:
            pricey=i.find('span', class_="special-price")
            pricey=pricey.find('span', class_="price")
            print(pricey.text)



    

                           
