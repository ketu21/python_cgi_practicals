#!/usr/bin/env python3

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector


def DataBase():
    '''Function to handle database connection '''
    return mysql.connector.connect(user="root", password="pramukhraj", host="localhost", database="sys")

def OutputResult(info):
    '''Function to print the html form after the script execution'''
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Insert Operation</title>")
    print("</head>")
    print("<body>")
    print("<h2>%s</h2>" % info)
    print("</body>")
    print("</html>")


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
    query = "INSERT INTO Student" \
            "(studentId,studentName,studentCity,studentBirthDate) " \
            "VALUES ('%d','%s','%s','%s' )" \
            % (studentId, studentName, studentCity, studentDate)

    db = DataBase()
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    db.close()

    OutputResult("Record Inserted")
else:
    OutputResult("Error inserting data")