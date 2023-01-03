from os.path import splitext, exists
from abc import ABC, abstractmethod


class DataFile(ABC):

    def __init__(self, file_path) -> None:
        if not file_path.endswith(self.ext):
            raise Exception(f'File type not supported: {splitext(file_path)[1]}')
        self.file_path = file_path
        if not exists(self.file_path):
            raise FileNotFoundError(f'File not found:\n\t{file_path}')

    @abstractmethod
    def ext(self):
        pass

    @abstractmethod
    def import_data(self):
        pass

    @abstractmethod
    def data(self):
        pass

