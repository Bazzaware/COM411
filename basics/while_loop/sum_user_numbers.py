from shared_code import clear_terminal

def main():
    clear_terminal()

    how_many_numbers = int(input( "How many numbers should I sum up?\n"))
    total_sum = 0
    number = 1
    print()
    while (number <= how_many_numbers):
        number_to_add = int(input(f"\tPlease enter number {number} of {how_many_numbers}:\n\t"))
        total_sum += number_to_add
        number += 1

    print(f"\n...Done! The answer is {total_sum}")


if (__name__ == "__main__"):
    main()