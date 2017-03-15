#!/usr/bin/env python3

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector


def DataBase():
    '''Function to handle database connection '''
    return mysql.connector.connect(user="root", password="pramukhraj", host="localhost", database="sys")


cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields from the html form
studentId = int(form.getvalue('student_id'))


if studentId != 0:
    # Insert query
    query = "SELECT * FROM Student WHERE studentId=%d" % studentId

    db = DataBase()
    cursor = db.cursor()
    cursor.execute(query)
    values = cursor.fetchone()  # fenction to fetch the values of the query result stored in cursor
    studentName = values[1]
    studentCity = values[2]
    studentDate = values[3]

    db.commit()
    db.close()

    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Insert Operation</title>")
    print("</head>")
    print("<body>")
    print("<h2>%d</h2>" % studentId)
    print("<h2>%s</h2>" % studentName)
    print("<h2>%s</h2>" % studentCity)
    print("<h2>%s</h2>" % studentDate)
    print("</body>")
    print("</html>")
else:
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Insert Operation</title>")
    print("</head>")
    print("<body>")
    print("<h2>No Student Id Entered</h2>")
    print("</body>")
    print("</html>")