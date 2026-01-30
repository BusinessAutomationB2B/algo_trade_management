'''
Created on Jul 27, 2019
Updated on Dec 9, 2019

This version, ETF insert works, for some reason, stock insert does not work

@author: chingl
'''
import numpy as np # for NaN handling
import time
import pandas as pd
from pandas_datareader import data as pdr
import pymysql.cursors
import yfinance as yf
# import fix_yahoo_finance as yf     # depredicated
from datetime import datetime
import logging
import get_id_password_function as auth
import os as os



# ----------------managing data base connection
# https://stackoverflow.com/questions/37730243/importing-data-from-a-mysql-database-into-a-pandas-data-frame-including-column-n/37730334
# for reading database
# this is required to read from mysql to pd
from sqlalchemy import create_engine
import pymysql


# ----------------managing data base connection-----------------------
# this is required to insert from CSV into mysql
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

def print_version():
    with conn:
        
        cur = conn.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        print("Database version: {}".format(version[0]))
        


# This is the function to read the tickers from the csv file
def read_au_etf_tickers():
    # file = '/home/tester/Documents/myGitRepo/AlgoTrading/trade_management/ticker/au_ETF.csv'# old path
    file = '/home/tester/GitHub/AlgoTrading/trade_management/ticker/au_ETF.csv'
    tickers = pd.read_csv(file, encoding = "ISO-8859-1", engine='python') # create a pandas df, 
    print("Number of tickers:", len(tickers))
    return (tickers)

def read_au_stk_tickers():
    # file = '/home/tester/Documents/myGitRepo/AlgoTrading/trade_management/ticker/au_asx300.csv'  # old path
    file = '/home/tester/GitHub/AlgoTrading/trade_management/ticker/au_asx300.csv'
    tickers = pd.read_csv(file, encoding = "ISO-8859-1", engine='python') # create a pandas df
    print("Number of tickers:", len(tickers))
    return (tickers)



##################################################### this works on 2019 12 09 ######### dealth with a single stock
# download a single stock
def download_au_stk():
    # this worked
    df = pdr.get_data_yahoo(tickers='ANZ.AX', start=datetime(2019,1,1), end=datetime(2019,12,1))
    df.to_csv('/home/tester/Documents/myGitRepo/AlgoTrading/trade_management/data/anz.csv')
    
# read a single stock
def read_au_stk():
    # file = '/home/tester/Documents/myGitRepo/AlgoTrading/trade_management/data/anz.csv'   # old path
    file = '/home/tester/GitHub/AlgoTrading/trade_management/data/anz.csv'
    df = pd.read_csv(file, index_col=None, encoding = "ISO-8859-1", engine='python') # create a pandas df
    print(df.head(3))
    return(df)

