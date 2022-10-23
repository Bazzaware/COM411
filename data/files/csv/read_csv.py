import csv
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def read(filePath):
    with open(filePath) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print(f"Values:")
        for line in csv_reader:
            print(f"{line}")


def main():
    sourceFile = f"{ROOT_DIR}/bots.csv"
    read(sourceFile)


if (__name__ == "__main__"):
    main()
