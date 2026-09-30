def transform(df):
    df = df.copy()

    df["name"] = df["name"].str.strip()
    df["city"] = df["city"].str.strip()
    df["age"] = df["age"].astype(int)

    return df
