import os
exitProgram = True


def DisplayMenu():
    print("Press 0 to select exit from program")
    for option in range(1, 2):
        print("Press", option, " to select ASCII image ", option)


class SelectedImageId():
    def __init__(self, selectedId):
        self.id = selectedId
        global exitProgram
        if (self.id.isdigit() and 1 <= int(self.id) <= 9):
            print("\nYou selected ", self.id)
        elif (int(self.id) == 0):
            print("Goodbye.")
            exitProgram = False
        else:
            print("Invalid selection. \nPlease try again.\n")
            main()


class DisplayImage():
    def __init__(self, selectedId):
        self.id = selectedId
        os.system('cls')
        print("display image")
        input("Press any key to continue.")


def main():
    print("This is an example for outputing ACSII art")

    while (exitProgram):
        DisplayMenu()
        selected = input(
            "\n Please select a number to display some ASCII art?:")
        selection = SelectedImageId(selected)
        if (exitProgram):
            DisplayImage(selection)


if __name__ == "__main__":
    main()
