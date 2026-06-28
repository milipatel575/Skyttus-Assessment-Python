# Print numbers from 1 to 10.

for i in range (1, 11):
    print( i)

# Display multiplication table for a given number.

num = int(input("enter a number: "))

for i in range (1, 11):
    print(num, "x", i, "=", num * i)

# Find factorial of a number.

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

# Generate the first N Fibonacci numbers.

num = int(input("enter a number: "))
a = 0
b = 1

print("fibonacci series: ", )

for i in range (num):
    print(a)

    c = a + b
    a = b
    b = c 

# Check if a number is prime.

num = int(input("enter a number: "))

count = 0

for i in range (1 , num + 1):

 if num % i == 0 :
    count += 1

if count == 2: 
    print(num, "is prime number!")
else:
    print("given number is not a prime number!")

# Reverse a number (e.g., 123 → 321).

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed Number =", rev)

# Count digits in a number.

num = int(input("Enter a number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Total Digits =", count)


# Find sum of even numbers between 1–100.

sum = 0 

for i in range (1, 101):
    if i % 2 == 0:
        sum = sum + i

print("sum of even numbers between 1-100 is : ", sum)


# Print a pyramid pattern.

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))

# Find all divisors of a number.

num = int(input("enter a number: "))

print("Divisiors numbers: ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)