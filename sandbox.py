class Student:
    def __init__(self, name = 'student', age = 18):
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def __repr__(self):
        info = "Name: " + self.name
        info += "\nAge: " + str(self.age)
        info += "\nCourses: " + " , ".join(self.courses)
        return info + "\n"


peter = Student(16)
print(peter.age, peter.name)
