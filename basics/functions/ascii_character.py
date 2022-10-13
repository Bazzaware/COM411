def main():
    code = int(input("Program Started!\nPlease enter an ASCII code:\n "))

    if code in range(32, 127):
        char = chr(code)
        print(f"The character represented by the ASCII code {code} is {char}")
    else:
        print("Please enter a number in the range of 32 and 126.")
    print("Program ended.")


if (__name__ == "__main__"):
    main()
