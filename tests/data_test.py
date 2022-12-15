import pytest
from os.path import join
from oop.Data import Data


def test_import_from_csv() -> None:
    '''
    Should import data from a csv file
    '''
    # arrange
    expected = list((
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
    assert result.DATA == expected
