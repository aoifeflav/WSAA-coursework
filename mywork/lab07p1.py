#Create a database and tables
#Author: Aoife Flavin

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = connection.cursor()

mycursor.execute("CREATE database wsaa2")
mycursor.close()
connection.close()