class User():
    def sign_in(self):
        print("Logged In")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrow}")


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 60)

wizard1.attack()
archer1.attack()
