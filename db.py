import os
from urllib.parse import quote_plus

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("MYSQLHOST", "localhost")
DB_USER = os.environ.get("MYSQLUSER", "root")
DB_PASSWORD = os.environ.get("MYSQLPASSWORD", "")
DB_NAME = os.environ.get("MYSQLDATABASE", "EduClass")
DB_PORT = int(os.environ.get("MYSQLPORT", 3306))


def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT,
    )


def get_database_uri():
    user = quote_plus(str(DB_USER))
    password = quote_plus(str(DB_PASSWORD))
    credentials = user if not password else f"{user}:{password}"
    return f"mysql+mysqlconnector://{credentials}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
