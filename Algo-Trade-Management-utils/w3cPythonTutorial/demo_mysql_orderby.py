import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tester",
  passwd="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY address"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)