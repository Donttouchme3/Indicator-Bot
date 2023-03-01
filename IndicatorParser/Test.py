import requests
from bs4 import BeautifulSoup

Html = requests.get('https://indicator.ru/').text
Soup = BeautifulSoup(Html, 'html.parser')
print(Soup)