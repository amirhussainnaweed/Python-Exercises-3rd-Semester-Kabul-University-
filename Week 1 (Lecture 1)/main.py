class Student:
    university = 'Kabul University'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_university():
        return Student.university

    @classmethod
    def get_name(cls):
        return Student.university


a = Student('ali')
b = Student('naweed')

print(a.name)
print(a.university)
print(a.get_university())
print(a.get_name())

print(b.name)
print(b.university)

#===================================================================================================================

#identity equality check

c = Student('amir')
d = Student('amir')

print(c is d)
print(c == d)