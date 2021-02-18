#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
username = str(input("username"))
password = str(input("password"))

a = str("admin")
b = str("12345")

while username != a or password != b:
    print("Access denied")
    username = str(input("username"))
    password = str(input("password"))
if username == a and password == b:
    print("Access granted")

