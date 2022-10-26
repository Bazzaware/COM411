from iterate_list import *


def main():
    _directions = directions()
    route = []
    for step in range(4):
        menu()
        userResponse = int(input())
        route.append(_directions[userResponse])
        step += 1

    print(f"\nEscape route: {route}")


if __name__ == "__main__":
    main()