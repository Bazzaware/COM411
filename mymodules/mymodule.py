from sys import platform
from os import system


def clear_terminal():
    if platform == "win32":
        system("cls")
    else:
        system("clear")
