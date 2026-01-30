'''
Created on Jul 27, 2019
updated on 7/3/2020 for linux mint Cinnamon

@author: chingl
'''
import numpy as np # for NaN handling
import time
import pandas as pd
# from pandas_datareader import data as pdr
import pymysql.cursors
# import fix_yahoo_finance as yf
import yfinance as yf
from datetime import datetime
import get_id_password_function as auth


# get the id and password from local file / dictionary
user_id,user_pw = auth.get_id_password()   # this somehow puts '\n' at the end of user_d, user_pw
print(user_id)
print(user_pw)

# chomp or remove the '\n' from the return user_id and user_pw 
user_id = user_id.replace('\n', '')    # remove '\n' only
user_pw = user_pw.replace('\n', '')    # remove '\n' only

yf.pdr_override()

conn = pymysql.connect(host='localhost', 
                       user = user_id,
                       
                       password = user_pw
                       
                       )
cursor = conn.cursor()

def printVersion():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        print("Database version: {}".format(version[0]))


def createDB(db):
    dbname = db
    sql = "CREATE DATABASE " + dbname 
    cursor.execute(sql)
    conn.commit()

def createDB_test():
    # dbname = db
    sql = "CREATE DATABASE `testdatabase`"
    cursor.execute(sql)
    conn.commit()

def showDB():
    sql = "show databases;"
    cursor.execute(sql)
    conn.commit()
    print("show databases;")


"""
def download_insert_price_manual():
    ticker = 'axta'
    YAHOO_VENDOR_ID = 3
    df = pdr.get_data_yahoo(tickers=ticker, start=datetime(2019,1,1), end=datetime(2019,8,1))
    print(df.index)
    # convert timestamp;
    # https://stackoverflow.com/questions/43108164/python-to-mysql-timestamp-object-has-no-attribute-translate?rq=1
    # df['Date'] = pd.to_datetime(df['Date'])


    
    # df.to_csv('C:/Users/chingl/Documents/python3-code/axta.csv')
    # print(df)
    # i = 0
    # for row in df.itertuples():
    #    if i < 3:
    #        print(row)
        # values = [YAHOO_VENDOR_ID, ticker_index[ticker]] + list(row)
        # values = [YAHOO_VENDOR_ID, 'axta'] + list(row)
        # print (values)
        # cursor.execute("INSERT INTO daily_price (data_vendor_id, ticker_id, price_date, open_price, high_price, low_price, close_price, adj_close_price, volume) VALUES" \
        # "(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        # tuple(values))

    i = 0
    for index, row in df.iterrows():
        if i < 3:
            print(index, row)
            i+=1

    cursor.execute("INSERT INTO daily_price (data_vendor_id, ticker_id, price_date, open_price, high_price, low_price, close_price, adj_close_price, volume) VALUES" \
        "(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (YAHOO_VENDOR_ID, ticker, row.index, row.open, row.high, row.low, row.adj close,row.volumn)
                   )
"""


"""
# unstable method - don't use it
def download_insert_Price(tickers):
    YAHOO_VENDOR_ID = 3
    for ticker in tickers:
    # Download data
    # https://www.programcreek.com/python/example/92135/pandas_datareader.data.get_data_yahoo
    df = pdr.get_data_yahoo(ticker, start=start_date)
    # Write to daily_price
    for row in df.itertuples():
        values = [YAHOO_VENDOR_ID, ticker_index[ticker]] + list(row)
        cursor.execute("INSERT INTO daily_price (data_vendor_id, 
        ticker_id, price_date, open_price, high_price, low_price, 
        close_price, adj_close_price, volume) VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        tuple(values))
"""

"""
def prepareDF():
    nyse = pd.read_csv('C" + dbname :/Users/chingl/Documents/python3-code/nyse_tickers.csv') # create a pandas df
    print("Number of NYSE tickers:", len(nyse))
    nyse.drop(['LastSale', 'MarketCap', 'IPOyear', 'Summary Quote','industry'], axis=1, inplace=True)
    nyse.columns = ['exchange_id','ticker', 'name', 'sector']
    nyse['exchange_id'] = 1
    #nyse.to_csv('C:/Users/chingl/Documents/python3-code/nyse.csv')
    # nyse = nyse[cols[-1:] + cols[:-1]]   #which is this ?????
    # test print
    #for index, row in nyse.iterrows():
    #    if index < 3:
    #        print(row.exchange_id,row.ticker,row.name,row.sector)

    # replace NaN with an empty string or ''
    #https://stackoverflow.com/questions/26837998/pandas-replace-nan-with-blank-empty-string/28390992
    nyse = nyse.replace(np.nan, '', regex=True)    



    return(nyse)
"""

 
if __name__=='__main__':
    print("hello")
    printVersion()
    # showDB()
    #createDB('`db_au_stk`')
    #createDB('`db_au_etf`')
    #createDB('`db_us_stk`')
    #createDB('`db_us_etf`')
    createDB_test()


    
    

 
