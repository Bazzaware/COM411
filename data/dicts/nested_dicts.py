from mymodules.mymodule import clear_terminal


def short_pattern():
    """Returns a preset dictionary"""
    pattern = dict({
        "sequence": "101",
        "occurrences": 5
    })
    return pattern


def medium_pattern():
    """Returns a preset dictionary"""
    pattern = {"str:": 1}
    return pattern


def long_pattern():
    """Returns a preset dictionary"""
    pattern = dict({
        "sequence": "1100110011001100",
        "occurrences": 50
    })
    return pattern


def run():
    """Initialises program"""
    clear_terminal()
    print("Analysing patterns...")
    patterns = dict({
        "short sequence": short_pattern(),
        "medium sequence": medium_pattern(),
        "long sequence": long_pattern(),
    })

    for key,value in patterns.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run()
