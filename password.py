import random
characters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*")
length = input("enter pasword lenght: ")
length = int(length )
password = ""
for c in range(length):
    password += random.choice(characters) 
print(password) 