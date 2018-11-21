import mysql.connector
from mysql.connector import Error

def insert_single(cursor):
    sql_insert_query = '''
        INSERT INTO member
        (name, age, gender) VALUES ('itachi', 25, 'male')
    '''
    cursor.execute(sql_insert_query);

def insert_multiple(cursor):
    datas = [
        ('wukong', 22, 'male'),
        ('bajie', 23, 'female'),
        ('wujing', 24, 'male')
    ]
    sql_insert_query = '''
        INSERT INTO member (name, age, gender) VALUES (%s, %s, %s)
    '''
    result = cursor.executemany(sql_insert_query, datas)
    print(result)

try:
    connection = mysql.connector.connect(
        host='localhost',
        database="family",
        user='wangzhen',
        password='wangzhen'
    )
    if connection.is_connected():
        # cursor = connection.cursor()
        # insert_single(cursor)

        # cursor = connection.cursor(prepared=True)
        cursor = connection.cursor()
        # cursor = connection.MySQLCursorPrepared()
        insert_multiple(cursor)

        connection.commit()
        print("Record inserted successfully into member table")
except Error as e:
    connection.rollback() # #rollback if any exception occured
    print('Error occured while operating on your database', e)
finally:
    if connection.is_connected():
        #closing database connection.
        cursor.close()
        connection.close()
        print('Mysql connection is close. Bye')