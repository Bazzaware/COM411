from operator import index


def directions():
    directions = ["Move Forward", "Move Backward","Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    _directions = directions()
    for directionIndex in range(len(_directions)):
        print(f"{directionIndex} : {_directions[directionIndex]}")


def main():
    menu()


if __name__ == "__main__":
    main()