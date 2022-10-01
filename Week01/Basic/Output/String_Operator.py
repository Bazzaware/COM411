
class HealthLevels():
    def __init__(self, lives, energy, shield):
        self.lives = lives
        self.energy = energy
        self.sheild = shield

        self.status = {
            "lives": "♥♥♥♥♥♥",
            "energy": "***********",
            "sheild": "♦♦♦♦♦♦♦♦♦"
        }


def health():
    return "♥"


def set_health_icon(icon, value):
    return icon * value


def main():
    msg = "main"
    print(f"We are at {msg}")


if __name__ == "__main__":
    main()
