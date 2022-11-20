import csv
from tui import started,menu
import process

def read_data(file_path: str) -> list:
    '''Reads in data from a CVS file and returns a list with headers removed.'''
    started(file_path)
    data = list()
    with open(file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
    return data


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = menu
        if selection == "years":
            process.list_years(athlete_data)
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
