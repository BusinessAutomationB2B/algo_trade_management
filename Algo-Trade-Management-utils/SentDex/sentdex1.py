# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\chingl\.spyder2\.temp.py
"""
import time
from datetime import datetime
from time import mktime
#600,000 lines of data!
bigDataFile = open('AMAT.txt','r')

#opens the file with the intention to read it, and reads it into memory!
#will consume the file size in RAM, keep this in mind!
readFile = bigDataFile.read()
#step 1:
#The first thing to do, is split the file. If we read it now, the file
#will read line 1\nline2\nline3 …and so on.
#so first, we want to split it up the way we humans read!

#This will now split lines into a similar format that we see in the file
#and also gives us a way to reference each line as its own entity
lineSplit = readFile.split('\n')
#now we need to begin formatting. Since we’ve split
#line by line, we now need to begin by referencing each line
#to do this, we use a ‘for’ loop.

for everyLine in lineSplit:

#this creates an array of data
#This makes stock name [0], date [2],[3], and price is [4]
    dividedLine = everyLine.split(',')

#with the array made, let’s assign the stuff we want to variables!

#not only can we do this to first make a pretty line to organize
#the data, we can use these variables as building blocks
#for actually analyzing the data!

#this gets us first the US2.AMAT, then we split away the US2 part
#for just the name!
stockName = dividedLine[0].split('.')[1]

 #this pulls the date information, albeit ugly format right now
 #we’ll fix that!
initialDate = dividedLine[2]+dividedLine[3] 
unixStamp = mktime(datetime.strptime(initialDate,'%Y%m%d%H%M%S').timetuple())
dateStamp = time.strftime('%m/%d/%Y %H:%M:%S',time.localtime(unixStamp))

#assigns the price data to a variable.
stockPrice = dividedLine[4]

#original printout:

#reformatted = stockName,initialDate,stockPrice

reformatted = unixStamp,dateStamp,stockName,stockPrice
# saveFormat = str(reformatted).replace('\",").replace('(',").replace(')',")
#print saveFormat
#print reformatted

appendFile = open('example2noprint.txt','a')
appendFile.write(saveFormat)
appendFile.write('\n')
#appendFile.write(reformatted)
appendFile.close()