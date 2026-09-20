"""Intermediate Python Topic Notes with Definitions and Examples.

This file covers key intermediate-level Python concepts with practical examples.
"""

print("=== Intermediate Python Topics ===\n")

# 1. Decorators
print("1) Decorators")
print("A decorator is a function that modifies another function without changing its code directly.")

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print()

# 2. Higher-order functions
print("2) Higher-order functions")
print("A higher-order function takes another function as an argument or returns a function.")

def apply_operation(numbers, operation):
    return [operation(n) for n in numbers]

print(apply_operation([1, 2, 3, 4], lambda x: x * 2))
print()

# 3. map(), filter(), reduce()
print("3) map(), filter(), and reduce()")
print("These are built-in functions used for processing collections.")
nums = [1, 2, 3, 4, 5]
print("map:", list(map(lambda x: x * 2, nums)))
print("filter:", list(filter(lambda x: x % 2 == 0, nums)))

from functools import reduce
print("reduce:", reduce(lambda a, b: a + b, nums))
print()

# 4. Modules and imports
print("4) Modules and Imports")
print("Modules are files containing Python code. You can import them into your program.")
import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print()

# 5. File handling
print("5) File Handling")
print("Python can read from and write to files on disk.")
with open("sample_file.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python!\nThis is a sample file.")

with open("sample_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("File content:", content)
print()

# 6. JSON
print("6) JSON")
print("JSON is used to store and exchange data in a text format.")
import json
person = {"name": "Alice", "age": 30, "city": "Kandy"}
json_string = json.dumps(person)
print("JSON string:", json_string)
parsed_data = json.loads(json_string)
print("Parsed JSON:", parsed_data)
print()

# 7. Regular expressions
print("7) Regular Expressions")
print("Regular expressions help search and manipulate strings using patterns.")
import re
pattern = r"\d+"
text = "My age is 25 and my year is 2025."
print("Matches:", re.findall(pattern, text))
print()

# 8. Object-oriented programming basics
print("8) Object-Oriented Programming")
print("OOP organizes code using classes and objects.")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Bruno", 3)
print(my_dog.bark())
print()

# 9. Inheritance
print("9) Inheritance")
print("A subclass can inherit attributes and methods from a parent class.")

class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

print("Cat sound:", Cat().speak())
print()

# 10. Dataclasses
print("10) Dataclasses")
print("Dataclasses provide a simple way to create classes meant for storing data.")

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    grade: int

student = Student("Asha", 90)
print(student)
print(student.name, student.grade)
print()

# 11. Type hints
print("11) Type Hints")
print("Type hints make code easier to understand and help static analysis tools.")

def square(number: int) -> int:
    return number * number

print("Square of 8:", square(8))
print()

# 12. Exception handling and custom errors
print("12) Exception Handling and Custom Errors")
print("You can raise your own errors and handle exceptions gracefully.")

class NegativeNumberError(ValueError):
    pass

def check_age(age: int):
    if age < 0:
        raise NegativeNumberError("Age cannot be negative")
    return age

try:
    print(check_age(-2))
except NegativeNumberError as e:
    print("Caught custom error:", e)
print()

# 13. Basic package understanding and virtual environments
print("13) Packages and Virtual Environments")
print("Packages help organize code modules, and virtual environments keep dependencies isolated.")
print("Example command: python -m venv venv")
print("Then activate it and install packages using pip.")
print()

print("=== End of Intermediate Topics ===")
