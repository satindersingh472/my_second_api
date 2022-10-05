from dataclasses import dataclass
import mariadb
import dbcreds

def connect_db():
    conn = mariadb.connect(user=dbcreds.user,host=dbcreds.host, password=dbcreds.password,port=dbcreds.port,database=dbcreds.database)
    cursor = conn.cursor()
    return cursor

def execute_statement(cursor,statement,list=[]):
    cursor.execute(statement,list)
    result = cursor.fetchall()
    return result

def close_connection(cursor):
    conn = cursor.connection
    cursor.close()
    conn.close()

def conn_exe_close(statement,list):
    cursor = connect_db()
    result = execute_statement(cursor,statement,list)
    close_connection(cursor)
    return result
