##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
i = 0
username = 'a'
password = 'a'
      
while username != 'admin' or password !='12345':
    if i == 3:
        break
    username = str(input())
    password = str(input())
    i += 1

if i < 3:
    print("Access granted")
else:
    print("Access denied")