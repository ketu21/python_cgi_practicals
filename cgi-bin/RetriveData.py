#!/usr/bin/env python3

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector


def DataBase():
    '''Function to handle database connection '''
    return mysql.connector.connect(user="root", password="pramukhraj", host="localhost", database="sys")


#Function that contains multiple parameters:
def OutputResult(studentId, studentName, studentCity, studentDate):
    """Function to print the html form after the script execution"""
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Insert Operation</title>")
    print("<form action="+'"update.py"'+" method="+'"post"'+">")
    print("Student Id: &nbsp;&nbsp;&nbsp;<input type="+'"number"'+" name ="+'"student_id"'+" value=",studentId,"><br />")
    print("Name: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="+'"text"'+" name ="+'"student_name"'+" value="+studentName+"><br/>")
    print("City: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="+'"text"'+" name ="+'"student_city"'+" value="+studentCity+"><br/>")
    print("Birth Date: &nbsp;&nbsp;&nbsp;<input type=" + '"date"' + "name=" + '"student_date"' + " value=" +studentDate+ "><br/>")
    print("<input type="+'"submit"'+"name="+'"action"'+" value="+'"Save"'+" />")
    print("<input type=" + '"button"' + "name=" + '"action"' + " value=" + '"Go Back"' + "formaction="+'"http://new.html"'+" />")
    print("</form>")
    print("<body></body>")
    print("</html>")


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
    OutputResult(studentId,studentName,studentCity,studentDate)
else:
    OutputResult(0,"NULL","NULL","NULL")