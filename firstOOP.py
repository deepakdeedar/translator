class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(PlayerCharacter.adding_things(2, 5))
print(player1.name)
print(player1.age)
player1.run()
