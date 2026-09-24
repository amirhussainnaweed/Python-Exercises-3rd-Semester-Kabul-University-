class InvalidOperationError(Exception):
    pass

while True:
    isdone = True
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
    except ValueError:
        print("Invalid numeric input")
        isdone = False
        continue
    finally:
        print("your calculation is done" + (" successfully" if isdone else " not successfully"))
    operation = input("Enter operation: (+, -, *, /)")

    try:
        if operation == "+":
            result = first_num + second_num
        elif operation == "-":
            result = first_num - second_num
        elif operation == "*":
            result = first_num * second_num
        elif operation == "/":
            result = first_num / second_num
        else:
            raise InvalidOperationError("Invalid operation")
        print("Result:" + str(result))
    except ZeroDivisionError:
        print("Cannot divide by zero")
        isdone = False
        continue
    except InvalidOperationError as e:
        print(e)
        isdone = False
        continue
    finally:
        print("your calculation is done" + (" successfully" if isdone else " not successfully"))
    again = input("Do you want to continue? (y/n): ")
    if again.lower() == "n":
        break