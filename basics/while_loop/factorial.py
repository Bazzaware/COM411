from shared_code import clear_terminal

def main():
    clear_terminal()

    given_number = int(input("Please enter a number?\n"))
    total_sum = 1
    number = 0

    while (number < given_number):
        number += 1
        total_sum *= number

    print(f"\nThe factorial is {total_sum}.")


if (__name__ == "__main__"):
    main()