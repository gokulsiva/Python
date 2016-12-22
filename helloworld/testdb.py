#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","guest","guest123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : {} ".format(data)

# disconnect from server
db.close()
