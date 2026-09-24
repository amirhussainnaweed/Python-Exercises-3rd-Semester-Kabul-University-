class InvalidGradeError(Exception):
    pass

def validate_grade(value):
    try:
        value = int(value)
    except ValueError:
        raise ValueError("Invalid grade, must be an integer")
    if not 0 <= value <= 100:
        raise InvalidGradeError("Invalid grade, must be between 0 and 100")
    return value

i = 5

for a in range(i):
    b = input("Enter a number: ")
    try:
        grade = validate_grade(b)
        print(f"{grade} Grade is saved")
    except ValueError as e:
        print(e)
    except InvalidGradeError as e:
        print(e)