from page_one import page1
from page_two import page2
import pandas as pd
import os


def combine_csv():
    master_df = pd.DataFrame()

    for file in os.listdir(os.getcwd()):
        if file.endswith(".csv"):
            master_df = master_df.append(pd.read_csv(file))

    master_df.to_csv("C:/Users/Daniel/PycharmProjects/Web_scrapping/2WSOP/data/combine_csv.csv", index=False)


if __name__ == "__main__":
    page1()
    page2()
    combine_csv()
