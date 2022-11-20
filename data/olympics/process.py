from tui import started, display_years, completed, display_medal_tally


def list_years(data: list) -> None:
    """Returns a list of years from Data"""
    started("Listing years")
    years = set()
    for line in data:
        year = line[9]
        years.add(year)
    display_years(years)
    completed()


def tally_medals(data: set) -> None:
    """Returns list of medals"""
    started("Tallying medals")
    medal_tally = dict({"Gold": 0, "Silver": 0, "Bronze": 0})
    for line in data:
        medal = line[14]
        if medal in ("Gold", "Silver", "Bronze"):
            medal_tally[medal] += 1
    display_medal_tally(medal_tally)
    completed()


def tally_team_medals(data: set) -> None:
    """Returns nested dictionary"""
    started("")
    completed()
