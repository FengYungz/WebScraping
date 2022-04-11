import requests
from bs4 import BeautifulSoup

page = requests.get('https://br.pinterest.com/charlottesears/scrap-quotes/')
soup = BeautifulSoup(page.content, 'html.parser')
#ret = soup.find('div',{'class':'pega'})
#ret = soup.find('div', class_='pega')

ret = soup.findAll('div')
print(f"O texto é: {ret}")

print(f"Status so request: {page}")