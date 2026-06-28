# Write a program to handle division by zero error.

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Write a program to handle invalid integer input.

try:
    num = int(input("Enter an integer: "))
    print("You entered: ", num)

except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")

# Write a program to open a file and handle the "file not found" error.

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

# Write a program to demonstrate multiple exception blocks.

try:
    num = int(input("Enter a number: "))
    result =  100 / num

    print("Result =", result)

except ValueError:
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e: 
    print("An unexpected error occurred: ", e)

# Write a program to use finally for resource cleanup.

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Error: File not found.")

finally:
    print("Closing file and cleaning up resources.")
    try:
        file.close()
    except NameError:
        pass


# Write a program to create a custom exception for invalid age (<18).

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    
    print("You are eligible.")

except InvalidAgeError as e:
    print("Error: ", e)

except ValueError:
    print("Please enter a valid age.")


# Write a program to handle IndexError when accessing a list.

try:
    my_list = [10, 20, 30, 40, 50, 60, 70, 80]

    index = int(input("Enter the index: "))
    print("Element at index", index, "is", my_list[index])

except IndexError:
    print("Error: Index is out of range.")

except ValueError:
    print("Error: Please enter a valid integer.")

# Write a program that takes two numbers and handles all possible errors.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("Unexpected Error:", e)

else:
    print("Result =", result)

finally:
    print("Program execution completed.")

# Write a program to log errors to a file instead of printing them.

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result =", result)

except Exception as e:
    log_file = open("error_log.txt", "a")
    log_file.write(str(e) + "\n")
    log_file.close()

# Write a program that validates an email format and raises an exception for invalid ones.

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result =", result)

except Exception as e:
    with open("error_log.txt", "a") as file:
        file.write(f"Error: {e}\n")