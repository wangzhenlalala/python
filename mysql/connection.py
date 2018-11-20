import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database="family",
        user='wangzhen',
        password='wangzhen'
    )
    if connection.is_connected():
        db_info = connection.get_server_info()
        print('connected to Mysql database...Mysql Server version on', db_info)
        sql_insert_query = '''
            INSERT INTO member
            (name, age, gender) VALUES ('itachi', 25, 'male')
        '''
        cursor = connection.cursor()
        cursor.execute(sql_insert_query)
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