#CRUD Operations - Update
#Author: Aoife Flavin

import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="wsaa2"
)

cursor = db.cursor()

sql="update student set name= %s, age=%s where id = %s"
values = ("Joe",33, 1)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()