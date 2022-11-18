import mymodules.mymodule as mymod

def observed():
    observations = set()
    observations = {"Flying Car", "Sky Scraper",
                    "Sky Scraper", "Laser", "Dome", "Dome"}
    return observations


def run():
    mymod.clear_terminal()
    print(observed())


if __name__ == "__main__":
    run()