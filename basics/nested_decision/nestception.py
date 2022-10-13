from shared_code import clear_terminal
def main():
    clear_terminal()
    room = input("Where should I look?\n")

    if (room.lower() == "bedroom"):
        where_in_room = input("Where in the bedroom should I look?\n")
        if (where_in_room.lower() == "under the bed"):
            print("Found some shoes but no battery")
        else:
            print("Found some mess but no battery.")

    elif (room.lower() == "bathroom"):
        where_in_room = input("Where in the bathroom should I look?\n")
        if (where_in_room.lower() ==  "in the bathtub\n"):
            print("Found a rubber duck but no battery")
        else:
            print("Found a wet surface but no battery.")

    elif (room.lower() == "lab"):
        where_in_room = input("Where in the lab should I look?\n")
        if (where_in_room.lower() ==  "on the table"):
            print("Yes! I found my battery!")
        else:
            print("Found some tools but no battery.")


    else:
        print("I do not know where that is but I will keep looking.")



if (__name__ == "__main__"):
    main()
