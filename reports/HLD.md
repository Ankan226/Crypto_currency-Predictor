# High Level Design (HLD)

## System Overview

The Cryptocurrency Volatility Prediction system uses historical cryptocurrency market data to predict future volatility using machine learning.

---

## Architecture

User Input → Streamlit Interface → Feature Processing → ML Model → Prediction Output

---

## Components

### Data Layer
Stores cryptocurrency historical data including OHLC prices, volume and market capitalization.

### Data Processing Layer
Handles:
- Data cleaning
- Feature engineering
- Data preparation

### Machine Learning Layer
Random Forest Regression model trained on processed features to predict volatility.

### Deployment Layer
Streamlit web interface used to allow users to input values and get volatility predictions.

---

## Technology Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib / Seaborn