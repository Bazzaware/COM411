import mymodules.mymodule as mymod


def observed():
    observations = []
    for item in range(7):
        observations.append(input("Please enter an observation:\n"))
    return observations


def run():
    mymod.clear_terminal()
    print(f"Counting observations...")
    observations = observed()
    result = set()

    for observation in observations:
        count = observation, observations.count(observation)
        result.add(count)
    print(f"\nObservations:")
    for item in result:
        print(f"{item[0]} observed {item[1]} times.")


if __name__ == "__main__":
    run()
