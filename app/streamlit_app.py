import streamlit as st
import numpy as np
import joblib


# page config
st.set_page_config(
    page_title="Crypto Volatility Predictor",
    page_icon=" 📈",
    layout="centered"
)


# load model
model = joblib.load("model/crypto_model.pkl")


st.title("Cryptocurrency Volatility Predictor")

st.write(
"""
This tool predicts **market volatility** based on cryptocurrency price indicators.
Enter the market values below to estimate volatility.
"""
)


# input columns
col1, col2 = st.columns(2)


with col1:
    open_price = st.number_input("Open Price", min_value=0.0)
    high_price = st.number_input("High Price", min_value=0.0)
    low_price = st.number_input("Low Price", min_value=0.0)


with col2:
    close_price = st.number_input("Close Price", min_value=0.0)
    volume = st.number_input("Volume", min_value=0.0)
    market_cap = st.number_input("Market Cap", min_value=0.0)


if st.button("Predict Volatility "):

    # derived features
    MA7 = close_price
    MA30 = close_price

    liquidity_ratio = volume / market_cap if market_cap != 0 else 0
    price_range = high_price - low_price


    features = np.array([[
        open_price,
        high_price,
        low_price,
        close_price,
        volume,
        market_cap,
        MA7,
        MA30,
        liquidity_ratio,
        price_range
    ]])


    prediction = model.predict(features)[0]


    st.success(f"Predicted Volatility: {prediction:.4f}")


    if prediction < 5:
        st.info("Market volatility is LOW")
    elif prediction < 20:
        st.warning("Market volatility is MODERATE")
    else:
        st.error("Market volatility is HIGH")