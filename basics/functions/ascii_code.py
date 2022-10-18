
def main():
    char = input("Program Started!\nPlease enter a standard character:\n ")

    if (len(char) == 1):
        code = ord(char)
        print(f"The ASCII code for {char} is {code}.")
    else:
        print("Please enter a single charater.")
    print("Program ended.")


if (__name__ == "__main__"):
    main()
