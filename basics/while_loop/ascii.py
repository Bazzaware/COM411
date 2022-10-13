from shared_code import clear_terminal

def main():
    clear_terminal()
    remaining_charge = 1
    bars_to_charge = int(input("How many bars should be charged?\n"))
    print()
    while (remaining_charge <= bars_to_charge):
        charge_icon = set_charge_icon("\u2588 ", remaining_charge)
        print(f"\nCharging: {charge_icon}")
        remaining_charge += 1
    print( "\nThe battery is fully charged.")


def set_charge_icon(icon, value):
    return icon * value


if (__name__ == "__main__"):
    main()