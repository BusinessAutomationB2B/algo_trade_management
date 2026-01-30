import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tester",
  passwd="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

# """james added this line on 2/2/2019:     users.fav as fav, \"""
 
sql = "SELECT \
  users.name AS user, \
  users.fav AS favs,\
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
      print(x)