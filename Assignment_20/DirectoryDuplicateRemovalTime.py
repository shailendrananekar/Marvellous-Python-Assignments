import os
import sys
import time
import hashlib
import datetime


def CalculateChecksum(path, BlockSize=1024):
    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if flag == False:
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if flag == False:
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate


def LoggerFile(contentLog, logfileName="Log.txt"):

    logfile = open(logfileName, "w")
    for log in contentLog:
        logfile.write(log + "\n")
    print("Log file created with name : ", logfileName)
    logfile.close()


def DeleteDuplicate(Path):

    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0
    logs = []
    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if Count > 1:
                logs.append(
                    "Deleted file : " + str(datetime.datetime.now()) + " - " + subvalue
                )
                os.remove(subvalue)
                # logs.append("Duplicate file is : " + subvalue)
                Cnt = Cnt + 1
        Count = 0
    LoggerFile(logs)


def main():
    Border = "-" * 54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if len(sys.argv) == 2:
        if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            starttime = time.time()
            DeleteDuplicate(sys.argv[1])
            endtime = time.time()
            print("Time taken to remove duplicate files is : ", endtime - starttime)

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)


if __name__ == "__main__":
    main()
