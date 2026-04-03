import mysql.connector;
from password_utils import get_decrypted_password


def connect_to_mysql():

    password = get_decrypted_password()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sanjay2512",
        database="test"
    )

    print("Connected to MySQL securely")

    conn.close()


if __name__ == "__main__":
    connect_to_mysql()