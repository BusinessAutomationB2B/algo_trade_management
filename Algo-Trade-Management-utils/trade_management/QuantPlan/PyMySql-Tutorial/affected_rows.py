#!/usr/bin/python

import pymysql

import get_id_password_function as auth


# get the id and password from local file / dictionary
user_id,user_pw = auth.get_id_password()   # this somehow puts '\n' at the end of user_d, user_pw
print(user_id)
print(user_pw)


con = pymysql.connect(host='localhost', user = 'root',
    password='Root@123', database ='testdb')


try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM cities WHERE id IN (1, 2, 3)')

        print(f'The query affected {cur.rowcount} rows')

finally:

    con.close()