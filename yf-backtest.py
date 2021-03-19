import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
import seaborn

msft = yf.Ticker("MSFT")
BTC = yf.Ticker("BTC-USD")

"""
for multiple stocks
tickers = ["AAPL", "AMZN", "TSLA"]
s = yf.download(tickers,start = "2010-12-20", end = "2020-12-25")
"""


# get historical market data, here max is 1986
def test():


    prices = msft.history(start = "2020-10-01", end = "2021-01-23")
    btcprices = BTC.history(start = "2018-10-01", end = "2021-01-23")
    # these are already dataframes
    print(type(prices))
    print(btcprices)


    #dict for buys. key is price, value is number of shares

    # when adding values if exists
    buys = {}
    #use .get to check if element exists
    last = 0
    balance = 0

    for price in prices["Open"]:
        print(price)
        # last points to the previous element
        if last > price:
            print("bear")
            if buys.get(price) != None:
                #if not already in buys, then buy
                buys[price] += 1
            else:
                #else buy another share at this price
                buys[price] = 1
            balance -= price

        else:
            print("bull")
        last = price

    # then sell
    # last has last price
    for i in buys.keys():
        balance += last * buys[i]
        print(balance)

    last = 0
    balance = 0

    for price in btcprices["Open"]:
        print(price)
        # last points to the previous element
        if last > price:
            print("bear")
            if buys.get(price) != None:
                # if not already in buys, then buy
                buys[price] += 1
            else:
                # else buy another share at this price
                buys[price] = 1
            balance -= price

        else:
            print("bull")
        last = price

    # then sell
    # last has last price
    for i in buys.keys():
        balance += last * buys[i]
        print(balance)


    plt.style.use("ggplot")
    prices["Open"].plot(figsize = (16,9))
    plt.figure()
    btcprices["Open"].plot()

    plt.show()


test()

"""
returns:
              Open    High    Low    Close      Volume  Dividends  Splits
Date
1986-03-13    0.06    0.07    0.06    0.07  1031788800        0.0     0.0
1986-03-14    0.07    0.07    0.07    0.07   308160000        0.0     0.0
...
2019-11-12  146.28  147.57  146.06  147.07    18641600        0.0     0.0
2019-11-13  146.74  147.46  146.30  147.31    16295622        0.0     0.0
"""