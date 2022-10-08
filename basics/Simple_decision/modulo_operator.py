from sys import platform
from os import system

def is_odd_number(number):
    result = True
    if((number % 2) == 0):
        result = False

    return result


def clear_terminal():
    if platform == "linux" or platform == "linux2":
        system("clear")
    elif platform == "win32":
        system("cls")


def main():
    clear_terminal()
    number = int(input("Please enter a whole number.\n "))

    if (is_odd_number(number)):
        print(f"The number {number} is an odd number.")
    else:
        print(f"The number {number} is an even number.")


if (__name__ == "__main__"):
    main()
