import mysql.connector
conn=mysql.connector.connect(user='root',passwd='',database='mycompany')
cur=conn.cursor()
cur.execute('CREATE TABLE employee(empno int primary key,empname varchar(80))')