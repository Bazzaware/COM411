from shared_code import clear_terminal

def main():
    clear_terminal()
    hear = input("What did I hear?\n").lower()
    see = input("\nWhat did I see?\n").lower()

    if(hear == "grrr" and see == "two red eyes"):
        print( "\nThere is a scary creature. I should get out of here!")
    else:
        print("\nI am a little scared but I will continue.")

if (__name__ == "__main__"):
    main()