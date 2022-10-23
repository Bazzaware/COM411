
import csv
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def extract(filePath):
    print(f"Extracting...", end="")
    with open(filePath) as file:
        csv_reader = csv.reader(file)
        ignoreHeadings = next(csv_reader)
        names = ""

        for line in csv_reader:
            names += f"{line[1]}\n"

    print(f"Done!\nThe extracted names are as follows:")
    print(f"{names}")


def main():
    sourceFile = f"{ROOT_DIR}/bots.csv"
    extract(sourceFile)


if __name__ == "__main__":
    main()
