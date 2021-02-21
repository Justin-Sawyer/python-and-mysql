import os
import pymysql


username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')


try:
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;",
                                  ['Bob', 'Jim'])
        connection.commit()
finally:
    connection.close()
