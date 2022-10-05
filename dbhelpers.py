
import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user,host=dbcreds.host, password=dbcreds.password,port=dbcreds.port,database=dbcreds.database)
        cursor = conn.cursor()
        return cursor
    except mariadb.ProgrammingError as error:
        print('programming error: ',error)
        return str(error)
    except Exception as error:
        print('Unknown Error', error)
        return str(error)
def execute_statement(cursor,statement,list=[]):
    try:
        cursor.execute(statement,list)
        result = cursor.fetchall()
        return result
    except mariadb.InternalError as error:
        print('Internal Error', error)
        return str(error)
    except mariadb.DatabaseError as error:
        print('Database Error',error)
        return str(error)
    except mariadb.OperationalError as error:
        print('Operational Error',error)
        return str(error)
    except mariadb.IntegrityError as error:
        print('Integrity error',error)
        return str(error)

def close_connection(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.OperationalError as error:
        print('Operational Error',error)
        return str(error)
    except Exception as error:
        print('Unknown Error',error)
        return str(error)


def conn_exe_close(statement,list):
    cursor = connect_db()
    if(cursor == None):
        return 'Connection Error'
    result = execute_statement(cursor,statement,list)
    close_connection(cursor)
    return result
