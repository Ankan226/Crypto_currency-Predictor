import pandas as pd
import numpy as np


df = pd.read_csv("data/cleaned_crypto_data.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["crypto_name", "date"])


# Moving averages
df["MA7"] = df.groupby("crypto_name")["close"].transform(
    lambda x: x.rolling(7).mean()
)

df["MA30"] = df.groupby("crypto_name")["close"].transform(
    lambda x: x.rolling(30).mean()
)


# Volatility
df["volatility"] = df.groupby("crypto_name")["close"].transform(
    lambda x: x.rolling(7).std()
)


# Liquidity ratio (safe division)
df["liquidity_ratio"] = df["volume"] / df["marketCap"]

# replace infinite values
df.replace([np.inf, -np.inf], np.nan, inplace=True)


# Price range
df["price_range"] = df["high"] - df["low"]


# drop missing rows
df = df.dropna()


df.to_csv("data/processed_crypto_data.csv", index=False)

print("Feature engineering completed")
print(df.head())