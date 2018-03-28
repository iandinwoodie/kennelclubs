import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.akc.org/dog-breeds/')
soup = BeautifulSoup(page.text, 'html.parser')
raw_breed_list = soup.find(class_='custom-select')
for breed in raw_breed_list.find_all('option'):
    if not breed.find(value_=''):
        name = breed.contents[0]
        print(name)
