# this program converts fahrenheit to celsius

def main():
    """
    Takes user input of a temperature in fahrenheit and converts it to celsius.

    Parameters:
        None

    Returns:
        None
    """
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature in celsius is: ", celsius)

main()