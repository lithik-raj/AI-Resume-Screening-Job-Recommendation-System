import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="bornl2006",
    database="EMPLOYEE"
)
cursor = conn.cursor()

cursor.execute("SHOW TABLES")

for table in cursor.fetchall():
    print(table)

conn.close()