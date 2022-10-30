import csv
import mymodule as mymod
import os

records = []
headings = []


def loadData(filePath):
    print(f"Loading data...", end="")
    with open(filePath, "r") as file:
        csvReader = csv.reader(file)
        headings = next(csvReader)
        for line in csvReader:
            records.append(line)
    print(f"Done!")


def displayMenu():
    menuOptions = ["[1] Display the names of all passengers",
                   "[2] Display the number of passengers that survived",
                   "[3] Display the number of passengers per gender",
                   "[4] Display the number of passengers per age group"]

    print(f"\nPlease select one of the following options:")
    for option in menuOptions:
        print(option)


def displayPassengerName():
    print(f"The names of the passengers are...")
    for passenger in records:
        print(passenger[3])


def main():
    mymod.clear_terminal()
    cwd = os.getcwd()
    filePath = cwd + "/data/titanic/titanic.csv"
    titanicData = loadData(filePath)
    print(f"Successfully loaded {len(records)} records.")
    displayMenu()
    selection = int(input("\n"))

    print(f"You have selected option: {selection}")
    if (selection == 1):
        displayPassengerName()


if __name__ == "__main__":
    main()
