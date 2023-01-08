import requests
from _csv import writer
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

"""
Extracting  Role,
            Company Name,
            Address,
            Date Posted,
            Apply
"""

job = soup.find_all('div', {'class': 'card-content'})


def fake_jobs():
    with open('fake_jobs.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Role', 'Company', 'Address', 'Date', 'Apply']
        thewriter.writerow(header)

        for h in job:
            role = h.find('h2', class_='title is-5').get_text()
            company = h.find('h3', class_='subtitle is-6 company').get_text()
            address = h.find('p', class_='location').get_text().replace('\n', '')
            date = h.find('time').get_text()
            apply = h.find_all('a', class_='card-footer-item')[1]['href']

            info = [role, company, address, date, apply]
            thewriter.writerow(info)


if __name__ == '__main__':
    fake_jobs()
