#!/usr/bin/python

import pymysql

con = pymysql.connect(host='localhost', user='root',
    password='Root@123',database='testdb')

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM cities')

        rows = cur.fetchall()

        for row in rows:
            print(f'{row[0]} {row[1]} {row[2]}')

finally:

    con.close()
