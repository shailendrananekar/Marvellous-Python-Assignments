import os


def DisplayFileContent(filename):
    flag = os.path.exists(filename)
    if flag == False:
        print("The path is invalid!")
        exit()
    print("File exist in current Directory.")

    fileContent = open(filename, "r")
    content = fileContent.read()
    print("File Content:\n", content)


def main():
    filename = input("Enter the file name to be traversed : ")
    DisplayFileContent(filename)


if __name__ == "__main__":
    main()
