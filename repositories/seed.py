
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getcwd())

import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

# establish a connection to MySQL database
connection = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_DATABASE")
)

mycursor = connection.cursor()

df = pd.read_csv('dataset/airlines.csv')

engine = create_engine(f"mysql+mysqlconnector://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/flight")

df.to_sql('Airline', con=engine, if_exists='append', index=False)

connection.commit()

# print(mycursor.rowcount, "record inserted.")
# mycursor.execute("Select * from Airline")


################################################################################################################

df = pd.read_csv('dataset/airports.csv')

mycursor = connection.cursor()

def insert_address(city, state, country):
    mycursor.execute("""
        INSERT INTO Address (city, state, country)
        VALUES (%s, %s, %s)
    """, (city, state, country))

    connection.commit()
    return mycursor.lastrowid


for index, row in df.iterrows():

    city = row['city']
    state = row['state']
    country = row['country']

    address_id = insert_address(city, state, country)

    mycursor.execute("""
        INSERT INTO Airport (code, name, address_id)
        VALUES (%s, %s, %s)
    """, (row['code'], row['name'], address_id))

    connection.commit()  # Save the changes

################################################################################################################

flights_df = pd.read_csv('dataset/flights.csv')
# print(flights_df.columns)
mycursor = connection.cursor()


# flight_no
insert_flight_query = """
    INSERT INTO Flight (airline_code, distance_km, dep_time, arri_time, dep_port, arri_port, booked_seats)
    VALUES (%s, %s, %s, %s, %s, %s, 0)
"""

relevant_columns = ['airline_code', 'distance_km', 'dep_time', 'arri_time', 'dep_port', 'arri_port']

# Convert the selected columns to tuples (rows of data)
flight_data = [tuple(row) for row in flights_df[relevant_columns].values]

batch_size = 1000

for i in range(0, len(flight_data), batch_size):
    batch = flight_data[i:i + batch_size]
    mycursor.executemany(insert_flight_query, batch)
    connection.commit()

print(f"{len(flight_data)} flights inserted into the database.")

################################################################################################################
mycursor = connection.cursor()

# Insert roles
mycursor.execute("INSERT INTO Role(name) VALUES ('admin');")
mycursor.execute("INSERT INTO Role(name) VALUES ('user');")

# Insert admin account
mycursor.execute("INSERT INTO Account(username, password, status) VALUES ('admin_user', '12345', 'active');")

# Fetch the account_id of the newly inserted admin account
mycursor.execute("SELECT account_id FROM Account WHERE username = 'admin_user';")
admin_account_id = mycursor.fetchone()[0]

# Fetch the role_id of the admin role
mycursor.execute("SELECT role_id FROM Role WHERE name = 'admin';")
admin_role_id = mycursor.fetchone()[0]

# Insert into Account_Role (assign admin role to admin_user)
mycursor.execute("INSERT INTO Account_Role(account_id, role_id) VALUES (%s, %s);", (admin_account_id, admin_role_id))

connection.commit()

mycursor.close()
connection.close()