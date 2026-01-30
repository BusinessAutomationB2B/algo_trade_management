# https://www.w3schools.com/python/python_mysql_create_table.asp

import mysql.connector

mydb = mysql.connector.connect(   #package.module.method
    host="localhost",
    user="tester",
    password = "root")

# print(mydb)

def makeDb(mcursor):
    mcursor.execute("CREATE DATABASE mydatabase")
    print("CREATE DATABASE mydatabase")
    
def makeTb(mcursor):   #make two tables
    mcursor.execute("USE mydatabase")
    mcursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")
    mcursor.execute("CREATE TABLE products (id INT PRIMARY KEY, name VARCHAR(255))")

def showDb(mcursor):
    mcursor.execute("Show Databases")
    for x in mycursor:
        print(x)

def showTb(mcursor):
    mcursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

 

# operation
mycursor = mydb.cursor()
#makeDb(mycursor)
makeTb(mycursor)

showDb(mycursor)
showTb(mycursor)


    

 