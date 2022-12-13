from oop.inhabitant import Inhabitant


class Human(Inhabitant):
    def __init__(self, name="Inhabitant", age=0, energy=...):
        super().__init__(name, age, energy)


if __name__ == '__main__':
    human = Human()

    print(repr(human))

    human.move(10)

