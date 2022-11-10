import secrets
import string
import random
import csv

letters = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation
characters = letters + numbers + special_chars

pass_purpose = input("Save password as: ")
length_for_pass = int(input("Desired password length: "))

password = ''

for i in range(length_for_pass):
	password += ''.join(secrets.choice(characters))

print("Your randomly generated password is: ", password)

with open('passwords.csv', mode='a') as passwords:
	passwords_writer = csv.writer(passwords, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	passwords_writer.writerow([pass_purpose, password])