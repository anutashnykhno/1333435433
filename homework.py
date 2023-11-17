class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привіт, я {self.name} і мені {self.age} років."


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def study(self):
        return f"{self.name} вивчає {self.major}."

student = Student("Олег", 50, "фізику")
print(student.greet())
print(student.study())
