def movements():
    path = ("Move Forward", 10, "Move Backward",
            5, "Move Left", 3, "Move Right", 1)
    return path


def main():
    print("moving....")
    print(f"Move {(movements()[0])} for {(movements()[1])} steps")
    print(f"Move {(movements()[2])} for {(movements()[3])} steps")
    print(f"Move {(movements()[4])} for {(movements()[5])} steps")
    print(f"Move {(movements()[6])} for {(movements()[7])} steps")


if __name__ == "__main__":
    main()
