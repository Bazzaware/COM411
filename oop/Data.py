import csv


class Data():
    DATA = list()

    def __init__(self, file_path: str) -> None:
        self.DATA = self.import_data(file_path)

    def import_data(self, file_path) -> None:
        with open(file_path) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for line in csv_reader:
                self.DATA.append(line)
        return self.DATA
