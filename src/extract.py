import pandas as pd


def extract():
    df = pd.read_csv("data/customers.csv")
    print(f"Extracted {len(df)} customers")
    return df