# insert a single stock
def insert_au_stk(d):
    df = d
    # df.to_sql(con=conn, name='anz.ax', if_exists='replace')
    cursor.execute("use `db_au_stk`")
    for index, row in df.iterrows():
        # the following code worked! 20190729 at 12:19, `anz.ax` is the table name in mysql
        cursor.execute("INSERT INTO `ANZ.AX` (`index`, `open`, `high`, `low`, `close`, `adjusted`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (row['Date'], row['Open'],row['High'],row['Low'],row['Close'],row['Adj Close'],row['Volume']))
    conn.commit()
#####################################################

    
# read and insert stock
# under testing - worked
def download_au_stk_auto(tks):
    # https://www.guru99.com/reading-and-writing-files-in-python.html
    # donwload error log:
    f = open("donwload_error_stk.txt","w+")

    # this worked
    tickers = tks
    tickerList = tickers['Code']+ '.AX'  # 'Code' for asx, 'ASXCode' for etf
    for ticker in tickerList:
        try:
            df = pdr.get_data_yahoo(tickers=ticker, start=datetime(2001,1,1), end=datetime(2020,3,6))
        except:
            print('download error: ', ticker)
            f.write('download error: %s%s\n'% (ticker))
        # file = '/home/tester/Documents/myGitRepo/AlgoTrading/trade_management/data/'
        file = '/home/tester/GitHub/AlgoTrading/trade_management/data/'
        df.to_csv( file + ticker + '.csv')
    f.close()

# under testing - worked
def read_insert_au_stk_auto(tks):
    # https://www.guru99.com/reading-and-writing-files-in-python.html
    # donwload error log:
    f = open("db_insert_error_stk.txt","w+")
    
    # now change to stock database
    sql = 'use `db_au_stk`'
    cursor.execute(sql)

    tickers = tks
    tickerList = tickers['Code']+ '.AX'   # 'Code' for asx, 'ASXCode' for etf
    for ticker in tickerList:   # e.g. ANZ.AX
        try:
            print("Processing ticker:", ticker)
            # file = '/home/tester/Documents/myGitRepo/AlgoTrading/trade_management/data/'  # old path
            file = '/home/tester/GitHub/AlgoTrading/trade_management/data/'
            df = pd.read_csv( file + ticker + '.csv', index_col=None, encoding = "ISO-8859-1", engine='python')  # create a pandas df
        except:
            print('csv file read error: ', ticker)
            fwrite('csv file read error:%s\n'%(ticker))
        # fill nan with 0
        # https://stackoverflow.com/questions/47286547/is-there-a-way-in-pd-read-csv-to-replace-nan-value-with-other-character
        # df.fillna(0,1,inplace=True)
        df.fillna(0)
        for index, row in df.iterrows():
            try:
                # print(index,row)  # this make it two slow
                # the following code worked! 20190729 at 12:58.  '`'+ ticker + '`'   -> this is very important to delimit the reference for mysql
                cursor.execute("INSERT INTO " + '`'+ ticker + '`'+ "(`index`, `open`, `high`, `low`, `close`, `adjusted`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (row['Date'],row['Open'],row['High'],row['Low'],row['Close'],row['Adj Close'],row['Volume']))
            except:
                # print('db insert error: ',ticker, row['Date'])     # to improve the speed for bulk download. good for checking overlapping dates
                f.write("db insert error:%s%s\n"% (ticker,row['Date']))    
        conn.commit()
        print("inserted " + ticker + "\n")
    f.close()





# ------------------------------------------------ETF--------------------------------------------------------
# read and insert ETF
# under testing - worked
def download_au_etf_auto(tks):
    # https://www.guru99.com/reading-and-writing-files-in-python.html
    # donwload error log:
    f = open("donwload_error_etf.txt","w+")
    # this worked   
    tickers = tks
    tickerList = tickers['ASXCode']+ '.AX'  # 'Code' for asx, 'ASXCode' for etf
    # https://realpython.com/python-exceptions/
    # error handling when download is in error
    for ticker in tickerList:
        try:
            df = pdr.get_data_yahoo(tickers=ticker, start=datetime(2020,3,1), end=datetime(2020,3,10))
        except:
            print('download error: ',ticker)
            f.write("download error:%s\n"% (ticker))
        df.to_csv('/home/tester/GitHub/AlgoTrading/trade_management/data1/' + ticker + '.csv')
    f.close()


# under testing - worked
def read_insert_au_etf_auto(tks):
    # https://www.guru99.com/reading-and-writing-files-in-python.html
    # donwload error log:
    f = open("db_insert_error_etf.txt","w+")
    
    # now change to etf database
    sql = 'use `db_au_etf`'
    cursor.execute(sql)
    
    tickers = tks
    tickerList = tickers['ASXCode']+ '.AX'   # 'Code' for asx, 'ASXCode' for etf
    for ticker in tickerList:
        try:
            df = pd.read_csv('/home/tester/GitHub/AlgoTrading/trade_management/data1/' + ticker + '.csv', index_col=None, encoding = "ISO-8859-1", engine='python') # create a pandas df
        except:
            print('csv file read error: ',ticker)
            f.write("csv file read error:%s\n"% (ticker))
        for index, row in df.iterrows():
            # need to add the logic in R code: if index is the same, delete the old data and insert again, else insert
            # the following code worked! 20190729 at 12:58.  '`'+ ticker + '`'   -> this is very important to delimit the reference for mysql
            try:
                cursor.execute("INSERT INTO " + '`'+ ticker + '`'+ "(`index`, `open`, `high`, `low`, `close`, `adjusted`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (row['Date'], row['Open'],row['High'],row['Low'],row['Close'],row['Adj Close'],row['Volume']))
            except:
                print('db insert error: ',ticker, row['Date'])
                f.write("db insert error:%s%s\n"% (ticker,row['Date']))    
        conn.commit()
        print("inserted " + ticker)
    f.close()



# need to write loop to loop each ticker in etf and print result into a file

def read_db_au_etf_auto(ticker,pw):
    """  D.R.Y. style
    Business Logic:
        read ticker data from mysql table into a pandas df
    """

    # usage sample:
    #   db_connection_str = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'
    #   db_connection = create_engine(db_connection_str)
    #   df = pd.read_sql('SELECT * FROM table_name', con=db_connection)

    db_connection_str = 'mysql+pymysql://root:'+ pw + '@localhost/db_au_etf'
    print(db_connection_str)
    db_connection = create_engine(db_connection_str)
    df = pd.read_sql('SELECT * FROM'+ '`'+ ticker + '`', con=db_connection)
    return df

# to see if it is above 200 day moving average
def tech_analysis(df):   # use either df['adjusted'] or df['close']
    print(df.head())
    #https://stackoverflow.com/questions/15752422/python-pandas-date-column-to-column-index
    df.set_index('index')
    # print(df.head())

    # -------------get the signal column by comparing close with 200 day moving average
    # https://www.datacamp.com/community/tutorials/moving-averages-in-pandas  // add moving average
    # df['pandas_SMA_3'] = df.iloc[:,4].rolling(window=3).mean()
    df['pandas_SMA_200'] = df['close'].rolling(window=200).mean()  # this is simpler but same as above
    # print(df.tail())
    # select single column as series
    #https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
    df['signal'] = df['close']-df['pandas_SMA_200']
    print(df.tail(1))
    # df.to_csv('/home/tester/GitHub/AlgoTrading/trade_management/sma200_analysis.csv')

    # ------------get multi period (52 weeks / yearly) high and low
    # https://stackoverflow.com/questions/31978132/how-to-calculate-daily-52-weeks-high-low-in-pandas
    df['365-Day-High'] = df['high'].rolling(window=200).max()
    df['365-Day-Low'] = df['low'].rolling(window=200).min()

    #df['365-Day-High'] = pd.rolling_max(df.High, window=250, min_periods=1)
    #df['365-Day-Low'] = pd.rolling_min(df.Low, window=250, min_periods=1)


        #-----------get daily and monthly return
    # https://www.codingfinance.com/post/2018-04-03-calc-returns-py/

    daily_returns['daily-return'] = df['close'].pct_change()
    monthly_returns['monthly-return'] = df['close'].pct_change().resample('M').ffill().pct_change()


    # ------------get the value of the last row in the columns
    # https://stackoverflow.com/questions/15862034/access-index-of-last-element-in-data-frame
    #     print(df['signal'].iloc[-1])
    #     print(df['signal'].iloc[-1] > 0)
    date = df['index'].iloc[-1]
    signal_value = df['signal'].iloc[-1]
    price_close = df['close'].iloc[-1]
    year_high = df['365-Day-High'].iloc[-1]
    year_low = df['365-Day-Low'].iloc[-1]
    daily_ret = daily_returns['daily-return'].iloc[-1]
    monthly_ret = monthly_returns['monthly-return'].iloc[-1]

    

    df.to_csv('/home/tester/GitHub/AlgoTrading/trade_management/sma200_analysis.csv')

    # test
    # print(signal_value, price_close, year_high, year_low, date)

    # return  
    return(signal_value, price_close, year_high, year_low, daily_ret,monthly_ret, date)
    

# worked - looping
def auto_tech_analysis_etf(pw):   # pw for reading db into pdf
    f = open("analysis_all_tickers1.csv","w+")
    f1 = open("analysis_all_tickers_error.txt","w+")
    # Set up f column headings as first line, below does not work, writes the header only
    f.write('Daily Scanning Rules,' + 'Close - MA(200),' + 'Close,' + '52 Wk High,' + '52 Wk Low,' + 'Daily Return, ' + 'Monthly_Return, ' 'Date' + '\n')

    tks = read_au_etf_tickers()
    tickers = tks
    tickerList = tickers['ASXCode']+ '.AX'  # 'Code' for asx, 'ASXCode' for etf
    for ticker in tickerList:
        print(ticker)  # for debug
        df=read_db_au_etf_auto(ticker,pw)
        # to handle empty df situation, 7/3/2020
        try:
            signal,close,high,low,daily,monthly,date = tech_analysis(df)   # high = 52 week high; low = 52 week low, see "def tech_analysis(df);" for more details
        except:
            print('auto analysis error: ',ticker)
            f1.write('auto analysis error: %s '%(ticker))

        #try:
        #f.write('the ticker ' + ticker + ' is above 200 SMA by value, %f\n'% (signal))   # to construct a two column csv file
        f.write('the ticker ' + ticker + ' is above 200 SMA by value, %f,%f,%f,%f,%f,%f,%s\n'% (signal,close,high,low,daily,monthly,date))   # to construct a multi column csv file   
        #except:
        #    print('auto analysis error when writing o/p file: ',ticker)
        #    f1.write('auto analysis error with writing o/p: %s '%(ticker))
    f.close()
    f1.close()
        
"""
empty df can have the following error message and halt the program. with try/excpet block, the program can go on

Traceback (most recent call last):
  File "/home/tester/GitHub/AlgoTrading/trade_management/insert_db_prices.py", line 323, in <module>
    auto_tech_analysis_etf()
  File "/home/tester/GitHub/AlgoTrading/trade_management/insert_db_prices.py", line 287, in auto_tech_analysis_etf
    sig=tech_analysis(df)
  File "/home/tester/GitHub/AlgoTrading/trade_management/insert_db_prices.py", line 273, in tech_analysis
    print(df['signal'].iloc[-1] > 0)
  File "/home/tester/.local/lib/python3.6/site-packages/pandas/core/indexing.py", line 1767, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "/home/tester/.local/lib/python3.6/site-packages/pandas/core/indexing.py", line 2137, in _getitem_axis
    self._validate_integer(key, axis)
  File "/home/tester/.local/lib/python3.6/site-packages/pandas/core/indexing.py", line 2062, in _validate_integer
    raise IndexError("single positional indexer is out-of-bounds")
IndexError: single positional indexer is out-of-bounds

"""




# 2020 03 11 moving daily data into individual filer for record keeping

def moving_data():
    # import os as os
    os.system('ls')
    os.system('date')
    os.system('echo mv daily download data:...')
    os.system('mv /home/tester/GitHub/AlgoTrading/trade_management/data1/*.csv  /home/tester/GitHub/AlgoTrading/trade_management/data1/baseline/')
    print('downloaded *.csv files moved! :)')






       
if __name__=='__main__':
    
    print_version()
    moving_data()

# ---------------The following subset operation (download, read and insert a single stock, ANZ) worked  - manual work                 
    # download_au_stk()
    # df=read_au_stk()
    # print(df)
    # insert_au_stk(df)


#----------------the following is for auto-operations for stocks-----------
    # tks = read_au_stk_tickers()
    # print(tks.head())
    # download_au_stk_auto(tks)
    # read_insert_au_stk_auto(tks)

#----------------the following is for auto-operations for ETF-----------
# the following code is verified on 17/10/2019
    tks = read_au_etf_tickers()  ## run this daily
    # print(tks)
    download_au_etf_auto(tks)    ## run this daily, first reset period
    read_insert_au_etf_auto(tks) ## run this daily


# --------------auto analysis TA ---------------------
    # single stock analysis - read db into df frame
    # df=read_db_au_etf_auto('vas.ax')
    # tech_analysis(df)

    # multi security analysis - worked on 2020 03 08
    auto_tech_analysis_etf(user_pw)
    


    
