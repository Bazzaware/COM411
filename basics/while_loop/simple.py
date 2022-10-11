from shared_code import clear_terminal

def main():
    clear_terminal()
    remaining_cables = 0
    cables_to_remove = int(input("How many cables should I remove?\n"))
    print()
    while (remaining_cables < cables_to_remove):
        print("Removed cable.")
        remaining_cables += 1


if (__name__ == "__main__"):
    main()