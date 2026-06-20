import pandas as pd

def datasets():
    try:
        return pd.read_csv("./data/social_following.csv")
    except FileNotFoundError:
        print("Data tidak di temukan. Pastikan data telah berada didalam folder ./data/social_following.csv")
        exit(1)