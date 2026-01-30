#!/usr/bin/python

import pymysql

con = pymysql.connect(host='localhost', user='root',
    password='Root@123', database ='testdb')

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM cities')

        rows = cur.fetchall()

        desc = cur.description

        print(f'{desc[0][0]:<8} {desc[1][0]:<15} {desc[2][0]:>10}')

        for row in rows:
            print(f'{row[0]:<8} {row[1]:<15} {row[2]:>10}')

finally:

    con.close()