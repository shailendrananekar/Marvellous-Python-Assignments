import os
import sys


def CopyContent(ABC):
    flag = os.path.exists(ABC)
    if flag == False:
        print("The path is invalid!")
        exit()
    print("File exist in current Directory.")

    abcFileContent = open(ABC, "r")
    abcData = abcFileContent.read()
    print("File Content:\n", abcData)

    demofile = open("Demo.txt", "w")
    demofile.write(abcData)
    demofile = open("Demo.txt", "r")
    demofileRead = demofile.read()
    print("Data copied to Demo.txt:\n", demofileRead)

    abcFileContent.close()
    demofile.close()


def main():

    CopyContent(sys.argv[1])


if __name__ == "__main__":
    main()
