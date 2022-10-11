
from shared_code import clear_terminal

def is_odd_number(number):
    result = True
    if((number % 2) == 0):
        result = False

    return result

def main():
    clear_terminal()
    number = int(input("Please enter a whole number.\n "))

    if (is_odd_number(number)):
        print(f"The number {number} is an odd number.")
    else:
        print(f"The number {number} is an even number.")


if (__name__ == "__main__"):
    main()
