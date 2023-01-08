from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

url = 'https://www.jumia.com.ng/laptops/hp/'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
hp = soup.find_all('article', {'class': ['prd _fb _spn c-prd col', 'prd _fb col c-prd']})


def jumia_hp():
    with open('hp_laptops.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Name', 'Price', 'old_price', 'link', 'rating', 'percentage']
        thewriter.writerow(header)
        for h in hp:
            name = h.find('h3', class_='name').get_text()
            price = h.find('div', class_='prc').get_text()
            old_price = h.find('div', class_='old')
            link = h.find('a', class_='core')['href']
            rating = h.find('div', class_='stars _s')
            percentage = h.find('div', class_='bdg _dsct _sm')

            if old_price is None:
                old_price = None
            if old_price is not None:
                old_price = old_price.get_text()
            if rating is None:
                rating = None
            if rating is not None:
                rating = rating.get_text()
            if rating is None:
                rating = None
            if percentage is not None:
                percentage = percentage.get_text()
            if link is not None:
                link = 'https://www.jumia.com.ng/laptops/' + link

            info = [name, price, old_price, link, rating, percentage]
            thewriter.writerow(info)


if __name__ == '__main__':
    jumia_hp()
