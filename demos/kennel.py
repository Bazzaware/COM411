from dog import Dog


class Kennel:

    def __init__(self):
        self.dogs = []

    def add_dog(self, dog):
        if dog.clean < 40:
            return False
        self.dogs.append(dog)
        return True

    def exercise_dogs(self):
        for dog in self.dogs:
            dog.run(5)

    def put_inside(self):
        for dog in self.dogs:
            dog.lick_self()

    def display_details(self):
        for dog in self.dogs:
            print(f"{dog.name} has {dog.energy} energy and is {dog.clean} clean")


if __name__ == "__main__":
        k = Kennel()

        d1 = Dog("Fido", "meh")
        d2 = Dog("Lassie", "Lionish")
        d3 = Dog("Butch", "Bleh")

        if k.add_dog(d1):
            print("Dog added")

        k.exercise_dogs()
        k.display_details()

        k.add_dog(d2)
        k.add_dog(d3)

        k.exercise_dogs()
        k.put_inside()
        k.display_details()


