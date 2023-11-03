
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
        self.happiness = 100
        self.health = 100

    def play(self):
        if self.energy >= 10 and self.happiness <= 90:
            print(f"{self.name} грає та веселиться!")
            self.energy -= 10
            self.happiness += 10
        else:
            print(f"{self.name} занадто втомлений або вже щасливий.")

    def sleep(self):
        if self.energy <= 90:
            print(f"{self.name} спить та відновлює енергію.")
            self.energy += 10
        else:
            print(f"{self.name} не втомлений, йому не потрібно спати.")

    def eat(self):
        if self.health <= 90:
            print(f"{self.name} їсть і покращує своє здоров'я.")
            self.health += 10
        else:
            print(f"{self.name} не голодний, йому не потрібно їсти.")