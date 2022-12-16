import pytest
from os.path import join
from oop.Data import Data


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
    result = Data(file_path)

    # assert
    assert result.DATA == expected_csv


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
    result = Data(file_path)

    # assert
    assert result.DATA == expected


def test_invalid_file_type() -> None:
    #  arrange
    file_path: str = join('data', 'files', 'txt', 'library.bad')
    expected = 'File type not supported: .bad'
    #  act
    with pytest.raises(TypeError) as exp:
        Data(file_path)

    # assert
    assert str(exp.value) == expected


def test_file_not_exits() -> None:
    #  arrange
    file_path: str = join('data', 'files', 'txt', 'fileNotExist.csv')
    expected = f'File not found:\n\t{file_path}'
    #  act
    with pytest.raises(FileNotFoundError) as exp:
        Data(file_path)

    # assert
    assert str(exp.value) == expected
