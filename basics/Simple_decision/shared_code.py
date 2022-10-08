from sys import platform
from os import system


def clear_terminal():
    if platform == "linux" or platform == "linux2":
        system("clear")
    elif platform == "win32":
        system("cls")


def main():
    clear_terminal()
    number = int(input("Please enter a whole number.\n "))


if (__name__ == "__main__"):
    main()
