from process import list_years, tally_medals, tally_team_medals

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
    user_selection = str(input("Your selection: ")).strip().lower()
    return user_selection


def display_medal_tally(data: list) -> None:
    """Displays medal tally"""
    started("Tallying medals")
    tally = tally_medals(data)
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")
    completed()


def display_team_medal_tally(data: list) -> None:
    """display the name of each team and the medals the team has one"""
    started("Tallying medals for each team")
    team_tally = tally_team_medals(data)
    for team, tally in team_tally.items():
        print(team)
        print(
            f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")
    completed()


def display_years(data: list) -> None:
    """Sort the years into descending order (the largest first) and display each year on a new line"""
    started("Listing years")
    years = list_years(data)
    for year in sorted(years, reverse=True):
        print(year)
    completed()
