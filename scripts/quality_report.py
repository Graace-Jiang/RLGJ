import hashlib
import pandas as pd


def sha256_file(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def profile_csv(path, name):
    print(f"\n===== {name} =====")
    df = pd.read_csv(path)

    print("\nRows and columns:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nNumeric summary:")
    print(df.describe())

    return df


def profile_excel(path, name):
    print(f"\n===== {name} =====")
    df = pd.read_excel(path, sheet_name="Industry Averages", header=None)

    print("\nRows and columns:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    return df


print("===== SHA-256 FILE INTEGRITY CHECK =====")
files = [
    "data/sp500_dividend_data.csv",
    "data/marginGlobal.xls",
]

for file in files:
    print(f"{file}: {sha256_file(file)}")


profile_csv("data/sp500_dividend_data.csv", "Raw Yahoo Finance Dataset")
profile_excel("data/marginGlobal.xls", "Raw Damodaran Dataset")
profile_csv("data/final_dataset.csv", "Merged Dataset")
profile_csv("data/clean_final_dataset.csv", "Clean Final Dataset")