#!/usr/bin/python

import pymysql

con = pymysql.connect(host='localhost', user='root',
    password='Root@123',database='testdb')

# user input
myid = 4

try: 

    with con.cursor() as cur:

            
        cur.execute('SELECT * FROM cities WHERE id=%s', myid) 
        
        cid, name, population  = cur.fetchone()
        print(cid, name, population)

finally:

    con.close()