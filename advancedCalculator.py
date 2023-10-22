num1 = float(input("Enter the first number: "))
operation = input("Enter the operation: ")
num2 = float(input("Enter the third number: "))

def calculator(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation"
    
print(calculator(num1, operation, num2))