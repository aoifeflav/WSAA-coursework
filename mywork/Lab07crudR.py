#CRUD Operations - Read
#Author: Aoife Flavin

import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="wsaa2"
)

cursor = db.cursor()
sql="select * from student where id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
 print(x)

cursor.close()
db.close()