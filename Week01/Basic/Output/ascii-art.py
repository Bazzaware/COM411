import os
runProgram = True
numberOfImages = 4


def DisplayMenu(nuberOfImages):
    print("Press 0 to select exit from program")
    for option in range(1, nuberOfImages):
        print("Press", option, " to select ASCII image ", option)


def SelectedImageId(id):
    global runProgram
    global numberOfImages

    if (id.isdigit() and 1 <= int(id) <= numberOfImages):
        print("\nYou selected ", id)
        return int(id)
    elif (int(id) == 0):
        print("Goodbye.")
        runProgram = False
    else:
        print("Invalid selection. \nPlease try again.\n")
        main()


def DisplayImage(selectedId):
    os.system('cls')
    match selectedId:
        case 1:
            print("display image")
        case _:
            print("I cant find that image!!")

    input("Press any key to continue.")


def main():
    print("This is an example for outputing ACSII art")

    while (runProgram):
        DisplayMenu(numberOfImages)
        userInput = input(
            "\n Please select a number to display some ASCII art?:")
        selectedId = SelectedImageId(userInput)
        if (runProgram):
            DisplayImage(selectedId)


if __name__ == "__main__":
    main()
