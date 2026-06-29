import mysql.connector


def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harnoor@123",
        database="youtube_analysis"
    )

    return connection