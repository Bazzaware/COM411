from curses.ascii import isdigit


def is_odd_number(number):
    result = True
    if((number % 2) == 0):
        result = False

    return result
