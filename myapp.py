import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
         # Simple Stock Price App

         show are the stock **closing price** and ***volume*** of Google!

         """)

# https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

tickerSimbol = 'ELSA.JK'

tickerData = yf.Ticker(tickerSimbol)

tickerDf = tickerData.history(
    periode='1d', start='2021-01-31', end='2022-02-04')

st.write("""
         ## Closing Price
         """)
st.line_chart(tickerDf.Close)

st.write("""
         ## Volume
         """)
st.line_chart(tickerDf.Volume)
