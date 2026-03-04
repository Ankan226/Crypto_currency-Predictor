import pandas as pd


def load_data():

    df = pd.read_csv("data/dataset_crypto.csv.csv")

    print("Dataset Loaded Successfully\n")
    print(df.head())

    return df


def clean_data(df):

    # drop useless column
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # convert date
    df["date"] = pd.to_datetime(df["date"])

    # sort data
    df = df.sort_values(["crypto_name", "date"])

    print("\nMissing Values\n")
    print(df.isnull().sum())

    # fill missing values
    df = df.ffill()

    return df


if __name__ == "__main__":

    df = load_data()

    df = clean_data(df)

    # save cleaned dataset
    df.to_csv("data/cleaned_crypto_data.csv", index=False)

    print("\nCleaned dataset saved")