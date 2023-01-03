from oop.DataFile import DataFile
from csv import reader


class CsvData(DataFile):

    ext = 'csv'
    data = list()

    def import_data(self):
        with open(self.file_path) as file:
            csv_reader = reader(file)
            next(csv_reader)
            for line in csv_reader:
                self.data.append(line)

    def export_to_json(self):
        return super().export_to_json()
