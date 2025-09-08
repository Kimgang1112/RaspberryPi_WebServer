import pymysql

conn = pymysql.connect(host='localhost', user='viego', password='BerylM7621227#', db='shopping_db2')

cur = conn.cursor()
cur.execute('select avg(age) from CUSTOMER where address="경기"')

result = cur.fetchone()
print(int(result[0]))

cur.close()
conn.close()

