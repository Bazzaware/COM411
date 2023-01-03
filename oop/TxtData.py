from oop.DataFile import DataFile


class TxtData(DataFile):

    ext = 'txt'
    data = list()

    def import_data(self):
        with open(self.file_path) as file:
            for line in file:
                self.data.append(line)

