#!/usr/lib/python

import cgi
import MySQLdb

form = cgi.FieldStorage()
password = None
if form.getvalue('password'):
    password = form.getvalue('password')

db = MySQLdb.connect('localhost', 'guest', 'guest123', 'SREEVANEE')
cursor = db.cursor()
cursor.execute('SELECT PASSWORD FROM PASSWORD')
result = cursor.fetchall()
check = False
if cursor.rowcount > 1:
    for row in result:
        if row[0] == password:
            check = True
elif cursor.rowcount == 1:
    if result[0][0] == password:
        check = True

if check:
    message = 'Logged in successfully.'
else:
    message = 'Incorrect password'

print 'Content-type:text/html\r\n\r\n'
print '<html>'
print '<head>'
print '<title>Chitta-Sheet</title>'
print '</head>'
print '<body>'
print message
print '</body>'
print '</html>'
