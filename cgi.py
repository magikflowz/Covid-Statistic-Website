#!/usr/local/bin/python3

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
fname = form.getvalue('firstname')
lname = form.getvalue('lastname')
email = form.getvalue('email')
number = form.getvalue('number')
country = form.getvalue('country')
subject = form.getvalue('subject')


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print (fname)
print (lname)
print(email)
print(number)
print(country)
print(subject)
print ("</body>")
print ("</html>")
