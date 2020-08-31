import mysql.connector
conn=mysql.connector.connect(user='root',passwd='')
cur=conn.cursor()
cur.execute('CREATE DATABASE mycompany DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci')