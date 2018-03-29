from bs4 import BeautifulSoup
import json
import requests
import os

page = requests.get('https://ckcusa.com/breeds/')
soup = BeautifulSoup(page.text, 'html.parser')
raw_breed_list = soup.find(id='combobox')
filtered_breed_list = []
for breed in raw_breed_list.find_all('option'):
    if breed['value'] != '':
        filtered_breed_list.append(breed.text)
repo_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
outfile = os.path.join(repo_dir, 'data', 'ckc.json')
with open(outfile, 'w') as ofile:
    json.dump(filtered_breed_list, ofile)

