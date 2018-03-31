from bs4 import BeautifulSoup
import csv
import os
import requests


def fetch_data(data_dir):
    page = requests.get('https://www.ukcdogs.com/breed-standards/')
    soup = BeautifulSoup(page.text, 'html.parser')
    selection = soup.find(id='dog_breed_jumplist')
    with open(os.path.join(data_dir, 'ukc.csv'), 'w') as outfile:
        wr = csv.writer(outfile, lineterminator=',\n')
        for linenum, breed in enumerate(selection.find_all('option')):
            if not linenum:
                wr.writerow(['breed'])
            if breed['value'] != '':
                wr.writerow([breed.text])


if __name__ == '__main__':
    club_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
    data_dir = os.path.join(os.path.split(club_dir)[0], 'data')
    fetch_data(data_dir)
