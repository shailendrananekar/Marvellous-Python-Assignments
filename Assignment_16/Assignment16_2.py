import os
import sys


def main():

    flag1 = os.path.exists(sys.argv[1])

    if flag1 == False:
        print("file doesn't exist !")
    print("Files exist in current Directory.")
    
    fileRead = open(sys.argv[1], "r")
    fileData = fileRead.read()
    print("File Content:\n", fileData)

    
    fileRead.close()


if __name__ == "__main__":
    main()
