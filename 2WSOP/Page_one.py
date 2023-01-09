from bs4 import BeautifulSoup
import pandas as pd
import requests


def page1():
    url = 'https://www.wsop.com/tournaments/results/?aid=2&grid=1622&tid=17298&dayof=7651'
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    main = soup.find('ul', {'class': 'results-7'})

    Rank = []
    for rank in main.find_all('li', {'class': 'place1'}):
        Rank.append(rank.text)
    del Rank[0]  # Remove index '#' from list

    Player = []
    for player in main.find_all('li', {'class': 'player1 cellbg'}):
        Player.append(player.text)

    Earning = []
    for earning in main.find_all('li', {'class': 'award1'}):
        Earning.append(earning.text)
    del Earning[0]  # remove index Earning from list

    POY = []
    for poy in main.find_all('li', {'class': 'POYpts cellbg'}):
        POY.append(poy.text)

    City = []
    for city in main.find_all('li', {'class': 'city1'}):
        City.append(city.text)
    del City[0]  # remove index from list

    State = []
    for state in main.find_all('li', {'class': 'state1 cellbg'}):
        State.append(state.text)

    Country = []
    for country in main.find_all('li', {'class': 'country1'}):
        Country.append(country.text)
    del Country[0]  # Remove index from the list

    # columns = [Rank, Player, POY, City, State, Country]
    dict = {'Rank': Rank, 'Player': Player, 'POY': POY, 'City': City, 'State': State, 'Country': Country}
    df = pd.DataFrame(dict)
    df.to_csv('Page1.csv', index=False)


if __name__ == "__main__":
    page1()


