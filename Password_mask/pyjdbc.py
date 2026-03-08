import mysql.connector

def connect_to_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="test"
    )

    print("Connected to MySQL successfully")

    conn.close()


if __name__ == "__main__":
    connect_to_mysql()