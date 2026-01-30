'''
Created on Jul 27, 2019

@author: chingl
'''
import numpy as np # for NaN handling
import time
import pandas as pd
from pandas_datareader import data as pdr
import pymysql.cursors
import fix_yahoo_finance as yf
from datetime import datetime

userParam= ' ****'  # get it from a local file / dictionary
pwParam ='****' # get it from a local file / dictionary

yf.pdr_override()
conn = pymysql.connect(host='localhost', 
                	user='userParam',
                       password = 'pwParam'
                       db = 'db_au_stk')
cursor = conn.cursor()


def print_version():
    with conn:
        
        cur = conn.cursor()
        cur.execute("SELECT VERSION()")

        version = cur.fetchone()
        
        print("Database version: {}".format(version[0]))


# to be tested???
# https://stackoverflow.com/questions/47328402/how-to-store-mysql-query-result-into-pandas-dataframe-with-pymysql
# amazing it is indexed by date column



def read_db_to_df():
    # sql = "select * from `nab.ax`"
    # df = cursor.execute(sql)

    sql = "SELECT * FROM `nab.ax`"
    df = pd.read_sql(sql, conn)
    print(df.head(3))
    # set index to ['index'] field - date data
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
    df=df.set_index('index')   # this assignment is important
    print(df)
    print(df.head(3))
    # https://stackoverflow.com/questions/20000726/calculate-daily-returns-with-pandas-dataframe
    
    # df['Return'] = df['Close']/df['Close'].shift(1) - 1
    # print(df)

    # daily_return = df['Close'].pct_change(1) # 1 for ONE DAY lookback
    # print(daily_return)

 









def read_au_etf_tickers():
    tickers = pd.read_csv('C:/Users/chingl/Documents/python3-code/data/au_ETF.csv', encoding = "ISO-8859-1", engine='python') # create a pandas df
    print("Number of tickers:", len(tickers))
    return (tickers)

def read_au_stk_tickers():
    tickers = pd.read_csv('C:/Users/chingl/Documents/python3-code/data/au_asx300.csv', encoding = "ISO-8859-1", engine='python') # create a pandas df
    print("Number of tickers:", len(tickers))
    return (tickers)


def download_au_stk():
    # this worked
    df = pdr.get_data_yahoo(tickers='anz.ax', start=datetime(2019,1,1), end=datetime(2019,8,1))
    df.to_csv('C:/Users/chingl/Documents/python3-code/data/anz.csv')

def read_au_stk():
    df = pd.read_csv('C:/Users/chingl/Documents/python3-code/data/anz.csv', index_col=None, encoding = "ISO-8859-1", engine='python') # create a pandas df
    print(df.head(3))
    return(df)


def insert_au_stk(d):
    df = d
    # df.to_sql(con=conn, name='anz.ax', if_exists='replace')
    cursor.execute("use `db_au_stk`")
    for index, row in df.iterrows():
        # the following code worked! 20190729 at 12:19, `anz.ax` is the table name in mysql
        cursor.execute("INSERT INTO `anz.ax` (`index`, `open`, `high`, `low`, `close`, `adjusted`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (row['Date'], row['Open'],row['High'],row['Low'],row['Close'],row['Adj Close'],row['Volume']))
    conn.commit()


# under testing - worked
def download_au_stk_auto(tks):
    # this worked
    tickers = tks
    tickerList = tickers['Code']+ '.AX'  # 'Code' for asx, 'ASXCode' for etf
    for ticker in tickerList:
        df = pdr.get_data_yahoo(tickers=ticker, start=datetime(2000,1,1), end=datetime(2019,8,1))
        df.to_csv('C:/Users/chingl/Documents/python3-code/data/' + ticker + '.csv')


# under testing - worked
def read_insert_au_stk_auto(tks):
    # now change to etf database
    sql = 'use `db_au_stk`'
    cursor.execute(sql)

    tickers = tks
    tickerList = tickers['Code']+ '.AX'   # 'Code' for asx, 'ASXCode' for etf
    for ticker in tickerList:
        df = pd.read_csv('C:/Users/chingl/Documents/python3-code/data/' + ticker + '.csv', index_col=None, encoding = "ISO-8859-1", engine='python') # create a pandas df
        for index, row in df.iterrows():
            # the following code worked! 20190729 at 12:58.  '`'+ ticker + '`'   -> this is very important to delimit the reference for mysql
            cursor.execute("INSERT INTO " + '`'+ ticker + '`'+ "(`index`, `open`, `high`, `low`, `close`, `adjusted`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row['Date'], row['Open'],row['High'],row['Low'],row['Close'],row['Adj Close'],row['Volume']))
        conn.commit()



# under testing - worked
def download_au_etf_auto(tks):
    # this worked
    tickers = tks
    tickerList = tickers['ASXCode']+ '.AX'  # 'Code' for asx, 'ASXCode' for etf
    for ticker in tickerList:
        df = pdr.get_data_yahoo(tickers=ticker, start=datetime(2000,1,1), end=datetime(2019,8,1))
        df.to_csv('C:/Users/chingl/Documents/python3-code/data/' + ticker + '.csv')


# under testing - worked
def read_insert_au_etf_auto(tks):
    # now change to etf database
    sql = 'use `db_au_etf`'
    cursor.execute(sql)
    
    tickers = tks
    tickerList = tickers['ASXCode']+ '.AX'   # 'Code' for asx, 'ASXCode' for etf
    for ticker in tickerList:
        df = pd.read_csv('C:/Users/chingl/Documents/python3-code/data/' + ticker + '.csv', index_col=None, encoding = "ISO-8859-1", engine='python') # create a pandas df
        for index, row in df.iterrows():
            # the following code worked! 20190729 at 12:58.  '`'+ ticker + '`'   -> this is very important to delimit the reference for mysql
            cursor.execute("INSERT INTO " + '`'+ ticker + '`'+ "(`index`, `open`, `high`, `low`, `close`, `adjusted`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row['Date'], row['Open'],row['High'],row['Low'],row['Close'],row['Adj Close'],row['Volume']))  
        conn.commit()
        print("inserted " + ticker)


       
if __name__=='__main__':
    
    print_version()


    read_db_to_df()
