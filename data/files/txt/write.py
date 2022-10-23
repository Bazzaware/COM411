import os

def search(filePath):

    print("Searching....")
    sections = ""
    books = "Books:\n"
    with open(filePath,"r") as file:
        for line in file:
            if (line.startswith("Section")):
                sections += f"{line.strip()}\n"
            else:
                books += f"{line.strip()}\n"
    print("....Done!")
    return f"{sections}\n\n{books}"



def save(filePath,dataToSave):
    with open(filePath,"w") as file:
        file.write(dataToSave)



def main():
    cwd = os.getcwd()
    sourceFile = f"{cwd}/data/files/txt/books.txt"
    destinationFile = f"{cwd}/data/files/txt/section-books.txt"
    data = search(sourceFile)
    save(destinationFile,data)




if (__name__ == "__main__"):
    main()