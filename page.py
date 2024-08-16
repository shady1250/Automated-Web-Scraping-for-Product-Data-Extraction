from bs4 import BeautifulSoup
import requests
import re
source=requests.get('https://www.vitalitymedical.com/convatec.html').text
soup=BeautifulSoup(source,'lxml')

page=soup.find('div', class_="count-container")
if page.find('p', class_="amount amount--has-pages") is not None:
    y=page.find('p', class_="amount amount--has-pages").text.split()
    x=(int(y[2]))

    if x%20==0:
        p=int(x/20)
    else:
        p=int( (x/20)+1)

    for i in range(0,p,1):
        for product in soup.find_all('li', class_="item last"):   
            title=product.find('h2', class_="product-name").text
            print(title)
        tool=soup.find('div', class_="toolbar")
        pg=tool.find('div', class_="pages")
        lin=pg.find('a', class_="next i-next")
        if lin is not None:
            linn="https://www.vitalitymedical.com/" + lin['href']
            source=requests.get(linn).text
            soup=BeautifulSoup(source,'lxml')

else:
    print('hello')
