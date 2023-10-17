from test import logo


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


result = 0
print(logo)
while True:
    if result == 0:
        num1 = float(input("Enter the first number: "))
    else:
        num1 = result

    num2 = float(input("Enter the second number: "))

    operation = input("Choose an operation (+, -, *, /): ")
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        continue

    print(f"Result: {result}")

    another_calculation = input(
        "Do you want to perform another calculation with the current result? (yes/no): "
    )
    if another_calculation.lower() == "no":
        start_new_calculation = input(
            "Do you want to start a new calculation? (yes/no): "
        )
        if start_new_calculation.lower() == "yes":
            result = 0
        else:
            break

print("Goodbye!")
