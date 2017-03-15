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
studentName = form.getvalue('student_name')
studentCity = form.getvalue('student_city')
studentDate = str(form.getvalue('student_date'))


if studentId != 0:
    # Insert query
    query = "UPDATE Student SET " \
            "studentName='%s',studentCity='%s',studentBirthDate='%s' WHERE studentId=%d" \
            % (studentName, studentCity, studentDate, studentId)

    db = DataBase()  # connecting to databse
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    db.close()

    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Insert Operation</title>")
    print("</head>")
    print("<body>")
    print("<h2>Record Inserted</h2>")
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