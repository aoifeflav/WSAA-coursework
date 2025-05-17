#Create the table in the database with the python script
#Author: Aoife Flavin

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "wsaa2"
)

mycursor = mydb.cursor()
sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

mycursor.execute(sql)

mycursor.close()
mydb.close()