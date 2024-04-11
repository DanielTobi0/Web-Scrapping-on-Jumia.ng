import requests
from _csv import writer
from bs4 import BeautifulSoup


def fake_jobs():
    """
    Extracting  Role,
                Company Name,
                Address,
                Date Posted,
                Apply
    """
    url = 'https://realpython.github.io/fake-jobs/'
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', {'class': 'card-content'})

    with open('jobs.csv', 'w', encoding='utf8', newline='') as f:
        csv_writer = writer(f)
        header = ['Role', 'Company', 'Address', 'Date', 'Apply']
        csv_writer.writerow(header)

        for job in jobs:
            role = job.find('h2', class_='title is-5').get_text()
            company = job.find('h3', class_='subtitle is-6 company').get_text()
            address = job.find('p', class_='location').get_text().replace('\n', '')
            date = job.find('time').get_text()
            apply = job.find_all('a', class_='card-footer-item')[1]['href']

            info = [role, company, address, date, apply]
            csv_writer.writerow(info)


if __name__ == '__main__':
    fake_jobs()
