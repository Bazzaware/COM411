import os


class Human():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.heightMeters = height
        self.weight = weight
        self.bmi = "{:.2f}".format(
            (self.weight / (self.heightMeters)**2))


def HealthMessage(bmi):
    if (bmi <= 18.4):
        print("You are underweight.")
    elif (bmi <= 24.9):
        print("You are a healthy weight.")
    elif (bmi <= 29.9):
        print("You are overweight.")
    elif (bmi <= 34.9):
        print("You are obse.")
    else:
        print(f"A BMI value of {bmi} is not valid!")


def main():
    os.system('cls')
    name = input("What is your name human?\n>")
    age = int(input("How old are you (in years)?\n>"))
    height = float(input("How tall are you (in meters)?\n>"))
    weight = float(input("How much do you weigh (in kilograms)?\n>"))

    human = Human(name, age, height, weight)
    print("\n***************************************************************************\n")
    print(f'{human.name} you are {human.age} years old and your bmi is {human.bmi}.')
    HealthMessage(float(human.bmi))
    print("\n***************************************************************************")


if __name__ == "__main__":
    main()
