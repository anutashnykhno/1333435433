class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
        self.happiness = 100
        self.health = 100

    def play(self):
        raise NotImplementedError("Метод 'play' повинен бути реалізований в підкласі.")

    def sleep(self):
        raise NotImplementedError("Метод 'sleep' повинен бути реалізований в підкласі.")

    def eat(self):
        raise NotImplementedError("Метод 'eat' повинен бути реалізований в підкласі.")

    def check_status(self):
        print(f"{self.name} ({self.species}): Здоров'я - {self.health}, Енергія - {self.energy}, Щастя - {self.happiness}")


class Cat(Animal):
    def play(self):
        if self.energy >= 10 and self.happiness <= 90:
            print(f"{self.name} грає, літає навколо та веселиться!")
            self.energy -= 10
            self.happiness += 10
        else:
            print(f"{self.name} занадто втомлений або вже щасливий.")

    def sleep(self):
        if self.energy <= 90:
            print(f"{self.name} спить, згортається у кульку.")
            self.energy += 10
        else:
            print(f"{self.name} не втомлений, йому не потрібно спати.")

    def eat(self):
        if self.health <= 90:
            print(f"{self.name} їсть рибку і покращує своє здоров'я.")
            self.health += 10
        else:
            print(f"{self.name} не голодний, йому не потрібно їсти.")


class Dog(Animal):
    def play(self):
        if self.energy >= 10 and self.happiness <= 90:
            print(f"{self.name} грає, принесення палички та веселиться!")
            self.energy -= 10
            self.happiness += 10
        else:
            print(f"{self.name} занадто втомлений або вже щасливий.")

    def sleep(self):
        if self.energy <= 90:
            print(f"{self.name} спить, облизується та мріє про біг по парку.")
            self.energy += 10
        else:
            print(f"{self.name} не втомлений, йому не потрібно спати.")

    def eat(self):
        if self.health <= 90:
            print(f"{self.name} їсть кістку і покращує своє здоров'я.")
            self.health += 10
        else:
            print(f"{self.name} не голодний, йому не потрібно їсти.")

if __name__ == "__main__":
    cat_name = input("Введіть ім'я котика: ")
    cat = Cat(cat_name, "Кіт")

    dog_name = input("Введіть ім'я собачки: ")
    dog = Dog(dog_name, "Собака")

    for _ in range(3):
        cat.play()
        dog.play()

    cat.sleep()
    dog.sleep()

    cat.eat()
    dog.eat()

    cat.check_status()
    dog.check_status()