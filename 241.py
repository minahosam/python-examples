import mysql.connector
conn=mysql.connector.connect(user='root',passwd='',database='mycompany')
cur=conn.cursor()
cur.execute("insert into emp values(1,'mina')")
conn.commit()