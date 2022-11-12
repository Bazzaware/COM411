def pattern() -> dict:
    """Returns a dictionary"""
    sequences = dict({
        'Short Sequence': 3,
        'Medium Sequence': 2,
        'Long Sequence': 1
    })
    return sequences


def run():
    """dummy string"""
    print(pattern())


if __name__ == "__main__":
    run()
