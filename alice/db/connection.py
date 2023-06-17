import sys

import mariadb

#connecting to database
def connect():
    try:
        conn = mariadb.connect(
            user='root',
            password='pass',
            host='localhost',
            port=3306,
            database='alicedb'
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platfrom: {e}")
        sys.exit(1)

    cur = conn.cursor()

    return conn, cur