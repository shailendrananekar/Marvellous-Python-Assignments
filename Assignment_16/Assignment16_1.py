import os
import sys


def main():

    flag1 = os.path.exists(sys.argv[1])

    if flag1 == False:
        print("file doesn't exist !")
        print("Creating file...")
        fileCreate = open(sys.argv[1], "w")
        for i in range(5):
            fileCreate.write(f"Student {i}.\n")

    print("Files exist in current Directory.")
    fileCreate.close()
    
    fileRead = open(sys.argv[1], "r")
    fileData = fileRead.read()
    print("File Content:\n", fileData)

    
    fileRead.close()


if __name__ == "__main__":
    main()
