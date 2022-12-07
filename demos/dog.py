class Dog:

    def __init__(self, name, pattern, breed="Unknown"):
        self.name = name
        self.pattern = pattern
        self.breed = breed
        self.energy = 50
        self.clean = 75

    def run(self, metres):
        self.energy -= metres
        self.clean -= 5
        print(f"{self.name} goes Pant pant pant")

    def lick_self(self):
        self.clean += 5


if __name__ == "__main__":
    dog1 = Dog("Fido", "White with brown patches", "Jack Russel")
    dog2 = Dog("Lassie", "Kind of like lion", "Lassie dog")

    print(f"{dog1.name} has {dog1.energy} energy and is {dog1.clean} clean")
    print(f"{dog2.name} has {dog2.energy} energy and is {dog2.clean} clean")
    dog1.run(5)
    dog2.lick_self()
    dog2.lick_self()
    dog2.lick_self()

    print(f"{dog1.name} has {dog1.energy} energy and is {dog1.clean} clean")
    print(f"{dog2.name} has {dog2.energy} energy and is {dog2.clean} clean")

    dog3 = Dog("Butch", "Black")
    print(dog3.breed)