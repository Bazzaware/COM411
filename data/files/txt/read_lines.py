def search(fileName):
    print("Searching..")

    with open(fileName) as file:
        for line in file:
            print(f"Looked in {line.strip()}")

    print("...Done!")



def main():
    search("library.txt")


if (__name__ == "__main__"):
    main()