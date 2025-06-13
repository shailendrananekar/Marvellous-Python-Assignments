import os
import sys


def FrequencyCount(file1, word):
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
        if i == word:
            wordCount = wordCount + 1
    print(f"The word '{word}' appears {wordCount} times in the file.")

    file1Content.close()


def main():

    FrequencyCount(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
