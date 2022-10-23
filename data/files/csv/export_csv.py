import csv
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def export(filePath, numberOfBots):
    print("Exporting...")
    with open(filePath, "a") as file:
        csv_writer = csv.writer(file, delimiter=",")
        for bot in range(numberOfBots):
            botId = input("Please enter the bot id:\n")
            botName = input("Please enter the bot name:\n")
            botPaint = input("Please enter the bot paint:\n")

            csv_writer.writerow([botId, botName, botPaint])




def main():
    destinationFile = f"{ROOT_DIR}/exported_bots.csv"
    export(destinationFile,2)


if __name__ == "__main__":
    main()
