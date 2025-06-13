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

    lineobj = file1Data.split("\n")
    print("Lines with more than 5 words:")
    lineCount = 0
    wordCount = 0
    for i in lineobj:
        for j in i.split():
            wordCount = wordCount + 1
        # print(f"Line {lineCount + 1}: {wordCount}")
        if wordCount > 5:
            print(f"{i}")
        wordCount = 0
        lineCount = lineCount + 1

    file1Content.close()


def main():

    Count(sys.argv[1])


if __name__ == "__main__":
    main()
