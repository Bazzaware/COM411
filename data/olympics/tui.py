def started(msg=""):
    """Prints start message"""
    print("-"*85)
    print(f"Operation started: {msg}")


def completed():
    """Display completed message"""
    print("\nOperation completed.\n",end="-"*85)


def run():
    """Initialised module"""
    started("message")
    completed()


if __name__ == "__main__":
    run()
