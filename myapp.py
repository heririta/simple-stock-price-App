from fileinput import close
import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
         # Simple Stock Price App

         show are the stock **closing price** and ***volume*** of Google!


         """)


tickerSimbol = 'GOOGL'

tickerData = yf.Ticker(tickerSimbol)

tickerDf = tickerData.history(
    periode='1d', start='2021-01-31', end='2022-01-31')


st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)
