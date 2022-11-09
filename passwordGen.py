import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols
length_for_pass = int(input("Desired password length: "))

password = "".join(random.sample(Use_for, length_for_pass))

print("Your randomly generated password is: ", password)