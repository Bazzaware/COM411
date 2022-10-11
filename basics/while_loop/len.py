from shared_code import clear_terminal

def main():
    clear_terminal()
    phrase = input("Please enter a phrase:\n")
    remaining_letters = 0
    reply = "\n"
    while (remaining_letters in range(len(phrase))):
        reply += "bop "
        remaining_letters += 1

    print(reply)

if (__name__ == "__main__"):
    main()