"""THIS IS A TEMPERATURE CONVERSION PROGRAM IN PYTHON"""

# This line of code is asking the user to input the unit of temperature they are using, whether it is
# Celsius or Fahrenheit, and storing the input in the variable `unit`.
unit = input("Is this temerature in celsius or Fahrenheit (C/F): \n \t")
# `temp = float(input("Please enter your temerature: \n \t"))` is asking the user to input the
# temperature value and storing it in the variable `temp`. The `float()` function is used to convert
# the user input into a floating-point number, which is necessary for performing mathematical
# operations on the temperature value later in the program.
temp = float(input("Please enter your temerature: \n \t"))

C = ["Celsius", "celsius", "C", "c", "Celsius degree", "Celsius degrees, celsius degree", "celsius degrees"]  #these are just some cases for the unit of temperature
F = ["Fahrenheit", "fahrenheit", "F", "f", "Fahrenheit degree", "Fahrenheit degrees", "fahrenheit degree", "fahrenheit degrees"] #these are just some cases for the unit of temperature

# This code block is checking if the user input for the unit of temperature is in the list of Celsius
# units (`C`). If it is, the program converts the temperature value from Celsius to Fahrenheit using
# the formula `(9 * temp) / 5 + 32` and rounds the result to one decimal place using the `round()`
# function. It then prints the converted temperature value in Fahrenheit.
if unit in C:
    temp = round((9 * temp) / 5 + 31, 1)
    print(f"Your termerature in Fahrenhreit is {temp}°F")
elif unit in F:
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Your termerature in Celsius is {temp}°F")
else:
    print(f"{unit} is an invalid unit of temerature")
