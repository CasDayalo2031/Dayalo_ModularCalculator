num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Choose an operation:")
print("(+) Addition")
print("(-) Subtraction")
print("(*) Multiplication")
print("(/) Division")

operation = input("Enter your choice: ")

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    if num2 != 0:
        result = divide(num1, num2)
    else:
        result = "Cannot divide by zero."
else:
    result = "Invalid operation."

print("Final Answer:", result)
