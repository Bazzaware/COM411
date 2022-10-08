from shared_code import clear_terminal


def number_comparison(first_number, second_number):
    if first_number < second_number:
        return "first"
    elif first_number > second_number:
        return "second"
    else:
        return "equal"


def main():
    clear_terminal()
    first = int(input("Please enter the first number. \n "))
    second = int(input("Please enter the second number.\n "))
    result = number_comparison(first,second)
    if (result == "equal"):
        print("Both numbers are equal.")
    else:
        print(f"\nThe {result} number is the smallest.")


if (__name__ == "__main__"):
    main()