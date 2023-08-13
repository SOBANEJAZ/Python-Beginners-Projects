import random
import string

letters = string.ascii_letters
numbers = string.digits
special_char = string.punctuation

character = letters

if numbers:
    character += numbers
if special_char:
    character += special_char

password = ""
len = int(input("Enter the length: "))
counter = 0

while counter < len:
    count_pass = random.choice(character)
    password += count_pass
    counter += 1
print("Your Password is:" , password)