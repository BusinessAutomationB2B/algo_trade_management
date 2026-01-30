# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:10:50 2013

@author: chingl
"""

import time
from datetime import datetime
from time import mktime

def backTest():

#Trade Rules:
#Buy every time you are not invested and stock price drops.
#sell every time the stock price is more than .2% higher than when you bought. (.002)

    
    bigDataFile = open('AMAT.txt','r')
    readFile = bigDataFile.read()
    lineSplit = readFile.split('\n')

    for everyLine in lineSplit:
    
        dividedLine = everyLine.split(',')
        countryName = dividedLine[0].split('.')[0]
        stockName = dividedLine[0].split('.')[1]
        initialDate = dividedLine[2]+dividedLine[3] 
        datetime.strptime(initialDate, '%Y%m%d%H%M%S').timetuple() 
        unixStamp = mktime(datetime.strptime(initialDate, '%Y%m%d%H%M%S').timetuple())
        dateStamp = time.strftime('%m/%d/%Y %H:%M:%S',time.localtime(unixStamp))
        
        #print dateStamp
        stockPrice = float(dividedLine[4])
        reformatted = countryName,unixStamp,dateStamp,stockName,stockPrice
        print reformatted

backTest()
