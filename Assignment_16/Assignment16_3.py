import os
import sys


def Count(file1):
    flag1 = os.path.exists(file1)

    if flag1 == False:
        print("file doesn't exist !")
        exit()
    print("Files exist in current Directory.")

    file1Content = open(file1, "r")
    file1Data = file1Content.read()
    print("File1 Content:\n", file1Data)

    wordobj = file1Data.split()
    wordCount = 0
    for i in wordobj:
        wordCount = wordCount + 1
    print(f"The total no of words are : {wordCount}.")

    lineobj = file1Data.split("\n")
    lineCount = 0
    for i in lineobj:
        lineCount = lineCount + 1
    print(f"The total no of lines are : {lineCount}.")

    print(f"The total no of characters are :  {len(file1Data)}.")

    file1Content.close()


def main():

    Count(sys.argv[1])


if __name__ == "__main__":
    main()
