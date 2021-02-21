import os
import pymysql


username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')


try:
    with connection.cursor() as cursor:
        """
        # Update ages #
        rows = [(23, 'bob'),
                (24, 'jim'),
                (25, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)
                           """
        # Update names to start with Capital letter like in video lesson
        names = [('Bob', 23),
                 ('Jim', 24),
                 ('Fred', 25)]
        cursor.executemany("UPDATE Friends SET name = %s WHERE age = %s;",
                           names)
        connection.commit()
finally:
    connection.close()
