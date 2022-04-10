from matplotlib import ticker
import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""
#Simple Webpage using datascience content

Below are some of the current datas\nThey show the **Volumes** and ***Closing price***

"""
)
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '1d', start = '2010-5-31', end= '2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

