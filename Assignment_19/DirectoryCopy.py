import os
import sys
import time
import shutil


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


def DirCopy(DirectoryName, copyDirectory):

    flag1 = os.path.exists(copyDirectory)
    if flag1 == False:
        os.mkdir(copyDirectory)

    flag = os.path.isabs(DirectoryName)

    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if flag == False:
        print("The path is invalid !")
        exit()

    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("Path is valid But the Target is not Directory ")
        exit()

    logs = []
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            # fname = os.path.join(FolderName, fname)
            shutil.copy2(os.path.join(FolderName, fname), copyDirectory)
            logs.append("Copied File is : " + fname)

    LogFile_Versions(logs)


def main():

    Border = "-" * 45
    print(Border)
    print("----------Marvellous Automation--------------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Application is used to perform directory cleaning")
            print("This directory Automation script")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the given script as : ")
            print("ScriptName.py NameofDirectory copyDirectory")

    elif len(sys.argv) == 3:
        DirCopy(sys.argv[1], sys.argv[2])

    else:
        print("Invalid number of command line arguments")
        print("Use the flags as : ")
        print("--h : used to display the help")
        print("--u : used to display the usage")

    print(Border)
    print("------Thank You for using our script---------")
    print("----------Marvellous Infosystem--------------")
    print(Border)


if __name__ == "__main__":
    main()
