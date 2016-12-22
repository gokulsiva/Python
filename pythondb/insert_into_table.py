#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect('localhost', 'guest', 'guest123', 'TESTDB')

cursor = db.cursor()

first_name = raw_input('Enter your first name : ')
last_name = raw_input('Enter your last name : ')
age = raw_input('Enter your age : ')
sex = raw_input("Enter your sex as either 'M' or 'F' : ")
income = raw_input('Enter your income : ')

sql = """INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
         VALUES ('{}', '{}', {}, '{}', {})""".format(str(first_name), str(last_name), int(age), str(sex), float(income))

cursor.execute(sql)
db.commit()

cursor.close()
db.close()

