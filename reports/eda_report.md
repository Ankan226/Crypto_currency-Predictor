# Exploratory Data Analysis (EDA) Report

## Dataset Overview

The dataset contains historical cryptocurrency market data including price and market statistics for multiple cryptocurrencies.

### Features in Dataset

- open : Opening price of cryptocurrency
- high : Highest price during the day
- low : Lowest price during the day
- close : Closing price
- volume : Trading volume
- marketCap : Market capitalization
- crypto_name : Cryptocurrency name
- date : Date of transaction

---

## Data Cleaning

The following preprocessing steps were applied:

- Removed unnecessary column `Unnamed: 0`
- Converted `date` column into datetime format
- Sorted data based on cryptocurrency name and date
- Handled missing values using forward fill

---

## Feature Engineering

New features were created to improve model performance:

- MA7 : 7-day moving average
- MA30 : 30-day moving average
- volatility : Rolling standard deviation of close price
- liquidity_ratio : volume / marketCap
- price_range : high - low

---

## Data Visualization

The following visualizations were performed:

1. Closing Price Distribution
2. Price comparison across cryptocurrencies
3. Correlation heatmap between features
4. Cryptocurrency price trends over time

These visualizations helped understand patterns, relationships and price behavior of different cryptocurrencies.

---

## Key Observations

- Cryptocurrency prices show high volatility.
- Trading volume has moderate correlation with price movement.
- Liquidity ratio helps understand trading activity.
- Volatility spikes occur during major market movements.