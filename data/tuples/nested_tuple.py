import mymodule as my


def steps():
    likelihoods=[("step 1", 50), ("step 2", 38), ("step 3",27), ("step 4", 99 ), ( "step 5",4)]
    return likelihoods

def main():
    my.clear_terminal()
    likelihoods = steps()
    goodSteps =[]
    badSteps = []
    for item in likelihoods:
        if ( item[1] >= 50):
            badSteps.append(item)
        else:
            goodSteps.append(item)

    print(f"Good steps: {len(goodSteps)}, Bad steps: {len(badSteps)}")
if __name__ == "__main__":
    main()