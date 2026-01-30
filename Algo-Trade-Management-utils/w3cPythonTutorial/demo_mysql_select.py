import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tester",
  passwd="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  #print(x[0],x[1],x[2])
  print(type(x))