# BAsic calculator in python
while True:


    operator = input("Enter operator(+ - * /): \n \t ")
    operator = input("Enter operator(+ - * /): \n \t ")
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))
    if operator == "+":
        result = num1 + num2
        print(result)
    elif operator == "-":
        result = num1 - num2
        print(result)
    elif operator == "*":
        result = num1 * num2
        print(result)
    elif operator == "/":
        result = num1 / num2
        print(result)
    else:
        print("Invalid operator")

    p = input("Do you want to continue(y/n): ")
    if p == "y":
        continue
    elif p == "n":
        break