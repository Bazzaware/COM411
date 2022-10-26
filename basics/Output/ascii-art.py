import os
from time import sleep, time


runProgram = True
numberOfImages = 3


def DisplayMenu(nuberOfImages):
    os.system('cls')
    print("Press 0 to select exit from program")
    for option in range(1, nuberOfImages):
        print("Press", option, " to select ASCII image ", option)


def SelectedImageId(id):
    global runProgram
    global numberOfImages

    if (id.isdigit() and 1 <= int(id) <= (numberOfImages - 1)):
        print("\nYou selected ", id)
        return int(id)
    elif (int(id) == 0):
        print("Goodbye.")
        runProgram = False
    else:
        print("Invalid selection. \nPlease try again.\n")
        input("\nPress ENTER to continue.")
        main()


def DisplayImage(selectedId):
    os.system('cls')
    if(selectedId == 1):
        Image1()
    elif(selectedId == 2):
        Image2()
    else:
        print(f"Invalid selection {selectedId}.")

    # Only works in version 3.10 or above.
    # match selectedId:
    #     case 1:
    #         Image1()
    #     case 2:
    #         Image2()
    #     case _:
    #         print("I cant find that image!!")

    input("\nPress ENTER to continue.")


def Image1():
    # Thank you for visiting https: // asciiart.website/
    # This ASCII pic can be found at
    # https: // asciiart.website/index.php?art = video % 20games/pac % 20man
    print("\t\t        _____")
    print("\t\t     -~\"     \"~-")
    HeadTop()
    Eyes1()
    HeadMid()
    Mouth1()
    HeadBottom()


def Image2():
    print("\t\t      Y\     /Y")
    print("\t\t      | \ _ / |")
    print("\t\t      | =(_)= |")
    print("\t\t    ,-~\/^ ^\/~-.")
    HeadTop()
    Eyes2()
    HeadMid()
    Mouth2()
    HeadBottom()


def HeadTop():
    print("\t\t   ^ ___     ___ ^.")
    print("\t\t  / .^   ^. .^   ^. \\")


def HeadBottom():
    print("\t\t   ^.             .^")
    print("\t\t    \"-.._____., -\"")


def Eyes1():
    print("\t\t Y  l    O! l    O!  Y")


def Eyes2():
    print("\t\t Y  lo    ! lo    !  Y")


def HeadMid():
    print("\t\t l_ `.___.' `.___.' _[")
    print("\t\t l^~\"-------------\"~^I ")


def Mouth1():
    print("\t\t !\,               ,/!")
    print("\t\t  \ ~-.,_______,.-~ /")


def Mouth2():
    print("\t\t !                   !")
    print("\t\t  \\                 /")


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
