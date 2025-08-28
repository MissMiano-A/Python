# Simple Calculator Program

# Ask the user for the first number
num1 = float(input("Enter the first number: "))

# Ask the user for the second number
num2 = float(input("Enter the second number: "))

# Ask the user for the operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on the chosen operation
if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)

elif operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)

elif operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)

elif operation == "/":
    if num2 != 0:  # avoid dividing by zero
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operation! Please enter +, -, * or /")


