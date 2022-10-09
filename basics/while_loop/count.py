from shared_code import clear_terminal

def main():
    clear_terminal()
    remaining_cables = 1
    cables_to_avoid = int(input("How many live cables should I avoid?\n"))
    print()
    while (remaining_cables <= cables_to_avoid):
        print(F"Avoiding...Done! {remaining_cables} live cables avoided.")
        remaining_cables += 1
    print( "\nAll live cables have been avoided.")


if (__name__ == "__main__"):
    main()