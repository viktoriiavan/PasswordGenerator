import random
import string

password_len = int(input("Write password length:"))
my_password = ""


for i in range(password_len):
    my_password += random.choice(string.printable)

print("Your new passwod:", my_password)