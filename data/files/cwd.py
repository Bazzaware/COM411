import os


def cwd():
    path = os.getcwd()
    return path


def filesInFolder(path):
    files = os.listdir(path)
    return files



def main():
    print(f"Processing....")
    currentWorkingDirectory = cwd()
    print(f"The current working directory is {currentWorkingDirectory}")
    print(f"The directory contains the following files:")
    for file in filesInFolder(currentWorkingDirectory):
        print(f"{file}")


if (__name__ == "__main__"):
    main()
