# R187. Projekt nr.11 Wykres akcji z plotly
# wersja która usuwa MultiIndex w data.columns pobranych z yfinance

import yfinance as yf # pip install yfinance
import plotly.graph_objects as go # pip install plotly

ticker = "TSLA"
userTicker = input("Write ticker name (e.g. TSLA): ")
if userTicker:
    ticker = userTicker.upper().strip()

data = yf.download(tickers=ticker, period="6mo", interval="1d", rounding=True)

if data is not None and not data.empty:
    data.columns = data.columns.get_level_values(0) # spłaszczanie kolumn (usuwa MultiIndex), by wykres miał prawidłową oś Y
    print(f"Data from server for ticker: {ticker}")
    print(data)

    chart = go.Figure()
    chart.add_trace( go.Candlestick(x=data.index,
                        open=data["Open"],
                        high=data["High"],
                        low=data["Low"],
                        close=data["Close"],
                        name="Price chart"
    ) )

    chart.update_layout( title=f"{ticker} share price",
                        yaxis_title="Stock Price (USD)" )

    chart.show()
else:
    print(f"Failed to download data for ticker: {ticker}. Please check if the ticker is correct.")