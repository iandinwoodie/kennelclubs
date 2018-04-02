from bs4 import BeautifulSoup
import csv
import os
import requests


def fetch_data(data_dir):
    base_url = 'https://www.kusa.co.za/index.php/documents/breed-standards/'
    groups = ['gundog-group', 'herding-group', 'hound-group', 'terrier-group',
              'toy-group', 'working-group', 'utility-group', 'emerging-breeds']
    breeds = []
    for group in groups:
        page = requests.get(base_url + group)
        soup = BeautifulSoup(page.text, 'html.parser')
        selection = soup.find(id='adminForm')
        for linenum, breed in enumerate(selection.find_all('a')):
                breeds.append(breed.text)
    with open(os.path.join(data_dir, 'kusa.csv'), 'w') as outfile:
        wr = csv.writer(outfile, lineterminator=',\n')
        for linenum, breed in enumerate(breeds):
            if not linenum:
                    wr.writerow(['breed'])
            wr.writerow([breed])


if __name__ == '__main__':
    club_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
    data_dir = os.path.join(os.path.split(club_dir)[0], 'data')
    fetch_data(data_dir)
