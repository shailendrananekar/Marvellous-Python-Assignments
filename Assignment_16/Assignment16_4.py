import os
import sys


def main():

    listofno = input("Enter the list of numbers separated by space: ").split()

    flag1 = os.path.exists(sys.argv[1])

    if flag1 == False:
        print("file doesn't exist !")
        print("Creating file...")
        fileCreate = open(sys.argv[1], "w")
        for i in range(len(listofno)):
            fileCreate.write(f"{listofno[i]}.\n")

    print("Files exist in current Directory.")
    fileCreate.close()

    fileRead = open(sys.argv[1], "r")
    fileData = fileRead.read()
    print("File Content:\n", fileData)

    fileRead.close()


if __name__ == "__main__":
    main()
