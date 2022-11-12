from simple_dict import pattern
from mymodules.mymodule import clear_terminal


def display_keys(data: dict):
    """Displays keys from a dictionary"""
    print("\nKeys:")
    for key in data.keys():
        print(f"{key}")


def display_values(data: dict):
    """Displays values from a dictionary"""
    print("\nValues:")
    for value in data.values():
        print(f"{value}")


def display_items(data: dict):
    """Display key value pairs from dictionary"""
    print("\nPairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    """Initialise program"""
    clear_terminal()
    pattern_data = pattern()
    print(f"Dictionary: \n{pattern_data}")
    display_keys(pattern_data)
    display_values(pattern_data)
    display_items(pattern_data)


if __name__ == "__main__":
    run()
