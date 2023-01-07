"""
A script to scrape Jumia Hp laptops
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

import requests
from bs4 import BeautifulSoup


def non_sponsor():
    url = 'https://www.jumia.com.ng/laptops/hp/'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    names = soup.findAll('h3', {'class': 'name'})
    price = soup.findAll('div', {'class': 'prc'})
    actual_price = soup.findAll('div', {'class': 'old'})
    percentage = soup.findAll('div', {'class': 'bdg _dsct _sm'})
    ratings = soup.findAll('div', {'class': 'rev'})

    for name in names:
        print(f'Names: {name.getText()}')
    for prices in price:
        print(f'Discount Price: {prices.getText()}')
    for actual in actual_price:
        print(f'Actual Price: {actual.getText()}')
    for percent in percentage:
        print(f'Percentage: {percent.getText()}')
    for rating in ratings:
        print(f'Rating: {rating.getText()}')


if __name__=='__main__':
    non_sponsor()

