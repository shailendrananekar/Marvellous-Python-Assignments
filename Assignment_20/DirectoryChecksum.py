import os
import sys
import time
import schedule
import hashlib


def LogFile_Versions(contentLog):

    flag1 = os.path.exists("LoggerFiles")
    if flag1 == False:
        os.mkdir("LoggerFiles")

    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" % (timestamp)
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "_")
    logfileName = os.path.join("LoggerFiles", filename)
    flag2 = os.path.exists(logfileName)
    if flag2 == False:
        logfile = open(logfileName, "w")
        logfile.close()
    logfile = open(logfileName, "a")

    for log in contentLog:
        logfile.write(log + "\n")
    print("Log file created with name : ", filename)

    logfile.close()


def CalculateChecksum(path, BlockSize=1024):
    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()


def DirectoryWatcher(DirectoryName):

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

    log = []
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)
            log.append("File name : " + fname + " - " + "Checksum : " + checksum)

            # print("File name : ", fname)
            # print("Checksum : ", checksum)

    LogFile_Versions(log)


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
            DirectoryWatcher(sys.argv[1])

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
