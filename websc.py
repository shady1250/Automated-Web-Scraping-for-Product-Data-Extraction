from bs4 import BeautifulSoup
import requests
source=requests.get('https://www.amazon.in/s?k=samsung+galaxy+m20&ref=nb_sb_noss').text
soup=BeautifulSoup(source,'lxml')

print(soup)

for article in soup.find_all('div', class_="sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"):
    title=article.find('span', class_='a-size-medium a-color-base a-text-normal').text
    print(title)
    amount=article.find('span', class_='a-price-whole').text
    print(amount)
    print()

    
