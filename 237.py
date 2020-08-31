import mysql.connector
try:
    conn=mysql.connector.connect(user='root',passwd='')
    mycursor=conn.cursor()
    mycursor.execute('CREATE DATABASE db_with_python')
except mysql.connector.Error as f:
    print(f)