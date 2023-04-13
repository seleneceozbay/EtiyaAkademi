from students import Student
from teachers import Teacher

studentList = []
teacherList = []


def add(type, obj):
    if type == "student":
        studentList.append(obj)
    else:
        teacherList.append(obj)


def getAll(type):
    if type == "student":
        for student in studentList:
            print(student.name)

    else:
        for teacher in teacherList:
            print(teacher.name)


student1 = Student("Selen", 1)
student2 = Student("Rümeysa", 2)

teacher1 = Teacher("Engin", "Java")
teacher2 = Teacher("Halit", "Python")

add("student", student1)
add("student", student2)
add("teacher", teacher1)
add("teacher", teacher2)

getAll("teacher")
getAll("student")
