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
                   "[4] Display the number of passengers per age group",
                   "[5] Display the number of survivors per age group"]

    print(f"\nPlease select one of the following options:")
    for option in menuOptions:
        print(option)


def displayPassengerName():
    print(f"The names of the passengers are...")
    for passenger in records:
        print(passenger[3])


def displayNumberOfSurvivors():
    numberSurvived = 0
    for person in records:
        if (person[1] == "1"):
            numberSurvived += 1

    print(f"{numberSurvived} passengers survived.")


def displayPassengerByGender():
    male = 0
    female = 0
    for person in records:
        if (person[4] == "male"):
            male += 1
        else:
            female += 1
    print(f"females: {female}, males: {male}")


def displayPassengersPerAgeGroup():
    children = 0
    adults = 0
    elderly = 0

    for person in records:
        if (person[5] != ""):
            age = float(person[5])
            if (age != ""):
                if (age < 18):
                    children += 1
                elif (age < 65):
                    adults += 1
                else:
                    elderly += 1
    print(
        f"children: {children}, adults: {adults}, elderly: {elderly}")


def displaySurvivorsPerAgeGroup():
    children = {"count": 0, "survived": 0}
    adults = {"count": 0, "survived": 0}
    elderly = {"count": 0, "survived": 0}

    for person in records:
        if (person[5] != ""):
            age = float(person[5])
            if (age < 18):
                children["count"] += 1
                if (person[1] == "1"):
                    children["survived"] += 1
            if (age < 65):
                adults["count"] += 1
                if (person[1] == "1"):
                    adults["survived"] += 1
            else:
                elderly["count"] += 1
                if (person[1] == "1"):
                    elderly["survived"] += 1

    childrenResults = f"{children['count']}/{children['survived']}"
    adultResults = f"{adults['count']}/{adults['survived']}"
    elderlyResults = f"{elderly['count']}/{elderly['survived']}"
    print(
        f"children: {childrenResults}, adults: {adultResults} , elderly: {elderlyResults}")


def main():
    mymod.clear_terminal()
    cwd = os.getcwd()
    filePath = cwd + "/data/titanic/titanic.csv"
    loadData(filePath)
    print(f"Successfully loaded {len(records)} records.")
    displayMenu()
    selection = int(input("\n"))

    print(f"You have selected option: {selection}\n")
    if (selection == 1):
        displayPassengerName()
    elif (selection == 2):
        displayNumberOfSurvivors()
    elif (selection == 3):
        displayPassengerByGender()
    elif (selection == 4):
        displayPassengersPerAgeGroup()
    elif (selection == 5):
        displaySurvivorsPerAgeGroup()
    else:
        print(f"Invalid input {selection}!")


if __name__ == "__main__":
    main()
