"""Beginner Python Topic Notes with Definitions and Examples.

This file explains core Python concepts for beginners and includes simple examples.
"""

print("=== Beginner Python Topics ===\n")

# 1. Variables, data types, and type conversion
print("1) Variables, Data Types, and Type Conversion")
print("A variable stores a value. Python has built-in data types like int, float, str, bool, and list.")
name = "Alice"
age = 25
height = 5.8
is_student = True

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Student:", is_student, type(is_student))

converted_age = str(age)
converted_height = int(height)
print("Converting age to string:", converted_age, type(converted_age))
print("Converting height to int:", converted_height, type(converted_height))
print()

# 2. Operators and expressions
print("2) Operators and Expressions")
print("Operators perform actions on values. Expressions combine values and operators.")
print("Addition:", 10 + 5)
print("Subtraction:", 10 - 5)
print("Multiplication:", 10 * 5)
print("Division:", 10 / 5)
print("Floor division:", 10 // 3)
print("Modulus:", 10 % 3)
print("Power:", 2 ** 3)
print("Comparison:", 10 > 5)
print("Logical AND:", True and False)
print("Logical OR:", True or False)
print()

# 3. Conditionals
print("3) Conditionals: if / elif / else")
print("Conditionals let the program choose different actions based on conditions.")
marks = 78
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
print()

# 4. Loops: for and while
print("4) Loops: for and while")
print("Loops repeat a block of code multiple times.")
print("For loop:")
for i in range(1, 4):
    print("Iteration:", i)

print("While loop:")
count = 1
while count <= 3:
    print("Count is:", count)
    count += 1
print()

# 5. Lists, tuples, sets, and dictionaries
print("5) Lists, Tuples, Sets, and Dictionaries")
print("These are built-in data structures used to store collections of items.")
my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
my_set = {1, 2, 2, 3}
my_dict = {"name": "Bob", "age": 22, "city": "Colombo"}

print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)
print("Dictionary value:", my_dict["name"])
print()

# 6. String operations and formatting
print("6) String Operations and Formatting")
print("Strings are sequences of characters, and Python provides built-in methods for manipulation.")
text = "python is fun"
print("Original:", text)
print("Uppercase:", text.upper())
print("Title case:", text.title())
print("Split:", text.split())
print("Replace:", text.replace("fun", "powerful"))
print("Formatted message:", f"Hello, {name}! You are {age} years old.")
print()

# 7. Functions: parameters, return values, scope
print("7) Functions")
print("Functions are reusable blocks of code. They can take parameters and return values.")

def add_numbers(x, y):
    return x + y

result = add_numbers(10, 20)
print("Result:", result)

# local scope example
value = 100

def show_value():
    local_value = 50
    print("Local value:", local_value)
    print("Global value:", value)

show_value()
print()

# 8. Default arguments and keyword arguments
print("8) Default Arguments and Keyword Arguments")
print("Default arguments are used when a value is not supplied. Keyword arguments pass values by name.")

def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Sam"))
print(greet("Sam", "Welcome"))
print(greet(message="Hi", name="Nina"))
print()

# 9. Recursion basics
print("9) Recursion Basics")
print("A recursive function calls itself to solve a smaller version of the same problem.")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print()

# 10. Lambda functions
print("10) Lambda Functions")
print("Lambda functions are small anonymous functions.")
add = lambda a, b: a + b
print("Lambda sum:", add(3, 5))
print("Sorted with lambda:", sorted([5, 2, 9, 1], key=lambda x: x))
print()

# 11. List comprehensions and dictionary comprehensions
print("11) List Comprehensions and Dictionary Comprehensions")
print("Comprehensions provide a compact way to create lists and dictionaries.")
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

student_scores = {"Alice": 90, "Bob": 85, "Charlie": 92}
passed = {name: score for name, score in student_scores.items() if score >= 90}
print("Passed students:", passed)
print()

# 12. Basic input/output
print("12) Basic Input/Output")
print("Input lets the user provide data to the program.")
try:
    user_name = input("Enter your name: ")
except EOFError:
    user_name = "Guest"
print("Hello,", user_name)
print()

# 13. Error handling: try / except / finally
print("13) Error Handling: try / except / finally")
print("Try/except handles exceptions and prevents crashes.")
try:
    try:
        number = int(input("Enter a number: "))
    except EOFError:
        print("No number entered. Using default number 2.")
        number = 2
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("This block always runs.")
print()

print("=== End of Beginner Topics ===")
