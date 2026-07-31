import yfinance as yf
import plotly.graph_objects as go

ticker = "TSLA"
userTicker = input("Write ticker name (e.g. TSLA): ")
if userTicker:
    ticker = userTicker.upper().strip()

data = yf.download(tickers=ticker, period="6mo", interval="1d", rounding=True)
print(f"Data from server for ticker: {ticker}")
# print(data)

if data is not None and not data.empty:
    chart = go.Figure()
    chart.add_trace( go.Candlestick(x=data.index,
                                    open=data[("Open", ticker)],
                                    high=data[("High", ticker)],
                                    low=data[("Low", ticker)],
                                    close=data[("Close", ticker)],
                                    name="Price chart"
                                    ))
    
    chart.update_layout( title = f"{ticker} share price", 
                        yaxis_title="Stock Price (USD)" )
    
    chart.show()
    
else:
    print("Wrong ticker: ", ticker)