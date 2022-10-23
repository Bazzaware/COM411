import csv
import os

def read(filePath):
    with open(filePath) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print(f"Values:\n")
        for line in csv_reader:
            print(f"{line}")














def main():
    cwd = os.getcwd()
    sourceFile = f"{cwd}/data/files/csv/bots.csv"
    read(sourceFile)



if (__name__ == "__main__"):
    main()