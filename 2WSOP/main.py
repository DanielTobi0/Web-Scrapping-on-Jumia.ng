from Page1 import page1
from Page2 import page2
import pandas as pd
import os


def combine_csv():
    master_df = pd.DataFrame()

    for file in os.listdir(os.getcwd()):
        if file.endswith(".csv"):
            master_df = master_df.append(pd.read_csv(file))

    master_df.to_csv("WSOP.csv", index=False)


if __name__ == "__main__":
    page1()
    page2()
    combine_csv()
