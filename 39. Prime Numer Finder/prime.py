def is_prime():
    """
    Check if a number is prime.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    num = int(input("Enter a number: "))

    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
    print(f"{num} is a prime number.")

is_prime()