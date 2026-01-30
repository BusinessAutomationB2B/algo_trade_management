# http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution
# time execution



# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:10:50 2013

@author: chingl
"""

import time
from datetime import datetime
from time import mktime

start_time = time.time()

def backTest():


#Trade Rules:
#Buy every time you are not invested and stock price drops.
#sell every time the stock price is more than .2% higher than when you bought. (.002)

    investmentAmount = 50000
    tradeComm = 7

    stance = 'none'
    buyPrice = 0
    sellPrice = 0
    previousPrice = 0

    totalProfit = 0

    tradeCount = 0
    startingPrice = 0

    startingTime = 0
    endingTime = 0

    totalInvestedTime = 0

    overallStartingTime = 0
    overallEndingTime = 0

    bigDataFile = open('AMAT.txt','r')
    readFile = bigDataFile.read()
    lineSplit = readFile.split('\n')

    for everyLine in lineSplit:
    
        dividedLine = everyLine.split(',')
        stockName = dividedLine[0].split('.')[1]
        initialDate = dividedLine[2]+dividedLine[3]
        # print initialDate 
        datetime.strptime(initialDate, '%Y%m%d%H%M%S').timetuple() 
        unixStamp = mktime(datetime.strptime(initialDate, '%Y%m%d%H%M%S').timetuple())
        # print unixStamp
        dateStamp = time.strftime('%m/%d/%Y %H:%M:%S',time.localtime(unixStamp))
        
        #print dateStamp
        stockPrice = float(dividedLine[4])
        reformatted = unixStamp,dateStamp,stockName,stockPrice
        # print reformatted
    
        if stance == 'none':
            #print stockPrice, previousPrice
            if stockPrice < previousPrice:
    
                print 'buy triggered!'
                buyPrice = stockPrice
                print 'bought stock for',buyPrice
                stance = 'holding'
        
                startingTime = unixStamp
        
                if tradeCount == 0:
    
                    startingPrice = buyPrice
                    overallStartingTime = unixStamp
    
                tradeCount += 1
    
        elif stance == 'holding':
            if stockPrice > buyPrice * .002 + buyPrice:
                print 'sell triggered!'
                sellPrice = stockPrice
                print 'finished trade, sold for:',sellPrice
                stance = 'none'
                tradeProfit = sellPrice - buyPrice
                totalProfit += tradeProfit
                print totalProfit
                endingTime = unixStamp
                timeInvested = endingTime - startingTime
                totalInvestedTime += timeInvested
        
                overallEndingTime = endingTime
        
                tradeCount += 1
    
        previousPrice = stockPrice   # this is a tricky mistake, it should be indented under the main loop
 
      
    print 'Trading Complete.'
    print 'Profit Per Stock:', totalProfit
    print 'Trade Count:', tradeCount
    grossPercProf = totalProfit/startingPrice * 100
    print 'Gross % Profit:', grossPercProf
    
    print 'How much gross profit did we make off of our',investmentAmount,'investment:'
    grossProf = investmentAmount/startingPrice*totalProfit
    print 'we made:', grossProf
    tradeCommsTotal = tradeComm * tradeCount
    print 'amount paid in commissions:',tradeCommsTotal
    netProf = grossProf-tradeCommsTotal
    print 'profit after commissions:',netProf
    netPercentProf = netProf/investmentAmount * 100
    print 'net percent profit after comms:',netPercentProf
    
    averageInvestedTimeHours = totalInvestedTime/tradeCount/3600
    
    print 'average holding length in hours:', averageInvestedTimeHours
    
    overallTime = overallEndingTime - overallStartingTime
    percentageInvested = totalInvestedTime/overallTime * 100
    
    print 'cumulative amount of time holding in days: ',overallTime/86400
    print 'Percentage of the time invested:',percentageInvested
 
backTest()

print 'execution time is: ', time.time() - start_time, " seconds"
print 'execution time is %s seconds ' %(time.time() - start_time)  
