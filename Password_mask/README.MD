# Secure DB Connection Framework (Password Mask)

This project demonstrates how to securely connect a Python application to a MySQL database without exposing the database password in plain text.

## Features
- Encrypt MySQL password using **Fernet encryption**
- Store encryption key in a separate file
- Prevent password exposure in logs
- Secure database connection framework

## Project Structure

Password_mask/
│
├── encrypt_once.py
├── password_utils.py
├── mysql_connect_safe.py
├── pyjdbc.py
└── secret.key


## How It Works

1. Generate encryption key
2. Encrypt the database password
3. Store encrypted password
4. Decrypt password when connecting to MySQL
5. Connect securely to database

## Install Dependencies

```bash
pip install mysql-connector-python cryptography