import os
import datetime
import pymysql


username = os.getenv('ifti_gitpod')


connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')


try:
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred', 'bob', 'jim']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)

        connection.commit()
finally:
    connection.close()
