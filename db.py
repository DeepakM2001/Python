import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="DBAdmin",
  password="1234"
)

print(mydb)
