from bs4 import BeautifulSoup
import csv
import os
import requests


def fetch_data(data_dir):
    page = requests.get('https://ckcusa.com/breeds/')
    soup = BeautifulSoup(page.text, 'html.parser')
    selection = soup.find(id='combobox')
    with open(os.path.join(data_dir, 'ckc.csv'), 'w') as outfile:
        wr = csv.writer(outfile, lineterminator='\n')
        for breed in selection.find_all('option'):
            wr.writerow([breed.text])


if __name__ == '__main__':
    club_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
    data_dir = os.path.join(os.path.split(club_dir)[0], 'data')
    fetch_data(data_dir)
