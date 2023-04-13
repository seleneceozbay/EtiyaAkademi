class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

        print("Öğrenci bilgileri oluşturuldu.")

    def studentInfo(self):
        print("Student Information! ")
        print(f"{self.id} nolu Öğrenci: {self.name} ")

    def doHomework(self):
        print(f"{self.name} is studying!")
