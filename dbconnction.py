import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="nothing"
)

dbse = mydb.cursor()

dbse.execute("CREATE TABLE waste (Employee_name VARCHAR(255), Employee_dep VARCHAR(255))")
mydb.commit
