#Putting it all together lab 7

import mysql.connector

class StudentDAO:
    def __init__(self):
        # Ideally, read these from a config file
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "wsaa"
        self.connection = None
        self.cursor = None

    def get_cursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_all(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create(self, values):
        cursor = self.get_cursor()
        sql = "INSERT INTO student (name, age) VALUES (%s, %s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.close_all()
        return newid

    def get_all(self):
        cursor = self.get_cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        result = cursor.fetchall()
        studentlist = []
        for row in result:
            studentlist.append(self.convert_to_dict(row))
        self.close_all()
        return studentlist

    def find_by_id(self, id):
        cursor = self.get_cursor()
        sql = "SELECT * FROM student WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.close_all()
        if result:
            return self.convert_to_dict(result)
        else:
            return None

    def update(self, id, name, age):
        cursor = self.get_cursor()
        sql = "UPDATE student SET name = %s, age = %s WHERE id = %s"
        values = (name, age, id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()
        return cursor.rowcount  # returns number of affected rows

    def delete(self, id):
        cursor = self.get_cursor()
        sql = "DELETE FROM student WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close_all()
        return cursor.rowcount  # returns number of affected rows

    def convert_to_dict(self, row):
        # Assuming student table columns: id, name, age
        return {
            "id": row[0],
            "name": row[1],
            "age": row[2]
        }

# Example instantiation
studentDAO = StudentDAO()

