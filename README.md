# Cryptocurrency Volatility Prediction

## Project Overview

Cryptocurrency markets are highly volatile and unpredictable. Understanding and forecasting volatility is important for traders, investors, and financial analysts.

This project builds a **machine learning model to predict cryptocurrency volatility** using historical market data such as price movements, trading volume, and market capitalization.

The model analyzes historical patterns and predicts potential volatility levels.

---

## Dataset

The dataset contains historical daily cryptocurrency data including:

- Open price
- High price
- Low price
- Close price
- Trading volume
- Market capitalization
- Cryptocurrency name
- Date

Additional features were engineered to improve prediction accuracy.

---

## Features Created

Feature engineering was performed to generate useful indicators:

- **MA7** – 7-day moving average
- **MA30** – 30-day moving average
- **Volatility** – rolling standard deviation of closing price
- **Liquidity Ratio** – trading volume divided by market cap
- **Price Range** – difference between high and low price

These features help the model understand market behavior.

---

## Machine Learning Model

The project uses a **Random Forest Regressor** to predict volatility.

Random Forest was chosen because it:

- Handles nonlinear financial data well
- Works effectively with tabular datasets
- Reduces overfitting through ensemble learning

---

## Model Performance

Evaluation metrics used:

- **RMSE (Root Mean Square Error)** : 62.52  
- **MAE (Mean Absolute Error)** : 9.53  
- **R² Score** : 0.9376  

The high R² score indicates that the model explains a significant portion of the volatility variance.

---

## Project Structure
Crypto_Currency Prediction
│
├── data
│ ├── dataset_crypto.csv
│ ├── cleaned_crypto_data.csv
│ └── processed_crypto_data.csv
│
├── src
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── model_training.py
│ └── evaluation.py
│
├── app
│ └── streamlit_app.py
│
├── model
│ └── crypto_model.pkl
│
├── notebooks
│ └── EDA.ipynb
│
├── reports
│ ├── eda_report.md
│ ├── HLD.md
│ ├── LLD.md
│ └── final_report.md
│
├── requirements.txt
└── README.md


---

## Project Pipeline

1. Data Collection  
2. Data Preprocessing  
3. Feature Engineering  
4. Exploratory Data Analysis  
5. Model Training  
6. Model Evaluation  
7. Deployment using Streamlit

---

## Running the Project

### Create Python Environment
python -m venv crypto_env

### Activate Environment
crypto_env\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Run preprocessing
python src/data_preprocessing.py

### Run feature engineering
python src/feature_engineering.py

### Train the model
python src/model_training.py

### Evaluate the model
python src/evaluation.py

### Run Streamlit application
streamlit run app/streamlit_app.py