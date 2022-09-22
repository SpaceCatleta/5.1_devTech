import sqlite3 as sql

connection: sql.Connection
cursor: sql.Cursor

default_path: str = ""


def open(path: str):
    global connection, cursor
    connection = sql.connect(path)
    cursor = connection.cursor()

    print('database: connected - {0}'.format(path))


def get_connection():
    conn = sql.connect(default_path,detect_types=sql.PARSE_DECLTYPES)
    return conn, conn.cursor()


def close_connection(conn, cursor):
    cursor.close()
    conn.close()


def close():
    connection.close()
    print('database: connection closed')
