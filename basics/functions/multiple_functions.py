def display_ladder(steps):
    print(f"\n| |")
    print(f"***\n| |\n" * steps)


def create_ladder():
    steps = int(input("How many steps remain?\n"))
    display_ladder(steps)

def main():
    create_ladder()

if (__name__ == "__main__"):
    main()
