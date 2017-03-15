#!/usr/bin/env python3

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector

cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
sid = int(form.getvalue('Sid'))
sname = form.getvalue('Sname')

db = mysql.connector.connect(user="root", password="pramukhraj", host="localhost", database="sys")
cursor= db.cursor()

query = "INSERT INTO Student(sid,sname) VALUES ('%d','%s' )" % (sid, sname)
cursor.execute(query)
db.commit()
db.close()

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello Id: %d Name: %s Inserted</h2>" % (sid, sname))
print ("</body>")
print ("</html>")