# -*- coding: utf-8 -*-
from datetime import date

import logging
import os
import time
from historical.StockListDownloader import StockListDownloader
from historical.yahoo.YahooDataDownloader import YahooDataDownloader
from historical.yahoo.YahooDataUpdater import YahooDataUpdater

logging.basicConfig(level=logging.INFO)
start = time.clock()


# Those commands are for downloading lists os stocks from www.nasdaq.com
StockListDownloader("nyse").downloadAndConvertStockList()
StockListDownloader("nasdaq").downloadAndConvertStockList()

# Those commands downloads historical data from yahoo finance for stocks given in stockName-list.csv, between given dates
YahooDataDownloader("nyse").downloadStocks(date(2009, 1, 1), date.today())
YahooDataDownloader("nasdaq").downloadStocks(date(2009, 1, 1), date.today())

# Those commands updates historical data if there are new data online, up to given date
#YahooDataUpdater("nyse").updateStocks(date.today())
#YahooDataUpdater("nasdaq").updateStocks(date.today())

end = time.clock()
print "All work took " + str(end - start) + " seconds."