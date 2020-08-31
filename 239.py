import mysql.connector
conn=mysql.connector.connect(user='root',passwd='')
cur=conn.cursor()
cur.execute('SHOW DATABASES')
for x in cur:   print(x)