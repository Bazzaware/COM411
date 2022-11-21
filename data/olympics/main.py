import csv
import os
from tui import started, menu, error, display_years, display_medal_tally, display_team_medal_tally

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


FILE_PATH = f"{ROOT_DIR}/athlete_events.csv"


def read_data(file_path: str) -> list:
    """Reads in data from a CVS file and returns a list with headers removed."""
    started(file_path)
    data = list()
    with open(file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
    return data


def run():
    """Entry point"""
    athlete_data = read_data(FILE_PATH)
    stop_program: bool = False
    while not stop_program:
        selection = menu()
        if selection == "years":
            display_years(athlete_data)
        elif selection == "tally":
            display_medal_tally(athlete_data)
        elif selection == "team":
            display_team_medal_tally(athlete_data)
        elif selection == "exit":
            stop_program = False
            break
        else:
            error("Invalid Selection!")


if __name__ == "__main__":
    run()
