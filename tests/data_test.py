import pytest
from os.path import join
from oop.CsvData import CsvData
from oop.TxtData import TxtData


def test_import_from_csv() -> None:
    '''
    Should import data from a csv file
    '''
    # arrange
    expected_csv = list((
        [
            ['1', 'Beep', 'Mercury'],
            ['2', 'Bop', 'Boulder'],
            ['3', 'Shadow', 'Black']
        ]
    ))
    file_path: str = join('data', 'files', 'csv', 'bots.csv')

    # act
    data_file = CsvData(file_path)
    data_file.import_data()

    # assert
    assert data_file.data == expected_csv


def test_import_from_txt() -> None:
    '''
    Should import data from a txt file
    '''
    # arrange
    expected = list((
        'The Law Section\n',
        'The Art Section\n',
        'The Technology Section\n',
        'The History Section'
    ))
    file_path: str = join('data', 'files', 'txt', 'library.txt')

    # act
    result = TxtData(file_path)
    result.import_data()

    # assert
    assert result.data == expected


def test_invalid_file_type() -> None:
    #  arrange
    file_path: str = join('data', 'files', 'txt', 'library.bad')
    expected = 'File type not supported: .bad'
    #  act
    with pytest.raises(Exception) as exp:
        CsvData(file_path)

    # assert
    assert str(exp.value) == expected


def test_file_not_exits() -> None:
    #  arrange
    file_path: str = join('data', 'files', 'txt', 'fileNotExist.csv')
    expected = f'File not found:\n\t{file_path}'
    #  act
    with pytest.raises(FileNotFoundError) as exp:
        CsvData(file_path)

    # assert
    assert str(exp.value) == expected
