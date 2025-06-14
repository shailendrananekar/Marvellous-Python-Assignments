import os


def FileExist(filename):
    flag = os.path.exists(filename)
    if flag == False:
        print("The path is invalid!")
        exit()
    print("File exist in current Directory.")


def main():
    filename = input("Enter the file name to be traversed : ")
    FileExist(filename)


if __name__ == "__main__":
    main()
