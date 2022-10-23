

def display_chars(path, numberOfChars):
    with open(path, "r") as file:
        return file.read(numberOfChars).strip()


def display_line(path):
    with open(path, "r") as file:
        return file.readline().strip()


def display_text(path):
    with open(path,"r") as file:
        return file.readlines()

def main():
    dataFile = "library.txt"
    numberOfChars = 5
    chars = display_chars(dataFile, numberOfChars)
    line = display_line(dataFile)
    allData = display_text(dataFile)
    print(f"The first {numberOfChars} characters are:\n{chars}")
    print(f"\nThe first line is :\n{line}")
    print("\nThe full text is :")
    for line in allData:
        print(line.strip())


if (__name__ == "__main__"):
    main()
