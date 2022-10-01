import os


class HealthLevels():
    def __init__(self, lives, energy, shield):
        self.lives = lives
        self.energy = energy
        self.sheild = shield

        self.status = {
            "lives": set_health_icon("♥", lives),
            "energy": set_health_icon("*", energy),
            "shield": set_health_icon("♦", shield)
        }


def set_health_icon(icon, value):
    return icon * value


def main():
    os.system("cls")
    question = "Please enter the"
    lives = int(input(f"{question} number of lives.\n = "))
    energy = int(input(f"\n{question} energy level.\n = "))
    shield = int(input(f"\n{question} shield level.\n = "))

    beeps_health = HealthLevels(lives, energy, shield)

    print("\nHealth has been set.\n")
    print(f"Lives: {beeps_health.status['lives']}")
    print(f"Energy: {beeps_health.status['energy']}")
    print(f"Shield: {beeps_health.status['shield']}")


if __name__ == "__main__":
    main()
