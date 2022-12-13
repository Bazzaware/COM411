from inhabitant import Inhabitant


class Human(Inhabitant):
    def __init__(self, name="Inhabitant", age=0, energy=...):
        super().__init__(name, age, energy)
        self.energy = energy

    def move(self, distance):
        self.energy -= distance
