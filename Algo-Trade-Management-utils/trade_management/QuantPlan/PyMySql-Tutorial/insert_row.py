#!/usr/bin/python

import pymysql

con = pymysql.connect(host='localhost', user='root',
    password='Root@123',database='testdb')

city = (9, 'Kiev', 2887000)

try: 

    with con.cursor() as cur:

        cur.execute('INSERT INTO cities VALUES(%s, %s, %s)', 
            (city[0], city[1], city[2])) 
        con.commit()

        print('new city inserted')

finally:

    con.close()