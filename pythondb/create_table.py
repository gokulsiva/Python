#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect('localhost', 'guest', 'guest123', 'TESTDB')

cursor = db.cursor()

# cursor.execute("drop table if exists EMPLOYEE")
try:
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME CHAR(20) NOT NULL,
             LAST_NAME CHAR(20),
             AGE INT,
             SEX CHAR(1),
             INCOME FLOAT )"""
    cursor.execute(sql)
except MySQLdb.OperationalError:
    print 'Table already exists'
cursor.close()
db.close()

