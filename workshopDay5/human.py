class Human:
    # name = "Ece"
    # built-in

    def __init__(self, name):
        self.name = name
        print("Bir human instance'i üretildi.")

    def __str__(self):
        return f"STR fonksiyonundan geriye dönen değer: {self.name}"

    def talk(self, sentence):
        print(f"{self.name}: {sentence}")

    def walk(self,):
        print(f"{self.name} is walking.")
