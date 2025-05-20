# country dao 
# data layer that connects to a datbase
# Author: Aoife Flavin

import mysql.connector
import dbconfig as cfg
class CountryDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from country"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from country where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, country):
        cursor = self.getcursor()
        sql="insert into country (country_name,visit_date, rating) values (%s,%s,%s)"
        values = (country.get("country_name"), country.get("visit_date"), country.get("rating"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        country["id"] = newid
        self.closeAll()
        return country


    def update(self, id, country):
        cursor = self.getcursor()
        sql="update country set country_name= %s,visit_date=%s, rating=%s  where id = %s"
        print(f"update country {country}")
        values = (country.get("country_name"), country.get("visit_date"), country.get("rating"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from country where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        #print("delete done")

    def convertToDictionary(self, resultLine):
        attkeys=['id','country_name','visit_date', "rating"]
        country = {}
        currentkey = 0
        for attrib in resultLine:
            country[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return country

        
countryDAO = CountryDAO()