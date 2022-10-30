import csv
import mymodule as mymod
import os

records = []
headings = []


def loadData(filePath):
    print(f"Loading data...",end="")
    with open(filePath,"r") as file:
        csvReader = csv.reader(file)
        headings = next(csvReader)
        for line in csvReader:
            records.append(line)
    print(f"Done!")



def main():
    mymod.clear_terminal()
    cwd = os.getcwd()
    filePath = cwd + "/data/titanic/titanic.csv"
    titanicData = loadData(filePath)
    print(f"Successfully loaded {len(records)} records.")

if __name__ == "__main__":
    main()
