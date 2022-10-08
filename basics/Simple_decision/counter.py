from shared_code import clear_terminal
from modulo_operator import is_odd_number


class comparison_counter():
    def __init__(self):
        self.odd = 0
        self.even = 0


def main():
    clear_terminal()
    numbers = [
        int(input("Please enter the first whole number.\n")),
        int(input("Please enter the second whole number.\n")),
        int(input("Please enter the third whole number.\n"))
    ]

    result = comparison_counter()
    for number in numbers:
        if(is_odd_number(number)):
            result.odd += 1
        else:
            result.even += 1


    print(f"\nThere were {result.even}  even and  {result.odd} odd numbers.")

if (__name__ == "__main__"):
    main()
