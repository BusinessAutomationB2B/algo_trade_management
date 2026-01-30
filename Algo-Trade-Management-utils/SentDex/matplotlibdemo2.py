# http://quantlabs.net/blog/2016/01/simplest-candlestick-demo-with-python-matplotlib/
# Source code:

# -*- coding: utf-8 -*-
#
# Created on Tue Jan 26 19:28:55 2016

# @author: quantlabsnet
#
#Python in Finance p107

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

start = (2016, 5, 1)
end = (2017, 6, 30)
# quotes = mpf.quotes_historical_yahoo_ohlc('^GDAXI', start, end)
quotes = mpf.quotes_historical_yahoo_ohlc('AXTA', start, end)

quotes[:2]

fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)

print('Hello')
 
mpf.candlestick_ohlc(ax, quotes, width=0.6, colorup='b', colordown='r')
 
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
ax.autoscale_view()

plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.show()
 
print('bye')