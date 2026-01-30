'''
Created on Jul 27, 2019

@author: chingl
'''
import numpy as np # for NaN handling
import time
import pandas as pd
from pandas_datareader import data as pdr
import pymysql.cursors
# import fix_yahoo_finance as yf
import yfinance as yf
from datetime import datetime
import get_id_password_function as auth


# get the id and password from local file / dictionary
user_id,user_pw = auth.get_id_password()   # this somehow puts '\n' at the end of user_d, user_pw
# print(user_id)
# print(user_pw)

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


# create a summary list
def create_eft_list_tables(db, tb):
    database = db   #  '`db_au_stk`'
    table = tb      # '`list`'
    sql = "use" +  db 
    cursor.execute(sql)
    # sql = "show databases"
    # cursor.execute(sql)

    sql = 'CREATE TABLE' + table + '  ( \
                 `` DATE NOT NULL,\
                `open` FLOAT NOT NULL,\
                `high` FLOAT NULL DEFAULT NULL,\
                `low` FLOAT NULL DEFAULT NULL,\
                `close` FLOAT NULL DEFAULT NULL,\
                `volume` BIGINT(20) NULL DEFAULT NULL,\
                `adjusted` FLOAT NULL DEFAULT NULL,\
                `created_date` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),\
                `last_updated` DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),\
                PRIMARY KEY (`index`) )'

    cursor.execute(sql)
    conn.commit()


# create a single stock table
def create_stk_tables(db, tb):
    database = db   #  '`db_au_stk`'
    table = tb      # '`vas`'
    sql = "use" +  db 
    cursor.execute(sql)
    # sql = "show databases"
    # cursor.execute(sql)

    sql = 'CREATE TABLE' + table + '  ( \
                 `index` DATE NOT NULL,\
                `open` FLOAT NOT NULL,\
                `high` FLOAT NULL DEFAULT NULL,\
                `low` FLOAT NULL DEFAULT NULL,\
                `close` FLOAT NULL DEFAULT NULL,\
                `volume` BIGINT(20) NULL DEFAULT NULL,\
                `adjusted` FLOAT NULL DEFAULT NULL,\
                `created_date` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),\
                `last_updated` DATETIME NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),\
                PRIMARY KEY (`index`) )'

    cursor.execute(sql)
    conn.commit()

# this is the ubuntu path
# /home/tester/Documents/myGitRepo/AlgoTrading/trade_management/ticker

def read_au_etf_tickers():
    # tickers = pd.read_csv('/home/tester/GitHub/AlgoTrading/trade_management/ticker/au_ETF.csv', encoding = "ISO-8859-1", engine='python') # create a pandas df
    tickers = pd.read_csv('/home/tester/vscProjects/Algo-Trade-Management/trade_management/ticker/au_ETF.csv', encoding = "ISO-8859-1", engine='python') # create a pandas df
    
    print("Number of tickers:", len(tickers))
    return (tickers)

def read_au_stk_tickers():
    # tickers = pd.read_csv('/home/tester/GitHub/AlgoTrading/trade_management/ticker/au_asx300.csv', encoding = "ISO-8859-1", engine='python') # create a pandas df
    tickers = pd.read_csv('/home/tester/vscProjects/Algo-Trade-Management/trade_management/ticker/au_asx300.csv', encoding = "ISO-8859-1", engine='python') # create a pandas df
    print("Number of tickers:", len(tickers))
    return (tickers)

def create_au_etf_tables_auto(tks):
    # ASXCode	Issuer	Name	Benchmark	Domicile	MER
    tickers = tks
    # print(tickers['ASXCode'].head(2))
    tickerList = tickers['ASXCode']+ '.AX'
    print(tickerList)
    for ticker in tickerList:
        # print(type(ticker))
        # print('`'+ ticker + '`')
        create_stk_tables('`db_au_etf`', '`'+ ticker + '`')
        
def create_au_stk_tables_auto(tks):
    # Code	Company	Sector	Market Cap	Weight(%)
    tickers = tks
    print(tickers)
    print(tickers['Code'].head(2))
    tickerList = tickers['Code']+ '.AX'
    print(tickerList)
    for ticker in tickerList:
        # print(type(ticker))
        # print('`'+ ticker + '`')
        create_stk_tables('`db_au_stk`', '`'+ ticker + '`') 
 
        
 
if __name__=='__main__':
    
    print_version()
    db='`db_au_etf`'
    tb='`vas`'
    create_stk_tables(db,tb)

    # Create ETF tables
    # tks = read_au_etf_tickers()
    # create_au_etf_tables_auto(tks) # success

    # Create stk tables
    # tks = read_au_stk_tickers()
    # create_au_stk_tables_auto(tks) # success
 
