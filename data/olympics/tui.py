_LINE_LENGTH = 85


def started(msg: str) -> None:
    """Prints start message"""
    print("-" * _LINE_LENGTH)
    print(f"Operation started: {msg}")


def completed() -> None:
    """Display completed message"""
    print("\nOperation completed.\n", end="-" * _LINE_LENGTH)


def error(msg: str) -> None:
    """Displays Error Message"""
    print(f"Error! {msg}")


def menu() -> str:
    """Displays Menu options"""
    print(f"""Please select one of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    user_selection = str(input("Your selection: "))
    return user_selection.strip().lower()


def display_medal_tally(tally: dict[str, int]) -> None:
    """Displays medal tally"""
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver': <10} | {tally['Silver']:<10} |")
    print(f"| {'Silver': <10 }| {tally['Silver']:<10} |")
    print(f"| {'Bronze': <10 }| {tally['Bronze']:<10} |")


def display_team_medal_tally(team_tally: dict[str, dict[str, int]]) -> None:
    """display the name of each team and the medals the team has one"""
    for team, tally in team_tally.items():
        print(team)
        print(
            f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years: set[int]) -> None:
    """Sort the years into descending order (largest first) and display each year on a new line"""
    for year in sorted(years, reverse=True):
        print(year)
