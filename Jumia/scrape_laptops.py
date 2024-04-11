from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer

driver = webdriver.Chrome('C:/Users/Daniel/PycharmProjects/chromedriver.exe')
driver.maximize_window()

url = 'https://www.jumia.com.ng/laptops/hp/'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
hp_laptops = soup.find_all('article', {'class': ['prd _fb _spn c-prd col', 'prd _fb col c-prd']})


def extract_jumia_hp():
    with open('hp_laptops.csv', 'w', encoding='utf8', newline='') as f:
        csv_writer = writer(f)
        header = ['Name', 'Price', 'old_price', 'link', 'rating', 'discount_percentage']
        csv_writer.writerow(header)
        for hp_article in hp_laptops:
            name = hp_article.find('h3', class_='name').get_text()
            price = hp_article.find('div', class_='prc').get_text()
            old_price = hp_article.find('div', class_='old')
            link = hp_article.find('a', class_='core')['href']
            rating = hp_article.find('div', class_='stars _s')
            discount_percentage = hp_article.find('div', class_='bdg _dsct _sm')

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
            if discount_percentage is not None:
                discount_percentage = discount_percentage.get_text()
            if link is not None:
                link = 'https://www.jumia.com.ng/laptops/' + link

            info = [name, price, old_price, link, rating, discount_percentage]
            csv_writer.writerow(info)
    driver.quit()


if __name__ == '__main__':
    extract_jumia_hp()
