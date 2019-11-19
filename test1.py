import random
characters = ("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*") 
lengh = input("enter the lenght")
lengh = int(lengh)
password = ""
for a in range(lengh): 
    password += random.choice(characters)
print(password)