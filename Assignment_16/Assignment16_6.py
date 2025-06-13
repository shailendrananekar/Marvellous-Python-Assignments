import os
import sys


def CopyContent(source, destination):
    flag1 = os.path.exists(source)
    
    if flag1 == False:
        print("path doesn't exist !")
        exit()
    print("Files exist in current Directory.")

    sourceFileContent = open(source, "r")
    sourceData = sourceFileContent.read()
    print("Source file Content:\n", sourceData)

    destinationfile = open(destination, "w")
    destinationfile.write(sourceData)
    destinationfile = open(destination, "r")
    destinationfileRead = destinationfile.read()
    print(f"Data copied to {destination}:\n", destinationfileRead)

    sourceFileContent.close()
    destinationfile.close()


def main():

    CopyContent(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
