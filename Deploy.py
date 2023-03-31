
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
import datetime as dt
import streamlit.components.v1 as components

# Set dark mode
st.set_page_config(page_title="Egyptian Financial Dashboard",
                   page_icon=":moneybag:", layout="wide")
st.markdown("""
<style>
body {
    color: #fff;
    background-color: #1e1e1e;
}
</style>
    """, unsafe_allow_html=True)


ticker_egg = yf.Ticker("EGP=x")

logo_path = "LI_Logo.png"

logo_url = "https://www.linkedin.com/in/mohamedahmed878/"


with st.container():
    #st.image(logo_path, width=150,use_column_width=True)
    st.markdown("<h3 style='text-align: center;'>" +
                f"<a href='{logo_url}' target='_blank'>Message me via LinkedIn</a>" +
                "</h1>", unsafe_allow_html=True)


today = dt.datetime.now().date()
thirty_days_ago = today - dt.timedelta(days=60)
# Get the data for the past day
hist = ticker_egg.history(period="1d")

# Extract the closing price for the last record
egp_price = hist["Close"].iloc[-1]


st.markdown("<h2 style='text-align: center; color: cyan;'>Daily Real Time Financial Dashboard Crypto And stocks</h3>",
            unsafe_allow_html=True)
st.markdown(
    f"<h2 style='text-align: center; color: lightgreen;'>EGP Now = {egp_price} $</h3>", unsafe_allow_html=True)

crypto, stock = st.tabs(['Crypto', 'Stock'])

#######################################

with crypto:
    ticker = st.selectbox('Choose Stock', [
                          'BTC-USD', 'SHIB-USD', 'ETH-USD', 'XRP-USD', 'DOGE-USD', 'BNB-USD', 'USDT-USD'], key='1')

    start_cr = st.date_input('Start Date', dt.date(2023, 1, 1), key='2')
    end_cr = st.date_input('End Date', key='3')
    data_cr = yf.download(ticker, start=start_cr, end=end_cr)

    fig_cr = px.line(data_cr,
                     x=data_cr.index,
                     y=data_cr['Close'],
                     title=ticker,
                     markers=True)
    st.plotly_chart(fig_cr, use_container_width=True)

with stock:
    ticker = st.selectbox('Choose Stock', ['AAPL', 'AMZN', 'META', "AI", 'GOOGL', 'PLTR',
                                                   'MSFT', 'NFLX', 'TSLA', 'UNH', 'MA', 'ITUB', 'PYPL', 'DIS', 'BAC', 'KO', 'NIO', 'INTC', 'CVX'], key=4)
    start_date = st.date_input('Start Date', dt.date(2023, 1, 1), key=5)
    end_date = st.date_input('End Date', key=6)
    data = yf.download(ticker, start=start_date, end=end_date)
    fig_st = px.line(data,
                     x=data.index,
                     y=data['Close'],
                     title=ticker,
                     markers=True)
    st.plotly_chart(fig_st, use_container_width=True)

with st.container():
    st.markdown("<h2 style='text-align: center; color: lightblue;'>Available Services</h2>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: lightgreen;'>Chat Bots</h3><p style='text-align: center;'>Our chat bots are designed to provide you with quick and personalized customer service 24/7.</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: lightgreen;'>Trading Bots</h3><p style='text-align: center;'>Our trading bots use advanced algorithms to help you make informed investment decisions and maximize your profits.</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: lightgreen;'>Stock Analysis</h3><p style='text-align: center;'>We offer comprehensive stock analysis tools to help you identify investment opportunities and make sound financial decisions.</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: lightgreen;'>Your personal Dashboard</h3><p style='text-align: center;'>Personalized Dashboard for your stocks and Crypto integrated with spot trends algorithms. </p>", unsafe_allow_html=True)
