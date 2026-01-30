#!/usr/bin/python

import pymysql
import pymysql.cursors

con = pymysql.connect(host='localhost',
        user='root',
        password='Root@123',
        db='testdb',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM cities')

        rows = cur.fetchall()

        for row in rows:
            print(row['id'], row['name'], row['population'])

finally:

    con.close()