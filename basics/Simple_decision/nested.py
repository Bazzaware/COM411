from shared_code import clear_terminal
def main():
    clear_terminal()
    cover = input("What type of cover does the book have?\n(soft\\hard) ")

    if (cover.lower() == "soft"):
        binding = input("Is the book perfect-bound?\n (yes\\no): ")
        if (binding.lower() == "yes"):
            print( "Soft cover, perfect bound books are very popular!" )
        else:
            print( "Soft covers with coils or stitches are great for short books")

    elif (cover.lower() == "hard"):
        print("Books with hard covers can be more expensive!")
    else:
        print("Incorect responce!!")


if (__name__ == "__main__"):
    main()