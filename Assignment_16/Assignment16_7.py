import os
import sys


def marks(file1):
    flag1 = os.path.exists(file1)

    if flag1 == False:
        print("file doesn't exist !")
        exit()
    print("Files exist in current Directory.")

    file1Content = open(file1, "r")
    file1Data = file1Content.read()
    print("File1 Content:\n", file1Data)

    lineobj = file1Data.split("\n")
    print("students with more than 75 marks:")

    for i in lineobj:
        studentinfo = {}
        key, val = i.split()
        studentinfo[key] = int(val)
        if studentinfo[key] > 75:
            print(f"{key} : {studentinfo[key]}")

    file1Content.close()


def main():

    marks(sys.argv[1])


if __name__ == "__main__":
    main()
