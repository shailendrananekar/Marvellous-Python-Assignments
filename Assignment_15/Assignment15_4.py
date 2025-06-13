import os
import sys


def CompareContent(file1, file2):
    flag1 = os.path.exists(file1)
    flag2 = os.path.exists(file2)

    if flag1 == False or flag2 == False:
        print("Either one of the file doesn't exist !")
        exit()
    print("Files exist in current Directory.")

    file1Content = open(file1, "r")
    file1Data = file1Content.read()
    print("File1 Content:\n", file1Data)

    file2Content = open(file2, "r")
    file2Data = file2Content.read()
    print("File2 Content:\n", file2Data)

    if file1Data == file2Data:
        print("Both files have the same content.")
    else:
        print("Files have different content.")
    print("File1 Size:", os.path.getsize(file1), "bytes")
    print("File2 Size:", os.path.getsize(file2), "bytes")

    file1Content.close()
    file2Content.close()


def main():

    CompareContent(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
