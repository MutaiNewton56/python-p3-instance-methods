class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
