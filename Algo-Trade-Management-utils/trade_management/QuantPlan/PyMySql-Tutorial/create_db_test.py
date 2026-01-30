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

        sql = "CREATE DATABASE `testdatabase`"
        cur.execute(sql)
        conn.commit()

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



 
if __name__=='__main__':
    print("hello")
    printVersion()
    # showDB()
    #createDB('`db_au_stk`')
    #createDB('`db_au_etf`')
    #createDB('`db_us_stk`')
    #createDB('`db_us_etf`')
    # createDB_test()


    
    

 
