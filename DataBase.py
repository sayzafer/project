import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
class DB():

    def __init__(self):
        self.mydb = mysql.connector.connect(user=os.getenv('dbUser'), password=os.getenv('dbPassword'),
                                    host=os.getenv('dbHost'),
                                    database=os.getenv('dbDatabase'))
        

        self.mycursor = self.mydb.cursor()

    def signUp(self,NationalId,Mail,Password,Name,LastName,Phone,Adress,Balance,Star):
        
        sql = "INSERT INTO tblUser (NationalId,Mail,Password,Name,LastName,Phone,Adress,Balance,Star) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (NationalId,Mail,Password,Name,LastName,Phone,Adress,Balance,Star)
        self.mycursor.execute(sql, val)
        self.mydb.commit()