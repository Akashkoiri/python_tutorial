from getpass import getpass

# This library helps us to hide the user inputs like password

username = input("Username: ")
password = getpass("Password: ")

print(username,password)