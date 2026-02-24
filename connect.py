import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
    # or your database host
        user='root',
        password='prince143'
    )

    if connection.is_connected():
        print("Successfully connected to the database")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

