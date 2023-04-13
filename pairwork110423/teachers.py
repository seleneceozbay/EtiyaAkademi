class Teacher:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def teacherInfo(self):
        print("Teacher Information! ")
        print(f"Öğretmenin Adı: {self.name}, Bölümü: {self.department}")

    def teach(self):
        print(f"{self.name} is resting..")
