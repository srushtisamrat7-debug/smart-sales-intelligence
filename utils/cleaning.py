import pandas as pd


def clean_data(df):
    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    return df