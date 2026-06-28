# Function to check if a number is prime.

def prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:    
        print(n, "is prime number")
    else:
            print(n, "is not a prime number")
    
n = int(input("enter a number: "))
prime(n)



# Function to reverse a string.

def reverse_string(text):
     rev = text[::-1]
     print("Resvers String =", rev)

s = input("Enter string: ")
reverse_string(s)
     

# Function to find factorial.

def factorial(num):
     fact = 1 

     for i in range(1, num + 1):
          fact = fact * i

     print("Factorial =", fact)

n = int(input("Enter number: "))
factorial(n)


# Function to calculate simple interest.

# formula =>
# SI = PRT/100

def simple_interest(p, r, t):
     si = (p * r * t)/100
     print("Simple Interest =", si)

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

simple_interest(p, r, t)


# Function to check if a word is palindrome.

def palidrome(word):
     rev = word[::-1]

     if word == rev:
          print("Palidrome")
     else:
          print("Not Palidrome")

w = input("Enter Word: ")
palidrome(w)


# Function to count vowels in a string.

def count_vowels(text):
     count = 0 

     for ch in text:
          if ch.lower() in "aeiou":
               count += 1
     print("Total Vowels =", count)

s = input("Enter String: ")
count_vowels(s)
     

# Function to merge two lists.

def merge(list1, list2):
     merged = list1 + list2
     print("merged list: ", merged)

l1 = [20, 500, 60]
l2 = [40, 80, 200]

merge(l1, l2)


# Function to find GCD of two numbers.

# formula =>
# gcd(a, b) = gcd(b,a mod b)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    print("GCD =", a)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

gcd(x, y)


# Function to find area of rectangle.

def rectangle_area(length, breadth):
    area = length * breadth
    print("Area of Rectangle =", area)


l = float(input("Enter Length: "))
b = float(input("Enter Breadth: "))

rectangle_area(l, b)

# Function to check Armstrong number.

def armstrong(num):
    temp = num
    total = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")


n = int(input("Enter a number: "))
armstrong(n)