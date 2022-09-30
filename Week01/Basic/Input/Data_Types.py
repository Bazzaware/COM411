import os


class Human():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.heightMeters = height
        self.weight = weight
        self.bmi = "{:.2f}".format(
            (self.weight / (self.heightMeters)**2))


def main():
    os.system('cls')
    name = input("What is your name human?\n>")
    age = int(input("How old are you (in years)?\n>"))
    height = float(input("How tall are you (in meters)?\n>"))
    weight = float(input("How much do you weigh (in kilograms)?\n>"))

    human = Human(name, age, height, weight)

    print(f'{human.name} you are {human.age} years old and your bmi is {human.bmi}')


if __name__ == "__main__":
    main()
