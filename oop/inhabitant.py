from abc import ABC, abstractmethod


class Inhabitant(ABC):

    MAX_ENERGY: int = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        pass

    @abstractmethod
    def move(self):
        pass
