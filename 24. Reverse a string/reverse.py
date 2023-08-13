"""
This is an important task to reverse a string
AND 
This is a type of question asked in interviews
These are the following approaches to reverse a string
1. By indexing and slicing
2. By using for loops
3. By using while loops
4. By using recursion
2. By reverse() function in python
3. By making our own reverse algorithms in python
"""
### we will only be looking at slicing the string by indexing and slicing
f = lambda string: string[::-1]
user_input = input("Enter a string: ")
reversed_string = f(user_input)

print("Reversed string:", reversed_string)

# Reversing a string by indexing and slicing is the fastest and most reliable solution.
