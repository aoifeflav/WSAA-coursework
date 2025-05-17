#Putting it all together lab 7

import mysql.connector

class StudentDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""

    def __init__(self):
        #read these from a config file
        self.host= "localhost"
        self.user= "root"
        self.password= ""
        self.database= "wsaa"

    def getCursor(self):
        self.conection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def CloseAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql= "insert into student(name, age) values(%s, %s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    def getAll(self):

    