num1 = int(input("Enter first numner: "))
num2 = int(input("Enter second number:"))

#using 'and' operator

if num1 > 0 and  num2 > 0 :
    print("both numbers are positive!")

#using 'or' operator

elif num1 > 0 or num2 > 0 :
    print("at least one number is positive!")
else:
    print("neighter number is positive!")


