# a program that converts kilometers to miles

def km_to_miles():
    """
    Convert kilometers to miles.

    Takes no parameters.

    Returns:
        None.
    """
    km = float(input("Enter a distance in kilometers: "))
    miles = km * 0.621371
    print(f"{km} kilometers is {miles} miles.")

km_to_miles()
