def sum_weights(*weights):
    sum = 0
    for weight in weights:
        sum += weight
    return sum


def calc_avg_weight(weight01,weight02):
    return (sum_weights(weight01,weight02) / 2)


def main():
    beepWeight = int(input("What is the weight of Beep?\n"))
    bopWeight = int(input("\nWhat is the weight of Bop?\n"))
    functionToCall = input("\nWhat would you like to calculate(sum or average)?\n")
    if (functionToCall == "sum"):
        sum = sum_weights(bopWeight,beepWeight)
        print(f"\nThe sum of Beep and Bop's weight is {sum} .")
    elif (functionToCall == "average"):
        average = int(calc_avg_weight(beepWeight,bopWeight))
        print(f"\nThe average weight  is {average}.")
    else:
        print("Incorrect selection")


if (__name__ == "__main__"):
    main()