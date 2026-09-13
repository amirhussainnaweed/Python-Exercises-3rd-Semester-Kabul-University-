from abc import ABC, abstractmethod
from enum import StrEnum


#duck Typing in python

# def make_sound(animal):
#     animal.sound()
#
# class dog:
#     def sound(self):
#         pass
#     def sound(self):
#         print("woof")
#
# class cat:
#     def sound(self):
#         pass
#     def sound(self):
#         print("meow")
#
# d = dog()
# c = cat()
#
# make_sound(d)
# make_sound(c)

#===============================================================================================================
print("=========================================================================================================")

class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __str__(self):
        return f"{self.name} - {self.email}"
    @abstractmethod
    def role_info(self):
        pass
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("invalid email")
        self._email = value



class Student(Person):
    def role_info(self):
        return f"{self.name} is a student"

class Lecturer(Person):
    def role_info(self):
        return f"{self.name} is a lecturer"



class Course:
    def __init__(self, courseName):
        self.name = courseName
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def __str__(self):
        return f"{self.name} and number of students: {len(self.students)}"


student1 = Student("Amir", "amir@gmail.com")
student2 = Student("Ahamd", "Ahamd@gmail.com")
lecturer = Lecturer("Ahmad Roheed", "AhamdRoheed@gmail.com")


people = [student1, student2, lecturer]

for person in people:
    print(person.role_info())
    print(person)

course = Course("Advanced Programming")
course.add_student(student1)
course.add_student(student2)

print(course)





