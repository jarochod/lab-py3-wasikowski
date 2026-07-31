# R187. Projekt nr.11 Wykres akcji z plotly
# wersja która używa data MultiIndex pobranych z yfinance

import yfinance as yf
import plotly.graph_objects as go

ticker = "TSLA"
userTicker = input("Write ticker name (e.g. TSLA): ")
if userTicker:
    ticker = userTicker.upper().strip()

# Pobieranie danych, które mogą mieć MultiIndex
data = yf.download(tickers=ticker, period="6mo", interval="1d", rounding=True)

# Sprawdzanie, czy dane są puste i czy zawierają MultiIndex
if data is not None and not data.empty:
    print(f"Data from server for ticker: {ticker}")
    print(data)

    chart = go.Figure()
    chart.add_trace(go.Candlestick(x=data.index,
                        # Poprawne, dynamiczne odwołanie do kolumn
                        # Używamy zmiennej 'ticker' wewnątrz tupli.
                        open=data[('Open', ticker)],
                        high=data[('High', ticker)],
                        low=data[('Low', ticker)],
                        close=data[('Close', ticker)],
                        name="Price chart"
                        ))

    chart.update_layout(title=f"{ticker} share price",
                        yaxis_title="Stock Price (USD)")
    chart.show()
else:
    print(f"Failed to download data for ticker: {ticker} or data is empty. Please check if the ticker is correct.")