#CRUD Operations - Create
#Author: Aoife Flavin

import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="wsaa2"
)
cursor = db.cursor()

sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)

cursor.execute(sql, values)

db.commit()

print("1 record inserted, ID:", cursor.lastrowid)

cursor.close()
db.close()
