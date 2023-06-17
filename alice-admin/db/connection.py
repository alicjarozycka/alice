import sys
from os import environ

import mariadb

#connecting to database
def connect():
    try:
        conn = mariadb.connect(
            user=environ["DB_USER"],
            password=environ["DB_PASSWORD"],
            host=environ["DB_HOST"],
            port=int(environ["DB_PORT"]),
            database=environ["DB_NAME"]
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platfrom: {e}")
        sys.exit(1)

    cur = conn.cursor()

    return conn, cur