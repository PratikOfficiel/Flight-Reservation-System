import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# establish a connection to MySQL database
connection = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_DATABASE")
)

# create a cusrsor object to perform quries
mycursor = connection.cursor()

# query for a table named users
mycursor.execute("SELECT user, host FROM mysql.user WHERE user = 'educative';")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


mycursor.close()
connection.close()


def get_db_connection():
    connection = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_DATABASE")
)
    return connection