import mysql.connector
conn=mysql.connector.connect(user='root',passwd='',database='mycompany')
cur=conn.cursor()
cur.execute("update emp set empname='k' where empno=1")
conn.commit()