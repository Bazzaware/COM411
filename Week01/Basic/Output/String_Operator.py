
class HealthLevels():
    def __init__(self):
        self.lives = 6
        self.energy = 9
        self.sheild = 15

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
