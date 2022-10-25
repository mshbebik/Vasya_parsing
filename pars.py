from urllib import response
import requests
from bs4 import BeautifulStoneSoup

url = 0
while url < 7: 
    url += 1
    url1 = f'https://scrapingclub.com/exercise/list_basic/?page={url}'
    response = requests.get(url1)
    soup = BeautifulStoneSoup(response.text)

    bots = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
    for tag in bots:   
        tag1 = tag.find("a").get("href")
        tag2 = f"https://scrapingclub.com{tag1}"
        response = requests.get(tag2)
        soup1 = BeautifulStoneSoup(response.text)
        names = soup1.find_all('h3', class_="card-title")
        prices = soup1.find_all('h4', class_=None)
        bots2 = soup1.find_all('div', class_="container mt-4")
        opis = soup1.find_all('p', class_="card-text")
    
    
        for i in range(0, len(bots2)):
                print(names[i].text)
                print(' ')
                print(prices[i].text)
                print(' ')
                print(opis[i].text)
                print('---' * 20)

