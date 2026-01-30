import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tester",
  passwd="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

print("cursor count before insert", mycursor.rowcount)

sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
  ('John', '154'),
  ('Peter', '154'),
  ('Amy', '155'),
  ('Hannah', ''),
  ('Michael', '')
]

sql1 = "INSERT INTO products (id, name) VALUES (%s, %s)"
val1 = [
  ('154','Chocolate Heaven'),
  ('155', 'Tasty Lemons'),
  ('156', 'Vanilla Dreams')
]
 
mycursor.executemany(sql, val)
mycursor.executemany(sql1, val1)

mydb.commit()

print("cursor count after insert", mycursor.rowcount)
print(mycursor.rowcount, "record(s) inserted")
