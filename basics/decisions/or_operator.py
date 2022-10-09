from shared_code import clear_terminal

def main():
    clear_terminal()
    adventure_type = input("What type of adventure should I have?\n").lower()

    if (adventure_type == "short" or adventure_type == "scary"):
        print("Entering the dark forest!")
    elif (adventure_type == "safe" or adventure_type == "long"):
        print("Taking the safe route!")
    else:
        print("Not sure which route to take.")


if (__name__ == "__main__"):
    main()