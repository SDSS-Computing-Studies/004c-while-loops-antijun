# Problem 1
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
Acces denied
"""

import time

username = (input("Enter your username: ")).strip()
password = (input("Enter your password: ")).strip()
real_username = str("admin")
real_password = str("12345")
count = 0

while username != real_username and password != real_password:
    print("Access denied")
    count = count + 1
    if count > 2:
        break
    username = (input("Enter your username: ")).strip()
    password = (input("Enter your password: ")).strip()

if username == real_username and password == real_password:
    print("Acess granted")
