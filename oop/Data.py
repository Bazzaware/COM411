import csv
from os.path import exists, splitext


class Data():
    DATA = list()

    def __init__(self, file_path: str) -> None:
        self.DATA = self.import_data(file_path)

    def import_data(self, file_path) -> None:
        if exists(file_path):
            if file_path.endswith('.csv'):
                self.import_csv(file_path)
            elif file_path.endswith('.txt'):
                self.import_txt(file_path)
            else:
                raise TypeError(f'File type not supported: {splitext(file_path)[1]}')
        else:
            raise FileNotFoundError(f'File not found:\n\t{file_path}')
        return self.DATA

    def import_csv(self, import_file):
        with open(import_file) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for line in csv_reader:
                self.DATA.append(line)

    def import_txt(self, import_file):
        with open(import_file) as file:
            for line in file:
                self.DATA.append(line)
