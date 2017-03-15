#!/usr/bin/env python3

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector

def DataBase():
    '''Function to handle database connection and other operations'''
    return mysql.connector.connect(user="root", password="pramukhraj", host="localhost", database="sys")


cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
student_id = int(form.getvalue('student_id'))

if student_id !=0:
    # Query to delete from database
    query = "DELETE FROM Student WHERE studentId =('%d')" % (student_id)

    db = DataBase()
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    db.close()

    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Delete Operation</title>")
    print("</head>")
    print("<body>")
    print("<h2>Record Deleted</h2>")
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