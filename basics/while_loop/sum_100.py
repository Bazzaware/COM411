from tokenize import Number
from shared_code import clear_terminal

def main():
    clear_terminal()
    print("Calculating the sum of the first 100 numbers...")

    sum_of_numbers = 100
    total_sum = 0
    number = 1

    while (number <= sum_of_numbers):
        total_sum += number
        number += 1

    print(f"...Done! The answer is {total_sum}")


if (__name__ == "__main__"):
    main()