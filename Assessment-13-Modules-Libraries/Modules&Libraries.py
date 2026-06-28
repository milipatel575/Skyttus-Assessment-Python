# Create a custom math module and import it in another file.

import mymath

print("Addition =", mymath.add(10, 5))
print("Substration =", mymath.substract(10, 5))
print("Multiplication =", mymath.multiply(10, 5))
print("Division =", mymath.divide(10, 5))

# Create a module to perform string operations.

import string_operation

s = "Python"

print("Upper: ", string_operation.to_upper(s))
print("Lower: ", string_operation.to_lower(s))
print("Reverse: ", string_operation.reverse(s))
print("Length: ", string_operation.count_characters(s))

# Use random module to generate 5 random integers.

import random

print("Five Random Numbers: ")

for i in range(5):
    print(random.randint(1, 100))

# Use datetime module to display current date and time.

from datetime import datetime

current =  datetime.now()

print("Current Date and Time:")
print(current)

# Use math module to find factorial of a number.

import math

num = int(input("Enter Number: "))

fact = math.factorial(num)

print("Factorial =", fact)

# Create a package shapes with modules for circle and rectangle.

from Shapes import circle
from Shapes import reactangle

print("Circle Area =", circle.area(5))
print("Reactangle Area =", reactangle.area(4, 6))

# Import multiple functions from one module and use them.

from calculator import add, sub, mul, div

print(add(10, 5))
print(sub(10, 5))
print(mul(10, 5))
print(div(10, 5))

# Write a program to shuffle a list using random module.

import random

numbers = [1, 2, 3, 4, 5]

print("Before Shuffle:", numbers)

random.shuffle(numbers)

print("After Shuffle:", numbers)

# Write a program to calculate the difference between two dates.

from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)

differnce = date2 - date1

print("Difference in days =", differnce.days)

# Use os module to list files in a directory.

import os

path = "."

files = os.listdir(path)

print("Files in Directory:")

for file in files:
    print(file)