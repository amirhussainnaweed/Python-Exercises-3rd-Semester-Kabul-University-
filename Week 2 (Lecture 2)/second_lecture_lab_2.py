from typing import TypedDict

class StudentRecord(TypedDict):
    name: str
    courses: set[str]



Students: dict[int, StudentRecord] = {
    101: {
        "name": "amir",
        "courses": {"cs101", "cs102", "cs103", "m101"}
    },
    102: {
        "name": "ahmad",
        "courses": {"cs101", "cs102", "cs104", "ph101"}
    },
    103: {
        "name": "sharif",
        "courses": {"cs101", "cs102", "cs104", "m101"}
    }
}

#adding courses
print("adding")
Students[101]["courses"].add("cs105")
print(Students[101]["courses"])
#droping courses
Students[101]["courses"].discard("cs105")
print(Students[101]["courses"])


#common courses between two students
print("common courses between two students")
print(Students[101]["courses"]&Students[102]["courses"])

#list of all unique courses
print("list of all unique courses")
unique_courses = ((Students[101]["courses"] | Students[102]["courses"]) | Students[103]["courses"])
print(unique_courses)