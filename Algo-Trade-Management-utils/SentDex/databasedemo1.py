# database demo using asx100

import MySQLdb

db = MySQLdb.connect("127.0.0.1", "root","root","world")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print data

sql = "SELECT * FROM CITY"
cursor.execute(sql)
results = cursor.fetchall()

for each in results:
    # print each [0], each[2]
    print each[1], each[2], each[3]
    

count = 0
for each in results:
    # print each [0], each[2]
    if each[2]== 'CHN':
        print each[1], each[2], each[3]
        count = count + 1
        
print "China has", count, "citys"        