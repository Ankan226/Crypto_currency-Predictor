import pandas as pd
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


df = pd.read_csv("data/processed_crypto_data.csv")


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


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = joblib.load("model/crypto_model.pkl")


predictions = model.predict(X_test)


# metrics
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)


print("Model Evaluation Results")
print("RMSE:", rmse)
print("MAE:", mae)
print("R2 Score:", r2)