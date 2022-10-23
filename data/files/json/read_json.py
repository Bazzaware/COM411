import json
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read(filePath):
    with open(filePath, "r") as file:
        jsonFile = json.load(file)
        print(f"City Name: {jsonFile['city']}")
        print(f"Population Size: {jsonFile['population']}")
        for bot in jsonFile['bots']:
            strength = bot['stats']['strength']
            speed = bot['stats']['speed']
            print(
                f"{bot['name']} has a strength level of {strength} and a speed level of {speed}.")


def main():
    sourceFile = f"{ROOT_DIR}/robocity.json"
    read(sourceFile)


if __name__ == "__main__":
    main()
