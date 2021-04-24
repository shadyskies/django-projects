import os
import mysql.connector
from dotenv import load_dotenv

def get_words():
    load_dotenv()
    mydb = mysql.connector.connect(
        host="localhost",
        user="django_projects",
        password=os.getenv('DB_PWD'),
        database="entries"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT word FROM entries ORDER BY RAND() LIMIT 2")

    myresult = mycursor.fetchall()
    return myresult