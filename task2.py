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

import time

username = (str(input("Enter your username: "))).strip()
password = (str(input("Enter your password: "))).strip()
real_username = str("admin")
real_password = str("12345")

while username != real_username and password != real_password:
    print("Access denied")
    username = (str(input("Enter your username: "))).strip()
    password = (str(input("Enter your password: "))).strip()

if username == real_username and password == real_password:
    print("Acess granted")
