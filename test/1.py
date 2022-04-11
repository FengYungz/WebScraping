import requests
from bs4 import BeautifulSoup

req = requests.get('https://sorteia-quiz.vercel.app/')
req.encoding = 'utf-8'

soup = BeautifulSoup('html.parser')
print(soup)