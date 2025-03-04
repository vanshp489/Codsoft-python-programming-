def calculator():
    print("Simple Calculator")
    print("Choose an operation: +, -, *, /")

    num1 = float(input("Enter the first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2  
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0: 
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
    else:
        print("Invalid operation!")
        return 

    print(f"Result: {num1} {operation} {num2} = {result}")
    calculator()

calculator()