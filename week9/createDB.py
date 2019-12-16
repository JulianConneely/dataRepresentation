import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Tropical1"
  
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE datarepresentation")