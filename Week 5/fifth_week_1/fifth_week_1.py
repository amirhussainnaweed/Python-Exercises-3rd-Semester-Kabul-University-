def add_student(
    filename: str,
    sid: int,
    name: str
) -> None:
    with open(
        filename, "a",
        encoding="utf-8"
    ) as file:
        file.write(
            f"{sid}|{name}\n"
        )


def list_students(filename: str) -> None:
    try:
        with open(
            filename, "r",
            encoding="utf-8"
        ) as file:
            for line in file:
                print(line.rstrip())
    except FileNotFoundError:
        print("File not found")


def find_student(
    filename: str,
    sid: int
) -> None:
    try:
        with open(
            filename, "r",
            encoding="utf-8"
        ) as file:
            isthere = False
            for line in file:
                part = line.rstrip().split("|")
                if int(part[0]) == sid:
                    isthere = True
                    print(line.rstrip())
            if not isthere:
                print("Student not found")
    except FileNotFoundError:
        print("File does not exist.")



def count_students(
    filename: str
) -> int:

    try:
        with open(
            filename, "r",
            encoding="utf-8"
        ) as file:

            count = 0

            for line in file:
                count+=1

            return count

    except FileNotFoundError:
        print("File does not exist.")
        return 0

#================================================

#adding five students and printing them
# add_student("students.txt", 101, "Amir")
# add_student("students.txt", 102, "Ahmad")
# add_student("students.txt", 103, "Zabih")
# add_student("students.txt", 104, "Ali")
# add_student("students.txt", 105, "Hafiz")
# list_students("students.txt")

#=================================================

#finding a student by id
find_student("students.txt", 1901)

#=================================================

#appending a new student
add_student("students.txt", 106, "Hassan")

#=================================================

#count students
print(count_students("students.txt"))

#=================================================