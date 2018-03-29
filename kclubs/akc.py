from bs4 import BeautifulSoup
import json
import requests
import os

page = requests.get('http://www.akc.org/')
soup = BeautifulSoup(page.text, 'html.parser')
raw_breed_list = soup.find(id='breed-search')
filtered_breed_list = []
for breed in raw_breed_list.find_all('option'):
    if breed['value'] != '':
        filtered_breed_list.append(breed.text)
repo_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
outfile = os.path.join(repo_dir, 'data', 'akc.json')
with open(outfile, 'w') as ofile:
    json.dump(filtered_breed_list, ofile)

