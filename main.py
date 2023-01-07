"""
A script to scrape Jumia Hp laptops
"""

import requests
from bs4 import BeautifulSoup
import csv


def non_sponsor():
    url = 'https://www.jumia.com.ng/laptops/hp/'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    names = soup.findAll('h3', {'class': 'name'})
    price = soup.findAll('div', {'class': 'prc'})
    actual_price = soup.findAll('div', {'class': 'old'})
    percentage = soup.findAll('div', {'class': 'bdg _dsct _sm'})
    ratings = soup.findAll('div', {'class': 'rev'})
    links = soup.findAll('a', {'class': 'core'})

    for name, prices, actual, percent, rating, link in zip(names, price, actual_price, percentage, ratings, links):
        print(
            f'Name: {name.getText()}\nPrice: {prices.getText()}\nActual Price: {actual.getText()}\nPercentage: {percent.getText()}\nRating: {rating.getText()}\nLink: https://www.jumia.com.ng/{link.get("href").replace("/", "")}')
        print('\n')



if __name__ == '__main__':
    non_sponsor()
