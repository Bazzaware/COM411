COL_MEDAL = 14
COL_TEAM = 6
COL_YEAR = 9


def list_years(data: list) -> set:
    """Returns a list of years from Data"""
    years = set()
    for line in data:
        year = line[COL_YEAR]
        years.add(year)
    return years


def tally_medals(data: list) -> dict[str, int]:
    """Returns list of medals"""
    medal_tally = dict({"Gold": 0, "Silver": 0, "Bronze": 0})
    for line in data:
        medal = line[COL_MEDAL]
        if medal in ("Gold", "Silver", "Bronze"):
            medal_tally[medal] += 1
    return medal_tally


def tally_team_medals(data: list) -> dict[str, dict[str, int]]:
    """Returns nested dictionary"""
    team_medal_tally = {}

    for line in data:
        team_name = line[COL_TEAM]
        team_medal = line[COL_MEDAL]
        if team_medal not in ("Gold", "Silver", "Bronze"):
            continue

        if team_name in team_medal_tally:
            team_medal_tally[team_name][team_medal] += 1
        else:
            team_medal_tally[team_name] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            team_medal_tally[team_name][team_medal] += 1

    return team_medal_tally
