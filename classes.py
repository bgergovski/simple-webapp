class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"{self.name} is my name")


person_1 = Person("Bobby")

person_1.talk()

x = "Hello"[0]
print({x})