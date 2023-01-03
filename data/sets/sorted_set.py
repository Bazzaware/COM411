import mymodules.mymodule as mymod


def observed():
    observations = []
    for item in range(5):
        observations.append(input("Please enter an observation:\n"))
    return observations


def remove_observations(observations):
    running = True
    while running:
        remove_bool = input("Do you wish to remove an observation (yes/no)?")
        if remove_bool.lower() == "yes":
            remove_item = input("What observation do you wish to remove?")
            observations.remove(remove_item)
            print(f"Done!")
        else:
            running = False


def run():
    mymod.clear_terminal()
    observations = observed()
    remove_observations(observations)

    result = set()
    for observation in observations:
        count = observation, observations.count(observation)
        result.add(count)
    print("\nObservations:")
    for item in sorted(result):
        print(f"{item[0]} observed {item[1]} times.")


if __name__ == "__main__":
    run()
