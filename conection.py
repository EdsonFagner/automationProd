import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='bd_prodproject'
)
mycursor = mydb.cursor()