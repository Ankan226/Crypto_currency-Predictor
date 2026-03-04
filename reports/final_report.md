# Cryptocurrency Volatility Prediction – Final Report

## Problem Statement

Cryptocurrency markets are highly volatile. Predicting volatility helps investors and traders manage risk and make better financial decisions.

The objective of this project is to build a machine learning model capable of predicting cryptocurrency volatility using historical market data.

---

## Dataset Description

The dataset contains historical records of multiple cryptocurrencies including:

- Open price
- High price
- Low price
- Close price
- Trading volume
- Market capitalization
- Date

---

## Data Preprocessing

The following steps were applied:

- Removal of unnecessary columns
- Handling missing values
- Date formatting
- Sorting data for time-series consistency

---

## Feature Engineering

Additional features were created to improve prediction performance:

- Moving averages (MA7 and MA30)
- Liquidity ratio
- Price range
- Rolling volatility

---

## Model Selection

Random Forest Regressor was chosen due to its ability to capture nonlinear relationships and handle complex financial data.

---

## Model Evaluation

Model performance was evaluated using:

- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)
- R² Score

### Results

RMSE : 62.52  
MAE : 9.53  
R² Score : 0.9376

The high R² score indicates that the model explains a large portion of variance in cryptocurrency volatility.

---

## Deployment

The trained model was deployed using a Streamlit web application that allows users to input market indicators and obtain predicted volatility.

---

## Conclusion

The developed system successfully predicts cryptocurrency volatility using historical price indicators and machine learning techniques. The model achieved strong predictive performance and provides a useful tool for understanding cryptocurrency market behavior.