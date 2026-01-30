import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

import mplfinance as mpf  # extra lib for pour candle stick chart

ticker = "BOE.AX"

df = yf.download(
    "BOE.AX",
    start="2020-01-01",
    auto_adjust=False,   # no corporate action adjustment just raw price
    group_by="column"    # 
)
# above df has multi header rows
'''
Price      Adj Close  Close   High    Low   Open  Volume
Ticker        BOE.AX BOE.AX BOE.AX BOE.AX BOE.AX  BOE.AX
Date                                                    
2020-01-02     0.392  0.392  0.408  0.392  0.408   29833
2020-01-03     0.400  0.400  0.408  0.400  0.408    9863
2020-01-06     0.400  0.400  0.424  0.384  0.424  104375
2020-01-07     0.392  0.392  0.392  0.376  0.392   32908
'''

df = df.droplevel(1, axis=1) if isinstance(df.columns, pd.MultiIndex) else df  # remove second header, row
print(df.head())


# display chart using mplfinance
'''
mpf.plot(
    df,
    type="candle",
    volume=True,
    style="yahoo",
    title="BOE.AX Price",
)
'''

fig = go.Figure(
    data=[
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Price"
        )
    ]
)

fig.update_layout(
    title="BOE.AX Interactive Candlestick Chart",
    xaxis_title="Date",
    yaxis_title="Price",
    xaxis_rangeslider_visible=True,  # bottom range slider
    template="plotly_white"
)

fig.show()