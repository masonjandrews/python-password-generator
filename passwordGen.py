import random
import csv

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols
pass_purpose = input("Save password as: ")
length_for_pass = int(input("Desired password length: "))

password = "".join(random.sample(Use_for, length_for_pass))

print("Your randomly generated password is: ", password)

with open('passwords.csv', mode='a') as passwords:
	passwords_writer = csv.writer(passwords, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	passwords_writer.writerow([pass_purpose, password])
