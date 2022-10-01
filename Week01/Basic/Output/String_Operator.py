def main():
    msg = "main"
    print(f"We are at {msg}")


class HealthLevels():
    def __init__(self):
        self.lives = "♥♥♥♥♥♥"
        self.energy = "***********"
        self.sheild = "♦♦♦♦♦♦♦♦♦"


def health():
    return "♥"


def set_health_icon(icon, value):
    return icon * value


if __name__ == "__main__":
    main()
