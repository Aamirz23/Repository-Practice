def calculator():
    print("Welcome to the Calculator!")
    print("Supported operations: +  -  *  /  %  //  **")
    
    try:
        operator = input("Enter the operator (e.g., +, -, *, /, %, //, **): ").strip()
        if operator not in ['+', '-', '*', '/', '%', '//', '**']:
            raise ValueError("Unsupported operator. Please choose a valid one.")
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        elif operator == '%':
            if num2 == 0:
                raise ZeroDivisionError("Cannot take modulus by zero.")
            result = num1 % num2
        elif operator == '//':
            if num2 == 0:
                raise ZeroDivisionError("Cannot floor-divide by zero.")
            result = num1 // num2
        elif operator == '**':
            result = num1 ** num2

        print(f"Result: {result}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Math Error: {zde}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Run the calculator
calculator()


