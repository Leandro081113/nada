# db_config.py
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',    # Cambia esto si tu base de datos no está en localhost
        user='root',   # Cambia esto por tu usuario de MySQL
        password='',   # Cambia esto por tu contraseña de MySQL
        database='perfumeria.sql'  # Cambia esto por el nombre de tu base de datos
    )
    return connection
