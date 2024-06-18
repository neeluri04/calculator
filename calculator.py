def calculator():
    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_operation():
        while True:
            print("Choose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            operation = input("Enter the operation (1/2/3/4): ")
            if operation in ['1', '2', '3', '4']:
                return operation
            else:
                print("Invalid choice. Please choose a valid operation.")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    if operation == '1':
        result = num1 + num2
        op_symbol = "+"
    elif operation == '2':
        result = num1 - num2
        op_symbol = "-"
    elif operation == '3':
        result = num1 * num2
        op_symbol = "*"
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            op_symbol = "/"
        else:
            print("Error: Division by zero is not allowed.")
            return

    print(f"The result of {num1} {op_symbol} {num2} is: {result}")

# Run the calculator
calculator()
