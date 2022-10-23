import json
import os as os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read(filePath):
    print(f"Reading....", end="")
    with open(filePath, "r") as jsonFile:
        data = json.load(jsonFile)

    print(f"...done")
    return data


def save(filePath, data):
    print(f"Exporting.....", end="")
    with open(filePath, 'w') as file:
        json.dump(data, file, indent=6)

    print(f"...done")


def main():
    sourceFile = f"{ROOT_DIR}/robocity.json"
    destinationFile = f"{ROOT_DIR}/exported.json"
    dataFromJson = read(sourceFile)
    save(destinationFile, dataFromJson)


if __name__ == "__main__":
    main()
