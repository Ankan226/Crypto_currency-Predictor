import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# load processed dataset
df = pd.read_csv("data/processed_crypto_data.csv")


# selected features
features = [
    "open",
    "high",
    "low",
    "close",
    "volume",
    "marketCap",
    "MA7",
    "MA30",
    "liquidity_ratio",
    "price_range",
]


X = df[features]

y = df["volatility"]


# train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# train model
model.fit(X_train, y_train)


# ensure model folder exists
os.makedirs("model", exist_ok=True)


# save model
joblib.dump(model, "model/crypto_model.pkl")


print("Model trained and saved successfully")