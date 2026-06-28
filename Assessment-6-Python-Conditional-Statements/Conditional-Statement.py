# Check if a person is eligible to vote (age ≥ 18).

age = int(input("Enter Your Age: "))
if age >= 18 :
    print("you are eligible to vote!")
else:
    print("you are not eligible for vote!")


# Grade calculator based on marks: 90+ = A, 80+ = B, else C.

student_marks = int(input("enter your marks: "))
if student_marks >= 90 :
    print("your grade is A")
elif student_marks >= 80 :
    print("your grade is B")
else:
    print("your grade is C")

# Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.

signal = input("Enter traffic light color: ")

if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Wait")
elif signal == "Green":
    print("Go")
else:
    print("Invalid signal")

# ATM withdrawal check: sufficient balance or not.

balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")

# Check if a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Check if a number lies within a given range.

num = int(input("Enter a number: "))

if 1 <= num <= 100:
    print("Number is within range")
else:
    print("Number is outside range")

# Username & password verification.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "Mahi" and password == "7755":
    print("Login successful")
else:
    print("Invalid username or password")

# Electricity bill calculator based on units consumed.

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Electricity bill =", bill)

# Simple calculator (add, subtract, multiply, divide).

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result =", num1 + num2)

elif operation == "-":
    print("Result =", num1 - num2)

elif operation == "*":
    print("Result =", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operation")

# Check type of triangle (equilateral, isosceles, scalene).

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
    print("Equilateral Triangle")

elif a == b or b == c or a == c:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")