#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect('localhost', 'guest', 'guest123', 'TESTDB')

cursor = db.cursor()

sql = """select * from EMPLOYEE"""

cursor.execute(sql)

result = cursor.fetchone()

# for row in result:
print 'Name : {} {}, Age : {}, Sex : {}, Income : {}'.format(result[0], result[1], result[2], result[3], result[4])

cursor.close()
db.close()
