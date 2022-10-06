
# import database and credentials file
import mariadb
import dbcreds

# connect to database with the help of dbcreds.py
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

#execute the given statement with cursor and stored procedure with list arguments 
# return the result
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
    except mariadb.ProgrammingError as error:
        print('Programming Error',error)
        return str(error)
    except TypeError as error:
        print('Type Error',error)
        return str(error)
    except Exception as error:
        print('Unknown Error',error)
        return str(error)

# close the connection after the data is fetched or running the execute statement
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

# using all three functions in one function to shrink the commands needed each time to
# ineract with database
def conn_exe_close(statement,list):
    cursor = connect_db()
    if(cursor == None):
        return 'Connection Error'
    result = execute_statement(cursor,statement,list)
    if(result == None):
        close_connection()
        return 'Error in performing a request'
    close_connection(cursor)
    return result
